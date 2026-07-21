# Práctica: Consultar datos con Amazon Athena

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

Partiendo de lo ya configurado: una **database** (`clientes`) con una **tabla** creada mediante un **Glue Crawler**, cuyo esquema fue inferido automáticamente a partir de un archivo en un bucket S3 (carpeta `documentos`). Ahora se aprovecha esa tabla para **consultar los datos directamente con Amazon Athena**.

## Cómo llegar a Athena desde Glue

Hay dos caminos desde la consola del Data Catalog:

- Desde la **database**: opción **"View data"**.
- Desde la **tabla**: en **Actions → "View data"**.

En ambos casos, se pregunta si se desea ir a **Athena** para previsualizar los datos.

> 💰 Athena es un servicio de **pago por uso**: el coste depende del **número de consultas** y de la **cantidad de datos leídos**. Para volúmenes pequeños, el coste es prácticamente insignificante.

## Configuración inicial obligatoria: Query result location

Al entrar por primera vez al editor de consultas de Athena, suele aparecer un aviso indicando que **falta configurar una ubicación de resultados** (query result location) en S3 — es un requisito indispensable para poder ejecutar cualquier consulta.

### Pasos para configurarlo

1. Ir a **Edit settings** en Athena.
2. En **Query result location**, seleccionar un bucket de S3:
   - Puede ser un bucket dedicado exclusivamente a esto.
   - O reutilizar un bucket ya existente (opción usada en el ejemplo, seleccionando desde el nivel superior del bucket).
3. Guardar (**Save**).
4. Esto crea automáticamente una **carpeta adicional** dentro del bucket donde se almacenarán los resultados de las consultas.

## El editor de consultas (Query Editor)

- En el panel izquierdo se selecciona la **database** (ej. `clientes`).
- Debajo aparecen las **tablas** disponibles, que se pueden expandir para ver sus **columnas y tipos de datos** — tal como en una base de datos relacional tradicional (aunque, como se vio antes, son solo metadatos sobre archivos en S3).

### Vista previa rápida de una tabla

- Sobre la tabla, en el menú de tres puntos → **"Preview table"**.
- Esto genera y ejecuta automáticamente una consulta tipo `SELECT * FROM <tabla> LIMIT 10`, mostrando las columnas y los datos.

## Ejecutar consultas SQL

Athena permite ejecutar **SQL estándar** sobre los datos del Data Catalog. Ejemplos del caso práctico:

```sql
-- Vista previa básica
SELECT * FROM clientes.documentos LIMIT 10;

-- Cálculo de la edad media, con alias y redondeo
SELECT ROUND(AVG(edad), 2) AS edad_media
FROM clientes.documentos;
```

- El editor ofrece **autocompletado** de nombres de columnas y tablas, muy útil al escribir las consultas.
- Se pueden ejecutar consultas con el botón **Run** o con el atajo **Ctrl + Enter**.
- Se pueden usar funciones SQL estándar: alias (`AS`), funciones de agregación (`AVG`), redondeo (`ROUND`), etc.

## Idea clave

Athena permite consultar, con sintaxis SQL estándar, datos que **siguen almacenados en su ubicación original en S3**, sin necesidad de moverlos ni cargarlos en una base de datos tradicional — todo gracias a los metadatos generados previamente por el Glue Crawler en el Data Catalog.
