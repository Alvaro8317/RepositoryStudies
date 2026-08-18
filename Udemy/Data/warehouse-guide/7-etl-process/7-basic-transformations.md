# Transformaciones básicas

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Después de ver los objetivos generales de la transformación, toca ver los tipos de transformación más
básicos y habituales dentro del proceso `ETL`.

## Deduplicación

Es habitual tener que asegurarse de que no hay duplicados en los datos, sobre todo cuando se integran
varios sistemas. Por ejemplo, si se combinan los datos de dos tiendas distintas para crear una
dimensión de producto unificada, puede que algunos productos estén disponibles en ambas tiendas — y
por tanto aparezcan duplicados al juntar los datos.

| clave_producto | producto | tienda |
|---|---|---|
| 1 | A | Tienda 1 |
| 2 | B | Tienda 1 |
| 1 | A | Tienda 2 (duplicado) |
| 3 | C | Tienda 2 |

Los duplicados no son deseables en una tabla de dimensión, así que se eliminan tomando solo los
valores distintos (`distinct`) tras juntar los datos.

## Filtrado de filas

Similar a la deduplicación en que también se eliminan filas, pero aquí se trata de eliminar valores
que no interesan (no necesariamente duplicados). Por ejemplo, al construir una tabla de hechos de
ventas, los datos fuente pueden incluir transacciones de reembolso (`Refund`) que no son relevantes
para esa tabla:

| clave_venta | tipo | cantidad |
|---|---|---|
| 1 | Venta | 10 |
| 2 | Refund | -5 |
| 3 | Venta | 8 |

Se puede filtrar, por ejemplo, con la condición `tipo = 'Refund'` (o de forma equivalente,
`cantidad < 0`) para descartar esas filas y quedarse solo con las de tipo `Venta`.

## Filtrado de columnas

Una vez filtradas las filas, puede quedar alguna columna que ya no aporta información — por ejemplo,
si tras el filtro anterior la columna `tipo` solo contiene el valor `Venta` en todas las filas, deja de
tener sentido conservarla, y se puede eliminar para quedarse solo con los datos realmente relevantes.

## Limpieza y mapeo de datos

Al integrar varias tablas de distintos sistemas fuente, conviene darles una forma coherente. Un caso
típico es el mapeo de valores: un sistema puede representar el sexo del cliente con abreviaturas
(`M`/`F`), mientras que otro lo escribe de otra forma. Para estandarizar, se mapean los valores a un
formato común:

| Valor origen | Valor estandarizado |
|---|---|
| `M` | `Hombre` |
| `F` | `Mujer` |

También entra aquí la limpieza de caracteres no deseados incluidos en los datos (por ejemplo,
caracteres de más en un texto) — hay que detectarlos y eliminarlos o sustituirlos para que los datos
queden limpios y sean realmente comparables entre sistemas.

## Sustitución de nulos

A veces conviene sustituir valores nulos por un valor concreto. Por ejemplo, si un día no se registra
ninguna venta (no hay fila para ese día), puede interesar representarlo explícitamente como `0 $` en
ventas en lugar de dejarlo como nulo o ausente.

> ⚠️ Si sustituir nulos por un valor concreto tiene sentido depende del caso de uso — no es una regla
> que aplique siempre.

## Normalización de valores

Parecido a la limpieza, pero enfocado en unidades y tipos de datos distintos entre sistemas. Por
ejemplo, un sistema puede reportar las ventas en miles (`1.5` = 1.500) con tipo decimal, mientras que
otro las reporta en unidades con tipo entero:

| Sistema | Valor original | Tipo | Transformación | Valor normalizado |
|---|---|---|---|---|
| Sistema A | `1.5` (miles) | decimal | `× 1000` y convertir a entero | `1500` |
| Sistema B | `1500` | entero | — | `1500` |

Al normalizar ambos a la misma unidad y tipo de dato, se pueden reunir en una única tabla consolidada.

## Generación de la clave sustituta (Surrogate Key)

Por último, normalmente también se quiere añadir una `Surrogate Key` a cada tabla, que suele
autogenerar el sistema de gestión de base de datos o la propia herramienta `ETL`. Esta clave sustituye
habitualmente a la `Natural Key` como identificador de la fila en el `Data Warehouse`.

## Próximas clases

Ver algunas de las transformaciones de datos más avanzadas, y después una demostración práctica de
transformaciones dentro del proceso `ETL`.
