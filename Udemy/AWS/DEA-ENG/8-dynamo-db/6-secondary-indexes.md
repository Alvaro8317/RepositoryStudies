# Índices secundarios en DynamoDB (LSI y GSI)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

Los **índices secundarios** permiten acceder a los datos usando una **clave alternativa**, distinta de
la [[4-primary-keys|clave primaria]] de la tabla — útiles cuando el patrón de acceso de la aplicación
no coincide con la clave primaria y se quiere evitar un escaneo completo de la tabla.

Hay dos tipos: **Local Secondary Index (LSI)** y **Global Secondary Index (GSI)**.

## LSI vs. GSI

|                        | **Local Secondary Index (LSI)**                         | **Global Secondary Index (GSI)**                                                                      |
| ---------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Clave de partición     | Debe ser **la misma** que la de la tabla base           | Puede ser **distinta** de la de la tabla base                                                         |
| Clave de ordenación    | Puede ser distinta (ese es su propósito)                | Puede ser distinta                                                                                    |
| Cuándo se crea         | Solo **al crear la tabla** — no se puede añadir después | Se puede **crear o modificar posteriormente**                                                         |
| Flexibilidad           | Menor                                                   | Mayor                                                                                                 |
| Límite por tabla       | Máximo **5** LSI por tabla                              | Sin ese límite fijo de 5                                                                              |
| Capacidad de escritura | Comparte la capacidad de la tabla base                  | Tiene su **propia capacidad**, pero cada escritura en la tabla base debe reflejarse también en el GSI |

> ⚠️ Con un GSI hay que tener en cuenta la relación entre su capacidad de escritura y la de la tabla
> base: cada operación de escritura (insert/update) en la tabla base debe propagarse también a todos
> los GSI asociados — la escritura no es solo contra la tabla base.

## Cuándo usar cada uno

- **LSI** — cuando se necesita mantener la **misma clave de partición** de la tabla base, pero con
  capacidades de ordenación/consulta adicionales **dentro de esa misma partición**. Útil cuando la
  **consistencia** es muy importante.
- **GSI** — cuando se necesita un patrón de acceso **más flexible**, con consultas eficientes basadas
  en atributos distintos a la clave primaria, y la posibilidad de **añadir o modificar** el índice
  después de haber creado la tabla.

## Ejemplo: tabla de productos (e-commerce)

Tabla base `productos`, con `id_producto` como clave de partición (única).

La aplicación necesita también:

- Listar todos los productos de una **categoría** concreta.
- Encontrar todos los productos de un **fabricante** concreto.

Solución: crear dos **GSI**:

1. **Índice de categoría** — clave de partición = `categoria`, clave de ordenación = `id_producto`
   (el atributo que era la clave de partición en la tabla base).
2. **Índice de fabricante** — clave de partición = `fabricante`, clave de ordenación = `id_producto`.

> Un GSI suele construirse como **clave compuesta**: el nuevo atributo de consulta (categoría,
> fabricante) actúa como clave de partición del índice, y la clave de partición original de la tabla
> base pasa a actuar como clave de ordenación dentro del índice — así se garantiza unicidad.

Con estos GSI, se pueden consultar los productos por categoría o por fabricante de forma eficiente, sin
necesidad de escanear toda la tabla — lo que se traduce en una recuperación de datos más rápida para el
usuario.

## Construcción del índice

Un índice secundario se construye normalmente usando **atributos proyectados** (los atributos de la
tabla base que se "copian" al índice). Se profundiza en la siguiente lección.
