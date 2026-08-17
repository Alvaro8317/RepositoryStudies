# Bases de datos relacionales

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Qué es una base de datos relacional?

Un `Data Warehouse` normalmente se aloja sobre una **base de datos relacional**, así que vale la
pena entender esta tecnología de cerca.

- Es, en esencia, una base de datos donde los datos se almacenan en **tablas** (también llamadas
  `relaciones`), estructurados en columnas y filas.
- Se consulta con `SQL`, un lenguaje declarativo y de sintaxis cercana al lenguaje natural (ej.
  `SELECT columnas FROM tabla`), relativamente sencillo de aprender.

Lo distintivo de una base de datos **relacional** es que permite poner las tablas **en relación**
entre sí mediante claves.

## Claves primarias y foráneas

| Concepto            | Función                                                                                   |
|-----------------------|----------------------------------------------------------------------------------------------|
| **Clave primaria** (`Primary Key`) | Identifica de forma única cada fila de una tabla. La columna que actúa como clave primaria no puede tener valores duplicados ni nulos. |
| **Clave foránea** (`Foreign Key`)  | Hace referencia a la clave primaria de otra tabla, permitiendo enlazar filas entre tablas distintas. |

Por ejemplo, si una tabla de pedidos tiene una columna `cliente_id` que es clave foránea hacia la
clave primaria `id` de una tabla de clientes, con el valor `2` en `cliente_id` se puede identificar
exactamente qué fila de la tabla de clientes corresponde (ej. "Sarah").

Estas relaciones entre tablas se explotan en `SQL` mediante `JOIN`s, que permiten combinar columnas
de varias tablas en una sola consulta usando las claves primarias y foráneas.

## Por qué esto fue un cambio de paradigma

Aunque hoy parezca algo sencillo, poder relacionar tablas mediante claves fue un **cambio de juego**
para el análisis de datos:

- Tradicionalmente, en los sistemas operativos (`OLTP`) los datos se consultaban y editaban tabla
  por tabla, valor por valor — sin mucho contexto adicional.
- Con la posibilidad de poner tablas en relación, se ganó mucho más **contexto** al combinar varias
  tablas en una sola consulta, lo que impulsó el análisis de datos de forma mucho más avanzada.
- Este fue precisamente el avance que dio lugar a `OLAP`, y está estrechamente ligado al auge de los
  propios `Data Warehouses`: al poder organizar los datos en varias tablas relacionadas, se pudo
  empezar a modelarlos y analizarlos de forma mucho más rica (esto se retoma más adelante con el
  `Star Schema`).

> ⚠️ Lograr un buen rendimiento de consulta sobre tablas relacionadas no fue trivial: según el
> instructor, la industria dedicó casi **dos décadas** a desarrollar los algoritmos y la lógica
> necesarios para que consultar datos relacionados fuera lo suficientemente rápido como para tener
> adopción real en el análisis de datos.

## Sistemas gestores de bases de datos relacionales (RDBMS)

La base de datos relacional en sí es solo el modelo de datos; el software que la gestiona es el
`RDBMS` (`Relational Database Management System`). Algunos ejemplos habituales en la industria:

| Categoría                  | Ejemplos                                                       |
|-------------------------------|--------------------------------------------------------------------|
| Comerciales / empresariales   | `Oracle`, `Microsoft SQL Server`                               |
| Código abierto                | `PostgreSQL` (el usado en este curso), `MySQL`                 |
| Servicios en la nube          | Bases de datos relacionales de `Amazon` (ej. `RDS`), `Azure SQL Database` |

## Próxima clase

Bases de datos **in-memory**, otra tecnología cada vez más relevante para los `Data Warehouses`.
