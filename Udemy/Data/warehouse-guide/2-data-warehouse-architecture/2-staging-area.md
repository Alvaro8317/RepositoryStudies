# Staging Area

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Por qué necesitamos la Staging Area?

En el proceso `ETL`, los datos están disponibles primero en los **sistemas de origen** (sistemas
operacionales que hacen funcionar el día a día de la empresa). El propósito de la `Staging Area` es
**extraer esos datos rápidamente** y dejarlos disponibles de forma segura, en tablas, dentro de
nuestro propio entorno.

- No queremos pasar mucho tiempo consultando los sistemas de origen: solo necesitamos **acceso de
  lectura**, extraer los datos rápido y sacarlos de ahí.
- Una vez los datos están en tablas en una base de datos relacional dentro de la `Staging Area`,
  podemos definir con calma todas las transformaciones necesarias con la herramienta `ETL` y
  cargarlas hacia la `Core Layer` — la capa de acceso para usuarios finales y aplicaciones, a menudo
  percibida como "el Data Warehouse" en sí.

> ⚠️ Los sistemas de origen suelen ser sistemas operacionales críticos para el negocio. Pasar mucho
> tiempo consultándolos directamente arriesga degradar su rendimiento — por eso la `Staging Area`
> prioriza una extracción rápida por encima de cualquier transformación.

### Motivo adicional: normalizar el formato de los datos

Las fuentes de origen pueden venir en formatos muy distintos: archivos `CSV`, `JSON`, bases de
datos, etc. El primer paso siempre es volcar todos esos datos en **tablas de una base de datos
relacional**, independientemente del formato de origen. Solo así se puede empezar a aplicar
transformaciones de manera consistente.

## Cómo funciona en la práctica

Ejemplo: una tabla de ventas en el sistema de origen.

1. **Extracción**: se lee rápidamente la tabla de ventas desde el sistema de origen y se extrae tal
   cual hacia la `Staging Area`.
2. **Transformación y carga**: desde la `Staging Area` se aplican las transformaciones definidas
   (en este ejemplo, un `merge` con tablas adicionales para incorporar columnas nuevas) y se carga
   el resultado en el `Data Warehouse`.

### Ciclos siguientes: truncar la Staging Area y cargar solo los datos nuevos

Después de cada ronda del proceso `ETL`, la `Staging Area` (en su variante temporal) se **trunca**
— queda vacía, porque es una capa puramente temporal. En la siguiente ejecución hay que identificar
qué datos son nuevos en el sistema de origen, para lo cual se necesita una **lógica delta**: una
columna delta que indique qué filas son nuevas desde la última carga.

Opciones comunes de columna delta:

| Columna delta       | Cómo funciona                                                             | Riesgo                                                                 |
|----------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Columna `ID`          | Se recuerda el último ID cargado (ej. `5`) y se cargan solo los mayores.  | Requiere que el ID sea **estrictamente ascendente**, si no se cargan datos incorrectos. |
| Columna de fecha      | Se cargan solo las filas posteriores a la última fecha cargada (ej. después del 2 de enero). | Es la opción más usada en la práctica, más confiable que un ID.       |

Una vez identificadas las filas nuevas, se les aplica la misma lógica de transformación ya definida
y se anexan (`append`) al `Data Warehouse`.

> ⚠️ Si se usa una columna `ID` como columna delta, hay que verificar que realmente sea
> estrictamente ascendente en el sistema de origen. Por eso, en la práctica, una **columna de
> fecha** suele ser la opción más segura como columna delta.

## Staging Area temporal vs. persistente

| Tipo                        | Comportamiento                                                                                   | Cuándo usarla |
|------------------------------|----------------------------------------------------------------------------------------------------|----------------|
| **Temporal** (la más común) | Se trunca después de cada ronda del `ETL`. Solo contiene los datos de la última extracción.       | Caso general: es más simple y no acumula datos innecesarios. |
| **Persistente**              | Nunca se trunca — siempre conserva los datos de origen ya extraídos en esta capa.                 | Cuando se necesita poder retroceder en el tiempo fácilmente sin volver a consultar los sistemas de origen (por ejemplo, si una transformación falla o los datos cambian y hay que reprocesar días anteriores). |

> ⚠️ Una desventaja de la capa temporal es que si las transformaciones fallan o los datos de origen
> cambian, a veces hay que reprocesar datos de días anteriores. Volver a los sistemas de origen para
> esto no es ideal (por el mismo motivo por el que evitamos pasar mucho tiempo ahí). Una `Staging
> Area` persistente resuelve esto, pero según la experiencia del instructor, es **mucho menos común**
> que la variante temporal.

## Resumen

- La `Staging Area` es la **zona de aterrizaje** de los datos extraídos de las fuentes, dentro del
  `Data Warehouse`.
- Su propósito es extraer los datos rápidamente hacia una base de datos relacional independiente,
  tocando lo menos posible los sistemas de origen.
- Desde ahí se definen y aplican las transformaciones hacia la `Core Layer`.
- Existen dos variantes: **temporal** (se trunca en cada ronda del `ETL`, la más habitual) y
  **persistente** (nunca se trunca, permite retroceder en el tiempo, pero es más rara en la
  práctica).
