# Carga de datos (Loading)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Después de ver el proceso de extracción, toca ver cómo se cargan los datos y todo el flujo de trabajo
completo para entender mejor el proceso de `Load`.

## Punto de partida: después de una ejecución del ETL

Una vez ejecutado el `ETL`, y antes de volver a ejecutarlo, la `Staging Area` queda vacía — después de
cada ejecución se vacía esa capa. Así que al ejecutar una `Delta Load`:

1. Se tiene almacenado el valor máximo de la columna delta de la ejecución anterior.
2. Con ese valor se sabe qué datos son nuevos en los sistemas fuente.
3. Esos datos nuevos se filtran y se extraen hacia `Staging`.
4. Desde `Staging`, todos los datos se empujan — junto con las transformaciones correspondientes —
   hacia la capa `Core`.

Para este último paso (`Staging` → `Core`) normalmente se usa **Insert/Update**: existen distintas
formas de escribir los datos en `Core`, y depende de si los datos ya existen o no en la tabla destino.

## Insert/Update

### Insert simple

El caso más común: se obtienen datos adicionales que aún no están presentes ni se han cargado nunca en
`Core`, y esos datos simplemente se añaden (`insert`) a la tabla.

| clave_venta | producto | cantidad |
|---|---|---|
| 1 | A | 10 |
| 2 | B | 5 |
| 3 (nueva) | C | 8 |
| 4 (nueva) | A | 3 |

### Update

Caso más raro pero también posible: un valor que ya existe en la tabla ha cambiado en el sistema
fuente, y por tanto hay que actualizarlo (`update`) en lugar de añadirlo.

| clave_primaria | valor (antes) | valor (después) |
|---|---|---|
| 2 | 100 | 150 (actualizado) |

Suele haber herramientas `ETL` que gestionan esto de forma automática: reconocen, normalmente en base
a la `Primary Key`, si una fila ya existe.

- Si existe y el valor cambió → se actualiza (`update`).
- Si no existe → se añade la fila completa (`insert`).

Estas son las dos operaciones principales del proceso de carga.

> ⚠️ Notar que no se menciona **borrar** (`delete`): normalmente no se borran datos del `Data
> Warehouse`, porque se quiere conservar el historial. En algunos casos puntuales podría ser necesario,
> pero en el caso común no lo es.

## Manejo de borrados en el sistema fuente

¿Qué pasa si una fila se elimina en el sistema fuente? Por ejemplo, un valor dimensional (un producto)
que ya no existe y se elimina de origen.

En ese caso, normalmente **no se debe borrar la fila** en el `Data Warehouse`. En su lugar, se añade
una columna adicional a modo de *flag* que indique si ese registro sigue vigente en el sistema fuente
o si ya fue eliminado de origen.

| clave_producto | producto | vigente_en_origen |
|---|---|---|
| 1 | A | true |
| 2 | B | false (eliminado en origen) |

Así es como normalmente se maneja la carga de datos usando Insert/Update en el `Data Warehouse`.

## Próximas clases

Ver cuáles son los distintos pasos intermedios del proceso de transformación.
