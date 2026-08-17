# Valores nulos en hechos

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Nulos en las medidas: normalmente no es un problema

Tener valores nulos en un hecho (la medida en sí) **no suele ser un problema**. Tanto `SQL` como
las herramientas de `BI` (`Power BI`, `Tableau`, etc.) manejan los nulos con facilidad en sus
agregaciones (`SUM`, `AVG`, `MIN`, etc.) — simplemente los ignoran en el cálculo.

### Ejemplo: monto entrante a una cuenta

| Día | Monto entrante |
|-------|-------------------|
| 1     | $50                |
| 2     | `NULL` (sin cambios) |

Al calcular el promedio del monto entrante, el resultado es **$50** — el valor nulo se excluye del
cálculo, no cuenta como cero.

> ⚠️ Este resultado puede ser **engañoso**: un promedio de $50 no significa que en promedio
> entraran $50 **por día**, sino que las transferencias que sí ocurrieron promediaron $50. Por eso,
> en algunos casos, tiene más sentido reemplazar el nulo por un **cero real**, si semánticamente lo
> que ocurrió fue "no entró nada" (y no "el dato no está disponible"). Cada caso debe evaluarse
> según lo que el nulo realmente representa.

## Nulos en claves foráneas: sí requieren cuidado

El único caso donde los nulos **sí son un problema real** es en las **claves foráneas** de la tabla
de hechos.

> ⚠️ Nunca se debe dejar una clave foránea como `NULL` en una `Fact Table`. Esto puede generar
> conflictos y datos faltantes al conectar la fact table con sus dimensiones — algunas filas
> quedarían sin poder unirse (`JOIN`) correctamente a la dimensión correspondiente.

### Solución: valores ficticios (dummy keys)

Cuando no hay un valor real disponible para una clave foránea, se debe usar un **valor ficticio**
(`dummy key`) en vez de `NULL` — por ejemplo, `999` o `-1`, cualquier valor que señale claramente
que se trata de un caso especial.

Ese mismo valor ficticio debe existir también como fila en la **tabla de dimensión**
correspondiente, con una descripción que explique el caso. Ejemplos:

- Un `wallet_id` inexistente → agregar la fila `999` en `dim_wallet` con una descripción como
  "cuenta obsoleta" (`deprecated account`).
- Una fecha inexistente → usar una fecha ficticia como `1900-01-01` en vez de `NULL`.

De esta forma, todas las filas de la fact table pueden seguir conectándose correctamente a sus
dimensiones, sin perder datos ni romper los `JOIN`s.

## Resumen

- Nulos en las **medidas** (hechos): generalmente está bien, las agregaciones los manejan de forma
  natural — solo hay que evaluar si conviene reemplazarlos por cero según el significado del dato.
- Nulos en **claves foráneas**: nunca dejarlos como `NULL` — usar un valor ficticio (`dummy key`)
  consistente entre la fact table y su dimensión.

## Próxima clase

Un tipo de hecho que **no** debería incluirse en una `Fact Table`: los hechos `to-date` (valores
acumulados a la fecha).
