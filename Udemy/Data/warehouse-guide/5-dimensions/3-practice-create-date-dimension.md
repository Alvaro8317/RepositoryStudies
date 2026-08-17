# Práctica: Crear la Date Dimension con SQL

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Idea general

La `Date Dimension` se puede configurar muy fácilmente en el sistema de gestión de base de datos
usando código SQL, y se puede **rellenar previamente sin ningún dato de origen** — a diferencia de
otras dimensiones, no depende de datos que vengan de un sistema fuente.

> ⚠️ Este no es un curso de SQL, así que el detalle del código no se explica línea por línea. El
> ejemplo usa `PostgreSQL`, pero si se usa `SQL Server`, `Oracle` u otro motor, es fácil encontrar
> código equivalente para crear una `Date Dimension` con una búsqueda rápida — la lógica es la misma.

## Pasos para crear la tabla

### 1. Crear la estructura de la tabla (`CREATE TABLE`)

Se define el nombre de cada columna, su tipo de dato y sus restricciones (`constraints`). Por
ejemplo, la clave primaria y la fecha (y en general, todas las columnas de esta dimensión) no deben
permitir valores nulos (`NOT NULL`).

### 2. Añadir la restricción de clave primaria (`ALTER TABLE`)

Una vez creada la tabla, se debe marcar físicamente una columna como clave primaria usando
`ALTER TABLE ... ADD CONSTRAINT ... PRIMARY KEY (...)`. Siempre se debe establecer explícitamente la
clave primaria de la tabla.

### 3. Crear un índice sobre la columna de fecha

Se crea un índice (`INDEX`) sobre la columna de fecha para mejorar el rendimiento de las consultas
que filtren o hagan `JOIN` por esa columna.

### 4. Insertar los datos (`INSERT INTO`)

Se rellena la tabla con `INSERT INTO`, generando los valores de la `Surrogate Key` mediante una
secuencia y calculando el resto de los atributos (año, mes, trimestre, etc.) para cada fecha.

> ⚠️ La tabla se puede prellenar hasta muy adelante en el futuro (ej. los próximos 10 años), ya que
> la `Date Dimension` es completamente calculable y no depende de que existan hechos futuros en la
> `Fact Table`.

## Reutilización

Una vez creada, esta tabla sirve como **plantilla reutilizable**: se puede guardar en una base de
datos de la empresa y reutilizar en distintos `Data Warehouses`, ajustando columnas (añadiendo,
quitando o modificando atributos) según el caso de uso antes de cargarla.
