# Degenerate Dimensions

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es una Degenerate Dimension

A veces hay una "dimensión" en el modelo de datos que en realidad **no tiene una tabla de dimensión
separada**, pero que aún así funciona en cierto modo como una dimensión — es decir, se usa para
agrupar o filtrar. A esto se le llama `Degenerate Dimension`.

En otras palabras: es solo una **clave de dimensión** (un atributo) que queda en la `Fact Table`, sin
que exista ninguna tabla de dimensión asociada a ella.

## Cómo surge

Supongamos una `Fact Table` de ventas transaccionales, donde varias transacciones se pueden resumir
juntas bajo un mismo pago (`payment_id`). En principio podríamos pensar en crear una `Payment
Dimension` separada con su propia clave foránea.

Pero a menudo ocurre que todos los atributos relevantes de ese "pago" ya fueron extraídos hacia otras
dimensiones, o simplemente ese valor de cabecera no aporta información adicional. En ese caso, a la
`Payment Dimension` solo le quedaría su clave primaria — sin ningún atributo descriptivo real.

> ⚠️ No tiene sentido mantener una tabla de dimensión separada si no aporta información adicional más
> allá de la propia clave. Ahí es donde entra la `Degenerate Dimension`: se conserva el valor (ej.
> `payment_id`) directamente en la `Fact Table`, sin crear una tabla de dimensión para él.

## Por qué sigue siendo útil

Aunque no haya tabla de dimensión asociada, el valor puede seguir siendo valioso para el análisis. Por
ejemplo:

- Resumir (`SUM`) el importe agrupado por `payment_id`.
- Calcular el promedio (`AVG`) del importe por pago.

Para eso se necesita poder agrupar por esa columna, así que vale la pena conservarla en la `Fact
Table` aunque ya no funcione como una clave foránea real.

## Convención de nombre: sufijo `DD`

Como esta columna ya no es una verdadera clave foránea (no referencia ninguna tabla de dimensión),
conviene **dejarlo explícito** en el nombre de la columna. `Kimball` sugiere usar el sufijo `DD` para
señalar que se trata de una `Degenerate Dimension` — por ejemplo, `payment_id_DD`.

## Casos típicos

Las `Degenerate Dimensions` aparecen sobre todo en **hechos transaccionales**. Ejemplos comunes:

- `ID` de pedido (`order_id`)
- Número de factura o de facturación (`invoice_number`)

En estos casos, toda la demás información relacionada ya suele estar extraída en otras dimensiones,
y solo queda el identificador en sí — pero sigue siendo un atributo relevante para agrupar y analizar,
por lo que se conserva en la `Fact Table` aunque no tenga dimensión asociada.

## Resumen

Una `Degenerate Dimension` es una clave/atributo de dimensión que vive directamente en la `Fact
Table`, sin tabla de dimensión propia — normalmente porque ya no aporta información adicional más
allá del identificador. Se recomienda marcarla explícitamente (ej. sufijo `DD`) para diferenciarla de
una clave foránea real.
