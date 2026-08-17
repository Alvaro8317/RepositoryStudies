# Valores nulos en dimensiones

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Repaso: nulos en la Fact Table

Ya vimos que en las claves foráneas de la `Fact Table` los `NULL` deben evitarse a toda costa,
sustituyéndolos por un valor ficticio (ej. un número negativo). Si se dejan como `NULL`, se rompe la
integridad referencial: al hacer el `JOIN` con la tabla de dimensión, esas filas simplemente
**desaparecen** del resultado.

### Ejemplo: por qué los NULL "desaparecen" en un JOIN

Imaginemos que queremos desglosar las ventas por tipo de promoción, uniendo la `Fact Table` con la
`Promotion Dimension` y agrupando por tipo de promoción. Si las filas sin promoción tienen `NULL` en
la clave foránea, esas filas no aparecerán en absoluto en el resultado agrupado — el usuario de
negocio perdería esos valores sin darse cuenta.

Usando en su lugar un valor ficticio (ej. `-1`) en la clave foránea, el usuario sigue viendo esas
filas agrupadas bajo una categoría como "Sin promoción" (`No Promo`).

## Nulos en las dimensiones: siempre sustituir por un valor descriptivo

Para que ese valor ficticio funcione, la `Dimension Table` correspondiente debe tener una **fila con
ese mismo valor ficticio**, pero con un atributo descriptivo — nunca `NULL`. Ejemplos:

- `Promotion Dimension`: fila con descripción `"Sin promoción disponible"`.
- Dimensiones de categoría: fila con descripción `"Sin categoría disponible"`.
- `Date Dimension`: fila con una fecha ficticia (ej. `1900-01-01`) — el valor debe respetar el mismo
  tipo de dato que la columna (`date`, no texto).

> ⚠️ La razón de fondo: un `NULL` no es descriptivo y puede significar cualquier cosa para el usuario
> de negocio. Un valor como `"Sin promoción disponible"` es mucho más claro y, además, le da al
> usuario la opción de decidir si ese valor debe aparecer o no en sus agregaciones, agrupaciones o
> gráficos — un `NULL`, en cambio, desaparece por defecto de los gráficos en las herramientas de `BI`
> sin que el usuario lo decida.

## Diferencia clave con los nulos en hechos (measures)

| Caso                                    | ¿Se debe reemplazar el `NULL`?                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| Nulo en una **medida** de la Fact Table | No necesariamente — las agregaciones (`SUM`, `AVG`) suelen manejar los nulos bien.            |
| Nulo en una **clave foránea**           | Sí, siempre — usar un valor ficticio para no romper la integridad referencial.                |
| Nulo en un **atributo de dimensión**    | Sí, siempre — usar un valor descriptivo para que sea comprensible para el usuario de negocio. |

> ⚠️ Puede haber un caso particular de nulos "esperados" en los hechos: por ejemplo, si nunca hay
> ventas en fin de semana porque las tiendas están cerradas, no conviene usar `0` en vez de `NULL`,
> ya que eso distorsionaría el promedio hacia abajo respecto a las horas en que sí hay operación.

## Resumen

En las tablas de dimensiones, siempre se deben sustituir los nulos:

- Por un **valor ficticio** consistente con el tipo de dato (ej. `1900-01-01` para fechas).
- Por un **valor descriptivo** cuando el nulo viene de un atributo (ej. "Sin promoción disponible",
  "Sin categoría disponible").

Esto evita que los usuarios finales pierdan datos silenciosamente en sus reportes y les da control
real sobre cómo tratar esos casos en sus análisis.
