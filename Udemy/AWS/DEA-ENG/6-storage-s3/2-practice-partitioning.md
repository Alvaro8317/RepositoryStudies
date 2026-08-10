# Práctica: Particionamiento en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: crear particiones en S3 a partir de una estructura de carpetas, catalogarlas con un
Glue Crawler y comprobar el efecto real del particionamiento en el rendimiento de las consultas de
Athena. Archivos usados: `sales_data_London.csv`, `sales_data_London_2.csv`,
`sales_data_New_York.csv` y `sales_data_Tokyo.csv` (carpeta `csv-files/` de este módulo), con columnas
`Date, Product_ID, Quantity, Unit_Price, Total_Sales, Location`.

## Paso 1 — Crear el bucket y la estructura de carpetas

Se crea un bucket S3 nuevo (temporal, solo para esta práctica; nombre único a nivel global) y, dentro
de él, dos carpetas de primer nivel:

- `London/`
- `New York/`

> ⚠️ Esta estructura de carpetas es la que el Glue Crawler usará para crear las particiones
> automáticamente — a diferencia de lo descrito en [[1-partitioning]], aquí las carpetas se nombran
> con el valor plano (`London`, `New York`), **no** con el esquema clave-valor de Hive
> (`location=London`). Esto tiene consecuencias más adelante (ver "Nombre de la columna de partición").

Se sube `sales_data_London.csv` a `London/` y `sales_data_New_York.csv` a `New York/` (10 registros
cada uno).

## Paso 2 — Crawler para catalogar y particionar

Se crea un Glue Crawler (ej. `partitions-test`):

- **Fuente de datos**: se apunta al bucket completo (no a una subcarpeta concreta), para que el
  crawler recorra ambas subcarpetas y genere las particiones automáticamente a partir de ellas.
- **Rol IAM**: se reutiliza el rol de crawler ya creado en una práctica anterior.
- **Base de datos**: la ya existente en el Data Catalog. Se deja el prefijo de tabla vacío.
- Sin schedule (on-demand), ejecución manual.

Tras ejecutarlo (~1 minuto), el resultado son **1 tabla nueva** y **2 particiones** (una por cada
subcarpeta encontrada).

### Nombre de la columna de partición

En el Data Catalog, la tabla creada tiene las columnas del CSV (`date`, `product_id`, `quantity`,
`unit_price`, `total_sales`, `location`) más una columna adicional para la partición.

> ⚠️ Como las carpetas no seguían la convención clave-valor de Hive, el crawler **no pudo inferir un
> nombre de columna a partir del nombre de la carpeta** y la llamó genéricamente **`partition_0`**
> — en vez de, por ejemplo, `location`. Esto es justo lo contrario de lo ideal: ahora hay dos columnas
> con información parecida (`location`, la columna real del CSV, y `partition_0`, la partición), y solo
> una de ellas (`partition_0`) tiene el beneficio de rendimiento del particionamiento.

## Paso 3 — Consultar en Athena y comparar rendimiento

La tabla aparece en Athena marcada como particionada. Una vista previa sin filtros devuelve los datos
combinados de ambas carpetas (20 registros: 10 + 10), incluyendo `partition_0` como columna adicional.

Se comparan dos filtros equivalentes en apariencia, pero con comportamiento muy distinto:

| Filtro | Columna | Datos escaneados |
| ------ | ------- | ------------------ |
| `WHERE location = 'New York'` | Columna normal del CSV | Escanea **todos los archivos de todas las particiones** (el motor no sabe que esa columna coincide con una partición) |
| `WHERE partition_0 = 'New York'` | Columna de partición | Escanea únicamente los archivos de esa partición — en este caso, **~50% menos de datos** (solo 1 de las 2 particiones) |

Esto demuestra el beneficio real del particionamiento visto en [[1-partitioning]]: filtrar por la
columna de partición evita escanear las particiones irrelevantes, mientras que filtrar por una columna
normal (aunque tenga el mismo valor) no aporta ninguna mejora, aunque conceptualmente sea la misma
condición.

## Paso 4 — Añadir archivos: dentro de una partición existente vs. una partición nueva

### Añadir un archivo a una partición ya existente

Se sube `sales_data_London_2.csv` (5 registros adicionales) a la carpeta `London/` ya existente.

Al volver a consultar sin necesidad de rehacer nada, Athena ya devuelve los 5 registros nuevos:
`London/` pasa de 10 a **15 registros**. Añadir datos dentro de una partición ya catalogada **no
requiere actualizar metadatos** — Athena simplemente lee lo que haya en esa ubicación de S3 en el
momento de la consulta.

### Añadir una partición nueva

Se crea una carpeta nueva `Tokyo/` con `sales_data_Tokyo.csv` (10 registros).

Al consultar sin filtros, **los datos de Tokyo no aparecen**: la partición existe físicamente en S3,
pero el Data Catalog todavía no sabe de su existencia — a diferencia del caso anterior, una carpeta
nueva sí requiere actualizar los metadatos de partición.

## Paso 5 — Registrar la partición nueva

Hay dos formas de poner al día los metadatos de partición:

### Opción A — Manual, con `ALTER TABLE ... ADD PARTITION`

```sql
ALTER TABLE <nombre_tabla> ADD PARTITION (partition_0='Tokyo')
LOCATION 's3://<bucket>/Tokyo/';
```

- El nombre de columna (`partition_0` en este caso) debe coincidir exactamente con el que generó el
  crawler.
- La ubicación (`LOCATION`) debe ser la ruta S3 exacta de la carpeta (se puede copiar desde las
  propiedades del objeto/carpeta en la consola de S3).
- Los valores van entre comillas simples.

Tras ejecutar el `ALTER TABLE` y volver a consultar sin filtros, ya aparecen los **35 registros**
totales (15 de Londres + 10 de Nueva York + 10 de Tokio).

### Opción B — Automática, con `MSCK REPAIR TABLE`

```sql
MSCK REPAIR TABLE <nombre_tabla>;
```

Detecta y añade automáticamente las particiones nuevas que encuentre en la ubicación S3 de la tabla.

> ⚠️ Para que `MSCK REPAIR TABLE` funcione de forma fiable, las carpetas en S3 deben seguir
> **estrictamente** la convención de nomenclatura clave-valor de Hive (ej. `year=2022/`). Como en esta
> práctica las carpetas se nombraron con el valor plano (`Tokyo`, no `location=Tokyo`), no se puede
> confiar en este comando — por eso se optó por el `ALTER TABLE ADD PARTITION` manual de la Opción A.

## Verificación final

En el Glue Data Catalog, dentro de la tabla creada, la sección de particiones ya muestra las **3
particiones** disponibles (`London`, `New York`, `Tokyo`), reflejando la partición añadida
manualmente.
