# AWS Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Glue?

**AWS Glue** es un servicio **ETL totalmente gestionado** que facilita el proceso de:

- **Extraer** datos de una fuente.
- **Transformarlos** en el camino.
- **Cargarlos (load)** en otro almacén de datos.

## Interfaz visual (drag and drop)

- Permite crear **jobs de ETL** de forma visual, arrastrando y soltando componentes.
- Incluye múltiples **fuentes y destinos de datos** integrables: buckets de S3, Amazon Redshift, otras bases de datos, etc.
- Incluye **transformaciones pre-construidas** listas para usar, lo que simplifica mucho la configuración.

## Ejecución automática

- Una vez configurado el job, los datos se extraen automáticamente, ya sea:
  - Según un **schedule** (calendario/horario).
  - De forma **manual**.
  - Mediante un **trigger** (basado en eventos).
- Por detrás, Glue **genera automáticamente un script** que ejecuta el job.
- El motor subyacente es **Apache Spark**, aunque toda la gestión de los clusters de Spark ocurre "bajo el capó" — el usuario no gestiona infraestructura.

## Características clave

- **Serverless:** no hay que preocuparse por la infraestructura subyacente.
- **Altamente escalable.**
- **Pago por uso (pay-per-use):** el coste depende del **tiempo de cómputo utilizado** y la potencia de cálculo asignada.
  - Es importante controlar este coste, ya que puede dispararse si no se gestiona bien.

## Personalización

- El script generado automáticamente puede **editarse y personalizarse**.
- Se pueden definir **transformaciones personalizadas** y **opciones de carga de datos personalizadas**.

---

## Glue Data Catalog

### El problema

Imaginemos un archivo de datos semiestructurados en un bucket de S3 (ej. un archivo **CSV**) dentro de un **data lake**. Tradicionalmente, consultar una columna específica o analizar esos datos directamente es complicado.

### La solución: Glue Data Catalog

- Es un **catálogo de metadatos centralizado**.
- Se alimenta mediante los llamados **Glue Crawlers**.
- También se puede extraer el esquema directamente dentro de un job ETL.

### ¿Qué hacen los Glue Crawlers?

- **Escanean** la fuente de datos.
- **Deducen el esquema automáticamente**: nombres de columnas, tipos de datos, formato del archivo (CSV, Parquet, etc.).
- **Almacenan** esta información (metadatos + esquema) en el **Glue Data Catalog**.
- Clasifican automáticamente los datos según su formato.

### Beneficio: consultas sin mover los datos

Con el esquema ya registrado en el Data Catalog, es posible **consultar los datos directamente donde están** (ej. el CSV sigue en el bucket S3, sin necesidad de copiarlo), usando:

- **Amazon Athena** — consultas estilo SQL.
- **Amazon Redshift**
- **Amazon QuickSight**

## Ejecución de Crawlers y ETL Jobs

- Tanto los **ETL Jobs** como los **Glue Crawlers** pueden ejecutarse:
  - Según un **schedule**.
  - **Manualmente**.
  - Mediante un **trigger** basado en eventos.

### Cargas incrementales

- Los **ETL Jobs** pueden configurarse para realizar **cargas incrementales**: solo se cargan los datos que no se habían cargado previamente.
- Los **Crawlers** también pueden ejecutarse de forma incremental: infieren el esquema únicamente a partir de los datos **añadidos recientemente** desde el último escaneo.
- Esto es más **eficiente** (menos potencia de cómputo necesaria) y ayuda a **controlar los costes**.

## Resumen de componentes

| Componente              | Función                                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AWS Glue (ETL Jobs)** | Extraer, transformar y cargar datos entre distintos almacenes, con interfaz visual y motor Spark gestionado |
| **Glue Crawlers**       | Escanear fuentes de datos e inferir automáticamente el esquema                                              |
| **Glue Data Catalog**   | Catálogo centralizado de metadatos/esquemas, consultable desde Athena, Redshift o QuickSight                |
