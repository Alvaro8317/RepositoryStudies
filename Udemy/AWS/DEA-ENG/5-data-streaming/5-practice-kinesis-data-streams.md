# Práctica: Crear un Kinesis Data Stream

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: configurar un flujo de datos en Kinesis, poner registros, consumirlos y procesarlos
con una función Lambda.

## Paso 1 — Crear el flujo de datos (stream)

En la consola de AWS, buscar el servicio **Kinesis** ("trabajar con datos de flujo en tiempo real").
Desde el menú se puede acceder a:

- **Kinesis Data Streams** — para recoger los datos de streaming con el flujo.
- Servicios adicionales para procesar/analizar los datos de streaming (ej. Firehose, se explora más
  adelante).

### Precio

- Aproximadamente **$0.015 por hora** por cada shard.
- Además, una tarifa por **unidad de carga útil (payload unit)**: alrededor de **$0.01 por 1 millón de
  unidades**.
- Para pruebas manuales con pocos registros, el coste es mínimo.

### Configuración del stream

Al hacer clic en **Crear flujo de datos (Create data stream)**:

- **Nombre**: admite mayúsculas, minúsculas, números, guiones y guiones bajos.
- **Modo de capacidad**:
  - **On-demand** — escala automáticamente según la demanda. Útil cuando el volumen de datos es
    **impredecible o variable**.
  - **Provisioned** — se especifica manualmente el número de shards. Útil cuando se conoce de
    antemano el volumen exacto de registros a procesar.
- La consola incluye un **estimador de shards (shard estimator)**: a partir del número de registros
  por segundo y el tamaño medio de cada registro, recomienda cuántos shards usar.

Para esta práctica se usa **modo Provisioned con 2 shards** (para poder observar cómo los distintos
shards procesan los datos), aunque el estimador para el volumen de esta prueba recomendaría solo un
shard.

> ⚠️ Todos los ajustes del stream son **editables después de la creación**: periodo de retención,
> número de shards, modo de capacidad y el **enhanced fan-out** (se explora más adelante). Por ahora se
> usa el modo estándar.

### Vista general tras la creación

Una vez creado, el stream queda en estado **Active** (ya se empieza a pagar por él). En la vista de
overview se puede ver:

- **Productores (Producers)** — de dónde vienen o se generan los datos que se escriben en el stream.
- **Consumidores (Consumers)** — las distintas opciones para leer el stream (se explorará usando
  **Amazon Data Firehose**).
- **Monitoring** — métricas de los registros que llegan al stream (puede tardar unos minutos en
  reflejar datos nuevos).
- **Configuración** — capacidad de escritura, capacidad de lectura y modo de capacidad, todo editable
  desde aquí.

## Paso 2 — Poner y consumir registros con la CLI

Sin un productor automatizado, se pueden escribir registros manualmente con la **AWS CLI** para
entender la mecánica del stream (a qué shard va cada registro, cómo consumirlo, etc.).

### Poner registros (`put-record`)

```bash
# Put records
aws kinesis put-record --stream-name data-stream-prod --partition-key "PartitionKey" --data $(echo -n "Data Entry 1" | base64) --profile local --region us-east-1
aws kinesis put-record --stream-name data-stream-prod --partition-key "PartitionKey2" --data $(echo -n "Data Entry 2" | base64) --profile local --region us-east-1
aws kinesis put-record --stream-name data-stream-prod --partition-key "PartitionKey3" --data $(echo -n "Data Entry 3" | base64) --profile local --region us-east-1
```

- El campo `--data` va **codificado en base64** para que el dato se transmita de forma eficiente.
- La respuesta de cada `put-record` incluye el **Shard ID** al que fue asignado el registro y un
  **Sequence Number** (único por shard para cada registro).
- La **partition key** determina el shard: la **misma clave siempre va al mismo shard**, pero una
  clave **distinta** también puede terminar en el mismo shard (sobre todo con pocos registros, como en
  esta prueba) — no hay garantía de que cada partition key distinta use un shard distinto.

### Consumir registros: Shard Iterator

El **Shard Iterator** es un puntero a una posición específica del stream desde la que empezar a leer
registros con `get-records`.

