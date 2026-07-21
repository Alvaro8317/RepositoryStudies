# Particionamiento de datos

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es el particionamiento?

El **particionamiento** es un aspecto de **rendimiento** en Glue, especialmente útil para la
**consulta** de datos una vez que el procesamiento ya se ha realizado — cuando se tienen grandes
conjuntos de datos distribuidos en distintas ubicaciones, por ejemplo dentro de un bucket S3.

Es importante tanto para la consulta de los datos como para el propio procesamiento en Glue.

Las particiones se configuran como **ubicaciones de archivos** (subcarpetas) que organizan los datos en
función de alguna condición. Un caso muy común es particionar por **fecha**, por ejemplo:

```text
bucket/
└── datos/
    └── 2023/
    └── 2024/
```

## Beneficios para la consulta

Si los datos están organizados en particiones y una consulta tiene una condición común como
`WHERE year = 2023`, el motor de consulta puede **saltarse el resto de particiones** y escanear
únicamente los datos relevantes:

- Se reduce la cantidad de datos leídos en cada ejecución de consulta (**exploración selectiva**).
- Se reducen las operaciones de I/O.
- Se **aceleran las consultas** y mejoran los tiempos de respuesta.

> ⚠️ Servicios como **Amazon Athena** cobran en función de la **cantidad de datos escaneados**. El
> particionamiento reduce esa cantidad de datos escaneados y, por tanto, también supone un **ahorro de
> costes** en las consultas.

## Beneficios para el procesamiento ETL

Con los datos organizados en particiones, Glue puede procesar **cada partición de forma
independiente**, lo que hace los datos más manejables: mejor rendimiento, menos tiempo de
procesamiento necesario y, en consecuencia, menor coste.

## Cómo se definen las particiones en Glue

- Normalmente se definen las particiones al configurar el **ETL Job**.
- También se pueden crear directamente con **Glue Crawlers**: los Crawlers pueden reconocer
  automáticamente las particiones si los datos están bien organizados en la estructura de carpetas.
- En **S3**, las particiones se especifican habitualmente mediante la propia **estructura de
  directorios** (como en el ejemplo anterior), siguiendo un esquema de partición consistente.
