# Transformaciones importantes en DataBrew

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Nest to Map / Nest to Array / Nest to Struct

### Nest to Map

Combina **varias columnas en una sola columna**, generando un mapa/diccionario de pares
**clave-valor**: la clave es siempre el **nombre de la columna** original y el valor es el valor de
esa columna en cada fila.

- Ejemplo: columnas `age` y `city` con valores `30` y `New York` se combinan en una única columna con
  un valor tipo `{"age": 30, "city": "New York"}` (formato similar a JSON).
- Cada fila del dataset original genera su propio objeto clave-valor en la nueva columna.

### Nest to Array

Muy similar a Nest to Map, pero en lugar de generar pares clave-valor, combina los valores de varias
columnas en un **array**: solo se conservan los valores, sin las claves (nombres de columna).

### Nest to Struct

Prácticamente igual que Nest to Map, pero garantiza al **100%** que se conserva el **tipo de dato
exacto** y el **orden exacto** de los valores. Se usa en lugar de Nest to Map cuando es importante
asegurar que tipo y orden se preserven estrictamente.

## Unnest Array / Unnest Map (transformaciones inversas)

- **Unnest Array**: toma un array dado en una columna y lo **expande en varias columnas** (una por
  cada valor del array).
- **Unnest Map**: toma un mapa con pares clave-valor en una columna y lo expande igualmente en varias
  columnas (una por cada clave).

Ambas son la operación inversa de Nest to Array / Nest to Map: separan de nuevo los valores combinados
en columnas independientes.

## Pivot

**Pivota** los datos de **filas a columnas**:

1. Se selecciona una **columna pivote** (ej. `quarter`, con valores Q1, Q2, Q3...).
2. Se selecciona el **valor a pivotar** (ej. `sales`).
3. Cada valor distinto de la columna pivote se convierte en una **nueva columna**, y las filas se
   reorganizan usando esos valores — por ejemplo, el valor de ventas del producto A en Q1 (`150`) pasa
   a la columna `Q1`.

El resultado es una tabla con estructura **similar a un informe** (formato "ancho").

## Unpivot

Es la operación **inversa** de Pivot: convierte columnas en filas.

- Se seleccionan las **columnas a despivotar** (ej. `Q1`, `Q2`).
- Se generan dos columnas nuevas: una de **atributos** (los nombres de las columnas seleccionadas, ej.
  `quarter`) y otra con los **valores** correspondientes.

> Aunque Pivot da una estructura más parecida a un informe, para **visualización de datos** suele ser
> preferible el formato "largo" que produce Unpivot: tener el trimestre en una única columna (en lugar
> de repartido en varias columnas Q1/Q2/Q3/Q4) facilita usar esa columna directamente como dimensión en
> herramientas de visualización.

## Transpose

Simplemente **intercambia filas y columnas**: es una rotación visual de la tabla completa.

- Ejemplo: si originalmente las columnas son `name`, `age`, `city`, tras transponer, esos nombres pasan
  a ser los valores de una columna de atributos (filas), y los valores originales de cada fila (ej.
  `Alice`, `Frank`) pasan a ser las nuevas columnas.

## Otras transformaciones comunes

| Transformación                | Descripción                                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Join**                       | Combina dos datasets usando una **columna de conexión** común (ej. una columna clave).                                 |
| **Split**                      | Divide una columna en varias, usando un **delimitador** (ej. separar código postal y ciudad por un espacio o guion).   |
| **Filter**                     | Filtra el dataset para descartar valores irrelevantes o con datos faltantes.                                           |
| **Sort**                       | Ordena los datos; suele ser un paso intermedio útil de cara a la visualización o para encadenar más transformaciones.  |
| **Conversiones de tipo**       | Convertir una columna de texto a `datetime`, a número, etc., para asegurar el tipo de dato correcto.                   |
| **Recuentos / estadísticas**   | Distintos tipos de conteos y estadísticas para resumir los datos.                                                       |

## Próximos pasos

En la siguiente clase se pone en práctica **AWS Glue DataBrew** en la consola.
