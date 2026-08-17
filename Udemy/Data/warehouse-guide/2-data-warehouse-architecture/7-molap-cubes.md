# Cubos MOLAP

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Qué es un cubo?

Un cubo es un método alternativo, ya bastante establecido y maduro, para aumentar aún más el
rendimiento de consulta de los `Data Marts`.

A diferencia de un `Data Warehouse` tradicional, donde los datos se almacenan en una base de datos
**relacional** (tablas con relaciones entre sí), en un cubo los datos se organizan de forma **no
relacional**, en múltiples **dimensiones**. Por eso también se les llama **`MOLAP`**
(`Multidimensional OLAP`): la expresión más precisa para un cubo es un **conjunto de datos
multidimensional**.

- Los datos no se organizan en tablas de columnas y filas, sino en **arrays** (matrices
  multidimensionales).
- Se usan **exclusivamente en `Data Marts`**, con fines analíticos, siempre que se necesite un
  rendimiento de consulta muy rápido.
- Una vez creado el cubo (con alguna tecnología/software específico), puede consumirse desde
  distintas herramientas de BI — por ejemplo, `Excel` tiene soporte nativo para consultar cubos.

## Cómo se estructuran los datos

Ejemplo: analizar datos de ventas en tres dimensiones — `productos`, `tiempo` y `clientes` —,
midiendo el importe de ventas.

- Aunque para dibujarlo se suelen usar tres dimensiones, en la práctica **un cubo puede tener más de
  tres dimensiones**.
- Los datos se pueden "rebanar y cortar" (`slice and dice`): por ejemplo, la intersección de un
  cliente específico en un mes específico da directamente el importe de ventas de ese cliente en ese
  período.

> ⚠️ El beneficio clave de un cubo es que los valores de esas celdas están **pre-calculados y
> pre-agregados** de la forma en que se van a consumir después (reportes, aplicaciones). Cuando se
> consulta el cubo, el dato ya está listo — no hay que calcularlo en el momento.

## Lenguaje de consulta: MDX

Los cubos no se consultan con `SQL`, sino con **`MDX`** (`Multidimensional Expressions`), un
lenguaje desarrollado por `Microsoft` que es hoy el más utilizado para consultar datos de cubos.

## Cuándo aportan más valor

El mayor beneficio de un cubo se obtiene en **herramientas interactivas** donde las **jerarquías**
son importantes y se necesita hacer `drill-down`/`slice and dice` sobre los datos — típicamente
herramientas de visualización (ej. `Excel`).

Recomendaciones prácticas:

- Un cubo debe construirse para un **caso de uso específico**, cargando solo las tablas relevantes
  para ese caso — de ahí que se usen dentro de `Data Marts` y no directamente sobre todo el `Data
  Warehouse`.
- A **menos dimensiones**, mayor es el beneficio (más simplicidad, mejor rendimiento). Cuantas más
  tablas y dimensiones se agreguen, más complejo se vuelve el cubo, y tanto la facilidad de uso como
  el rendimiento se degradan.
- Por eso conviene tener un `Data Mart` independiente (y su propio cubo) por cada caso de uso
  específico, en vez de un único cubo gigante para todo.

## ¿Son siempre necesarios?

No. Un cubo es **opcional** — si el rendimiento de consulta de una base de datos relacional ya es
suficiente, se puede seguir usando directamente esa base de datos, organizando los datos con un
`Star Schema` (se verá en detalle más adelante). Opcionalmente, esos mismos datos relacionales
pueden después cargarse en un cubo si se necesita un salto adicional de rendimiento.

> ⚠️ Con el avance del hardware y de tecnologías como las bases de datos in-memory, el
> almacenamiento columnar y el procesamiento paralelo, los cubos MOLAP se están volviendo **menos
> imprescindibles** que antes — siguen siendo relevantes, pero hoy existen alternativas (como
> modelos tabulares, también comunes en el stack de `Microsoft`) que logran buen rendimiento sin la
> complejidad técnica adicional de un cubo. Si el rendimiento de la base de datos relacional ya es
> bueno (algo cada vez más común), no siempre hace falta dar el salto a un cubo.
