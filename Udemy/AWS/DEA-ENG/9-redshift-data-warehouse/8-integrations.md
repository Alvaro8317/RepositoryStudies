# Redshift: integraciones

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Redshift se integra con múltiples servicios de AWS. La integración más importante es, probablemente,
con **S3**.

## Resumen de integraciones

| Servicio / comando                    | Qué permite                                                                           |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| **COPY**                              | Copiar datos desde un bucket de **S3** existente hacia Redshift.                      |
| **UNLOAD**                            | Exportar (descargar) datos desde Redshift a un bucket de **S3**.                      |
| **Redshift Spectrum**                 | Consultar datos almacenados en **S3** directamente, sin necesidad de copiarlos.       |
| **Amazon EMR**                        | Cargar datos desde un clúster EMR a Redshift.                                         |
| **AWS Lambda**                        | Invocar una función Lambda **desde dentro de una consulta** de Redshift.              |
| **AWS DMS**                           | Usar una base de datos de Redshift como **destino (target)** para AWS DMS.            |
| **Amazon EC2**                        | Cargar datos desde instancias EC2 a Redshift.                                         |
| **AWS Data Pipeline**                 | Automatizar el movimiento y/o transformación de datos hacia/desde tablas de Redshift. |
| **Kinesis Data Streams / Amazon MSK** | **Streaming ingestion**: ingesta de datos de streaming directamente en Redshift.      |
| **DynamoDB**                          | Cargar datos en una tabla de Redshift desde una única tabla de DynamoDB.              |
| **Amazon Aurora (Zero-ETL)**          | Replicar cambios de Aurora en Redshift segundos después de producirse.                |

## Streaming ingestion

- Permite integrar **Kinesis Data Streams** y **Amazon MSK** (Managed Streaming for Apache Kafka)
  directamente con Redshift.
- Proporciona **ingesta de datos de streaming de alta velocidad y baja latencia**.
- Los datos de streaming se transmiten directamente a **vistas materializadas** (tratadas en otra
  parte del curso).
- Reduce el **tiempo de acceso a los datos** y el **coste de almacenamiento**, al no requerir un
  paso intermedio de staging.

## Comando COPY (S3 → Redshift)

- Sintaxis general: `COPY <tabla_destino> FROM <fuente> <autorización>`.
- Usa **procesamiento paralelo masivo (MPP)** para cargar grandes cantidades de datos — lee y
  carga los datos en paralelo.
- Puede cargar datos desde **múltiples fuentes** a la vez (ej. varios archivos en S3).
- Analiza los datos cargados para determinar automáticamente el **esquema de compresión óptimo**
  con el que almacenarlos (ej. **gzip**, entre otros disponibles).
- Es mucho **más rápido y eficiente** que usar `INSERT` para cargar grandes volúmenes de datos —
  es el método recomendado para cargar desde S3.
- **Descifra** los datos cargados desde S3 si están cifrados.
- Requiere:
  - Un **archivo de manifiesto (manifest file)**.
  - Un **rol IAM** que permita a Redshift acceder al bucket de S3.

## Comando UNLOAD (Redshift → S3)

- Exporta datos desde Redshift hacia un bucket de S3.
- También aprovecha las capacidades de **procesamiento paralelo** para acelerar la exportación.
- Soporta varios **formatos de exportación**: **Parquet**, **CSV**, **ORC**.

## Auto-copy desde S3

- Redshift permite configurar la **copia automática** de datos desde S3 hacia una base de datos de
  Redshift, usando la interfaz de la consola, sin tener que ejecutar `COPY` manualmente cada vez.

## Enrutamiento de red: pública vs. Enhanced VPC Routing

- El tráfico de red generado por `COPY`, `UNLOAD` y **Redshift Spectrum** pasa por una **interfaz
  de red** interna al cluster de Redshift, que está **fuera de la VPC** del usuario.
- Por defecto, ese tráfico se **enruta a través de Internet pública** para llegar a su destino.
- Se puede activar **Redshift Enhanced VPC Routing** para que, en su lugar, el tráfico se **enrute
  a través de la VPC** del usuario.

## Amazon Aurora Zero-ETL Integration

- Permite que los cambios realizados en una base de datos **Aurora** se **repliquen en Redshift**
  **segundos después** de producirse la actualización.
- Al ser una integración directa, **elimina la necesidad de pipelines de datos personalizados**
  entre Aurora y Redshift.

> ⚠️ El comando `COPY` es la forma recomendada de cargar grandes volúmenes de datos en Redshift —
> es mucho más rápido que `INSERT` porque aprovecha el procesamiento paralelo masivo del cluster.
