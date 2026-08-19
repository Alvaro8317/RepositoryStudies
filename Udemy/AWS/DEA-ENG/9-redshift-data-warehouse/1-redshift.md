# Amazon Redshift

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon Redshift?

**Amazon Redshift** es un servicio de **almacén de datos (data warehouse) a escala de petabytes**,
**totalmente gestionado**, usado con **fines analíticos**.

- En esencia, es una **base de datos relacional compatible con ANSI SQL**, pensada para el
  **almacenamiento de datos analíticos** (data warehousing) — soporta todos los comandos SQL
  habituales.
- Ofrece un **rendimiento muy rápido**, y se puede usar con:
  - **Redshift Query Editor v2** (herramienta propia de AWS).
  - Cualquier otra **herramienta de inteligencia empresarial (BI)** conectada a Redshift como
    fuente de datos.
- Está diseñado para **manejar grandes cantidades de datos** con **alto rendimiento y
  escalabilidad**, de forma que puede seguir escalando a medida que crecen los datos.
- Soporta la carga de datos en **múltiples formatos**: **CSV**, **JSON**, y también formatos
  columnares como **Parquet** o **Avro**.

## Escalabilidad: clusters

- Redshift escala mediante **clusters**, que se pueden **redimensionar** a medida que crecen las
  necesidades de datos.
- La arquitectura de clusters se tratará en más detalle más adelante.

## Almacenamiento columnar

- A diferencia de una base de datos **OLTP** (con muchas operaciones de **escritura**, típica de un
  entorno productivo donde se generan los datos), Redshift se usa con **fines analíticos**, por lo
  que está **optimizado para lectura**.
- Los datos se almacenan en **formato columnar**, lo que optimiza el rendimiento de las consultas
  de dos formas:
  - **Reduciendo las operaciones de I/O**.
  - Mejorando el **ratio de compresión**.
- En una consulta analítica normalmente **no se necesitan todas las columnas** de una tabla (por
  ejemplo, agregar o mostrar solo 2-3 columnas de 100). En un almacenamiento **por filas**, habría
  que escanear todas las columnas igualmente. En un almacenamiento **columnar**, solo se leen las
  columnas necesarias, lo que **reduce drásticamente el escaneo** y mejora el rendimiento de las
  consultas de lectura.

## Procesamiento paralelo masivo (MPP)

- Redshift utiliza **Massively Parallel Processing (MPP)**: una arquitectura que **distribuye los
  datos y las consultas entre múltiples nodos** de un clúster.
- Esto permite una **ejecución paralela de alto rendimiento**.

## Integraciones

Redshift se integra con otros servicios de AWS, lo que facilita **ingestar, transformar y analizar**
datos de forma conjunta:

- **Amazon S3**
- **DynamoDB**
- **AWS Glue**
- **AWS Lambda**

## Compresión

- Redshift utiliza una **compresión avanzada**, que ayuda tanto a **reducir el almacenamiento**
  como a **mejorar el rendimiento** de las consultas.

## Seguridad

- **Cifrado en reposo y en tránsito** a nivel de base de datos.
- **Control de acceso a objetos** de grano fino mediante **roles y políticas IAM**.
- **VPC security groups** para controlar el acceso a nivel de red.

## Casos de uso

- **Almacén de datos (data warehouse)** para fines analíticos en general.
- **Inteligencia empresarial (BI)**: distintas herramientas de BI usando Redshift como fuente de
  datos.
- **Análisis de logs**.
- **Procesamiento de datos IoT**.
- **Dashboards de datos en tiempo real**, para casos muy sensibles al tiempo.

> ⚠️ Redshift está **optimizado para lectura analítica**, no para las cargas de escritura
> intensivas típicas de una base de datos OLTP — esa es la diferencia clave a tener en cuenta
> frente a servicios como RDS o Aurora.