> ⚠️ Un Shard Iterator tiene una validez limitada de solo **5 minutos**; si caduca hay que solicitar
> uno nuevo.

Tipos de iterador usados aquí:

```bash
# Get LATEST ShardIterator
aws kinesis get-shard-iterator --stream-name data-stream-prod --shard-id "shardId-000000000000" --shard-iterator-type LATEST --profile local
```

- **LATEST** — apunta justo después del último registro en el momento de la llamada: permite
  consumir todo lo que se escriba **a partir de ahora**.

```bash
# Get OLDEST ShardIterator
aws kinesis get-shard-iterator --stream-name data-stream-prod --shard-id "shardId-000000000000" --shard-iterator-type TRIM_HORIZON --query 'ShardIterator' --output text --profile local
```

- **TRIM_HORIZON** — apunta al registro **más antiguo** disponible todavía en el shard (dentro del
  periodo de retención): permite leer todo el histórico desde el principio.

Con cualquiera de los dos, se usa el iterador obtenido para leer los registros:

```bash
# Get Records after ShardIterator
aws kinesis get-records --shard-iterator "YourShardIterator" --profile local
```

- La respuesta incluye los registros (con su `Data` en **base64**, hay que decodificarlo para leer el
  contenido original), el retraso en milisegundos y un **`NextShardIterator`** para seguir avanzando
  secuencialmente por el shard.
- Si no hay registros nuevos en la posición del iterador, la respuesta puede venir vacía — esto es
  normal en una prueba manual con pocos datos; en un entorno productivo con flujo constante de datos no
  suele ocurrir.

## Paso 3 — Consumir el stream con una función Lambda (trigger)

En vez de leer manualmente con la CLI, se conecta una función **Lambda** al stream mediante un
**trigger**: cada vez que llegan registros nuevos, Lambda los procesa automáticamente.

Lambda encaja bien aquí porque es:

- **Stateless** — procesamiento simple, sin necesidad de mantener estado entre invocaciones.
- **Serverless** — escala automáticamente según la carga de trabajo (sin servidores que gestionar).

Es una buena opción para tareas de procesamiento **sencillas** y **rápidas de desarrollar**, sobre
todo cuando la llegada de datos es **esporádica o variable**.

### Rol de la función Lambda

Antes de crear la función, hace falta un **rol de IAM** (servicio `Lambda`) con permisos para:

- **Leer del stream de Kinesis** — política administrada **`AmazonKinesisReadOnlyAccess`**.
- **Escribir en S3** — política administrada **`AmazonS3FullAccess`** (para mantener la demo simple;
  en un caso real conviene restringir el acceso a un bucket/prefijo concreto, como se hizo en la
  infraestructura CDK del proyecto).

Nombre de ejemplo para el rol: `lambda-kinesis-role`.

### Crear la función y el trigger

1. Crear la función Lambda (runtime Python), asignando el **rol existente** creado en el paso
   anterior en vez del rol de ejecución por defecto.
2. Añadir un **trigger** desde el resumen de la función:
   - **Origen**: Kinesis.
   - **Stream**: el stream creado anteriormente.
   - **Consumer**: se deja vacío — no se usa un consumidor dedicado (modelo estándar, sin enhanced
     fan-out).
   - **Batch size**: se deja el valor por defecto (se podría ajustar si llegan muchos registros por
     segundo).
   - **Starting position**:
     - **Trim horizon** — el shard iterator más antiguo disponible.
     - **Latest** — el más reciente (el que se usa en esta demo, para procesar solo los registros
       que entren a partir de ahora).

### Código de la función

El código obtiene los registros del evento de Kinesis, decodifica el payload en base64, construye un
nombre de archivo a partir de la partition key y el timestamp, y lo escribe en el bucket S3 (el nombre
del bucket hay que ajustarlo al propio).

> ⚠️ Tras pegar/editar el código hay que hacer clic en **Deploy** para que los cambios surtan efecto.

### Prueba

Al introducir registros adicionales en el stream con `put-record` (CLI), los objetos aparecen casi de
inmediato en el bucket S3 — el trigger dispara la función en **tiempo real**.

Esto es útil porque el stream, por defecto, solo retiene los datos **24 horas**: persistirlos en S3
permite conservarlos para análisis a más largo plazo.
