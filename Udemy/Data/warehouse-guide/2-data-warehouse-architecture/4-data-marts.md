# Data Marts

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## ¿Qué es un Data Mart?

Ya conocemos la `Staging Area` y la `Core Layer` — esta última suele servir como capa de acceso del
`Data Warehouse`. Pero en empresas grandes, donde el `Data Warehouse` se construye para muchos casos
de uso distintos (diferentes herramientas, departamentos, regiones, todos consultando el mismo
`Data Warehouse`), esto puede volverse complicado de manejar. Para resolverlo, a veces se añade una
capa adicional encima de la `Core Layer`: los **`Data Marts`**.

- Un `Data Mart` es, en esencia, un **subconjunto del `Data Warehouse`** (de la `Core Layer`).
- Sus datos se modelan de forma **dimensional**: tablas de hechos (`Fact Tables`) en el centro,
  rodeadas de tablas de dimensiones (`Dimension Tables`).
- Se construye para un **caso de uso específico** — eso es justamente lo que lo convierte en un
  `Data Mart`.
- A veces, además de seleccionar un subconjunto de datos, también se **agregan** los datos para que
  sirvan mejor al caso de uso puntual.

> ⚠️ El modelado dimensional (hechos y dimensiones) no es exclusivo de los `Data Marts`. Si la
> `Core Layer` funciona como capa de acceso directa (sin `Data Marts` encima), sus datos también
> pueden modelarse en hechos y dimensiones.

## Ventajas de usar Data Marts

| Ventaja                  | Descripción                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------|
| **Usabilidad**             | Es más fácil para los usuarios (a menudo no técnicos) enfocarse solo en los datos relevantes para su caso de uso, sin sentirse abrumados por todas las tablas del `Data Warehouse`. Esto es clave para la adopción del `Data Warehouse`/`Data Mart`. |
| **Rendimiento**             | Al modelar los datos dimensionalmente para un caso de uso específico, se puede usar tecnología especializada (ej. bases de datos in-memory, cubos OLAP) que ofrece consultas mucho más rápidas. |

Mejor rendimiento y mejor usabilidad se refuerzan mutuamente: ambos aumentan la aceptación del
`Data Warehouse`/`Data Mart` por parte de los usuarios.

## Casos de uso típicos

Un `Data Mart` suele construirse cuando exista una necesidad de separar por:

- **Herramientas distintas**: por ejemplo, un `Data Mart` en una base de datos in-memory para
  visualización con `Power BI` (donde el rendimiento de consulta importa mucho), y otro `Data Mart`
  distinto, con otro tipo de base de datos, para análisis predictivo con otra herramienta que no
  necesita ese tipo de almacenamiento.
- **Departamentos distintos**: ej. ventas, finanzas, marketing — cada uno con datos relevantes
  propios dentro de la `Core Layer`, pero no todos relevantes para todos los departamentos.
- **Regiones distintas**: `Data Marts` separados por región geográfica.

## Nota sobre la terminología

El concepto de `Data Mart` es un tema **ampliamente debatido** en la comunidad de data warehousing:
algunos lo describen como un "`Data Warehouse` a pequeña escala", mientras que otros consideran esa
definición incorrecta.

> ⚠️ La recomendación del instructor es no obsesionarse con la discusión terminológica ("¿qué es
> realmente un `Data Mart`?", "¿debería usar un `Data Mart` o solo mi `Data Warehouse`?"). Lo
> importante es enfocarse en el **problema de negocio** concreto: si un `Data Mart` resuelve ese
> problema (usabilidad, rendimiento, separación por caso de uso), vale la pena usarlo,
> independientemente de si encaja perfecto en una u otra definición formal.

Si el `Data Warehouse` (la `Core Layer`) está muy centralizado y sirve muchos casos de uso
distintos, un `Data Mart` suele ser útil. Si no, puede no ser necesario — depende del contexto de
cada proyecto.
