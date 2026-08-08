# Troubleshooting común en Kinesis Data Streams

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Problemas frecuentes en flujos de datos, muchos relacionados con el rendimiento, y cómo resolverlos.
Contenido teórico relevante para el examen.

## Problemas del lado del productor

### Tasas de escritura lentas / throughput exceptions

- Suelen deberse a **límites de servicio** o **límites de tasa de API** (rate limits), visibles como
  excepciones de rendimiento (throughput exceptions) al superar la capacidad del stream.
- Algunas llamadas a nivel de stream (ej. `CreateStream`, `DeleteStream`) tienen límites de **5 a 20
  llamadas por segundo**.
- **Solución**: monitorizar las excepciones de rendimiento para detectar si la aplicación productora
  está chocando con algún límite de servicio; si es así, aumentar el **número de shards**.

### Shards calientes (hot shards)

- Una estrategia de **partition key** poco eficaz puede distribuir los datos de forma desigual entre
  shards, sobrecargando algunos más que otros — esto son los **hot shards**.
- **Solución**:
  - Elegir una estrategia de partición que distribuya los datos de forma **uniforme** entre shards.
  - Monitorizar las **métricas a nivel de shard** para identificar shards calientes.

### Ineficiencia por lotes muy pequeños

- Con alto rendimiento, procesar registro a registro (llamadas API individuales muy pequeñas) es poco
  eficiente.
- **Solución**: usar **estrategias de batching** — procesar varios registros por lote en una sola
  llamada.

## Problemas del lado del consumidor

### Tasas de lectura más lentas de lo esperado

- Similar al caso de escritura: puede deberse a **límites de shard**.
- **Solución**: aumentar el **número de shards**.

### Límite máximo de `get-records` mal configurado

- Un valor demasiado bajo en el número máximo de registros por `get-records` puede limitar
  artificialmente el rendimiento de lectura.
- **Solución**: volver a los **valores por defecto** del sistema.

### Problemas en la lógica de procesamiento

- Si el consumidor tiene problemas, probar con registros vacíos/de prueba y revisar la lógica del
  código para mejorar el rendimiento.

## Otras cuestiones comunes

### `GetRecords` devuelve un array vacío

No es necesariamente un error:

- Cada llamada a `get-records` devuelve un **Shard Iterator** que hay que reutilizar en la siguiente
  llamada (normalmente dentro de un bucle). Solo es **nulo** cuando el shard se ha **cerrado**.
- Un array vacío puede darse por dos motivos:
  1. **No hay datos en el shard** — puede que el periodo de retención haya expirado o que no se haya
     escrito nada todavía.
  2. **No hay datos justo en la posición** a la que apunta el iterador — los datos pueden estar más
     adelante en el shard.
- Con la **Kinesis Client Library (KCL)** esto se gestiona automáticamente. Si se implementa
  manualmente con el AWS SDK, hay que manejarlo explícitamente en el código.

### Registros omitidos (skipped records)

- Suele deberse a **excepciones no gestionadas** en la lógica de procesamiento.
- **Solución**: revisar el manejo de excepciones en el código de procesamiento de registros.

### El Shard Iterator caduca inesperadamente

- Un Shard Iterator caduca de forma natural a los **5 minutos** sin uso — esto es normal.
- Si caduca de forma **inesperada en producción**, puede deberse a que, con un número muy alto de
  shards, la tabla de **DynamoDB** que usa Kinesis (KCL) internamente no tiene suficiente **capacidad
  de escritura** para almacenar los datos de seguimiento.
- **Solución**: aumentar la capacidad de escritura de esa tabla DynamoDB.

### Los consumidores se están quedando atrás (consumer lag)

Pasos a seguir:

1. **Aumentar el periodo de retención** — para no perder datos de forma permanente mientras se
   investiga y resuelve el problema.
2. **Monitorizar el retraso** con las métricas **`IteratorAgeMilliseconds`** / **`MillisBehindLatest`**.
3. Interpretar el patrón:
   - **Picos puntuales (spiky)** — normalmente un problema transitorio (ej. fallos de API) que se
     resuelve solo; se puede ignorar.
   - **Aumento constante y creciente** — indica un problema real: lógica de procesamiento ineficiente
     o recursos insuficientes.
   - **Solución**: aumentar el **número de shards** o mejorar la **lógica de procesamiento**.

### Errores de permisos de KMS

- Ocurre al leer/escribir en un stream **cifrado** sin los permisos necesarios.
- **Solución**: asegurar permisos suficientes sobre la **clave KMS** correcta (y ajustar las
  **políticas de IAM** si es necesario) para poder cifrar/descifrar los datos.
