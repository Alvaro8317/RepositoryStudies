# Redshift: User-Defined Functions (UDF)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Las **UDF (User-Defined Functions)** en Redshift son **funciones personalizadas** que los propios
usuarios pueden crear para realizar operaciones específicas que **no están cubiertas por las
funciones integradas** (built-in) de Redshift. Permiten **extender la funcionalidad del lenguaje
SQL** dentro de Redshift.

## Tipos de UDF

| Tipo | Lenguaje | Cómo se crea |
| --- | --- | --- |
| **SQL scalar UDF** | Sentencias SQL | `CREATE FUNCTION ... LANGUAGE SQL` |
| **Python scalar UDF** | Python | `CREATE FUNCTION ... LANGUAGE plpythonu` |
| **Lambda UDF** | Cualquier lenguaje soportado por AWS Lambda | `CREATE EXTERNAL FUNCTION`, invocando una función Lambda existente |

- Las **SQL UDF** son las más sencillas: encapsulan una expresión SQL reutilizable como si fuera
  una función.
- Las **Python UDF** permiten escribir lógica personalizada en Python, útil para operaciones más
  complejas que serían difíciles de expresar solo en SQL.
- Las **Lambda UDF** permiten invocar una función **AWS Lambda** directamente desde una consulta
  SQL de Redshift, delegando el procesamiento a Lambda (por ejemplo, para reutilizar lógica ya
  implementada fuera de Redshift, o integrarse con otros servicios).

## Uso

- Una vez creada, una UDF se invoca dentro de una consulta SQL igual que cualquier función
  integrada de Redshift (ej. `SELECT mi_funcion(columna) FROM tabla`).

> ⚠️ En [Data Sharing](16-data-sharing.md), solo se pueden compartir **UDF de tipo SQL** — no se
> soportan funciones en Python ni Lambda a través de un `datashare`.
