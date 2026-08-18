# Datos de origen y diseño de la tabla de hechos

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con el plan del caso práctico definido (ver [[1-case-study-overview]]), toca analizar los datos de
origen y diseñar, a partir de ellos, la `Fact Table` de ventas y sus dimensiones.

## Los datos de origen

Los datos de origen son un archivo con **datos de ventas** (`sales`), relacionados con la dimensión de
producto (`product`) ya cargada previamente, mediante un `product_id`. Cada fila representa una
transacción.

### Cargar los datos de origen

Antes de diseñar nada, los datos se cargan primero como fuente de datos, en el esquema `public` de la
base de datos (que en este caso práctico solo cumple el rol de sistema fuente):

1. En `pgAdmin`, ejecutar el script SQL que crea la tabla `sales` en el esquema `public`, con todas
   las columnas y tipos de datos de los datos de origen, sin ninguna transformación.
2. Importar los datos desde el archivo `.csv` correspondiente: clic derecho sobre la tabla →
   `Import/Export Data` → modo `Import`, seleccionar el archivo, marcar que el archivo tiene cabecera
   (`Header`) y que el delimitador es una coma.

## Análisis de las columnas de origen

| Columna                     | Análisis                                                                                                                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transaction_id`            | `Primary Key`. Es una `Natural Key`, pero al ser ya un valor numérico incremental, sirve perfectamente como `Surrogate Key` — no hace falta crear una clave adicional.            |
| `transactional_date`        | Es una `timestamp`. Se usará como **columna delta** para habilitar la `Delta Load` (carga incremental).                                                                           |
| `product_id`                | `Natural Key` de la dimensión de producto. Además de esta clave natural, hay que incorporar la `Foreign Key` hacia la `Surrogate Key` ya configurada en la dimensión de producto. |
| `customer_id`               | Clave potencial para una futura dimensión de cliente. No se va a usar por ahora, pero conviene incluirla igualmente, por si en el futuro se necesita una `Customer Dimension`.    |
| `payment`                   | Solo toma 3 valores distintos.                                                                                                                                                    |
| `loyalty_card`              | Solo toma 2 valores (`true`/`false`).                                                                                                                                             |
| `credit_card`               | Un número sin información asociada.                                                                                                                                               |
| `cost`, `price`, `quantity` | Medidas: `cost` y `price` son valores unitarios por producto; `quantity` puede ser mayor que 1.                                                                                   |

### `payment` + `loyalty_card` → Junk Dimension

`payment` (3 valores) y `loyalty_card` (2 valores) combinados dan 6 combinaciones posibles. Al ser
atributos de baja cardinalidad sin una dimensión propia clara, se agrupan en una **`Junk Dimension`**
de pago (`payment`), con todas las combinaciones posibles precalculadas.

### `credit_card` → Degenerate Dimension

`credit_card` no tiene información adicional asociada — es solo un identificador. Se trata de una
**`Degenerate Dimension`**: se deja directamente en la `Fact Table` como un valor en sí mismo, sin
vincularlo a una tabla de dimensión adicional.

### `transactional_date` → Date Key

La `timestamp` incluye fecha y hora, pero para este caso de uso la hora no es relevante. Se conserva
la `timestamp` original, pero además se añade una `Foreign Key` de fecha (`Date Key`) que apunta a la
`Date Dimension` ya configurada previamente.

### Medidas calculadas

`cost` y `price` son valores unitarios, y hay que multiplicarlos por `quantity` para obtener medidas
aditivas que realmente tengan sentido al sumarlas:

- `total_cost` = `cost` × `quantity`
- `total_price` = `price` × `quantity`
- `profit` = `total_price` − `total_cost`

## Diseño final de la Fact Table de ventas

| Columna              | Tipo / origen                                                      |
| -------------------- | ------------------------------------------------------------------ |
| `transaction_id`     | `Primary Key` (clave natural = clave sustituta)                    |
| `transactional_date` | `timestamp` original                                               |
| `date_key`           | `Foreign Key` → `Date Dimension`                                   |
| `product_id`         | `Natural Key` de producto                                          |
| `product_key`        | `Foreign Key` → `Product Dimension` (`Surrogate Key`)              |
| `payment_key`        | `Foreign Key` → `Payment Dimension` (`Junk Dimension`)             |
| `credit_card`        | `Degenerate Dimension`                                             |
| `customer_id`        | `Natural Key` de cliente (reservada, sin dimensión propia todavía) |
| `total_cost`         | Medida calculada (`cost × quantity`)                               |
| `total_price`        | Medida calculada (`price × quantity`)                              |
| `profit`             | Medida calculada (`total_price − total_cost`)                      |

> ⚠️ En el diseño final aparecen varias dimensiones relacionadas con esta `Fact Table` (fecha,
> producto, pago...) — se verá en la práctica que en total son ocho.

## Próximas clases

Configurar esta estructura de tablas y el esquema en `pgAdmin`, y después diseñar el `ETL` en
`Pentaho`.
