# Configurar las tablas en pgAdmin

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Con el diseño final de la `Fact Table` ya definido (ver [[2-source-data-and-fact-table-design]]), toca
configurar las tablas correspondientes en `pgAdmin` (el sistema de gestión de base de datos), antes de
diseñar la ingesta de datos y el flujo `ETL` completo.

## Tabla de hechos de ventas — Staging

Se crea la tabla `sales` en la capa de `Staging` con **exactamente la misma estructura** que en los
datos de origen — sin ninguna transformación adicional, ya que en `Staging` solo se extraen los datos
tal cual están en el sistema fuente.

## Tabla de hechos de ventas — Core

Se crea la tabla `sales` en la capa `Core` con el **diseño final** definido previamente: incluye todas
las `Foreign Keys` (`date_key`, `product_key`, `payment_key`) y las columnas adicionales calculadas
(`total_cost`, `total_price`, `profit`).

## Dimensión de pago (Payment) — solo Core

> ⚠️ Esta `Junk Dimension` de pago solo necesita tabla en la capa `Core`, **no** en `Staging`: toda su
> información sale directamente de la tabla de ventas, que ya ha sido puesta en `Staging`. No hace
> falta un `Staging` adicional para ella.

Estructura de la tabla:

- `payment_key` — `Primary Key` / `Surrogate Key`, configurada como una secuencia autoincremental
  (cada fila nueva obtiene el siguiente valor: 1, 2, 3...).
- `payment` y `loyalty_card` — los dos atributos que se combinan en esta `Junk Dimension`, con todas
  las combinaciones posibles precargadas.

## Próximas clases

Ir a `PDI` (`Pentaho Data Integration`) para diseñar la puesta en escena (`Staging`) de la `Fact
Table` de ventas.
