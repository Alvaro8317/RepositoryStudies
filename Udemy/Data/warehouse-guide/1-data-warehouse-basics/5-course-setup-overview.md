# Resumen del setup del curso

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Antes de entrar en detalle, un resumen rápido de las herramientas y el entorno que se usarán a lo
largo del curso (se profundiza en cada pieza más adelante).

## Fuentes de datos

En el mundo real hay muchos tipos de fuentes de datos: archivos CSV, archivos Excel, bases de datos,
archivos de texto comunes, otras aplicaciones/sistemas fuente, etc. En el curso, por ejemplo, se
usarán archivos CSV alojados en un bucket de **S3** en AWS.

## Herramienta de integración de datos

Se necesita una herramienta que mueva los datos desde las fuentes hasta el Data Warehouse, y que
también permita transformarlos (por eso se le llama **integración de datos**).

El curso usará **Airbyte** porque:

- Es fácil de usar y configurar.
- Tiene una versión gratuita (trial) disponible.
- Es una solución moderna.

> ⚠️ El curso no busca enseñar una herramienta específica, sino los **principios** detrás de la
> integración de datos, para poder aplicarlos con cualquier herramienta. Existen muchas alternativas
> a Airbyte.

## Dónde alojar el Data Warehouse

El Data Warehouse necesita estar alojado en algún tipo de base de datos. Opciones:

- **RDS en AWS** (lo que se usará en el curso) — muy común alojarlo en la nube.
- Auto-alojado en un servidor propio.
- Soluciones más especializadas de muy alto rendimiento, como **Snowflake** o **Redshift** (AWS),
  entre otras plataformas — solo mencionadas como ejemplos, no se profundiza aún.
