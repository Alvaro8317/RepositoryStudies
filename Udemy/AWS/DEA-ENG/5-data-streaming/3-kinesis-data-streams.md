# Kinesis Data Streams (KDS)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Flujo general

Kinesis Data Streams se encarga de **capturar e ingerir** el flujo de datos. El recorrido básico es:

**Productores** → escriben registros en el **stream** (dividido en **shards**) → **Consumidores** leen
esos registros para procesarlos.

## Productores (Producers)

Los productores son la **fuente de los datos**: cualquier dispositivo o aplicación que genera el flujo
y lo escribe en el Kinesis Data Stream. Hay varias formas de implementarlos:

| Opción                             | Cuándo usarla                                                                                                                                                                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS SDK**                        | Aplicaciones personalizadas que necesitan control total: permite personalizar todos los detalles de bajo nivel (batching, gestión de errores, etc.). Es la opción más **flexible**.                                                         |
| **Kinesis Producer Library (KPL)** | Aplicaciones de **muy alto rendimiento** que necesitan enviar grandes volúmenes de datos de forma eficiente. Ya trae optimizaciones y maneja tareas complejas (ej. reintentos por lotes) que con el SDK habría que implementar manualmente. |
| **Kinesis Agent**                  | Aplicación **pre-construida** para ingerir datos de logs en servidores, sin necesidad de escribir código — solo se configura.                                                                                                               |

## Registros de datos (Data Records)

- Un **data record** es la unidad de datos que un productor escribe en el stream.
- Puede contener datos estructurados o no estructurados (ej. objetos JSON), hasta **1 MB** por
  registro.
- Cada registro incluye, además del dato en sí, una **partition key**.
- La partition key es procesada por un algoritmo que **asigna cada registro a un shard específico**,
  lo que permite procesar los datos **en paralelo** de forma eficiente.

## Shards

Los shards son las **unidades de capacidad de procesamiento** del stream.

| Dirección           | Límite por shard                                           |
| ------------------- | ---------------------------------------------------------- |
| Escritura (entrada) | 1 MB/s **o** 1.000 registros/s (lo que se alcance primero) |
| Lectura (salida)    | 2 MB/s                                                     |

- El **número de shards** determina la capacidad total de ingesta y procesamiento del stream: a mayor
  rendimiento necesario, más shards se requieren.
- Gracias a las partition keys, los datos se procesan en paralelo entre shards.

### Resharding: Merge y Split

En modo **Provisioned**, el número de shards se puede ajustar manualmente mediante dos operaciones:

| Operación | Efecto                                                                                                                                                                                               |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Split** | Divide un shard en **dos**, aumentando la capacidad del stream. Se usa típicamente para dividir un **shard "caliente" (hot shard)** — uno que recibe desproporcionadamente más tráfico que el resto. |
| **Merge** | Fusiona **dos shards en uno**, reduciendo la capacidad del stream y **ahorrando costes**.                                                                                                            |

## Retención y durabilidad

- Los datos se retienen por defecto **24 horas** (también el valor mínimo).
- El periodo de retención se puede extender hasta **365 días**.
- Por durabilidad, los datos se **replican en varias zonas de disponibilidad (AZs)**, aumentando la
  resiliencia ante fallos.

> ⚠️ Los datos en un Kinesis Data Stream son **inmutables**: una vez escritos, no se pueden eliminar ni
> modificar. Solo desaparecen automáticamente al vencer el periodo de retención.

## Escalado y modos de capacidad

Los shards se pueden añadir o quitar de dos formas:

- **Manualmente**, añadiendo shards dinámicamente cuando se necesita más capacidad.
- **Automáticamente**, mediante autoescalado elástico según la demanda.

Esto se traduce en dos **modos de capacidad**:

| Modo            | Descripción                                                                                                                                               | Cobro                                      |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Provisioned** | El número de shards se especifica **manualmente** y se puede aumentar/disminuir.                                                                          | Tarifa por hora según el número de shards. |
| **On-demand**   | Escala automáticamente en función de los picos de rendimiento de los **últimos 30 días**. Empieza con un valor por defecto de 4 MB/s (4.000 registros/s). | Según el rendimiento **real** utilizado.   |

## Consumidores (Consumers)

Los consumidores leen los registros del stream para procesarlos posteriormente:

- **Aplicación personalizada con AWS SDK** — control total sobre la lectura.
- **Kinesis Client Library (KCL)** — forma eficiente de construir aplicaciones consumidoras de alto
  rendimiento y alta escalabilidad, análoga a la KPL del lado productor.
- **Otros servicios de AWS conectados directamente al stream:**
  - **Kinesis Firehose** — para cargar los datos de forma robusta y escalable en distintos destinos.
  - **Managed Apache Flink** (antes Kinesis Data Analytics) — para análisis complejos (SQL, apps Flink)
    sobre el stream.
  - **AWS Lambda** — para ejecutar código ligero y personalizado en respuesta al flujo de datos, de
    forma serverless (sin gestionar servidores) y con autoescalado automático según el volumen de
    datos.
