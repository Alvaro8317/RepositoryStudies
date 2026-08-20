# Redshift Spectrum

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Redshift Spectrum** es una característica que permite consultar datos que se encuentran en
**buckets de S3** directamente desde Redshift, sin necesidad de cargarlos físicamente en tablas.

Es un concepto similar a las [Federated Queries](11-federated-queries.md), pero en lugar de
consultar datos en otras bases de datos, permite consultar datos almacenados en **S3**.

## Caso de uso

- Se utiliza especialmente para consultar **grandes cantidades de datos** almacenadas en S3, en
  distintos formatos.
- Los datos se quedan en S3 — **no se cargan** físicamente en Redshift.
- Se consultan con **SQL estándar**, como si fueran tablas normales de Redshift.
- Permite **omitir el ETL**: los datos están disponibles para consultar directamente, sin
  necesidad de moverlos primero al data warehouse.
- Soporta distintos **formatos de datos** y compresión, incluyendo **gzip** y **snappy**.

## Cómo funciona

1. Se configuran **tablas externas** en Redshift, que solo **definen la estructura** de los datos
   (esquema) — la ubicación física de los datos sigue estando en S3, no se mueven.
2. Al ejecutar una consulta en Redshift que hace referencia a una tabla externa, **Spectrum se
   encarga automáticamente** de recuperar de S3 solo los datos necesarios para esa consulta.
3. Las tablas externas se registran en un **catálogo de datos externo**, que puede ser:
   - **AWS Glue Data Catalog**.
   - **Amazon Athena**.
   - **Apache Hive Metastore**.
4. Cuando se realizan cambios en los datos externos (en S3), esos cambios están **disponibles
   automáticamente** para cualquier consulta del clúster de Redshift.
5. Opcionalmente, las tablas externas se pueden **particionar** por una o varias columnas, lo que
   puede **mejorar el rendimiento** de las consultas.
6. Una vez definidas, las tablas externas se pueden **unir (JOIN)** con tablas normales de
   Redshift, igual que con cualquier otra tabla.

### Ejemplo práctico

```sql
CREATE EXTERNAL SCHEMA SPECTRUM_SCHEMA
FROM DATA CATALOG DATABASE 'spectrum_db' IAM_ROLE 'arn:aws:iam::123456789012:role/service-role/AmazonRedshift-CommandsAccessRole-20260819T202502'
CREATE EXTERNAL DATABASE IF NOT EXISTS;

CREATE EXTERNAL TABLE SPECTRUM_SCHEMA.ORDERS (
    ORDER_ID VARCHAR(20),
    ORDER_DATE VARCHAR(20),
    CUSTOMER_NAME VARCHAR(100),
    STATE VARCHAR(20),
    CITY VARCHAR(20)
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://alvaro8317-dea-certification-prod/redshift_spectrum/';

SELECT
    *
FROM
    "awsdatacatalog"."spectrum_db"."orders";
```

## Arquitectura y rendimiento

- Redshift Spectrum se ejecuta en **servidores dedicados**, independientes del clúster de
  Redshift.
- Muchas de las tareas de cálculo intensivo (ej. **filtrado de predicados**, **agregaciones**) se
  trasladan a la capa de Spectrum, en lugar de ejecutarse en el clúster.
- Como resultado, las consultas de Spectrum consumen **mucha menos capacidad de procesamiento del
  clúster** que otras consultas.
- Spectrum **escala automáticamente** según la demanda de la consulta, pudiendo usar **miles de
  instancias** en paralelo para aprovechar un procesamiento masivamente paralelo.

> ⚠️ Spectrum reside fuera del clúster de Redshift y escala de forma independiente — por eso el
> impacto sobre la capacidad de cómputo del clúster es mínimo, incluso con consultas sobre grandes
> volúmenes de datos.

## Operaciones sobre tablas externas

| Operación | Comando |
| --- | --- |
| Crear una tabla externa | `CREATE EXTERNAL TABLE` |
| Insertar el resultado de un `SELECT` en una tabla externa existente | `INSERT INTO EXTERNAL TABLE` |
| Actualizar / eliminar datos | Soportado (`UPDATE` / `DELETE`) |

## Consideraciones importantes

- El **clúster de Redshift y el bucket de S3 deben estar en la misma región**.
- Redshift Spectrum **no soporta Enhanced VPC Routing** con clústeres aprovisionados — puede
  requerir pasos de configuración adicionales para acceder a los datos en S3.
- Spectrum soporta **alias de S3 Access Points**, pero **no soporta VPC** junto con esos alias.
- A menos que se use un **AWS Glue Data Catalog habilitado para Lake Formation**, no es posible
  controlar permisos de usuario a nivel de tabla externa.
- El usuario de base de datos que ejecute consultas de Spectrum debe tener permiso para **crear
  tablas temporales** en la base de datos (las consultas de Spectrum a veces las usan
  internamente).
- Redshift Spectrum **no es compatible con Amazon EMR con Kerberos**.

> ⚠️ Sin Lake Formation, el control de permisos sobre tablas externas es limitado — para
> granularidad fina de permisos hay que usar un Glue Data Catalog habilitado para **Lake
> Formation**.
