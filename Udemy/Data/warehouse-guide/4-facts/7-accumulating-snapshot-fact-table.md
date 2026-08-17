# Accumulating Snapshot Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es

El tercer y último tipo de `Fact Table`. Es similar a la [[6-periodic-snapshot-fact-table]] en que
cada fila también representa la agregación de una medida a través de muchos eventos, pero la
diferencia clave está en cómo se define el período:

- En la `Periodic Snapshot`, el período es **estandarizado** (un día, una semana, un mes).
- En la `Accumulating Snapshot`, el período **no está estandarizado** — está definido por la
  **duración de vida de un proceso**, con un principio y un final concretos, y normalmente varios
  **hitos** (`milestones`) o pasos intermedios que también interesa analizar.

Este tipo de tabla es útil para analizar **flujos de trabajo o procesos** completos.

## Ejemplo: cumplimiento de pedidos (order fulfillment)

Un pedido que llega a un fabricante, con hitos como: inicio y fin de producción, fecha de
inspección, fecha de envío.

- **Medidas**: cantidad de productos pedidos, tipo de producto, cantidad de productos dañados
  encontrados en la inspección, etc.
- **Claves foráneas**: una clave de fecha **por cada hito del proceso** — fecha de pedido, fecha de
  inicio de producción, fecha de fin de producción, fecha de inspección, fecha de envío, etc.

## Características

| Característica     | Detalle                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Frecuencia de uso  | Es el tipo de `Fact Table` **menos común** de los tres, pero aun así se presenta en la práctica.                                                                           |
| Cuándo usarla      | Cuando analizar el flujo de trabajo o el proceso en sí (no solo el resultado final) es importante.                                                                         |
| Patrón de columnas | **Pocas medidas, pero muchas claves foráneas de fecha/hora** — una por cada hito del proceso — a diferencia de la `Periodic Snapshot` (muchas medidas, pocas dimensiones). |

> ⚠️ Aunque hay muchas claves foráneas de fecha (una por cada hito), todas siguen apuntando
> conceptualmente a la **misma** dimensión de fecha, solo que utilizada varias veces con distintos
> significados (fecha de pedido, fecha de envío, etc.). Esto se conoce como `Role-Playing
> Dimension` — un concepto que se profundizará más adelante, al hablar en detalle de dimensiones.

## Próxima clase

Resumen y comparación de los tres tipos de `Fact Table`: `Transactional`, `Periodic Snapshot` y
`Accumulating Snapshot`.
