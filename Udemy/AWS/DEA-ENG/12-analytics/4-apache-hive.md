# Apache Hive

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Apache Hive** es un sistema de **data warehouse distribuido**, construido sobre **Apache
Hadoop**, que facilita la consulta y gestión de datos que residen en almacenamiento distribuido.

## Conceptos clave

- Los datos se almacenan como **tablas estructuradas**, en diversos formatos (texto plano,
  **Parquet**, etc.) dentro de **HDFS** o de otros sistemas de almacenamiento compatibles (ej.
  **S3**).
- Se pueden consultar con un lenguaje similar a SQL llamado **HiveQL**, lo que lo hace muy
  accesible para analistas de datos que ya conocen SQL.

## Hive Metastore

- El **Hive Metastore** es el repositorio central de **metadatos** sobre las tablas de Hive: tipos
  de datos, columnas, ubicación de los archivos, etc.
- Es conceptualmente similar al **AWS Glue Data Catalog**.
- Estos metadatos son necesarios para ejecutar cualquier consulta Hive: dónde están los datos, cómo
  están formateados y cómo deben leerse/procesarse.

## Hive en AWS (sobre EMR)

- Hive puede venir **preinstalado** en clústeres de **EMR**.
- Al ejecutarse sobre EMR, se integra fácilmente con otros servicios de AWS: **S3** para
  almacenamiento de datos, **Glue Data Catalog** para metadatos, o bases de datos adicionales como
  **Redshift** o **Amazon RDS**.

### Migración de un Hive on-premises a la nube

- La forma más sencilla de migrar un sistema Hive on-premises es crear un clúster **EMR** y migrar
  directamente la carga de trabajo existente — Hive se ejecuta igual, pero gestionado en la nube.
- Una vez el Hive Metastore corre sobre EMR, también se puede migrar a **Glue Data Catalog** — por
  ejemplo, con un job **ETL** que extraiga los metadatos del Hive Metastore y actualice el Glue
  Data Catalog.

> ⚠️ El Glue Data Catalog es compatible con Hive y es completamente **serverless**, por lo que
> suele ser la opción más sencilla frente a mantener un Hive Metastore propio.

### Usar Glue Data Catalog como metastore de Hive

- Es posible usar el **Glue Data Catalog** como metastore para las cargas de trabajo Hive que
  corren en EMR, en lugar de (o junto con) el Hive Metastore tradicional.
- Esto permite ejecutar consultas Hive directamente sobre datos catalogados en Glue Data Catalog,
  usándolo como repositorio central de metadatos para ambas plataformas — sin duplicar datos.
