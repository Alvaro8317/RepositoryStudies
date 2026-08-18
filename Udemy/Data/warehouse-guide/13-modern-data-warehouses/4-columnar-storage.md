# Almacenamiento en columnas (Columnar Storage)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Como se vio en una clase anterior, una tabla con aspecto de filas y columnas se almacena
internamente en bloques. La forma tradicional de almacenar esos bloques es **basada en filas**
(`row-based storage`): un bloque contiene todos los valores de una única fila (por ejemplo, el
valor de la primera columna, luego el de la segunda columna, y así sucesivamente).

## Row-based storage: eficiente para procesamiento transaccional

Almacenar los datos por filas es muy eficiente para el **procesamiento transaccional** (`OLTP`),
porque una transacción normalmente necesita insertar o actualizar todos los valores de una fila a
la vez — y con `row-based storage`, esos valores ya están juntos en el mismo bloque.

El problema aparece con las consultas **analíticas**: normalmente solo se necesita procesar una o
unas pocas columnas, no todas. Con `row-based storage`, para obtener esas pocas columnas hay que
escanear igualmente todas las filas completas, enviar todos esos datos a memoria y procesarlos —
aunque la mayoría de las columnas leídas no se necesiten para la consulta. Esto es ineficiente para
fines analíticos.

## Columnar storage: optimizado para consultas analíticas

`Columnar storage` invierte esta lógica: en lugar de almacenar los bloques por filas, los almacena
**por columnas**. Por ejemplo, un bloque contiene todos los valores de la columna `transaction_id`,
otro bloque contiene todos los valores de `product_id`, y así sucesivamente.

Con esto, si una consulta `SELECT` solo necesita una columna, solo hace falta leer el bloque
correspondiente a esa columna — sin escanear ni procesar el resto de los datos. Al procesar mucha
menos cantidad de datos, la consulta es mucho más rápida y eficiente.

## Ventaja adicional: mejor compresión

Como cada bloque en `columnar storage` almacena datos de un único tipo (una sola columna), todos
los valores del bloque comparten el mismo tipo de dato. Esto permite elegir una codificación de
compresión específicamente optimizada para ese tipo de dato, logrando una compresión mucho más
eficiente que con `row-based storage`. Con ello:

- Se necesita menos espacio de almacenamiento.
- El procesamiento vuelve a ser más rápido, al haber menos datos que mover y leer.

## Ejemplo práctico

En una tabla con, por ejemplo, 100 columnas, si una consulta analítica solo necesita 5 de ellas:

| Almacenamiento | Datos que hay que procesar                              |
| -------------- | ------------------------------------------------------- |
| Row-based      | El 100% de las columnas de cada fila escaneada          |
| Columnar       | Solo el 5% de las columnas (las 5 columnas consultadas) |

> ⚠️ Este patrón — consultar solo un subconjunto de columnas de tablas muy anchas — es muy habitual
> en análisis de datos, por lo que `columnar storage` suele suponer una mejora de rendimiento muy
> significativa frente a `row-based storage` en cargas de trabajo analíticas.

Por estas razones, los `Data Warehouses` modernos, especialmente los que están en la nube, utilizan
bases de datos columnares — hoy en día, `columnar storage` es un factor muy importante para el
rendimiento de las consultas analíticas.
