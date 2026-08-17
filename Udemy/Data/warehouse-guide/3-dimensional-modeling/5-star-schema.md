# Star Schema

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El esquema más importante del Data Warehouse

El `Star Schema` es el esquema más importante en un `Data Warehouse`, especialmente en los `Data
Marts`. Organiza los datos en hechos y dimensiones (ya vistos en [[3-fact-tables]] y
[[4-dimension-tables]]), conectados mediante claves primarias y foráneas: la `Fact Table` (ej. una
tabla de ventas) contiene una clave foránea que se relaciona con la clave primaria de cada
`Dimension Table` (ej. una tabla de productos).

## Relación uno a muchos

Entre una `Fact Table` y una `Dimension Table` suele haber una relación **uno a muchos** (`1:N`):

- **Lado "1"** (la dimensión): cada valor de la columna de conexión (ej. `product_id`) ocurre **una
  sola vez** — es único.
- **Lado "N"** (la tabla de hechos): el mismo valor de esa columna puede **repetirse muchas veces**
  (ej. el mismo producto vendido en múltiples transacciones).

## Un solo nivel de jerarquía → redundancia de datos

En un `Star Schema`, cada dimensión tiene **un único nivel de conexión** con la tabla de hechos — no
hay conexiones adicionales entre dimensiones. Si una dimensión contiene, además del atributo
principal, otro nivel de jerarquía (ej. una tabla de productos que incluye también la
`categoría` del producto), ese valor de categoría se **repite** por cada producto que pertenezca a
ella (ej. "ajo" y "plátano" ambos en la categoría "frutas y verduras" — el valor de categoría queda
duplicado).

Esta repetición es **redundancia de datos**.

## Normalización vs. desnormalización

| Concepto             | Qué es                                                                                                       | Ventaja                                                                                                            | Desventaja                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Normalización**    | Técnica (matemática) que reduce la redundancia de datos separando la información en más tablas relacionadas. | Menor espacio de almacenamiento; más fácil mantener/actualizar datos de forma correcta (operaciones de escritura). | Más tablas → consultas más complejas (más `JOIN`s) → peor rendimiento de lectura y peor usabilidad. |
| **Desnormalización** | Aceptar cierta redundancia de datos a cambio de menos tablas y consultas más simples.                        | Mejor rendimiento de lectura y mejor usabilidad — ideal para casos de uso de reporting/visualización.              | Mayor espacio de almacenamiento; actualizar datos duplicados requiere más cuidado.                  |

> ⚠️ Un `Star Schema` está **hasta cierto punto desnormalizado**, y esto es intencional: como el
> caso de uso principal es la **lectura** de datos para reporting y visualización (no operaciones
> transaccionales), aceptar redundancia de datos a cambio de mejor rendimiento y usabilidad es la
> decisión correcta. El `Snowflake Schema` (siguiente clase) es la alternativa que reduce esta
> redundancia mediante normalización.

## Ejemplo práctico

Un `Star Schema` implementado en `Power BI`: la tabla de ventas (hecho) en el centro, con las
dimensiones a su alrededor, y las relaciones físicamente creadas entre ellas — visualmente, el lado
"1" en la dimensión y el lado "N" (representado como el asterisco/estrella) en el hecho.

## Casos con múltiples tablas de hechos

Lo ideal es definir un **grano** (`Grain`) y agrupar todos los hechos relevantes en una única `Fact
Table` — esta es la situación más común y la deseable. Sin embargo, a veces no es posible, y puede
haber **múltiples tablas de hechos**.

- En ese caso, una misma dimensión (ej. la jerarquía de productos) puede estar conectada a más de
  una tabla de hechos, si es relevante para ambas.
- Normalmente, las tablas de hechos **no se conectan directamente entre sí**.

> ⚠️ Este es un caso más complejo — el objetivo aquí es entender primero el modelo general (una
> tabla de hechos). Variaciones y retos comunes de modelado se cubren más adelante en el curso.

## Por qué es el esquema más usado

El `Star Schema` es el esquema más común en un `Data Mart` porque combina:

- **Usabilidad** (facilidad de uso).
- **Alto rendimiento de consulta**.
- **Simplicidad**: es la forma más sencilla de modelar los datos, especialmente comparado con el
  `Snowflake Schema`.

Además, un `Star Schema` rinde de forma óptima cuando se conocen de antemano las necesidades de
consulta — es decir, cuando se sabe qué conjunto de consultas se van a ejecutar habitualmente (ej.
"beneficio por año", "beneficio por categoría"), sin necesitar consultas súper complejas. Cuanto más
acotado y conocido ese conjunto de consultas, mejor rendimiento y usabilidad se obtiene con el `Star
Schema`.

## Próxima clase

El `Snowflake Schema`, una variación del `Star Schema` que reduce la redundancia de datos mediante
normalización.
