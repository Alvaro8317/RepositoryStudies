# ACID, locks y deadlocks

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Conceptos fundamentales de las bases de datos relacionales (aplicables en general, no solo en
[[1-rds|RDS]]): las propiedades **ACID** que garantizan transacciones fiables, y los mecanismos de
**locks** que las hacen posibles bajo acceso concurrente.

## ACID

Conjunto de propiedades que garantizan que las transacciones de una base de datos relacional se
procesen de forma fiable.

| Propiedad | Significado |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Atomicidad** | Una transacción es siempre todo o nada: si una parte falla, toda la transacción falla y no se guarda nada. Cada transacción se trata como una única unidad de éxito/fracaso. |
| **Consistencia** | Las transacciones deben seguir las reglas y restricciones definidas en la base de datos; tras cada transacción, la base de datos debe permanecer en un estado correcto y coherente. |
| **Aislamiento** | Las transacciones se procesan de forma independiente — los cambios de una transacción no son visibles para otras hasta que se completa. |
| **Durabilidad** | Una vez completada una transacción, queda registrada de forma permanente, incluso ante un fallo del sistema. |

Estas propiedades garantizan la integridad y coherencia de los datos.

## Locks (bloqueos)

Mecanismo — normalmente gestionado automáticamente por la propia base de datos, aunque también se
puede invocar manualmente — que evita conflictos cuando varias transacciones intentan acceder o
modificar los mismos datos de forma concurrente.

> ⚠️ El comportamiento exacto y la sintaxis de los locks pueden variar según el motor de base de
> datos. Los ejemplos siguientes usan sintaxis de **PostgreSQL**.

### Exclusive locks (bloqueos exclusivos)

- Se usan cuando una transacción quiere **modificar** datos (`INSERT`, `UPDATE`, `DELETE`).
- Son el modo de bloqueo **más restrictivo**: ninguna otra transacción puede leer ni escribir el
  recurso mientras el lock está activo.
- Se usan habitualmente para cambios estructurales importantes sobre una tabla (ej. añadir una
  columna, eliminar la tabla completa).

```sql
LOCK TABLE nombre_tabla IN ACCESS EXCLUSIVE MODE;
```

### Shared locks (bloqueos compartidos)

- Equivalen a "bloqueos de lectura": permiten que **múltiples transacciones** lean los datos
  (`SELECT`) de forma simultánea.
- Mientras el shared lock está activo sobre una tabla o fila, **ninguna otra transacción puede
  modificarla** hasta que se libere.
- Se usan para garantizar la coherencia de las operaciones de lectura.

```sql
LOCK TABLE nombre_tabla IN SHARE MODE;
```

También se puede aplicar un bloqueo más granular a nivel de **fila** en lugar de tabla completa, para
un control más fino de qué se bloquea.

### Bloqueo exclusivo a nivel de fila (`SELECT ... FOR UPDATE`)

Se usa cuando se seleccionan filas con la **intención de actualizarlas**: bloquea esas filas en modo
exclusivo para que ninguna otra transacción pueda modificarlas de forma conflictiva hasta que la
transacción actual se complete.

```sql
SELECT * FROM nombre_tabla WHERE id = 1 FOR UPDATE;
```

## Deadlocks (interbloqueos)

Un **deadlock** ocurre cuando dos o más transacciones quedan bloqueadas entre sí: cada una retiene un
recurso (tabla o fila) que la otra necesita para continuar, y cada una espera a que la otra libere el
suyo.

- Sin intervención externa (manual), las transacciones implicadas esperarían **indefinidamente** y
  no podrían avanzar.
- Requiere algún tipo de intervención — por ejemplo, cancelar manualmente una de las transacciones en
  conflicto — para resolverse.
