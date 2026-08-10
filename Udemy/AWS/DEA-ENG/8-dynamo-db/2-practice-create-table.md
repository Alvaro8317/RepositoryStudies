# Práctica: Crear una tabla en DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Primera vista rápida de la consola de DynamoDB, creando una tabla de ejemplo. Es solo un vistazo
general — cada concepto mencionado aquí (clave de partición, clave de ordenación, modos de capacidad,
índices secundarios) se profundiza en lecciones posteriores.

## Tablas, no bases de datos

- En DynamoDB **no se crean bases de datos** — se crean directamente **tablas**.
- Al ser una base de datos sin esquema (schema-less), para crear una tabla solo hace falta indicar:
  - Un **nombre de tabla** (ej. `libros`).
  - Una **clave primaria** (ej. `id_libro`).

## Items en vez de filas

- En DynamoDB no se habla de "filas" sino de **items** — es el equivalente conceptual a una fila de
  una base de datos relacional.

## Clave de partición (partition key)

- Identifica de forma única cada item de la tabla (salvo que exista también clave de ordenación).
- Al ser DynamoDB una **base de datos distribuida**, la clave de partición es la que determina cómo se
  **reparten los datos entre los distintos hosts**.
- Si se añade también una **clave de ordenación (sort key)** como segunda parte de la clave primaria,
  entonces sí pueden existir varios items con la misma clave de partición, siempre que difieran en la
  clave de ordenación.

## Configuración de la tabla

### Clase de tabla (table class)

- **Standard** (por defecto) — clase de propósito general, la más usada habitualmente. Incluida en la
  capa gratuita.
- **Standard-Infrequent Access** — optimizada para datos a los que se accede con poca frecuencia,
  permite ahorrar costes en esos casos de uso.

### Modo de capacidad (capacity mode)

- **Provisioned** — hay que especificar manualmente cuántas unidades de capacidad de lectura y
  escritura se necesitan (ej. 5 unidades de lectura y 5 de escritura). Incluido en la capa gratuita.
  Opcionalmente se puede activar **auto scaling**, definiendo un mínimo, un máximo y un objetivo de
  utilización.
- **On-demand** — AWS gestiona automáticamente la capacidad según la carga real. Más caro, pero útil
  cuando la carga de trabajo es muy **impredecible**.

### Índices secundarios (secondary indexes)

- Permiten optimizar rendimiento y coste cuando existen **patrones de acceso específicos** distintos
  de la clave de partición definida — por ejemplo, consultar frecuentemente por región o por categoría
  en lugar de por el ID principal.

### Cifrado

- Se deja la configuración por defecto.

## Resultado

Con solo el nombre de la tabla y la clave de partición ya es posible crear la tabla — el resto de
opciones (clase de tabla, modo de capacidad, índices secundarios, cifrado) son configurables pero no
estrictamente necesarias para el primer paso.
