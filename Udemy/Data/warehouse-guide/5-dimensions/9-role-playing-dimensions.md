# Role-Playing Dimensions

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es una Role-Playing Dimension

Una `Role-Playing Dimension` es una dimensión — típicamente la `Date Dimension`, el caso más común —
a la que una misma `Fact Table` **hace referencia varias veces**, cada una con un significado o "rol"
distinto.

### Ejemplo

Una `Fact Table` de producción puede tener dos claves foráneas de fecha distintas: la fecha de pedido
(`order_date`) y la fecha en la que empezó la producción (`production_start_date`). Ambas apuntan
conceptualmente a lo mismo (una fecha del calendario), así que no tiene sentido **duplicar
físicamente** la `Date Dimension` en la base de datos — una tabla para "fecha de pedido" y otra para
"fecha de producción".

En su lugar, se reutiliza la **misma** `Date Dimension`, pero se conecta a la `Fact Table` **dos
veces**, una por cada clave foránea:

- Primer rol: la fecha de pedido.
- Segundo rol: la fecha de inicio de producción.

Con esto se puede analizar tanto los pedidos recibidos (agrupando por la fecha de pedido) como la
producción (agrupando por la fecha de inicio de producción), usando ambas veces la misma tabla física
de dimensión, pero con relaciones/uniones distintas.

## Cómo implementarlo

### En herramientas de BI (ej. Power BI, Tableau)

Se configuran **múltiples relaciones** entre la `Fact Table` y la misma `Date Dimension`: una
relación **activa** (la que se usa por defecto en los cálculos) y una o más relaciones **inactivas**,
que se activan explícitamente cuando se necesita analizar por ese otro rol.

### En SQL

Si el análisis se hace principalmente en SQL, se recomienda crear una **vista** (`view`) adicional por
cada rol que desempeña la dimensión.

> Una vista no duplica los datos físicamente: es solo una referencia con un nombre propio hacia la
> tabla física original. Aparece como si fuera una tabla independiente, pero internamente sigue
> apuntando a los mismos datos — así se evita la redundancia de duplicar la dimensión.

Por ejemplo, se puede crear una vista `production_start_date_dim` dedicada al rol de "fecha de inicio
de producción", y usarla en los `JOIN`s de ese análisis en particular, mientras la tabla física
`date_dim` sigue sirviendo también para el rol de "fecha de pedido".

## Resumen

La `Role-Playing Dimension` aparece cuando una `Fact Table` referencia la misma dimensión (más
comúnmente la `Date Dimension`) varias veces con distintos significados. No se debe duplicar
físicamente la dimensión — en vez de eso:

- En herramientas de `BI`: usar relaciones activas/inactivas hacia la misma tabla.
- En SQL: crear una vista dedicada por cada rol, facilitando el análisis sin duplicar datos.
