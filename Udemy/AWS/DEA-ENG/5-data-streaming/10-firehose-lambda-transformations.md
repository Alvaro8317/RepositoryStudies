# Práctica: Transformaciones con AWS Lambda en Data Firehose

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Continuación de la práctica anterior ([[9-practice-data-firehose]]): se añade una transformación de
registros "sobre la marcha" usando **AWS Lambda** en el mismo delivery stream de Firehose.

## Ubicación de las opciones de transformación

Dentro del delivery stream, en **Configuration**, aparece la sección **Transform and convert
records** (junto a los ajustes de destino, que también se pueden editar desde ahí — por ejemplo,
algunos parámetros del bucket S3).

> ⚠️ La **partición dinámica (dynamic partitioning)** solo se puede activar en el momento de crear el
> stream — no se puede añadir después editando la configuración. Es útil porque evita que los datos se
> acumulen todos juntos y en su lugar los distribuye en subcarpetas, lo que mejora la eficiencia y el
> rendimiento del consumo posterior.

## Conversión de formato vs. transformación con Lambda

En la pantalla de edición hay dos opciones independientes:

- **Convert record format** — permite convertir el formato de salida (ej. a Parquet/ORC) activando una
  casilla y especificando el formato deseado.
- **Transform source records with AWS Lambda** — permite aplicar transformaciones de datos
  personalizadas mediante una función Lambda. Es la opción usada en esta práctica.

## Creación de la función Lambda desde Firehose

Al activar la transformación con Lambda, se puede elegir una función:

- Navegando por las funciones existentes, o
- Introduciendo directamente el ARN.

También se puede **crear una nueva función** directamente desde ahí, que es el camino seguido en esta
práctica.

### Blueprints (planos)

Al crear la función se ofrecen **blueprints** (plantillas preconstruidas) que ya traen la
configuración base de la función. Buscando por "firehose" aparecen varias opciones, entre ellas:

- **Process records sent to a Firehose delivery stream** (disponible tanto en Node.js como en
  Python) — plano genérico de procesamiento de registros de Firehose, que devuelve cada registro con
  un estado de procesamiento (`Ok`, `Dropped`, `ProcessingFailed`).

Se elige este blueprint por defecto y se confirma con **Use blueprint**.

### Configuración de la función

- **Nombre**: se le da un nombre descriptivo (ej. `firehose-function-test`).
- **Runtime**: se puede cambiar si se elige otro blueprint (ej. Python en vez de Node.js).
- **Execution role**: como en cualquier función Lambda, hay que elegir un rol de ejecución. En esta
  práctica se reutiliza un rol ya creado previamente con permisos para escribir en el bucket S3, en
  lugar de crear uno nuevo por defecto.

### Código por defecto del blueprint

El código que trae el blueprint:

1. Decodifica (`decode`) cada registro recibido.
2. Vuelve a codificar (`encode`) la salida.
3. Devuelve la cantidad de registros procesados con éxito.

No se necesita ningún cambio adicional para esta práctica — aquí es donde normalmente se añadiría
lógica personalizada (conversiones, filtrado, enriquecimiento, etc.). Se deja el código por defecto y
se crea la función.

## Selección de la función en el delivery stream

De vuelta en la configuración del delivery stream:

1. Se activa **Transform source records with AWS Lambda**.
2. Se navega para seleccionar la función recién creada.

> ⚠️ La función recién creada puede **tardar un poco en aparecer** en la lista al navegar — puede ser
> necesario refrescar la pantalla.

En esta pantalla también se puede seguir ajustando el **tamaño de buffer** y el **intervalo de
buffer** (en esta práctica, 60 segundos), y opcionalmente convertir el formato de grabación (aunque
esto también podría resolverse como parte de la lógica del código de la función Lambda). No se hacen
cambios adicionales — solo se selecciona la función para las transformaciones. Se guardan los cambios
y el delivery stream vuelve a quedar en estado **Active**.

## Prueba del flujo completo

Desde **CloudShell**, se reutilizan los mismos comandos `put-record` de la práctica anterior.

> ⚠️ Los registros se envían al **Kinesis Data Stream** (la fuente), no directamente al delivery
> stream de Firehose — es el stream de Kinesis el origen configurado en Firehose.

Se envían varios registros (se puede reutilizar el mismo comando varias veces sin problema). El
procesamiento es casi en tiempo real, así que puede tardar uno o dos minutos en verse reflejado en el
bucket S3 de destino.

Al refrescar el bucket, los objetos aparecen organizados automáticamente en subcarpetas por **año,
mes y día** (el prefijo por defecto basado en tiempo que aplica Firehose, distinto de la partición
dinámica). Se puede descargar cualquiera de los archivos generados y abrirlo con un editor de texto
para comprobar los registros procesados.

> ⚠️ El propósito de la función Lambda es únicamente **transformar/procesar los datos dentro del
> flujo** — no es responsable de la entrega al destino. La entrega al bucket S3 configurado como
> destino del delivery stream ocurre automáticamente después de la transformación.

## Limpieza de recursos

Al terminar, es importante eliminar los recursos creados para evitar costes innecesarios:

1. **Delivery stream de Firehose** — eliminar primero, desde la consola de Firehose.
2. **Kinesis Data Stream** — eliminar después, desde la consola de Kinesis (acción **Delete**).

En ambos casos la consola pide confirmar escribiendo `delete` antes de completar el borrado.
