# SCD Type 2 — Fechas de vigencia y flag de valor actual

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El problema pendiente

En [[4-scd-type-2-add-new-row]] vimos que `SCD Type 2` añade una fila nueva por cada cambio, lo que
preserva perfectamente la historia. Pero con ese enfoque, tal como está, todavía **no podíamos
identificar cuál es el valor actual** (ej. el nombre vigente de un producto) entre las distintas filas
históricas de un mismo producto.

## La solución: Effective Date y Expiration Date

Se agregan dos columnas adicionales a la `Dimension Table`:

- **`Effective Date`** (fecha de entrada en vigor): desde cuándo es válido ese valor.
- **`Expiration Date`** (fecha de caducidad): hasta cuándo es válido ese valor.

Con estas dos columnas, cada fila queda delimitada al periodo exacto en el que sus valores fueron (o
son) válidos. Por ejemplo, si la fila 3 fue válida solo hasta finales de mayo de 2022, a partir de ese
momento se debe usar la fila nueva (con la nueva `Surrogate Key`) que representa el valor vigente
desde entonces.

> ⚠️ Para la `Expiration Date` de la fila vigente, no se debe dejar `NULL`. Es mejor usar una fecha muy
> lejana en el futuro (ej. 100-200 años adelante). La razón es práctica: funciones SQL como `BETWEEN`
> no funcionan bien con `NULL`, y usar una fecha ficticia lejana permite seguir filtrando con esas
> funciones sin casos especiales.

## Uso en el proceso ETL: encontrar la clave foránea correcta

Estas columnas son necesarias para que el proceso ETL pueda determinar la `Surrogate Key` correcta a
usar en la `Fact Table`. El flujo, paso a paso:

1. **Añadir la fila nueva** en la dimensión cuando se detecta un cambio, con su `Effective Date` y
   `Expiration Date` correspondientes.
2. **Hacer un lookup en la dimensión** para encontrar la clave foránea correcta a usar en la `Fact
   Table`: se busca por la `Natural Key` **y**, adicionalmente, se verifica cuál fila tiene la fecha
   actual dentro de su rango de vigencia (`Effective Date` ≤ fecha actual < `Expiration Date`).

Por ejemplo, si el ETL corre el 1 de junio de 2023, y esa fecha cae dentro del rango de vigencia
únicamente de la fila 4, esa es la fila — y por tanto la `Surrogate Key` — correcta a usar en la
`Fact Table` para los hechos nuevos.

> Se profundizará en cómo implementar este lookup más adelante, en la sección de `ETL` del curso.

## Columna adicional opcional: flag de "valor actual"

Para facilitar aún más el filtrado, se puede añadir una columna booleana (`is_current` o similar) que
indique directamente si esa fila es la versión vigente o no. Esta práctica también es sugerida por
`Kimball`, y sirve como atajo de filtrado adicional para los usuarios de negocio que solo quieren ver
los valores actuales, sin tener que comparar fechas.

## Por qué SCD Type 2 requiere sí o sí una Surrogate Key

Con `SCD Type 2`, la `Natural Key` (ej. `Product_ID`) deja de ser única en la dimensión, ya que un
mismo producto puede tener varias filas (una por cada versión histórica). Por eso es indispensable
usar una `Surrogate Key` como clave primaria — sin ella, este enfoque simplemente no sería posible.

## Resumen

| Columna             | Propósito                                                                          |
| ------------------- | ---------------------------------------------------------------------------------- |
| `Effective Date`    | Desde cuándo es válida esa fila/versión del valor.                                 |
| `Expiration Date`   | Hasta cuándo es válida — usar una fecha lejana en el futuro en vez de `NULL`.      |
| `is_current` (flag) | Opcional — marca directamente cuál fila es la versión vigente, para filtrar fácil. |

## Próxima clase

¿Es posible combinar `SCD Type 1` y `SCD Type 2` para distintos atributos dentro de la misma tabla de
dimensión?
