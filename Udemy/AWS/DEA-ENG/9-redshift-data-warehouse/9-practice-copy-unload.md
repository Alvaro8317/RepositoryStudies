# Práctica: cargar y descargar datos en Redshift (COPY / UNLOAD)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Objetivo

Practicar con **Redshift Query Editor v2** el flujo completo de:

1. **Cargar datos** desde un bucket de S3 a una tabla de Redshift con el comando **COPY** (por SQL
   y usando el asistente/wizard de carga).
2. **Descargar (exportar)** datos de Redshift a un bucket de S3 con el comando **UNLOAD**, y
   entender el efecto de la opción `PARALLEL`.

> ⚠️ Si el cluster es **Redshift Serverless** (en vez de provisioned), hay que verificar que existe
> un **VPC endpoint de tipo Gateway** para S3 en la VPC del workgroup — sin él, las llamadas a S3
> desde `COPY`/`UNLOAD` (que salen a través de la interfaz de red interna del cluster) pueden no
> tener conectividad y las operaciones fallarán.

## Parte 1: cargar datos con COPY

### Preparar el origen en S3

1. Crear un nuevo bucket de S3 (nombre único, resto de ajustes por defecto; para esta práctica se
   desactivó el bloqueo de acceso público solo por simplicidad — **en un entorno productivo habría
   que revisar esto con más cuidado**).
2. Subir el archivo CSV de origen (`orders.csv`) al bucket, dentro de un prefijo/carpeta (en este
   caso `redshift-source/`).

### Crear la tabla destino

Antes de poder copiar los datos, hay que crear la tabla en Redshift (no existía previamente en el
esquema `public`):

```sql
CREATE TABLE orders (
    order_id varchar(20),
    order_date varchar(20),
    customer_name varchar(100),
    state varchar(50),
    city varchar(50)
);
```

> ⚠️ El primer intento de carga usó un tipo de dato más estricto (ej. `date`/`int`) para columnas
> como `order_date`, y el `COPY` falló con un error de tipo (**"invalid digit found"**). La causa
> fue un formato de fecha inesperado en el CSV. La solución más simple para esta práctica fue
> **recrear la tabla usando `varchar` en las columnas problemáticas** — en un entorno productivo,
> lo correcto sería validar/transformar los datos con un proceso ETL antes de cargarlos.

### Cargar los datos con COPY

```sql
COPY public.orders
FROM 's3://alvaro8317-dea-certification-prod/redshift-source/'
CREDENTIALS 'aws_iam_role=arn:aws:iam::123456789012:role/service-role/AmazonRedshift-CommandsAccessRole-20260819T202502'
DELIMITER ','
IGNOREHEADER 1
REGION 'us-east-1';
```

- `FROM`: ruta del bucket/prefijo de S3 donde está el archivo (puede apuntar a un archivo concreto
  o a un prefijo con varios archivos).
- `CREDENTIALS`: el **rol IAM** asociado al cluster de Redshift (visible en la consola, en
  **Properties** del cluster → **Associated IAM roles**), que debe tener permisos para leer el
  bucket de S3.
- `DELIMITER ','`: el archivo CSV usa coma como delimitador.
- `IGNOREHEADER 1`: la primera fila del archivo es la cabecera y debe ignorarse.
- `REGION`: región donde está el bucket de S3 (en este caso `us-east-1`).

### Depurar errores de carga

Si el `COPY` falla, se puede consultar la tabla del sistema `sys_load_error_detail` para ver el
detalle de los errores:

```sql
SELECT *
FROM sys_load_error_detail
WHERE table_name = 'orders'
ORDER BY start_time DESC
LIMIT 20;
```

Una vez corregido el tipo de dato de la tabla (`DROP TABLE` + `CREATE TABLE` con `varchar`), volver
a ejecutar el `COPY` — debería completarse correctamente.

Verificar los datos cargados:

```sql
SELECT * FROM orders;
```

### Alternativa: asistente de carga (Load Data wizard)

Redshift Query Editor v2 ofrece un asistente visual que hace lo mismo por debajo (genera y ejecuta
un `COPY`):

1. **Load data** → elegir **Load from S3 bucket**.
2. Seleccionar el bucket/archivo de origen y la **región**.
3. Configurar el **formato de archivo** (delimitador, si tiene cabeceras, etc.).
4. Elegir si se carga en una **tabla existente** o se **crea una tabla nueva**:
   - Al crear una tabla nueva, el asistente propone un **esquema** inferido del archivo, que se
     puede ajustar (eliminar columnas, cambiar tipos de datos, definir clave primaria,
     restricciones `UNIQUE`/`NOT NULL`, añadir columnas nuevas como un `id` autoincremental, etc.).
5. Seleccionar el **rol IAM** desde un desplegable (más sencillo que copiar el ARN a mano).
6. Confirmar — el asistente ejecuta el `COPY` correspondiente automáticamente.

> ⚠️ El mismo problema de tipos de datos puede aparecer aquí: si la carga falla, ajustar el tipo
> de la columna conflictiva (ej. `order_date` a `varchar`) y reintentar.

## Parte 2: descargar datos con UNLOAD

El comando **UNLOAD** hace lo contrario de `COPY`: exporta el resultado de una consulta desde
Redshift a un bucket de S3.

```sql
UNLOAD('SELECT * FROM orders')
TO 's3://alvaro8317-dea-certification-prod/redshift-destiny/orders_table_parallel_off.csv'
CREDENTIALS 'aws_iam_role=arn:aws:iam::123456789012:role/service-role/AmazonRedshift-CommandsAccessRole-20260819T202502'
DELIMITER AS ','
ALLOWOVERWRITE
PARALLEL OFF;
```

- La fuente es una **consulta** (`SELECT`) — puede ser una consulta con transformaciones, no solo
  un `SELECT *` de una tabla.
- `TO`: ruta de destino en S3.
- `CREDENTIALS`: mismo rol IAM usado para `COPY`, esta vez con permisos de escritura en el bucket.
- `ALLOWOVERWRITE`: permite sobrescribir un archivo existente en esa ruta.
- `PARALLEL`: controla si se usa el procesamiento paralelo del cluster.

### Efecto de PARALLEL ON vs. OFF

- Con **`PARALLEL ON`** (comportamiento por defecto si se omite la opción): `UNLOAD` usa las
  **node slices** del cluster para escribir **varios archivos en paralelo** — los datos quedan
  particionados entre esos archivos.
- Con **`PARALLEL OFF`**: se genera **un único archivo** con todos los datos, sin particionar.

> ⚠️ En la práctica, ejecutar `UNLOAD` con `PARALLEL ON` (por defecto) generó varios archivos en el
> bucket, algunos de ellos vacíos — resultado esperado de repartir la escritura entre las node
> slices. Al usar `PARALLEL OFF`, se generó un único archivo con todos los datos, más fácil de
> inspeccionar/descargar para este caso de uso puntual.
> ⚠️ Antes de ejecutar `UNLOAD` en el editor, puede ser necesario desmarcar la opción de **sesión
> aislada (isolated session)** si ya hay demasiadas conexiones abiertas en el editor de consultas.

Una vez completado el `UNLOAD`, el archivo (o archivos) aparece en el bucket/prefijo de destino y
puede descargarse directamente desde la consola de S3.
