# SCD Type 2 — Add New Row

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El problema que resuelve: SCD Type 1 no respeta la historia

En `SCD Type 1` ([[3-scd-type-1-overwrite]]), un cambio de atributo (ej. la categoría de un producto
pasa de "Dulces" a "Galletas") sobrescribe el valor y afecta **retroactivamente** todo el histórico:
todas las ventas pasadas de ese producto quedarían reasociadas a la nueva categoría, aunque en su
momento pertenecieran a la categoría anterior.

Lo deseable, en cambio, es que las ventas ocurridas **antes** del cambio sigan asociadas al valor
anterior, y solo las ventas ocurridas **después** del cambio se asocien al nuevo valor — es decir,
particionar correctamente la historia.

## Qué es SCD Type 2

`SCD Type 2` resuelve esto **sin tocar** las filas existentes: cuando hay un cambio en un atributo, se
**añade una fila nueva** en la tabla de dimensión, con una nueva `Surrogate Key`, que contiene el
valor actualizado. La fila anterior se mantiene intacta, representando el estado histórico.

> ⚠️ Es probablemente la `SCD` más poderosa y la **estrategia por defecto** a usar cuando se esperan
> cambios comunes en los atributos de una dimensión, precisamente porque particiona la historia de
> forma perfecta.

## Cómo se implementa

1. En la `Dimension Table`, al detectar un cambio en un atributo, se inserta una **fila nueva** con
   una `Surrogate Key` nueva (ej. `4`) y el valor actualizado — sin modificar ni eliminar la fila
   anterior.
2. En la `Fact Table`, **no se necesita ningún cambio retroactivo**: simplemente, a partir del momento
   del cambio, los nuevos hechos usan la nueva `Surrogate Key` como clave foránea. Los hechos
   anteriores al cambio siguen apuntando a la `Surrogate Key` antigua, tal como ya estaban.

Con esto, la historia queda perfectamente respetada: las ventas anteriores al cambio siguen agrupadas
bajo el valor antiguo, y las posteriores bajo el valor nuevo — sin necesidad de tocar la `Fact Table`
en absoluto.

## Contar valores correctamente pese a las filas duplicadas

Con `SCD Type 2`, un mismo producto puede terminar teniendo **varias filas** en la dimensión (una por
cada versión histórica de sus atributos). Esto no es un problema para contar productos únicos,
siempre que se conserve la `Natural Key` (ej. `Product_ID`) junto a la `Surrogate Key`: basta con
contar valores **distintos** de la `Natural Key` (`COUNT(DISTINCT product_id)`) para obtener el número
correcto de productos.

## Limitación pendiente

Con este enfoque tal como está, todavía no es posible distinguir cuál de las filas de un mismo
producto representa el **valor actual** (la versión vigente) frente a las versiones históricas. Se
necesitan estrategias adicionales para resolver esto — se tratarán en la próxima clase.

## Resumen

| Tipo         | Estrategia                                                  | Historial                                | Cambios en la Fact Table                     |
| ------------ | ----------------------------------------------------------- | ---------------------------------------- | -------------------------------------------- |
| `SCD Type 2` | Añadir una fila nueva con nueva `Surrogate Key` por cambio. | Se conserva, perfectamente particionada. | Ninguno — solo usar la nueva clave a futuro. |

## Próxima clase

Cómo identificar la fila "actual" de un producto dentro de un `SCD Type 2` (ej. columnas de vigencia
como fechas de inicio/fin o un flag de "es la versión actual").
