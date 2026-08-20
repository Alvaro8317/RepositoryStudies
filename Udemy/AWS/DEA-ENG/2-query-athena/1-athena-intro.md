# Amazon Athena — Introducción

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon Athena?

**Amazon Athena** es un servicio de **consulta interactiva** de AWS que permite consultar, mediante
**SQL estándar**, archivos almacenados directamente en un bucket de **S3** — sin moverlos ni copiarlos.

- Soporta datos no estructurados o semiestructurados: **CSV**, **Avro**, **Parquet**, entre otros.
- Para poder consultarlos, los archivos deben estar previamente registrados (esquema + metadatos) en
  el **Glue Data Catalog** — es decir, como bases de datos y tablas.

## Características clave

| Característica         | Descripción                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Serverless**         | No hay infraestructura que gestionar; se aprovisiona automáticamente según necesidad.                                |
| **Alta escalabilidad** | Escala automáticamente al crecer el volumen de datos.                                                                |
| **Alto rendimiento**   | Consultas SQL rápidas sobre los datos del Data Catalog.                                                              |
| **Pago por uso**       | El coste depende del **número de consultas** y la **cantidad de datos analizados**, no de infraestructura reservada. |

## Flujo de trabajo típico

1. Los archivos se almacenan en un bucket de **S3** (data lake).
2. Un **Glue Crawler** escanea esos archivos, infiere el esquema y crea/actualiza las tablas
   correspondientes en el **Glue Data Catalog**.
3. Con las tablas ya registradas en el Data Catalog, se consultan los datos directamente con
   **Athena** usando SQL — los datos siguen físicamente en S3.
4. Los resultados de Athena pueden usarse, a su vez, como fuente de datos para otras aplicaciones.

> ⚠️ Athena no almacena datos por sí misma: consulta directamente los archivos en S3, apoyándose en
> el esquema definido en el Glue Data Catalog (alimentado por los Glue Crawlers).

## Schema-on-read

- Athena aplica **schema-on-read** (esquema al leer): los datos en S3 se guardan tal cual, **sin
  cambiar los datos originales**.
- El esquema definido en el Glue Data Catalog se **proyecta** sobre esos datos únicamente **en el
  momento de la consulta**, traduciéndolos a un formato estructurado similar al de una base de
  datos relacional.
- Esto contrasta con el enfoque tradicional de las bases de datos relacionales (**schema-on-write**),
  donde el esquema se aplica y valida al **escribir** los datos.

## Seguridad

- Athena usa **IAM** (para controlar qué usuarios/roles pueden ejecutar qué acciones) y **ACLs**
  (Access Control Lists) para controlar el acceso tanto a los **datos** como a las **consultas**.

## Integraciones

| Herramienta / opción  | Uso                                                                   |
| --------------------- | --------------------------------------------------------------------- |
| **Amazon QuickSight** | Visualización de datos e informes a partir de resultados de Athena.   |
| **Drivers ODBC**      | Conectar Athena a otras aplicaciones externas.                        |
| **Amazon Kinesis**    | Integración con fuentes de datos en streaming (se verá más adelante). |

## Casos de uso

- **Análisis de logs**: analizar registros almacenados en un bucket S3 directamente con SQL.
- **Análisis exploratorio de datos (ad hoc)**: consultas rápidas e interactivas, útiles por ejemplo
  para data scientists que necesitan explorar archivos sin procesos previos.
- **Data lakes sobre S3**: Athena permite consultar los datos del lago con buen rendimiento y
  conectarlos a herramientas de visualización/reporting para construir informes.
