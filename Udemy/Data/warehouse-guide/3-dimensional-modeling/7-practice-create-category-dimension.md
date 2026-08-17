# Práctica: crear una dimensión de categoría con SQL

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Objetivo

Demostración rápida de cómo extraer una dimensión simple a partir de una tabla más ancha, usando
`SQL` directamente en `DBeaver` sobre la instancia `PostgreSQL` del curso. Es un ejemplo de por qué
es común usar `SQL` en el modelado dimensional.

Archivos usados (guardados en `files/`): `SQL+Script_DM_Example.sql` y `products.csv`.

## Punto de partida: tabla de productos

Se parte de una tabla `products` con columnas `product_id`, `product_name`, `category` y
`subcategory` — más de la información que realmente se necesita si solo interesa la categoría.

```sql
CREATE TABLE products (
    product_id varchar(5),
    product_name varchar(100),
    category varchar(50),
    subcategory varchar(50)
);
```

El objetivo es construir una **tabla de categorías** simplificada, que contenga solo los valores
distintos de `category` junto con un `ID` de categoría — de forma que la tabla de productos pueda
quedarse solo con la clave foránea hacia esa dimensión.

## Pasos

### 1. Reconectar la instancia RDS

Como la instancia se había detenido temporalmente (ver [[3-practice-staging-schema-setup]] en el
módulo de arquitectura), primero hay que iniciarla de nuevo desde la consola de `AWS` (`RDS` →
`Databases` → seleccionar la instancia detenida → `Start`) antes de poder conectarse desde
`DBeaver`.

### 2. Crear la estructura de la tabla `products`

Desde un script SQL abierto sobre el esquema `public` (clic derecho en el esquema → `SQL Editor` →
`Open SQL Script`), se ejecuta el `CREATE TABLE` de arriba — solo la estructura, sin datos todavía.

### 3. Importar los datos desde el CSV

Clic derecho sobre la tabla `products` recién creada → `Import Data` → `CSV`, seleccionando el
archivo `products.csv`.

> ⚠️ Al mapear las columnas del CSV a la tabla destino, hay que revisar que los nombres coincidan —
> en este caso el CSV traía `product (brand)` en vez de `product_name`, y `sub_category` en vez de
> `subcategory`. `DBeaver` permite ajustar ese mapeo manualmente en el asistente de importación antes
> de proceder.

### 4. Extraer los valores distintos de categoría

```sql
SELECT DISTINCT category
FROM products;
```

Usar `DISTINCT` es clave aquí: sin él, se verían todas las filas repetidas (una por cada producto),
en vez de solo los valores únicos de categoría.

### 5. Generar un ID para cada categoría

Se usa la función de ventana `ROW_NUMBER()` para asignar un número consecutivo a cada categoría
distinta, dándole alias `category_id` y colocándola como primera columna del resultado:

```sql
SELECT
    ROW_NUMBER() OVER (ORDER BY category) AS category_id,
    category
FROM products;
```

### 6. Guardar el resultado como una nueva tabla

Un `SELECT` normal solo genera un resultado de consulta, no persiste una tabla. Para crear la nueva
tabla de categorías se usa `SELECT ... INTO`:

```sql
SELECT DISTINCT category
INTO category
FROM products;
```

> ⚠️ No es posible escribir el resultado directamente sobre la tabla `products` (daría error) — se
> necesita una tabla nueva. En este ejercicio se pasa primero por una tabla intermedia llamada
> `category` (con los valores distintos), y luego se usa esa tabla para generar la tabla final con
> el `ID` ya incluido:

```sql
SELECT
    ROW_NUMBER() OVER (ORDER BY category) AS category_id,
    category
INTO category_table
FROM category;
```

### 7. Verificar el resultado

```sql
SELECT * FROM category_table;
```

Con esto queda creada la dimensión `category_table`, visible en el navegador de bases de datos de
`DBeaver`, con las categorías distintas y su `ID` correspondiente.

> ⚠️ Este ejercicio se detiene en el nivel de categoría por simplicidad — en un caso real se podría
> continuar de la misma forma para extraer también las subcategorías.

## Próxima clase

Profundizar en las tablas de hechos (`Fact Tables`), llevándolo también a la práctica.
