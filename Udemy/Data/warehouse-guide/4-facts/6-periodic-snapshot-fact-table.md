# Periodic Snapshot Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es

En una `Periodic Snapshot Fact Table`, **cada fila representa la agregación de una medida a través
de muchos eventos**, tomada en un **período estándar** (hora, día, semana, mes, etc.).

En vez de guardar cada evento individual (como en [[5-transactional-fact-table]]), se agregan todas
las transacciones ocurridas dentro de ese período y se guarda el resultado ya resumido — de ahí el
nombre "snapshot" (instantánea).

> ⚠️ El período estándar elegido (ej. un día, una semana) **define el grano** de esta tabla — igual
> que en una `Transactional Fact Table` el evento define el grano, aquí es el período el que lo
> define.

## Relación con la Transactional Fact Table

Detrás de una `Periodic Snapshot Fact Table` suele existir, de forma subyacente, una tabla
transaccional: se toman todas las transacciones ocurridas en el período (ej. una semana) y, al
final de ese período, se calculan las agregaciones correspondientes (ingresos totales, ventas
totales, costos totales, etc.).

### Ejemplos

- **Ventas**: en vez de una fila por transacción, una fila por semana con los ingresos, ventas y
  costos totales de esa semana.
- **Llamadas**: una fila por día, resumiendo el número de llamadas, el número de llamadas perdidas
  y la duración total de las llamadas de ese día.

En ambos casos se observa el mismo patrón: **muchas medidas, pero pocas dimensiones** asociadas
(comparado con una `Transactional Fact Table`, que suele tener muchas claves foráneas).

## Características

| Característica                    | Detalle                                                                                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tamaño                            | Normalmente **menor** que una tabla transaccional, ya que el grano es menos detallado (agregado en vez de por evento individual).                                    |
| Crecimiento                       | Crece de forma **controlada y continua** (una fila más por cada nuevo período — un día, una semana), sin los picos de crecimiento rápido de una tabla transaccional. |
| Aditividad                        | Los datos suelen seguir siendo **aditivos**, ya que el grano fue definido pensando específicamente en lo que se necesita analizar.                                   |
| Valor analítico                   | No se pierde tanto valor analítico pese a la agregación, precisamente porque el grano se elige con cuidado según las necesidades reales de análisis.                 |
| Muchas medidas, pocas dimensiones | A diferencia de la tabla transaccional, aquí predominan los hechos sobre las claves foráneas.                                                                        |

## Manejo de períodos sin eventos

Si un período no tuvo ninguna transacción (ej. sin ventas durante un fin de semana), hay que decidir
entre `NULL` y `0`:

- Usar **`0`** si representa fielmente la realidad (hubo cero ventas).
- Usar **`NULL`** si no se quiere que ese período afecte cálculos como el promedio (ej. no se quiere
  que un fin de semana sin actividad baje artificialmente la media diaria).

Este es el mismo criterio ya visto en [[2-null-values-in-facts]] al decidir entre `NULL` y `0` en
una medida.

## Próxima clase

El tercer y último tipo: `Accumulating Snapshot Fact Table`.
