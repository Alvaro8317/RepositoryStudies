# Fundamentos de la extracción de datos

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Por qué extraer a la Staging Area

Ya se ha visto que hay que extraer los datos de las fuentes de datos hacia la `Staging Area`. Una vez
hecho esto, esos datos ya forman parte del `Data Warehouse`, en la capa de `Staging`.

Se hace así para **no sobrecargar innecesariamente los sistemas fuente**: son sistemas productivos, y
no se puede correr el riesgo de ralentizarlos por estar trabajando directamente sobre ellos mientras
se comprenden los datos y se planifican los pasos de transformación. Por eso se necesita tener los
datos en un entorno propio de `staging`, que además es el lugar donde todos los datos quedan
finalmente disponibles en tablas SQL.

Desde la `Staging Area` ya se pueden planificar y ejecutar las transformaciones, y cargar el
resultado en la siguiente capa (`Core`).

## Staging transitorio vs. permanente

> ⚠️ El tipo más común de `Staging Area` es el **tipo transitorio (`transient`)**.

En este tipo, una vez que los datos se copian de `Staging` a `Core` (aplicando las transformaciones
correspondientes), se **eliminan o truncan** de la `Staging Area`. A partir de ahí, la `Staging Area`
queda vacía hasta la siguiente ejecución, cuando se carguen nuevos datos — y solo esos datos nuevos se
copiarán después a la capa `Core`.

También existe el tipo **permanente**, en el que los datos no se eliminan de `Staging` tras la carga,
pero el curso se centra en el tipo transitorio por ser el más común.

## Carga inicial vs. carga delta

Hay dos tipos de carga de datos hacia el `Data Warehouse`:

| Tipo de carga         | Descripción                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| **Carga Inicial** (`Initial Load`) | La primera ejecución real del `ETL`: se cargan todos los datos relevantes por primera vez (más allá de pruebas previas con extracciones pequeñas). |
| **Carga Delta** (`Delta Load`)     | Las cargas posteriores a la inicial: ya no se cargan todos los datos, sino solo los datos adicionales/nuevos que se han producido en el sistema de origen desde la última carga. |

## Próximas clases

Profundizar en cómo funcionan exactamente la `Initial Load` y la `Delta Load`.
