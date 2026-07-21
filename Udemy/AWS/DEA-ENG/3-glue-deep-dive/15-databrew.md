# AWS Glue DataBrew

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es DataBrew?

**AWS Glue DataBrew** es una herramienta de **preparación de datos** con una interfaz **visual**, muy
similar a **Power Query** en Excel o Power BI para quien ya esté familiarizado con esa herramienta.

- Permite ver una **vista previa** de los datos y aplicar **pasos de transformación** sobre ellos.
- Se usa principalmente para **limpiar y reestructurar** datos: este preprocesamiento puede formar
  parte de la fase de transformación de un ETL, y también es muy común para preparar datos de cara al
  **Machine Learning**.
- Forma parte de la suite más amplia de **AWS Glue**, orientada a la **integración de datos**.
- Incluye más de **250 transformaciones preconstruidas** para modificar y transformar datos de forma
  sencilla.
- Es una herramienta **sin código (no-code)**: no hace falta ser experto en programación para usarla.
- Permite **automatizar tareas repetitivas** programando los trabajos (jobs), ahorrando tiempo y
  asegurando que los datos queden preparados, coherentes y con su calidad verificada.

## Integración con otros servicios de AWS

Una vez preparados los datos, DataBrew se integra fácilmente con otros servicios:

- **Amazon S3**: almacenar los datos limpios en un bucket de destino.
- **Amazon Redshift**: mover los datos para análisis más detallado.
- **AWS Lake Formation**: seguridad y gobernanza de los datos.
- **AWS IAM**: gestión de permisos.

## Interfaz: vista previa y perfiles de datos

En la interfaz de un proyecto de DataBrew se puede ver:

- Una **vista previa** de los datos.
- **Perfiles de columna** (column profiles): estadísticas como número de valores distintos,
  distribución de los datos, media, moda, etc. — dan una visión general de los datos y ayudan a
  identificar visualmente inconsistencias o problemas.

## Conceptos clave

### Project (Proyecto)

Es donde se configuran las tareas de transformación: se parte de un **dataset**, se le van añadiendo
**steps** (pasos de transformación) y se puede ver una vista previa del dataset en cada momento. Todos
los steps aplicados se combinan en una **recipe**.

Ejemplos de steps: dividir una columna (por ejemplo, separar ciudad y código postal en dos columnas
usando un carácter específico), redondear un valor numérico, poner un texto en mayúsculas, unir
(join) o agrupar (group by) datos, eliminar duplicados, ordenar por una columna, etc.

### Recipe (Receta)

Es la **combinación de los pasos de transformación** aplicados a un dataset. Las recipes se pueden
**guardar y reutilizar** en otros proyectos con otros datasets — son reutilizables.

### Job (Trabajo)

Es la **ejecución de una recipe sobre un dataset**. Al configurar un job se especifica una
**ubicación de salida** (por ejemplo, un bucket S3) donde almacenar el resultado. Los jobs se pueden
**programar** (schedule) para ejecutarse a intervalos regulares, automatizando así las tareas de
preparación de datos.

### Data profiling

Se puede ejecutar sobre **todo el dataset** (perfil completo) o consultar la vista previa de
estadísticas de una **columna específica**: dependiendo del tipo de dato, se muestran distintos tipos
de estadísticas y visualizaciones (distribución de valores, cantidad de valores nulos, valores únicos o
distintos, etc.), útiles para entender los datos e identificar posibles problemas.

## Próximos pasos

En la siguiente clase se profundiza en transformaciones de datos específicas para remodelar (reshape)
los datos, importantes de cara a la visualización de datos o a modelos de Machine Learning.
