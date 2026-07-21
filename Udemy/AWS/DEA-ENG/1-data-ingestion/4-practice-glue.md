# Práctica: Configuración de un Glue Crawler

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

Continuando con lo visto sobre **AWS Glue** y el **Glue Data Catalog**, en esta práctica se configura paso a paso un **Glue Crawler** para detectar los metadatos de un archivo almacenado en un bucket de S3, generar una tabla en el Data Catalog y dejarla lista para ser consultada (con Athena, en la siguiente clase).

## Navegación en la consola de Glue

En el panel izquierdo de **AWS Glue** encontramos:

- **ETL Jobs**
- **Data Catalog:**
  - **Databases**
  - **Tables**
  - **Crawlers**

### Conceptos clave

- Una **table** (tabla) es el resultado de combinar los **metadatos** que detecta un crawler: nombres de columnas, tipos de datos, formato del archivo (ej. CSV).
- Una **database** (base de datos) es simplemente un **contenedor** donde viven las tablas.
- ⚠️ Aunque en la interfaz se ve como una base de datos y tablas al estilo SQL, en realidad **solo son metadatos**: los datos siguen físicamente en el bucket S3, **no se duplican ni copian**.

> Importante: si se selecciona como fuente de datos un bucket completo o una carpeta con subcarpetas, **todos los archivos deben tener el mismo esquema/formato**; de lo contrario no se podrá crear una tabla consistente.

## Pasos para crear un Crawler

### 1. Crear el crawler

- Ir a **Crawlers → New crawler**.
- Asignar un **nombre** (ej. `mi-primer-crawler`) y, opcionalmente, una **descripción**.

### 2. Configurar la fuente de datos (Data Source)

- Como no existe una tabla previa, se indica que **se creará automáticamente** en la primera ejecución del crawler (no es necesario mapear a una tabla existente).
- **Add data source → S3**.
- Navegar hasta el **bucket** correspondiente (se puede usar la barra de búsqueda si hay muchos buckets).
- Seleccionar la **carpeta** o el **bucket completo** a rastrear (ej. carpeta `documentos`).
- Definir si en próximas ejecuciones se deben rastrear **todas las subcarpetas de nuevo** o **solo las subcarpetas nuevas** (por defecto: rastrear todas).

### 3. Permisos (IAM Role)

- Seleccionar un **rol IAM existente** con los permisos necesarios, o **crear uno nuevo** con los permisos por defecto que requiere el crawler para ejecutar su tarea.

### 4. Output — Base de datos y tabla

- Si no existe una **database**, se puede crear directamente desde este paso (ej. llamarla `clientes`).
- El **nombre de la tabla** se genera automáticamente a partir del **nombre de la carpeta** rastreada (ej. `documentos`).
- Se puede añadir opcionalmente un **prefijo** al nombre de la tabla (ej. `tabla_`).

### 5. Programación (Schedule)

- Se puede configurar el crawler para ejecutarse:
  - **On demand** (bajo demanda / manual) — mayor control sobre cuándo se ejecuta.
  - Por **hora, día, semana o mes**.
- En este ejemplo se deja configurado como **on demand**.

### 6. Revisión y creación

- Revisar el resumen de toda la configuración.
- **Create crawler.**

## Ejecución del crawler

- Una vez creado, se ejecuta manualmente con **Run**.
- Tras aproximadamente **1-2 minutos**, el crawler finaliza (estado: *completed*).

## Resultado

Al navegar a la base de datos creada (ej. `clientes`) aparece la nueva **tabla** generada por el crawler, mostrando:

- La **ubicación real de los datos** (siguen en el bucket S3, sin copia).
- La **clasificación del formato** detectada automáticamente (ej. CSV).
- Los **nombres de columna** y **tipos de datos** inferidos correctamente al inspeccionar la tabla.
