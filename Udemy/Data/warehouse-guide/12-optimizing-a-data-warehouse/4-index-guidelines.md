# Directrices prácticas para usar índices

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Ya se conocen los dos tipos de índices — `B-tree` (`10-b-tree-index.md`... ver [[2-b-tree-index]]) y
`Bitmap` (ver [[3-bitmap-index]]) —. Ahora toca ver **cuándo y dónde** conviene usarlos.

## ¿Un índice en cada columna?

No. Los índices tienen un coste: espacio de almacenamiento adicional, y una escritura/actualización
más lenta, porque cada índice también hay que mantenerlo al insertar o actualizar datos. Por eso hay
que pensar bien cuándo usarlos, y solo hacerlo cuando realmente son necesarios.

## Regla 1: las tablas pequeñas no necesitan índices

Si una tabla es pequeña, normalmente el optimizador de consultas (`query optimizer`) ni siquiera va a
usar el índice, porque no aporta ningún beneficio real frente a un `full table scan`. Los índices
solo tienen sentido en **tablas grandes** que sufren un rendimiento de consulta bajo, especialmente
si se filtran mucho los datos.

## Regla 2: indexar las columnas que se filtran con frecuencia

Conviene poner un índice en las columnas (y tablas) que se usan a menudo para **filtrar** los datos.
Por ejemplo, si se filtra con frecuencia por `customer_id` y ese filtro solo recupera, digamos, un
10% de la tabla, es un buen candidato para índice — evita el `full table scan` cuando solo hace falta
una fracción de los datos.

## Aplicado al Data Warehouse: fact tables y dimension tables

### Claves primarias (Fact / Dimension)

Un índice `B-tree` es la mejor opción para las claves primarias (`Surrogate Key`) — y, de hecho, al
definir una columna como clave primaria en la base de datos, normalmente ya se crea este índice
`B-tree` de forma automática.

### Claves foráneas (en la Fact Table)

Las claves foráneas se usan mucho para filtrar y para unir (`JOIN`) tablas, así que indexarlas también
mejora el rendimiento. Qué tipo de índice conviene depende, de nuevo, de la **cardinalidad**:

- Con pocos valores distintos (ej. 5, 10, 20, 100) → **`Bitmap Index`** suele ser la mejor opción.
- Con un rango muy amplio de valores distintos (ej. clave foránea hacia una dimensión enorme) →
  **`B-tree`** suele ser mejor.

### Dimension tables

Antes de indexar una tabla de dimensión hay que preguntarse:

1. **¿Es una tabla grande?** Si es pequeña (unos cientos de filas), probablemente no haga falta ningún
   índice — no aportará beneficio. Si tiene millones de filas, seguir al punto 2.
2. **¿Hay columnas que se usan mucho para filtrar/buscar?** Si es así, elegir el tipo de índice según
   la cardinalidad de esa columna:
   - Cardinalidad baja (pocas categorías distintas, ej. pocas subcategorías en una dimensión enorme)
     → `Bitmap Index`.
   - Cardinalidad alta → `B-tree`.

## Resumen

| Situación | Índice recomendado |
|---|---|
| Tabla pequeña | Ninguno |
| Clave primaria (`Surrogate Key`) | `B-tree` (normalmente automático) |
| Clave foránea / columna de filtro con cardinalidad baja | `Bitmap Index` |
| Clave foránea / columna de filtro con cardinalidad alta | `B-tree` |

## Próximas clases

Demostración práctica: cómo crear un índice sobre una columna concreta del `Data Warehouse`.
