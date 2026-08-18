# Transformaciones avanzadas

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Tras ver las transformaciones básicas, toca ver algunos ejemplos importantes de transformaciones más
avanzadas.

## Unir tablas (Join / Lookup)

A menudo se necesita unir varias tablas para obtener la `Foreign Key` en la tabla de hechos. Es
habitual que en la tabla de hechos solo se tenga disponible la `Natural Key` (por ejemplo, el ID de
producto del sistema fuente), mientras que en la tabla de dimensión se ha añadido una `Surrogate Key`.
Para poder referenciar esa `Surrogate Key` como `Foreign Key` en la tabla de hechos, hay que unir
(`join`) ambas tablas usando la `Natural Key` como columna común.

| clave_venta | id_producto (natural) | ... |
|---|---|---|
| 1 | 533 | ... |

| clave_producto (sustituta) | id_producto (natural) | producto |
|---|---|---|
| 3 | 533 | A |
| 2 | 252 | B |

Al hacer el `join` por `id_producto`, la tabla de hechos obtiene la columna adicional
`clave_producto` (la `Foreign Key`), que ahora referencia la `Primary Key` de la dimensión — el `join`
funciona básicamente como una búsqueda (`lookup`).

> ⚠️ Si la dimensión es una `Slowly Changing Dimension` con fechas de vigencia (`fecha_efectiva` /
> `fecha_caducidad`), el `join` por la `Natural Key` no basta por sí solo: podría devolver varias filas
> para la misma clave natural (una por cada versión histórica). Hay que añadir una condición adicional
> que filtre a la fila donde la fecha del hecho (por ejemplo, la fecha de la transacción) esté entre
> `fecha_efectiva` y `fecha_caducidad`, para quedarse con un único valor vigente en ese momento. Si no
> se trabaja con `Slowly Changing Dimensions`, basta con un `join` simple.

### Fusionar columnas de varias tablas

Otro uso habitual del `join` es fusionar varias tablas relacionadas en una sola tabla de dimensión más
compacta y fácil de usar — por ejemplo, unir una tabla de productos con una tabla de categorías (por la
columna de categoría) para obtener una única tabla de dimensión de producto. Esto no solo mejora la
usabilidad, sino también el rendimiento, porque evita tener que hacer esos `joins` manualmente (y
consumir recursos de cómputo) cada vez que se consulta la dimensión.

## División de datos (Split)

A veces una columna contiene en realidad varios tipos de información que interesa tener por separado.
Por ejemplo, una columna `ubicación` de una dimensión de tienda puede incluir ciudad, estado y código
postal juntos, y conviene dividirla en columnas independientes para poder usarlas de forma
individual.

Formas habituales de dividir una columna:

- **Por delimitador**: por ejemplo, dividir por comas (`,`) o por espacios en blanco, extrayendo lo
  que hay antes/después de cada delimitador.
- **Por longitud o posición**: dividir siempre en una posición fija de caracteres — por ejemplo,
  "dividir después de los 2 primeros caracteres", dejando esos caracteres en una columna y el resto en
  otra (útil, por ejemplo, para separar el código de estado del código postal).

| ubicación original | ciudad | estado | código_postal |
|---|---|---|---|
| `Some Street, New York NY 10001` | `New York` | `NY` | `10001` |

## Agregación (cambio de granularidad)

Cuando se quiere cambiar la granularidad de los datos, normalmente hay que agregarlos. Existen varios
tipos de agregación según lo que se necesite calcular:

| Tipo de agregación | Uso típico |
|---|---|
| `SUM` (suma) | Sumar un importe a lo largo de las filas que se agregan — por ejemplo, sumar el importe de ventas de todas las transacciones de un día. |
| `COUNT` (conteo de filas) | Contar el número de filas — por ejemplo, el número de ventas/transacciones de un día (una fila = una venta). |
| `COUNT DISTINCT` (conteo de valores distintos) | Contar cuántos valores distintos hay — por ejemplo, cuántos productos diferentes se vendieron en un día. |
| `AVG` (media) | Calcular el promedio de una columna a lo largo de las filas agregadas. |

Por ejemplo, para pasar de granularidad "una fila por transacción" a granularidad "una fila por día",
se agrupa por fecha y se aplican estas agregaciones sobre las columnas correspondientes.

## Cálculo de valores adicionales (columnas derivadas)

También se pueden crear columnas nuevas calculadas a partir de otras — restando, multiplicando, o
agrupando valores existentes. Por ejemplo, si se tiene el importe de venta y el porcentaje de impuesto
(un valor no aditivo, que no se puede sumar directamente entre filas), se puede calcular una columna
`importe_impuesto` en valor absoluto multiplicando ambas columnas:

| importe_venta | porcentaje_impuesto | importe_impuesto (calculado) |
|---|---|---|
| 100 | 10 % | 10 |

Así se obtiene una columna aditiva y más útil para el análisis a partir de un valor que, en su forma
original (porcentaje), no lo era.

## Próximas clases

Poner en práctica estos tipos de transformación con una demostración dentro de un proceso `ETL` real.
