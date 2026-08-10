# Práctica: Claves primarias en DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada demostrando en la consola los conceptos vistos en [[4-primary-keys]]: unicidad de la
clave de partición, y cómo una clave compuesta (partition key + sort key) permite compartir la misma
partition key entre varios items.

## Unicidad de la clave de partición simple

Sobre la tabla `libros` (con `id_libro` como clave de partición simple, ver
[[2-practice-create-table]]):

- Intentar crear un nuevo item reutilizando un `id_libro` **ya existente** falla con el error:

  > *"The conditional request failed" — ya existe un elemento con la clave primaria proporcionada.*

- Usar un `id_libro` **nuevo** (no usado antes) permite crear el item sin problemas.

> ⚠️ Esto confirma en la práctica que, sin clave de ordenación, la clave de partición debe ser única
> para toda la tabla — no se puede tener dos items con el mismo valor.

## La clave primaria no se puede cambiar después de crear la tabla

- En la vista de una tabla ya creada se pueden modificar varios ajustes (capacidad, clase de tabla,
  etc.), pero **no** la clave primaria.
- Para usar una clave primaria distinta (ej. añadir una clave de ordenación) hace falta **crear una
  tabla nueva** — no es una operación de edición sobre la tabla existente.

## Crear una tabla con clave compuesta

Se crea una segunda tabla (`libros2`) con:

- **Clave de partición**: `id_libro`.
- **Clave de ordenación (sort key)**: `id_autor`, tipo **String**.

> Igual que con la clave de partición, el tipo de dato de la clave de ordenación se restringe a
> **string, number o binary** — a diferencia de los atributos normales del item, que admiten más tipos
> de datos.

El resto de la configuración se deja igual que en la primera tabla: clase de tabla **Standard**, modo
**Provisioned** sin auto scaling (5 unidades de lectura / 5 de escritura), cifrado por defecto.

## Crear items con clave compuesta

- Al crear un item en una tabla con clave compuesta, **ambos** valores (partition key y sort key) son
  obligatorios — si se deja la sort key vacía, la creación del item falla porque forma parte de la
  clave primaria.
- Es posible crear **dos items con la misma partition key** (ej. `id_libro = B1`), siempre que
  difieran en la **sort key** (ej. `id_autor = autor1` vs. otro valor distinto):
  - Intentar crear un segundo item con la **misma combinación exacta** de partition key + sort key
    falla igual que en el caso de clave simple — la combinación debe seguir siendo única.
  - Con una sort key **distinta**, el item se crea sin problema, aunque comparta partition key con
    otro item ya existente.

> La clave de partición sigue siendo la responsable de **distribuir los datos entre particiones**,
> pero ya no tiene que ser única por sí sola — la unicidad la garantiza la **combinación** de
> partition key + sort key.

## Siguiente paso

Cuando el patrón de acceso necesario no coincide con la clave primaria (ej. consultar frecuentemente
por categoría en vez de por `id_libro`), hace falta recurrir a **índices secundarios** — se tratan en
la siguiente lección.
