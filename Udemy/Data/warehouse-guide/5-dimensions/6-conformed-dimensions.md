# Conformed Dimensions

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es una Conformed Dimension

Una `Conformed Dimension` es una dimensión que se **comparte entre múltiples Fact Tables** (o
múltiples `Star Schemas`). Su propósito es permitir **comparar hechos entre distintas tablas de
hechos** en un mismo reporte o análisis — algo que sin una dimensión compartida no sería posible.

### Ejemplo motivador

Imaginemos un `Data Mart` con un `Star Schema` de ventas, y queremos analizar también los costos —
una segunda `Fact Table` de costos. Para poder comparar ventas y costos en un mismo análisis,
necesitamos una dimensión compartida entre ambos hechos: una `Conformed Dimension`.

- **`Date Dimension`**: el ejemplo más típico. Tanto la `Fact Table` de ventas como la de costos se
  conectan a la misma `Date Dimension`, lo que permite comparar ambos hechos por fecha.
- **`Region Dimension`**: si ambas tablas de hechos incluyen la región (o el país), se puede comparar
  ventas y costos agrupando por ese atributo compartido.

Esta capacidad de comparar medidas de tablas de hechos independientes usando una dimensión compartida
se llama `Drill Across`.

## Requisito: atributos compartidos

Para que una dimensión funcione como `Conformed Dimension`, ambas tablas de hechos deben compartir
**atributos idénticos** — o al menos un **subconjunto** de atributos — de esa dimensión. Por ejemplo,
tanto el hecho de ventas como el de costos deben tener una clave foránea de fecha que apunte a la
misma `Date Dimension`.

## No hace falta la misma granularidad

Un punto clave: las tablas de hechos que comparten la dimensión **no necesitan tener la misma
granularidad**.

- El hecho de costos podría tener grano diario: una fila por fecha, con la clave foránea única
  (`Periodic Snapshot Fact Table`).
- El hecho de ventas podría tener grano transaccional: múltiples filas por la misma fecha (valores
  duplicados de la clave foránea de fecha).

Esto es justamente lo que hace tan potente a la `Conformed Dimension`: aunque las tablas de hechos
sean independientes y tengan granularidades distintas, se pueden seguir comparando sus medidas a
través de la dimensión compartida.

## Distintas claves foráneas para distinta granularidad

También es posible que ambas tablas de hechos usen **claves foráneas distintas** dentro de la misma
dimensión, si tienen grano diferente:

- El hecho de costos (grano mensual) podría usar una clave foránea basada en año + mes.
- El hecho de ventas (grano diario) podría usar la clave foránea diaria.

En ese caso, hay que tener cuidado de usar los atributos correctos de la dimensión según el grano de
cada hecho.

Una alternativa para evitar mantener dos claves foráneas distintas es, en el hecho con grano mensual,
usar siempre el primer día del mes como clave foránea diaria. Es una opción válida, pero si la
dimensión ya tiene disponible una clave a nivel de mes, suele preferirse usar esa clave foránea de mes
directamente en vez de forzar el primer día del mes.

## Resumen

- Una `Conformed Dimension` se comparte entre varias `Fact Tables` para poder compararlas entre sí
  (`Drill Across`).
- Requiere atributos compartidos (o un subconjunto) entre las tablas de hechos involucradas.
- No requiere la misma granularidad entre las tablas de hechos — cada una puede usar su propia clave
  foránea, mientras apunten a la misma dimensión.
- Si se van a combinar múltiples `Fact Tables` en el análisis, conviene diseñar `Conformed Dimensions`
  desde el inicio del modelo de datos.
