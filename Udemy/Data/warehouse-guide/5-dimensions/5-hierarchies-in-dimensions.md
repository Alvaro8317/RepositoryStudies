# Jerarquías en dimensiones

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## El problema: datos normalizados en el sistema origen

En los sistemas fuente, los datos se usan para procesamiento transaccional y por eso suelen estar
**normalizados**. Por ejemplo, una tabla de productos suele tener solo el `ID` de categoría, y la
descripción de esa categoría vive en una tabla separada. Esto ahorra espacio en disco y funciona bien
para el rendimiento de escritura — es un buen ajuste para el procesamiento transaccional.

Pero un `Data Warehouse` está pensado para **procesamiento analítico**: buscamos alto rendimiento de
lectura y alta usabilidad. Si mantenemos los datos normalizados y replicamos esa estructura para
todas las dimensiones y sus jerarquías, terminamos con muchas claves foráneas y obtenemos un
`Snowflake Schema` — ver [[6-snowflake-schema]] en `3-dimensional-modeling/`.

> ⚠️ Es común que personas con más experiencia en modelado de datos (acostumbradas al modelo
> transaccional) tiendan por hábito a normalizar los datos también en el `Data Warehouse`. Hay que
> resistir esa costumbre: normalizar las dimensiones aquí no aporta beneficios reales y sí perjudica
> el rendimiento y la usabilidad.

## La solución: aplanar (desnormalizar) las jerarquías

En vez de mantener cada nivel de jerarquía en su propia tabla, se debe **aplanar** la dimensión: unir
(`JOIN`) los distintos niveles (ej. producto y categoría, vía `category_id`) y escribir el resultado
en el `Data Warehouse` como **una sola tabla** de dimensión.

Este es el enfoque recomendado por defecto — colapsar las jerarquías en una tabla más ancha, en vez
de tener múltiples dimensiones enlazadas entre sí.

## Combinar atributos de distintos niveles de la jerarquía

Además de aplanar, puede tener sentido **precalcular combinaciones** de atributos de distintos
niveles en una sola columna, para que estén listas para usar directamente:

- Combinar `año` + `trimestre` en una sola columna (ej. `"2022 Q1"`).
- Combinar `ciudad` + `estado` (ej. `"Nashville, TN"`).

> ⚠️ Esto es especialmente útil cuando un mismo valor puede repetirse en distintos niveles de la
> jerarquía y generar ambigüedad — por ejemplo, `Nashville` puede existir como ciudad en más de un
> estado. Una columna combinada como `"Nashville, TN"` evita esa confusión y facilita el análisis sin
> que el usuario final tenga que resolverlo por su cuenta.

## Resumen

Al tratar jerarquías en las dimensiones:

- Evitar replicar la normalización del sistema origen — no crear un `Snowflake Schema` innecesario.
- Aplanar las jerarquías, uniendo los distintos niveles en una sola tabla de dimensión.
- Considerar columnas combinadas para atributos de distintos niveles cuando facilite el uso o resuelva
  ambigüedades (ej. valores duplicados entre niveles).

El objetivo final es tener **menos dimensiones** y **tablas más aplanadas**, priorizando siempre
usabilidad y rendimiento de lectura sobre la reducción de redundancia.
