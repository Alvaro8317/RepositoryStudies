# Snowflake Schema

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Relación con el Star Schema

En teoría, el `Star Schema` es en realidad un **caso especial** del `Snowflake Schema`: el
`Snowflake Schema` es el concepto más general, ya que permite **múltiples niveles** de jerarquía en
las dimensiones. Dicho de otro modo, un `Star Schema` es un `Snowflake Schema` con un único nivel de
jerarquía.

> ⚠️ Aunque esto sea cierto en teoría, en la práctica el `Star Schema` es **mucho más común**.

## Qué es y cómo se ve

En [[5-star-schema]] vimos que un `Star Schema` acepta cierta **redundancia de datos** (ej. el
nombre de una categoría repetido por cada producto que pertenece a ella) a cambio de mejor
usabilidad y rendimiento de lectura.

En un `Snowflake Schema`, esa redundancia se reduce: en vez de repetir el texto de la categoría en
cada fila, se mantiene solo el `ID` (mucho más liviano en disco) y toda la información de la
categoría se almacena **una sola vez**, en una tabla propia — creando así un **segundo nivel de
jerarquía**. Esta ramificación adicional, visualmente, ya no se parece a una estrella sino a un
copo de nieve, de ahí el nombre del esquema.

A diferencia del `Star Schema`, el `Snowflake Schema` está, por tanto, **más normalizado**.

## Ventajas

| Ventaja                          | Por qué                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------------|
| Menor uso de espacio en disco        | Menos redundancia de datos → menor costo de almacenamiento, relevante con volúmenes muy grandes (millones/miles de millones de filas). |
| Más fácil de mantener/actualizar     | Al haber menos datos duplicados, hay menor riesgo de inconsistencias o corrupción de datos al actualizar — cada valor suele vivir en un solo lugar. |

## Desventajas

| Desventaja                       | Por qué                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------------|
| Mayor complejidad                    | Más tablas → más difícil entender dónde vive cada dato.                                          |
| Más `JOIN`s necesarios               | Se requieren más uniones para reconstruir la información completa.                                |
| Menor rendimiento de lectura         | Más `JOIN`s implican más cómputo y más escaneo de tablas → consultas más lentas.                  |
| Menor usabilidad                     | Consecuencia directa de la mayor complejidad y el menor rendimiento.                              |

## Recomendación práctica

> ⚠️ El objetivo principal de un `Data Warehouse` es **leer** datos (reporting, análisis) — no tanto
> operaciones de escritura frecuentes. Por eso, aunque el `Snowflake Schema` reduce redundancia, esa
> ventaja pesa menos que sus desventajas de rendimiento y usabilidad para este caso de uso.

- En el **`Data Mart`**: usar `Star Schema` por defecto, evitando `Snowflake Schema` siempre que sea
  posible.
- En la **`Core Layer`**: también se recomienda `Star Schema` como opción por defecto. Solo
  considerar `Snowflake Schema` ahí si hay problemas reales con operaciones de escritura (dificultad
  para mantener los datos) o, en casos poco frecuentes, si el costo de almacenamiento es un factor
  crítico. Si se modela el `Core` en `Snowflake Schema`, habrá que remodelar los datos al cargarlos
  en el `Data Mart` (que sí debería quedar en `Star Schema`).

En general, `Star Schema` debería ser el esquema por defecto por las ventajas que aporta a los
casos de uso típicos de un `Data Warehouse`. Aun así, vale la pena conocer el `Snowflake Schema`
para reconocerlo si aparece en la práctica.
