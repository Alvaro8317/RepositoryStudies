# SCD Type 3 — Add New Column

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Un punto intermedio entre Type 1 y Type 2

- `SCD Type 1` ([[3-scd-type-1-overwrite]]): completamente estático, solo refleja el estado actual.
- `SCD Type 2` ([[4-scd-type-2-add-new-row]]): conserva **toda** la historia de cambios.

`SCD Type 3` se ubica en un punto intermedio: en vez de conservar todo el historial o ninguno, permite
mantener un número limitado de **versiones alternables** del valor — normalmente dos: el estado actual
y el estado anterior.

## Cómo se implementa

A diferencia de `Type 2`, aquí **no se añade una fila nueva** — se añade una **columna adicional** en
la misma fila. Esa columna extra contiene el valor histórico (anterior), mientras que la columna
original sigue conteniendo el estado actual.

Con estas dos columnas, se pueden analizar los datos usando cualquiera de los dos estados: el actual o
el anterior, simplemente eligiendo la columna correspondiente al agrupar.

## Cuándo usarlo: cambios grandes, predecibles y simultáneos

Este tipo se usa típicamente cuando ocurre un **cambio significativo y planificado que sucede de una
sola vez** — no cambios frecuentes ni impredecibles.

### Ejemplo: reestructuración organizacional

Si una empresa reestructura sus categorías, o cambia las regiones de su jerarquía organizacional (ej.
antes solo existían "Norte" y "Oeste", y ahora se introduce "Sur"), se puede aplicar `Type 3` para
mantener tanto la región actual como la anterior.

Esto le da al usuario de negocio (ej. un gerente) la posibilidad de comparar: analizar las ventas con
la nueva estructura de regiones, pero también poder "volver" al estado anterior y ver cómo se verían
las cifras si la reestructuración no hubiera ocurrido — simplemente agrupando por la columna de región
anterior en vez de la actual.

## Flexibilidad adicional

- Sigue siendo posible **añadir una fila nueva** si aparece un atributo completamente nuevo sin nada
  asociado en el pasado (ej. una nueva línea de productos).
- También es posible usar **más de dos columnas** (ej. una tercera columna para un estado aún más
  anterior) si se necesita reflejar más de dos versiones.

> ⚠️ No se recomienda llevar esto al extremo (ej. decenas o cientos de columnas de histórico) — el
> caso típico y práctico es mantener solo dos estados: actual y anterior.

## Limitaciones: por qué Type 3 no es la opción por defecto

`Type 3` encaja bien solo en una situación específica: un cambio grande y **predecible**, donde todos
los valores cambian a la vez en un momento conocido.

| Situación                                              | Tipo recomendado                                                |
| ------------------------------------------------------ | --------------------------------------------------------------- |
| Cambios frecuentes e impredecibles                     | `SCD Type 2` — conserva todo el historial correctamente.        |
| Cambios menores que no importan para el análisis       | `SCD Type 1` — la opción más simple.                            |
| Cambio grande, planificado, que ocurre de una sola vez | `SCD Type 3` — permite alternar entre estado actual y anterior. |

## Resumen

`SCD Type 3` añade una columna adicional (en vez de una fila) para conservar un número limitado de
versiones de un atributo — típicamente el valor actual y el anterior. Es la mejor opción cuando ocurre
un cambio grande, planificado y simultáneo (ej. una reestructuración organizacional) y los usuarios de
negocio necesitan poder alternar entre el estado nuevo y el antiguo en su análisis.
