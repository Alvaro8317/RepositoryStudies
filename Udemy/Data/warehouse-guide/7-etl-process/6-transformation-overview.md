# Visión general de la transformación (Transform)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Después de ver el proceso de carga, toca ver la parte de transformación del `ETL`. Siempre se quieren
transformar los datos para darles coherencia y sacarles más partido: desde la `Staging Area` se
definen ciertas transformaciones, y luego esos datos transformados se cargan en la capa `Core`
normalmente mediante la operación de `Insert/Update` vista en la clase anterior.

Antes de entrar en los tipos concretos de transformaciones, conviene tener claro cuál es realmente el
**objetivo** de transformar los datos: crear una vista consolidada de todos los datos, optimizada para
propósitos de análisis.

## Los dos objetivos principales

### 1. Crear una vista consolidada

Significa integrar datos de múltiples sistemas, lo cual puede incluir:

- Conversiones de tipos de datos.
- Normalización de nombres de columnas.
- Distintos tipos de normas/estándares que se quieren establecer para que los datos sean compatibles
  entre sí.

Por ejemplo, distintos sistemas fuente pueden representar el mismo tipo de dato de forma distinta:

| Sistema | Columna cantidad | Tipo de dato | Formato de fecha |
|---|---|---|---|
| Sistema A | cantidad en miles | decimal | `DD/MM/YYYY` |
| Sistema B | cantidad en unidades | entero | `YYYY-MM-DD` |

Todo esto se debe consolidar para que los datos sean compatibles entre sí y se puedan cargar en una
única tabla del `Data Warehouse`.

### 2. Remodelar los datos según las necesidades del negocio

Además de consolidar, también se busca remodelar (`reshape`) los datos para adaptarlos a las
necesidades analíticas o de generación de informes — esto puede incluir añadir información adicional o
reestructurar los datos para poder analizarlos.

Ejemplos de remodelación:

- **Remodelación simple**: reestructurar una tabla para poder usarla de forma dimensional — por
  ejemplo, incluir `Foreign Keys` que antes no estaban presentes.
- **Remodelación más drástica**: por ejemplo, datos que llegan en un formato tipo tabla dinámica de
  Excel (una fila por categoría, una columna por periodo) no son cómodos de analizar, porque
  normalmente se quieren los datos almacenados en filas y columnas de forma normalizada. En estos
  casos se puede hacer un `pivot` de los datos para llevarlos a esa forma. No es algo tan común, pero
  es un buen ejemplo de una remodelación con más impacto.
- **Filtrado de columnas**: también es habitual descartar columnas que no interesan en la tabla final
  (por ejemplo, una columna de `total` calculada que no se quiere conservar).

> ⚠️ Todo esto son operaciones de limpieza y remodelación para que los datos se ajusten a los
> requisitos de negocio y de presentación de informes — no son solo conversiones técnicas de formato.

## Próximas clases

Existe una lista amplia de tipos de transformaciones distintas. En las próximas dos clases se verán
primero los tipos de transformación más básicos, y después los más avanzados.
