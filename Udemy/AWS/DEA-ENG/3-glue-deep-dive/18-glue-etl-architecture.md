# Arquitectura y operativa de ETL Jobs en AWS Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Flujo general

Un **ETL Job** de Glue conecta un origen de datos, ejecuta la lógica de extracción, transformación y
carga, y actualiza (opcionalmente) el **Glue Data Catalog**:

1. **Orígenes de datos**: bucket **S3**, **Amazon RDS**, **Amazon Redshift**, u otras bases de datos
   accesibles vía **JDBC** — incluso combinando varias fuentes a la vez en un mismo job.
2. **Job**: ejecuta el script (generado automáticamente o personalizado) que hace **extract →
   transform → load**, sobre un motor **Spark** gestionado por Glue.
3. **Destinos**: los datos transformados se cargan en S3, Redshift, RDS, o cualquier otro destino
   compatible con JDBC.

El **Glue Crawler** y el **Glue Data Catalog** también forman parte de este flujo: el crawler
escanea los orígenes y alimenta el catálogo con metadatos/esquema, que luego el job puede consultar
o actualizar (ver `1-data-ingestion/3-glue.md`).

## Cifrado

Los ETL Jobs de Glue soportan dos capas de cifrado:

- **En reposo (server-side encryption)**: los datos almacenados quedan cifrados.
- **En tránsito**: mediante **SSL**.

## Ejecución: schedule vs. trigger basado en eventos

Además de la ejecución programada (**schedule**, ver `5-schedules.md`), los jobs se pueden lanzar
mediante **triggers**: desencadenadores que automatizan la ejecución de un job en respuesta a un
**evento** (por ejemplo, la llegada de un archivo nuevo), en vez de a una hora fija.

## Dimensionar DPUs con métricas de trabajo

Los ETL Jobs se pueden acelerar aprovisionando más **DPUs** (ver `1-glue-cost.md` para el modelo de
coste), pero conviene saber cuántas son realmente necesarias antes de sobre-aprovisionar:

- Se pueden habilitar **métricas del trabajo (job metrics)**, que ayudan a entender qué número de
  DPUs requiere un job concreto para un rendimiento adecuado, evitando pagar de más por capacidad
  que no se llega a usar.

## Manejo de errores: CloudWatch y SNS

- Los errores que se producen durante la ejecución de un ETL Job se reportan a **Amazon
  CloudWatch**, donde se pueden visualizar.
- CloudWatch se puede integrar con **Amazon SNS** para enviar notificaciones al equipo (email, SMS,
  etc.) cuando ocurre un error, sin necesidad de estar consultando CloudWatch manualmente.

## Boto3: interactuar con Glue desde scripts ETL

- **Boto3** es el **SDK de AWS para Python**, y es la biblioteca habitual usada dentro de los scripts
  ETL de Glue para interactuar programáticamente con el **Glue Data Catalog** y otros servicios de
  AWS (por ejemplo, para leer/actualizar metadatos desde el propio script).

> ⚠️ No confundir Boto3 con **PySpark**: PySpark es el motor/API de procesamiento de datos (Spark en
> Python) que ejecuta la lógica de transformación, mientras que Boto3 es el SDK de AWS que permite
> hablar con los servicios de AWS (Glue Data Catalog incluido) desde el mismo script.
