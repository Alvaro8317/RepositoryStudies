# Redshift: Materialized Views

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Este es un tema importante no solo en Redshift específicamente, sino en general en el mundo de las
bases de datos.

## Vistas normales vs. Materialized Views

A veces tenemos una consulta que se ejecuta con frecuencia. Para ahorrar tiempo, simplificarla,
hacerla reutilizable o usarla en distintas aplicaciones, podemos crear una **vista**.

- Una **vista normal** solo almacena la **lógica de la consulta** (ej. una sentencia `SELECT`), no
  los datos.
- Al hacer `SELECT` sobre la vista, en realidad se ejecuta la consulta subyacente cada vez.
- Si la consulta subyacente requiere muchos cálculos, esto puede tardar bastante en devolver el
  resultado.

```sql
CREATE VIEW ORDERS_VIEW AS
SELECT ORDER_ID, CUSTOMER_NAME
FROM ORDERS
WHERE ORDER_DATE = '01-04-2018';

SELECT * FROM ORDERS_VIEW;
```

Una **Materialized View** combina las ventajas de una **tabla** y una **vista**:

- **Pre-calcula** los resultados de la consulta, ejecutándola en un **horario programado**.
- Almacena ese conjunto de resultados precalculados **físicamente**, de forma similar a una tabla
  — con la diferencia de que se genera a partir de una vista subyacente.
- Como los datos de la tabla base pueden cambiar, la Materialized View también debe
  **actualizarse periódicamente** para mantenerse consistente.

|                | Vista normal                            | Materialized View                          |
| -------------- | --------------------------------------- | ------------------------------------------ |
| Almacena       | Solo la lógica de la consulta           | Los resultados precalculados (físicamente) |
| Al consultarla | Ejecuta la consulta subyacente cada vez | Lee datos ya calculados — muy rápido       |
| Mantenimiento  | No requiere                             | Requiere actualización periódica (refresh) |

> ⚠️ Solo tiene sentido crear una Materialized View si la consulta subyacente es **compleja y
> costosa** (potencial real de mejora de rendimiento) **y** se consulta **con regularidad**. Si la
> consulta ya es rápida, o no se reutiliza, no aporta beneficio.

```sql
CREATE MATERIALIZED VIEW SALES_SUMMARY AS
SELECT CITY, COUNT(ORDER_ID) AS ORDER_AMOUNT
FROM ORDERS
GROUP BY CITY;

SELECT * FROM SALES_SUMMARY;
```

También se puede crear una Materialized View a partir de **otra Materialized View existente** como
referencia — no es necesario basarse siempre en tablas.

## Creación

La sintaxis es casi idéntica a la de una vista normal, añadiendo la palabra clave `materialized`:

```sql
CREATE MATERIALIZED VIEW nombre_vista
AUTO REFRESH YES
AS
SELECT ...
```

- `AUTO REFRESH`: activa la actualización automática de los datos. **Por defecto es `NO`.**
- Se puede modificar después de creada la vista (ej. pasar de `NO` a `YES`).

## Materialized Views para streaming ingestion

Un caso de uso importante es utilizar **Kinesis Data Streams** o **Amazon MSK** (Managed Streaming
for Apache Kafka) como fuente de datos directamente para una Materialized View — muy útil para
analizar datos en streaming, con muy poca sobrecarga operativa.

Pasos:

1. **Crear un IAM Role** con los permisos necesarios para acceder a Kinesis / MSK y al stream de
   datos.
2. **Crear un esquema externo** (`external schema`) que apunte a la fuente de streaming (ej.
   Kinesis).
3. **Crear la Materialized View** dentro de ese esquema externo, consumiendo los datos del stream:

```sql
CREATE MATERIALIZED VIEW nombre_vista
AUTO REFRESH YES
AS
SELECT ...
FROM external_schema.stream_name
```

- Se puede activar `AUTO REFRESH YES` para mantener los datos actualizados automáticamente (no al
  100% en tiempo real, pero se ejecuta según un horario).

## Consideraciones sobre el refresh

- **Auto refresh**: se ejecuta automáticamente cuando hay recursos del clúster disponibles, para
  minimizar interrupciones en otras cargas de trabajo. Se activa con el parámetro `AUTO REFRESH` en
  la definición de la vista, o después de creada (ej. desde el editor de consultas de la consola, o
  mediante la Scheduler API).
- **Refresh manual**: se ejecuta con una sentencia SQL explícita para actualizar la Materialized
  View bajo demanda.

## Comandos principales

| Comando                     | Uso                                       |
| --------------------------- | ----------------------------------------- |
| `CREATE MATERIALIZED VIEW`  | Crear la vista materializada.             |
| `ALTER MATERIALIZED VIEW`   | Modificarla (ej. activar `AUTO REFRESH`). |
| `REFRESH MATERIALIZED VIEW` | Actualizar manualmente los datos.         |
| `DROP MATERIALIZED VIEW`    | Eliminarla.                               |

> ⚠️ Redshift decide automáticamente el mejor momento para ejecutar el `auto refresh`, teniendo en
> cuenta la disponibilidad de recursos del clúster y el impacto en las cargas de trabajo
> productivas.
