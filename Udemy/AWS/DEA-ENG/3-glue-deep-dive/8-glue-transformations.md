# Capacidades de transformación en AWS Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Visión general del proceso ETL

Repasando el flujo completo de un **ETL Job** en Glue, con foco en las capacidades de transformación
disponibles:

1. **Discovery / Extract**: se conecta una fuente de datos (existen distintos tipos de fuentes
   disponibles) y se extraen los datos.
2. **Transform**: los datos extraídos se transforman (opcional, pero es donde entran las capacidades
   descritas en este apunte).
3. **Load**: los datos transformados se cargan en el almacén de destino.

Al cargar en el destino también se puede decidir si se actualiza el **Glue Data Catalog** — por ejemplo,
crear una tabla nueva e indicar en qué database del catálogo se debe almacenar.

## Transformaciones básicas

Operaciones sencillas disponibles en el editor Visual ETL:

- **Filter**: filtrar registros según condiciones.
- **Join**: unir varios conjuntos de datos.
- **Aggregations**: agregaciones (sumas, conteos, etc.).

## Transformaciones avanzadas

### Find Matches

Permite identificar **registros duplicados o coincidentes** entre distintos conjuntos de datos, incluso
cuando no existe un campo común exacto (como un identificador o clave primaria) para relacionarlos.

- Caso de uso típico: comparar un catálogo de productos propio con el catálogo de un competidor, donde
  la estructura es distinta y puede haber diferencias de ortografía o de formato.
- Es una transformación **basada en Machine Learning (ML)**, útil también para limpiar un mismo dataset
  y encontrar duplicados internos causados por errores tipográficos o datos incompletos.

### PII Detector (Personally Identifiable Information)

Permite **detectar y gestionar información sensible** dentro de los datos, relevante para cumplir
regulaciones de privacidad como el **GDPR**.

- Escanea los datos en busca de información potencialmente sensible: nombres, números que puedan ser
  identificativos (ej. número de seguridad social), datos de tarjetas de crédito, etc.
- Una vez detectada, se pueden configurar acciones para **proteger** esa información, por ejemplo:
  - **Tokenizar** los valores sensibles.
  - **Eliminar** por completo los campos detectados.

### Conversión de formato de archivo

Uno de los casos de uso más comunes: transformar el formato de los datos de origen a un formato más
optimizado para análisis.

- Ejemplo típico: convertir de **CSV** a **Parquet**, un formato de almacenamiento **columnar** mucho
  más eficiente para consultas analíticas.
- También es posible convertir entre otros formatos habituales, como **JSON**.

## Carga en el destino

Tras las transformaciones, los datos se cargan en el almacén de destino, por ejemplo:

- Una base de datos o data warehouse en **Amazon Redshift**.
- Un bucket de **Amazon S3**.

> Si los datos se guardan en S3, no es necesario moverlos a otro sitio para consultarlos: se pueden
> ejecutar consultas directamente sobre esos datos usando **Amazon Athena** o **Amazon Redshift**
> (Redshift Spectrum) sin mover la información fuera de S3.
