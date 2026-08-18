# Conectar el Data Warehouse a Power BI

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Una vez creado el `Data Warehouse`, se puede usar de varias formas: consultarlo directamente con
`SQL` (agrupaciones, filtros, etc.), o conectarlo a una herramienta específica de reporting/BI. Esta
clase es una demo práctica conectando el `Data Warehouse` a **`Power BI`**, uno de los casos de uso
más importantes — el flujo es equivalente en la mayoría de herramientas de `BI`/visualización de
datos.

> ⚠️ No es un curso de `Power BI` en profundidad — el objetivo es mostrar cómo el `Data Warehouse`
> se integra con este tipo de herramientas y por qué resulta tan útil.

## Obtener las credenciales de conexión

Un `Data Warehouse` no deja de ser una base de datos, así que para conectarlo desde `Power BI` (o
cualquier otra herramienta) hacen falta las credenciales de conexión habituales: host, puerto, nombre
de la base de datos, usuario y contraseña. Estos datos se pueden consultar en el sistema de gestión de
base de datos (ej. propiedades de conexión del servidor en `pgAdmin`).

> ⚠️ Para conectar herramientas externas conviene usar un usuario con acceso de solo lectura a la base
> de datos, en vez de las credenciales de administración.

## Conectarse desde Power BI

En `Power BI`, para conectar una fuente de datos: `Obtener datos` → `Base de datos` → seleccionar el
motor correspondiente (en este caso `PostgreSQL`). Se introduce el servidor (ej. `localhost` si el
`Data Warehouse` está alojado localmente) y el nombre de la base de datos.

### Import vs. DirectQuery

Al conectar, `Power BI` pregunta si se quiere **importar** los datos o **consultarlos directamente**:

- **`Import`**: los datos se cargan e importan al archivo de `Power BI`, y se procesan en memoria
  dentro de la propia herramienta.
- **`DirectQuery`** (consulta directa): `Power BI` consulta la base de datos en cada operación, sin
  importar los datos. Tiene sentido cuando la base de datos/`Data Warehouse` de origen ya tiene un
  rendimiento muy alto, ya que se aprovecha directamente esa potencia.

Tras introducir las credenciales (usuario/contraseña), se muestran todas las tablas disponibles para
seleccionar cuáles cargar.

> ⚠️ No hace falta cargar todo el `Data Warehouse`: normalmente solo interesan las tablas de la capa
> `Core` necesarias para el caso de uso (dimensiones + tabla de hechos relevantes, incluida la
> dimensión de fecha). Esto funciona, en la práctica, de forma parecida a un `Data Mart` — solo se
> traen las tablas específicas que hacen falta.

## Vista de modelo: recrear el Star Schema

En la vista de modelo de `Power BI` se pueden crear las relaciones entre tablas arrastrando la clave
primaria (`Surrogate Key`) de cada dimensión sobre la clave foránea correspondiente en la tabla de
hechos (por ejemplo, la clave foránea de fecha de transacción sobre la clave de la dimensión de
fecha). Con esas relaciones creadas, se reconstruye visualmente el `Star Schema`: la tabla de hechos
en el centro y las dimensiones alrededor.

Estas relaciones son clave para el usuario final: una vez configuradas, los usuarios pueden combinar
tablas de hechos y dimensiones sin tener que preocuparse de hacer los `JOIN`s manualmente.

## Crear visualizaciones

Con el modelo ya relacionado, se pueden crear visualizaciones fácilmente arrastrando y soltando
campos:

- **Gráfico de líneas**: arrastrar la fecha (de la dimensión de fecha) y una medida de la tabla de
  hechos (ej. beneficio) para ver la evolución en el tiempo, con posibilidad de hacer `drill-down` por
  los distintos niveles de la jerarquía de fecha.
- **Gráfico de barras**: arrastrar una medida (ej. beneficio) junto con un atributo de dimensión (ej.
  categoría de producto) para comparar el beneficio por categoría.
- **Interactividad**: al hacer clic sobre un valor en un gráfico (ej. una categoría de producto), los
  demás visuales del reporte se filtran automáticamente en consecuencia.

Con esto se demuestra, de forma práctica, cómo el `Data Warehouse` habilita reporting y análisis con
alto rendimiento y alta usabilidad al conectarlo con herramientas de `BI` como `Power BI`.
