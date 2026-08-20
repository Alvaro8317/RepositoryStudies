# Redshift: comando VACUUM

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Por qué es necesario VACUUM?

Con el tiempo, a medida que se **añaden**, **eliminan** o **actualizan** filas en una tabla, los
datos pueden **fragmentarse**. Esto puede provocar:

- Un **mayor uso de almacenamiento**.
- Un **menor rendimiento** de las consultas.

Esto ocurre porque:

- Cuando se **borran datos** de una tabla, el espacio que ocupaban **no se libera físicamente de
  inmediato** — solo se marca como **disponible para reutilización**.
- A medida que se añaden y eliminan datos, el **orden de clasificación (sort order)** de la tabla
  también puede desorganizarse, lo que ralentiza aún más el rendimiento de las consultas.

El comando **VACUUM** realiza tareas de mantenimiento para solucionar esto:

- **Reordena las filas** de la tabla (recupera el sort order).
- **Recupera el espacio en disco** ocupado por filas marcadas como eliminadas pero no liberadas
  físicamente.

> ⚠️ Redshift ejecuta un `VACUUM DELETE` **automáticamente en segundo plano** de vez en cuando,
> pero también se puede (y a veces conviene) ejecutar **manualmente**.

Durante la ejecución de `VACUUM`, las tablas siguen siendo **accesibles**, aunque quedan
**bloqueadas para actualizaciones y eliminaciones**.

## Umbral de ordenación (sort threshold)

- Por defecto, `VACUUM` **omite la fase de ordenación** de una tabla cuando esta ya está ordenada
  en un **95% o más** — no hay suficiente beneficio adicional en volver a ordenarla.
- Este umbral (por defecto **95%**) se puede configurar.

## Sintaxis y variantes

El comando se ejecuta sobre una tabla específica, con un método o estilo concreto:

```text
VACUUM [FULL | SORT ONLY | DELETE ONLY | REINDEX | RECLUSTER] tabla
[TO threshold PERCENT] [BOOST]
```

### VACUUM FULL

- **Ordena** la tabla especificada **y** recupera el espacio en disco ocupado por filas marcadas
  para eliminación (por `UPDATE`/`DELETE`) pero aún no liberadas.
- Es la opción **recomendada para la mayoría de aplicaciones** y el **valor por defecto** si no se
  especifica ninguna variante.

### VACUUM SORT ONLY

- Solo **ordena** los datos de la tabla, sin recuperar espacio.
- Útil porque el orden de los datos es importante para el rendimiento en consultas con cláusulas
  `WHERE` o `JOIN`.

### VACUUM DELETE ONLY

- Solo **libera el espacio** ocupado por filas marcadas como eliminadas pero no borradas
  físicamente.
- Bloquea temporalmente las operaciones de `UPDATE`/`DELETE`, pero los datos siguen siendo
  **accesibles**.

### VACUUM REINDEX

- **Reconstruye completamente el índice** de las tablas — tarda **más tiempo** que `VACUUM FULL`.
- Aplica a tablas con una **sort key intercalada (interleaved sort key)**: varias columnas
  designadas como claves de ordenación, todas con la **misma importancia** entre sí.
- Con el tiempo, muchas actualizaciones y cambios de datos pueden hacer que la **distribución de
  valores** de la columna de sort key deje de ser óptima para este tipo de índice.
- `VACUUM REINDEX`:
  1. **Analiza** la distribución de la sort key.
  2. **Reconstruye el índice**.
  3. Ejecuta además un **VACUUM FULL** adicional al terminar.
- Es útil específicamente para tablas con **interleaved sort keys** que han tenido muchos cambios
  de datos, ya que puede mejorar significativamente el rendimiento — aunque el proceso es lento.

### VACUUM RECLUSTER

- Solo **ordena las partes de la tabla que están desordenadas**; las partes ya ordenadas se dejan
  como están.
- Es más **selectivo** y **consume menos recursos** que un `VACUUM FULL`.
- Recomendado para **tablas grandes con ingestas frecuentes**.

## Opciones adicionales

- **`TO threshold PERCENT`**: permite especificar el umbral por encima del cual `VACUUM` omite la
  fase de ordenación, y también el umbral para la fase de recuperación de espacio — hace el
  comando más eficiente al evitar trabajo innecesario.
- **`BOOST`**: añade recursos adicionales (memoria, espacio en disco) al proceso de `VACUUM`,
  según estén disponibles, para acelerarlo.

## Resumen de variantes

| Variante        | Qué hace                                        | Cuándo usarla                                                                 |
| --------------- | ----------------------------------------------- | ----------------------------------------------------------------------------- |
| **FULL**        | Ordena + recupera espacio                       | Por defecto, recomendado para la mayoría de casos                             |
| **SORT ONLY**   | Solo ordena                                     | Cuando el orden importa para `WHERE`/`JOIN` y no hace falta recuperar espacio |
| **DELETE ONLY** | Solo recupera espacio                           | Cuando solo interesa liberar espacio en disco                                 |
| **REINDEX**     | Reanaliza y reconstruye el índice + VACUUM FULL | Tablas con interleaved sort keys y muchos cambios de datos                    |
| **RECLUSTER**   | Ordena solo las partes desordenadas             | Tablas grandes con ingestas frecuentes                                        |
