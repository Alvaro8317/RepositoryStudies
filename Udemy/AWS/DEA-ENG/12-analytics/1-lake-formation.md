# AWS Lake Formation

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**AWS Lake Formation** ayuda a construir y configurar un **data lake seguro y bien organizado**.
Un data lake puede ser bastante complejo de gestionar, y Lake Formation automatiza y controla
muchas de esas tareas.

Se construye **sobre AWS Glue**: puede gestionar todos los procesos que también gestiona Glue.

## Qué gestiona Lake Formation

Lake Formation cubre todos los aspectos de un data lake:

- **Recopilación de datos**: automatiza la ingesta de datos hacia el data lake — normalmente
  almacenado en buckets de **S3**.
- **Catalogación de datos**: automatiza el registro de los datos en el **AWS Glue Data Catalog**,
  para que puedan buscarse y gestionarse desde todos los servicios.
- **Limpieza y transformación de datos**: se apoya en **AWS Glue** para estas tareas.
- **Seguridad y control de acceso**: ofrece **control de acceso de grano fino**, para gestionar
  con precisión quién puede ver qué datos concretos. Está integrado con **IAM**.
- **Data sharing entre cuentas de AWS**: permite compartir datos de forma segura entre distintas
  cuentas de AWS, usando **AWS Resource Access Manager (RAM)**.
- **Integración con otros servicios de análisis**: funciona junto a **Amazon Redshift** y
  **Amazon Athena**, entre otros.

## Blueprints

Los **blueprints** son **plantillas** para las tareas de ingesta de datos más habituales.

- Ayudan a **automatizar** el proceso de cargar datos en el data lake, por ejemplo desde bases de
  datos o almacenes de objetos como buckets S3.

## Cómo funciona

1. **Especificar el origen de los datos**: puede ser un servicio (S3, RDS, DynamoDB) o una base
   de datos on-premises. Lake Formation permite integrar todas esas fuentes en un data lake
   centralizado.
2. **Ingesta automatizada con blueprints**: una vez definidas las fuentes, Lake Formation usa
   blueprints para automatizar la ingesta de los datos.
3. **Catalogación**: a medida que se ingieren, Lake Formation cataloga cada objeto en el **AWS
   Glue Data Catalog** — el catálogo centralizado que clasifica y organiza los datos según sus
   metadatos (tipo, fecha de creación, etc.), haciéndolos **buscables y accesibles**.
4. **Limpieza y transformación**: estructura los datos en un formato más utilizable, eliminando
   datos inservibles y mejorando su calidad. Para esto, Lake Formation se integra con **AWS
   Glue**, usando jobs de transformación para operaciones ETL más complejas.
5. **Seguridad**: aplica políticas de seguridad de grano fino sobre los datos ya ingeridos y
   catalogados.
6. **Análisis**: con los datos ya organizados y seguros en el data lake, se pueden usar distintos
   servicios de análisis y machine learning:
   - **Amazon Redshift**: consulta los datos directamente desde S3 usando el Glue Data Catalog.
     Con [Redshift Spectrum](../9-redshift-data-warehouse/13-redshift-spectrum.md) se pueden
     consultar tablas gestionadas por Lake Formation, que también controla los permisos de acceso.
   - **Amazon Athena**: también usa el Glue Data Catalog, y Lake Formation puede gestionar los
     permisos que se aplican directamente sobre los datos consultados por Athena.
   - **Amazon SageMaker**: para machine learning, puede integrarse con datos gestionados por Lake
     Formation.

> ⚠️ La ventaja clave de Lake Formation es centralizar tanto la **organización** (catalogación,
> limpieza) como los **permisos** del data lake, de forma que ese mismo control de acceso se
> respeta automáticamente al consultar los datos desde Redshift, Athena o SageMaker.
