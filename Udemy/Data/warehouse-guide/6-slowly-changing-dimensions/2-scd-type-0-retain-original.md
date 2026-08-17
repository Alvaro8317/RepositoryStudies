# SCD Type 0 — Retain Original

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Qué es

`SCD Type 0` es el tipo más simple: se conservan siempre los datos originales, sin aplicar ningún
cambio. Es aplicable cuando **no hay cambios** en el atributo de la dimensión — o, más precisamente,
cuando esos cambios (si llegaran a ocurrir) **no necesitan reflejarse** en la tabla de dimensión.

> ⚠️ Hay que estar realmente seguro de que no habrá cambios (o de que no importan) antes de aplicar
> este tipo. No es una opción por omisión, sino una decisión consciente sobre ese atributo en
> particular.

## Cuándo aplica

- **La `Date Dimension`**, en general, es el ejemplo más común: es una tabla estática que no cambia.
  > ⚠️ Excepción: algunos atributos dentro de la propia `Date Dimension` sí pueden cambiar — por
  > ejemplo, los días festivos de la empresa (`company holidays`), que pueden actualizarse año a año.
- Atributos etiquetados como "originales", por ejemplo el nombre original de un producto — un valor
  que se sabe que se debe mantener tal cual llegó, sin actualizarlo nunca.

## Por qué es la opción más sencilla

Si un atributo cae en este caso, no hace falta aplicar ninguna estrategia ni lógica adicional: se
carga el valor en la tabla de dimensión y ya está — no requiere ningún trabajo extra de ETL para
gestionar cambios.

## Resumen

| Tipo         | Estrategia                                                                  |
| ------------ | --------------------------------------------------------------------------- |
| `SCD Type 0` | No se aplica ningún cambio — se conserva siempre el valor original cargado. |

## Próxima clase

Cuando sí es necesario reflejar cambios: `SCD Type 1` (`Overwrite`), donde se sobrescribe el valor
antiguo con el nuevo.
