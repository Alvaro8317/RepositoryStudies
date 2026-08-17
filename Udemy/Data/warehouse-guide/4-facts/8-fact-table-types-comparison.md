# Comparativa: los tres tipos de Fact Table

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Resumen y comparación de [[5-transactional-fact-table]], [[6-periodic-snapshot-fact-table]] y
[[7-accumulating-snapshot-fact-table]], cerrando el bloque de tipos de tablas de hechos.

| Aspecto                     | Transactional                                        | Periodic Snapshot                                                                    | Accumulating Snapshot                                                              |
|--------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Qué define una fila**         | Una transacción individual.                                 | La agregación de una medida durante un período estandarizado (día, semana, mes...). Otras dimensiones (ej. región) también pueden formar parte del grano — ej. "por día y por región". | El ciclo de vida completo de un proceso o evento (con un inicio y un final concretos). |
| **Dimensión de fecha**          | La fecha **de la transacción**.                             | La fecha de la **instantánea** — siempre el final del período agregado.                    | **Múltiples** fechas de instantánea, una por cada hito del proceso — todas relacionadas con el final de su respectivo período/hito. |
| **Cantidad de dimensiones**     | Alta — muy dimensional, gran flexibilidad de análisis.       | Menor que la transaccional.                                                                | Alta, mayormente a través de **claves foráneas de fecha** (una por hito).                |
| **Qué se mide**                  | El rendimiento de **cada transacción** individual.           | La agregación de las medidas durante el período.                                          | La agregación de las medidas a lo largo de la vida útil del proceso.                     |
| **Tamaño**                       | El más grande de los tres — grano muy detallado.             | Menor, porque los datos ya están agregados.                                               | Variable, según la cantidad de hitos y procesos.                                          |
| **Rendimiento**                  | Suele ser bueno, pero es el que más se beneficia de agregación adicional si hace falta. | Mejor de base, porque la agregación ya ocurrió al definir el grano.                        | Depende del caso — se beneficia también de un buen diseño de grano.                        |

## Ideas clave para recordar

- **La transacción define el grano** en `Transactional`; **el período estandarizado** en `Periodic
  Snapshot`; **el proceso completo (con sus hitos)** en `Accumulating Snapshot`.
- Detrás de una `Periodic Snapshot` suele existir, de forma subyacente, una tabla `Transactional`
  que se agrega.
- Hoy en día, con bases de datos de buen rendimiento, no siempre es necesario agregar los datos por
  motivos de performance — pero cuando sí hace falta, definir bien el grano (como ya se hace de
  forma natural en `Periodic Snapshot`) es la solución.

## Próxima sección

Con esto se cierra el bloque de tipos de `Fact Table`. El curso continúa profundizando en las
dimensiones.
