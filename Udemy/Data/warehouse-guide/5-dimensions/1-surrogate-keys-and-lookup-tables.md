# Surrogate Keys y Lookup Tables

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Repaso: por qué usar Surrogate Keys

Ya hemos visto que una `Dimension Table` siempre necesita una clave primaria, y que la `Natural Key`
que viene directamente del sistema fuente no es la mejor opción para esa clave primaria. En su lugar,
debemos sustituirla por una `Surrogate Key`: normalmente un número entero que se incrementa de uno en
uno.

¿Es necesario conservar la `Natural Key` original? No es obligatorio, pero sí se puede — a menudo no
hace falta.

## La Lookup Table

Para poder sustituir la `Natural Key` por la `Surrogate Key`, conviene generar una **tabla de
búsqueda** (`Lookup Table`): una tabla simple que solo contiene la referencia entre la `Surrogate Key`
creada y la `Natural Key` original.

Generarla es sencillo:

1. Consultar en SQL los distintos valores (`DISTINCT`) de la `Natural Key` (ej. el `ID` de producto).
2. Rellenar una secuencia numérica junto a cada valor para obtener la `Surrogate Key`.

Esto se puede hacer directamente en SQL o también con herramientas ETL.

## Cómo referenciar la Surrogate Key desde la Fact Table

La pregunta natural es: si la tabla de dimensión ahora usa `Surrogate Keys`, ¿cómo se crea la
referencia correcta desde la `Fact Table`, que originalmente solo tiene la `Natural Key` del sistema
fuente?

Hay dos escenarios típicos:

- Usar la `Lookup Table` para traducir la `Natural Key` de la tabla de hechos a la `Surrogate Key`
  correspondiente.
- Si la tabla de dimensión ya conserva tanto la `Surrogate Key` como la `Natural Key`, se puede hacer
  directamente un `JOIN` entre la `Fact Table` y la `Dimension Table`.

> ⚠️ Esta sustitución de la `Natural Key` en la `Fact Table` suele ser el **último paso**, después de
> haber realizado todas las demás transformaciones sobre la tabla de hechos.

## Ejemplo práctico: JOIN para sustituir la clave

```sql
SELECT
    s.*,
    p.product_key  -- Surrogate Key de la dimensión de producto
FROM sales_fact AS s
LEFT JOIN product_dimension AS p
    ON s.product_id = p.product_id  -- match por Natural Key
```

Puntos clave del ejemplo:

- Se parte de la `Fact Table` original con todos los atributos ya transformados (`s.*`).
- Se usa un `LEFT JOIN` desde la tabla de hechos (`s`) hacia la dimensión (`p`), usando alias para
  facilitar la referencia a columnas.
- El `JOIN` se hace por la `Natural Key` compartida (ej. `product_id`).
- El resultado añade la `Surrogate Key` de la dimensión (`product_key`) a la tabla de hechos,
  reemplazando así valores como `P034` por su equivalente entero (ej. `34`).

> ⚠️ Esto es solo un ejemplo de cómo hacerlo — existen otras formas (por ejemplo, quitar el prefijo
> `P` y convertir el resto a entero directamente), pero usar un `LEFT JOIN` contra la dimensión es una
> práctica muy común.

Con este resultado final, la `Fact Table` ya tiene las referencias correctas a la `Dimension Table`.
Por ejemplo, la línea de pedido 1 (gafas de sol TR7) queda correctamente vinculada al nombre de
producto y a sus atributos relacionados (categoría, subcategoría, etc.) en la dimensión — sin
necesidad de mantener esos atributos duplicados en la tabla de hechos.

## Características de una Dimension Table

Con esta estructura, las tablas de dimensiones tienden a tener:

| Característica | Detalle                                                                                        |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Filas**       | Pocas, en comparación con la `Fact Table`.                                                       |
| **Columnas**    | Muchas — tabla ancha, con distintos atributos descriptivos.                                      |
| **Contenido**   | Especialmente útil cuando hay valores de texto largos y muchos atributos descriptivos.           |

Estas dimensiones se usan luego para **agrupar y filtrar** los datos (`slice and dice`), usando solo
algunos de sus atributos según el análisis — por ejemplo, agrupar por nombre de producto. Este es el
punto de partida de cualquier análisis de datos, y por eso las dimensiones son tan importantes.

## Próxima clase

La dimensión más importante y más utilizada: la `Date Dimension`.
