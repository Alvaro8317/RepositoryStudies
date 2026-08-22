# Dynamic Frame y Resolve Choice

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es un Dynamic Frame?

Un **Dynamic Frame** es la estructura de datos nativa de **AWS Glue ETL**, diseñada específicamente
para manejar **datos heterogéneos** — es decir, un conjunto de datos donde los registros no
comparten necesariamente la misma estructura (por ejemplo, mezclando fechas, texto, objetos JSON y
listas dentro del mismo dataset).

- Es una colección de **Dynamic Records** (registros dinámicos).
- Proporciona funcionalidades ETL avanzadas más allá de lo que ofrece un **Spark DataFrame**
  estándar, aunque conceptualmente es similar a este.
- Ofrece **APIs tanto para Scala como para Python** (PySpark).
- Es posible **convertir entre un Spark DataFrame y un Glue Dynamic Frame** y viceversa dentro de un
  mismo script, según convenga en cada paso del procesamiento.

**Ejemplo de dato heterogéneo**: un dataset de eventos donde cada registro tiene un `id` único, un
`type` (tipo de evento) y un `payload` cuyo contenido/estructura varía según el `type` — un Dynamic
Frame puede manejar esta variabilidad sin necesitar un esquema fijo común para todos los registros.

## Transformaciones disponibles

Sobre un Dynamic Frame, Glue ETL permite aplicar transformaciones como:

- **Drop**: eliminar campos (por ejemplo, campos nulos).
- **Filter**: filtrar registros según una función/condición.
- **Join**: enriquecer datos combinando varios datasets.
- **Map**: añadir o eliminar campos, realizar búsquedas externas (lookups), etc.
- **Transformaciones de Machine Learning**: identificar registros duplicados o coincidentes en el
  dataset — ver **Find Matches** en `8-glue-transformations.md`.
- **Conversión de formato**: CSV, JSON, Avro, Parquet, ORC, XML.
- **Transformaciones de Apache Spark**: por ejemplo algoritmos como **K-means**, aprovechando la
  conversión entre Spark DataFrame y Dynamic Frame mencionada arriba.

## Resolve Choice

**Resolve Choice** es una funcionalidad de Glue ETL que resuelve **ambigüedades** dentro de un
Dynamic Frame — el caso típico es cuando **varios campos comparten el mismo nombre** o cuando los
**tipos de datos son inconsistentes** entre registros para un mismo campo.

Cuatro operaciones principales disponibles:

| Operación      | Qué hace                                                                                |
| -------------- | ---------------------------------------------------------------------------------------- |
| **make_cols**  | Crea una **columna nueva por cada tipo** encontrado (ej. si hay dos campos con el mismo nombre pero tipos distintos). |
| **cast**       | **Convierte** todos los valores del campo al **tipo especificado**.                     |
| **make_struct** | Crea una **estructura (struct)** que contiene cada tipo de dato encontrado para ese campo. |
| **project**    | **Proyecta** el campo a un único tipo de dato dado, descartando el resto.               |

> No hace falta memorizar el detalle exacto de cada operación de Resolve Choice para el examen —
> basta con saber que **Resolve Choice existe** y para qué sirve (resolver ambigüedad de nombres/tipos
> en un Dynamic Frame), y reconocer estas cuatro opciones si aparecen.
