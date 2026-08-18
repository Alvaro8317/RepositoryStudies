# ETL de la Fact Table de ventas

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con la dimensión de pago ya cargada en `Core` (ver [[6-payment-dimension-etl]]), toca construir la
transformación final que lee los datos de `Staging`, aplica todas las transformaciones diseñadas y
carga el resultado en la `Fact Table` de ventas en `Core`.

## Diseñar la consulta en SQL primero

Al igual que con la dimensión de pago, conviene probar y ajustar la lógica en `SQL` (`pgAdmin`) antes
de construirla en `Spoon`.

### Columnas directas

Se seleccionan las columnas que se mantienen tal cual (`transaction_id`, `transactional_date`,
`price`, `quantity`, `cost`, etc.), dejando fuera las que ya no hacen falta — por ejemplo, los valores
de pago, que ahora viven en la `Payment Dimension`.

> ⚠️ Al probar el `join` con la `Payment Dimension`, la `Foreign Key` puede aparecer vacía si todavía
> no se ha ejecutado la transformación `core_dim_payment` — hay que ejecutar primero esa dimensión y
> volver a intentarlo (en la práctica, a veces hace falta ejecutarlo dos veces, porque tarda un poco en
> reflejarse el cambio).

### Date Key

Se construye una clave de fecha numérica (`YYYYMMDD`) a partir de `transactional_date`:

1. Extraer el **año** y multiplicarlo por `10000` (para dejar espacio a los 4 dígitos siguientes).
2. Extraer el **mes** y multiplicarlo por `100` (para dejar espacio a los 2 dígitos del día).
3. Extraer el **día** y sumarlo.

Por ejemplo, el 4 de mayo se convierte en el número correspondiente a `AAAAMMDD`.

### Foreign Key de producto

Se obtiene haciendo un `JOIN` entre los datos de origen y la dimensión de producto, usando la
`Natural Key` (`product_id`) como condición de unión — así se trae la `Surrogate Key` correcta de la
dimensión de producto.

## Construir la transformación en Spoon

1. **Table Input**: se pega la consulta SQL ya validada (columnas directas + `date_key` + FK de
   producto).
2. **Calculator** (para `total_price`): `price × quantity`, tipo `Number`, precisión de 2 decimales.
3. **Calculator** (para `total_cost`): `cost × quantity`, tipo `Number`, precisión de 2 decimales.
4. **Calculator** (para `profit`): `total_price − total_cost`, tipo `Number`, precisión de 2 decimales.
5. **Insert/Update**: hacia el esquema `core`, tabla `sales`.
   - Se compara por la clave primaria (`transaction_id`) para detectar si la fila ya existe.
   - No hace falta marcar el propio `transaction_id` como campo a actualizar (es la clave de
     comparación); el resto de campos sí se actualizarían si la fila ya existiera.

> ⚠️ En cada paso conviene usar la vista previa (`Preview`) para verificar los resultados antes de
> seguir, especialmente en cálculos como estos.

## Próximas clases

Ensamblar esta transformación junto con la de la dimensión de producto en el `Job` de `Core`, y
probar el flujo completo.
