# Práctica: Trabajo ETL visual en Glue

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En esta práctica se configura un **ETL Job** muy sencillo en **AWS Glue** para mover datos entre dos
ubicaciones de S3: se extraen desde un bucket origen (el mismo cubo donde ya se cargó el archivo CSV) y
se cargan en un bucket/carpeta destino, simulando una zona de un **Data Lake**.

El flujo sigue el patrón que da nombre a Glue: **ETL — Extract, Transform, Load**.

- **Extract**: conectar a una fuente (S3).
- **Transform**: transformaciones intermedias (no se usan en esta práctica, se ven más adelante).
- **Load**: cargar el resultado en un destino (S3).

## Preparar el destino en S3

Antes de crear el job, se prepara en el bucket una carpeta destino que actuará como zona del Data Lake,
por ejemplo `clientes` (carpeta nueva, distinta de la carpeta origen usada por Athena/el crawler).

## Crear el ETL Job con Visual ETL

En la consola de **Glue → ETL Jobs → Visual ETL** se crea un nuevo trabajo:

- Se le puede dar un nombre descriptivo al job (ej. `mi-primer-trabajo-etl`) y también nombres
  descriptivos a cada nodo (fuente, transformación, destino) para que el flujo sea fácil de entender.
- Existen otras formas de desarrollar jobs (por ejemplo, **Notebooks**, para desarrollo interactivo),
  pero en esta práctica se usa el editor **Visual ETL**, la opción más sencilla.
- El editor permite añadir tres tipos de nodos: **fuentes** (sources), **transformaciones** y
  **destinos** (targets).

### 1. Configurar la fuente (Source)

- Añadir una fuente de tipo **S3**.
- Indicar la **ruta** en S3 navegando con el explorador integrado (bucket → carpeta con el CSV).
- Activar **Infer schema** (inferir esquema): Glue detecta automáticamente el esquema del archivo, de
  forma muy similar a como lo hace un **Glue Crawler**.

> ⚠️ Al inferir el esquema desde el propio job, también se crea una tabla con sus metadatos en el
> **Glue Data Catalog**, sin necesidad de ejecutar explícitamente un Crawler aparte.

### 2. Transformaciones (opcional)

El editor visual ofrece varios tipos de transformación: consultas **SQL**, evaluación de calidad de
datos, detección de datos sensibles, agregaciones, etc. En esta práctica, centrada solo en la
**ingestión** de datos, no se usa ninguna.

### 3. Configurar el destino (Target)

- Añadir un nodo de tipo **S3** como destino y conectarlo a la salida de la fuente (o de la
  transformación, si la hubiera).
- **Formato de salida**: por defecto Glue usa **Parquet**.
  - Parquet es un formato **columnar**, mucho más eficiente para lecturas analíticas que un CSV.
  - Otros formatos habituales para este mismo propósito: **Avro** y el propio **Parquet** (se
    profundizará más adelante en los distintos formatos de datos).
- **Ruta destino**: navegar hasta el bucket/carpeta destino preparada previamente (ej. `clientes`).
- **Data Catalog update options** — qué hacer con el catálogo en cada ejecución del job:
  - **No actualizar el catálogo** (opción por defecto).
  - **Crear una tabla** en el Data Catalog y, en ejecuciones siguientes, actualizar el esquema y
    añadir nuevas particiones.
  - **Crear una tabla** manteniendo el esquema existente, pero añadiendo solo las nuevas particiones.
- En esta práctica se elige **crear la tabla** y **actualizar esquema + añadir particiones**, indicando
  la **database** (ej. `clientes`) y un **nombre de tabla** (ej. `clientes_destino`).

> Sobre particiones: cuando los datos destino se organizan en subcarpetas adicionales (por ejemplo, una
> carpeta por día), cada una de esas carpetas se registra como una **partición**. Esto hace las lecturas
> más eficientes: al filtrar por un día concreto, el motor de consulta solo necesita mirar en la
> partición correspondiente en lugar de escanear todos los datos.

## Guardar y elegir el rol IAM

- Antes de poder ejecutar el job hay que **guardarlo** (Save).
- En **Job details** hay que seleccionar un **IAM Role** con permiso para leer y escribir datos. Se
  puede reutilizar el rol creado previamente para el Crawler.
- Otras opciones relevantes en Job details:
  - **Glue version**: se deja por defecto (Spark).
  - **Worker type**: se deja el valor por defecto.
  - **Number of workers (DPUs)**: por defecto son 10; para prácticas conviene reducirlo al **mínimo
    permitido (2 DPUs)** para no incrementar el coste innecesariamente.
  - **Job bookmarks**: ayudan a la **carga incremental** (se detalla en una clase posterior).

## Primera ejecución: error de permisos

Al ejecutar el job por primera vez, este falla con un error de tipo **S3 Access Denied**: el rol IAM
seleccionado no tiene permiso suficiente para leer/escribir en el bucket.

### Solución: añadir permisos al rol en IAM

1. Ir a **IAM → Roles** y buscar el rol usado por el job (el rol de servicio de Glue).
2. **Add permissions → Attach policies**.
3. Buscar y adjuntar una política de S3 (para simplificar, en un entorno de práctica se puede usar
   acceso completo a S3).

> ⚠️ En un entorno productivo conviene usar políticas más granulares (acceso restringido a
> buckets/prefijos concretos) en lugar de acceso completo a S3.

## Segunda ejecución: éxito

Tras actualizar los permisos del rol, se vuelve a ejecutar el job con la misma configuración. Tras
aproximadamente 2 minutos, la ejecución finaliza correctamente.

### Verificación del resultado

- En el bucket S3, dentro de la carpeta destino (`clientes`), aparece el archivo generado en formato
  **Parquet**.
- En el **Glue Data Catalog**, dentro de la database `clientes`, aparece la nueva tabla
  (`clientes_destino`) con los nombres de columna correctamente detectados.

## Próximos pasos

En la siguiente clase se verá cómo **programar (schedule)** la ejecución de estos ETL Jobs y también de
los Crawlers.
