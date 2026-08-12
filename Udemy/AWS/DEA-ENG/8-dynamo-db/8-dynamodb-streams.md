# DynamoDB Streams

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**DynamoDB Streams** permite hacer un seguimiento (tracking) de los cambios realizados en una tabla:
captura **todas** las operaciones de escritura (inserciones, actualizaciones y eliminaciones) y las
ordena cronológicamente en un stream, listo para ser consumido y procesado en tiempo real. Esto abre
la puerta a una amplia gama de casos de uso en tiempo real basados en esos cambios.

> ⚠️ Los streams **no están activados por defecto** — hay que habilitarlos explícitamente en la tabla.
> Además, no son retroactivos: solo se capturan los cambios que ocurren **después** de activar el
> stream, nunca los anteriores.

## Funcionamiento

- Cada cambio se organiza en un **registro (record)**, y un registro representa **una única operación
  de escritura completa** — si esa operación modifica varios atributos a la vez, todos esos cambios
  quedan reflejados en el mismo registro.
- Los registros están disponibles para ser consumidos **casi en tiempo real**.
- Internamente, el stream se organiza en **shards**, de forma similar a [[../5-data-streaming/3-kinesis-data-streams|Kinesis Data Streams]]
  — pero, a diferencia de Kinesis, AWS gestiona automáticamente la capacidad y el número de shards; no
  hay que administrarlos.
- Los datos de un stream se retienen durante **24 horas**.

## Opciones del stream (`StreamViewType`)

Definen exactamente qué información se captura en cada registro:

| Opción                 | Qué captura                                                                     | Cuándo usarla                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **KEYS_ONLY**          | Solo los **atributos clave** del elemento modificado                            | Cuando basta con saber *que* un elemento cambió, sin necesitar el detalle                             |
| **NEW_IMAGE**          | Todos los atributos del elemento, **tal como quedan tras** la modificación      | Cuando se necesita conocer el estado resultante (ej. procesar el nuevo valor con Lambda)              |
| **OLD_IMAGE**          | Todos los atributos del elemento, **tal como estaban antes** de la modificación | Cuando se necesita saber el estado previo al cambio                                                   |
| **NEW_AND_OLD_IMAGES** | Ambas imágenes (antes y después) de todos los atributos                         | Vista más completa — útil para **auditoría** o registro, ya que muestra exactamente qué cambió y cómo |

> La opción a elegir depende del caso de uso: para auditoría/logging conviene `NEW_AND_OLD_IMAGES`
> (imagen completa del cambio); para procesar solo el resultado (ej. una función Lambda que reacciona
> al nuevo valor) suele bastar con `NEW_IMAGE`.

## Casos de uso

Los casos de uso suelen girar en torno a una **arquitectura basada en eventos**:

- **AWS Lambda** — ejecutar código personalizado en respuesta a cada cambio (el patrón más común).
- **Kinesis Data Firehose** — distribuir los cambios hacia destinos como **S3** o **Amazon Redshift**.
- **Kinesis Data Streams** — capturar el stream de cambios para procesarlo con más flexibilidad.
- **Clústeres de Elasticsearch** — mantenerlos sincronizados con los datos de DynamoDB, útil para
  búsqueda y analítica.
- **Aplicaciones propias** — usando el **Kinesis Client Library (KCL)**, que simplifica el consumo de
  streams tanto de Kinesis Data Streams como de DynamoDB Streams, para sincronizar datos entre sistemas
  o procesamiento más complejo.
- **AWS Glue** — incorporar los cambios en un proceso ETL.
- **Replicación multi-región** — propagar los cambios de una tabla a otra región, para mantener los
  datos disponibles y consistentes en varias regiones.

## Ejemplo: procesar cambios con Lambda

1. **Habilitar el stream** en la tabla y elegir el `StreamViewType` (ej. `KEYS_ONLY`, `NEW_IMAGE`,
   `OLD_IMAGE` o `NEW_AND_OLD_IMAGES`).
2. **Crear la función Lambda** con el código que debe ejecutarse en respuesta a cada cambio.
3. **Configurar el stream como trigger** de la función, mediante un **event source mapping**: cada vez
   que aparece un nuevo registro en el stream, se invoca automáticamente la función Lambda.
