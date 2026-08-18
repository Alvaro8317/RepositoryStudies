# Índice de mapa de bits (Bitmap Index)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

El **índice de mapa de bits** (`Bitmap Index`) es un tipo especial de índice especialmente útil en
`Data Warehouses`, ya que rinde muy bien con grandes cantidades de datos combinadas con **cardinalidad
baja**: columnas que solo pueden tomar unos pocos valores distintos (ej. dos o tres), aunque la tabla
en sí sea enorme.

## Ventajas y desventajas

- ✅ **Muy eficiente en almacenamiento**: los datos se guardan como bits.
- ✅ **Muy buen rendimiento de lectura**.
- ⚠️ **Poco eficiente para manipulación de datos**: actualizar o insertar filas es más lento.

> ⚠️ En un `Data Warehouse` este inconveniente resulta fácil de asumir, porque el uso principal es
> leer datos (reporting/análisis), no manipularlos constantemente — por eso el `Bitmap Index` suele
> ser una muy buena opción ahí.

## Cómo funciona

En lugar de una estructura tipo lista/árbol como el `B-tree`, el `Bitmap Index` crea un **mapa de
bits por cada valor posible** de la columna, indicando en qué filas aparece ese valor (`1` = aparece,
`0` = no aparece).

Ejemplo con una columna `payment_type` que solo tiene dos valores posibles (`Visa` y `MasterCard`):

| Fila | Visa | MasterCard |
|---|---|---|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3 | 1 | 0 |
| 4 | 0 | 1 |

Para encontrar todas las filas con `Visa`, basta con mirar el bitmap de esa columna (filas 1, 2 y 3),
sin necesidad de escanear la tabla completa.

## Próximas clases

Ver directrices prácticas sobre cuándo y en qué columnas/tablas conviene usar cada tipo de índice
(`B-tree` o `Bitmap`).
