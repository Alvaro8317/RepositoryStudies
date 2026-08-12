# APIs de DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

DynamoDB expone un conjunto de APIs para interactuar mediante programación con el servicio: crear
tablas, insertar elementos, consultar datos, etc. — en general, las operaciones **CRUD** (crear, leer,
actualizar, eliminar) sobre las tablas. Se agrupan en **cuatro categorías** de operaciones de alto
nivel:

1. **Plano de control (Control Plane)** — gestión del propio servicio.
2. **Plano de datos (Data Plane)** — lectura/escritura de elementos.
3. **DynamoDB Streams API** — acceso y gestión de los streams de una tabla.
4. **Transactions API** — agrupar varias operaciones en una única operación atómica.

## Plano de control (Control Plane)

Operaciones administrativas: gestionan el servicio en sí, no los datos.

| API               | Qué hace                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **CreateTable**   | Crea una nueva tabla.                                                                                  |
| **DescribeTable** | Recupera información general de una tabla (configuración, estado, etc.).                               |
| **ListTables**    | Lista todas las tablas de la cuenta/región.                                                            |
| **UpdateTable**   | Modifica la configuración de una tabla (rendimiento provisionado, índices secundarios globales, etc.). |
| **DeleteTable**   | Elimina la tabla completa y todos sus datos.                                                           |

## Plano de datos (Data Plane)

Operaciones que interactúan directamente con los datos almacenados en las tablas. Hay dos formas de
hacerlo: mediante **PartiQL** o mediante las **APIs CRUD clásicas** de DynamoDB.

### PartiQL

**PartiQL** es un lenguaje de consulta compatible con SQL soportado por DynamoDB, lo que facilita las
operaciones CRUD si ya se está familiarizado con SQL.

- **ExecuteStatement** — lee múltiples elementos, o escribe/actualiza un único elemento de una tabla, usando sintaxis PartiQL.
- **BatchExecuteStatement** — realiza operaciones por lotes (leer, escribir o actualizar múltiples elementos) con PartiQL.

### APIs CRUD clásicas

> ⚠️ En todas estas operaciones es obligatorio especificar la **clave primaria** del elemento.

| Operación                     | Qué hace                                                                                                                              | Límite              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **PutItem**                   | Escribe un único elemento en una tabla.                                                                                               | —                   |
| **BatchWriteItem**            | Escribe varios elementos en una o varias tablas.                                                                                      | Hasta 25 elementos  |
| **GetItem**                   | Obtiene un único elemento de una tabla mediante su clave primaria.                                                                    | —                   |
| **BatchGetItem**              | Obtiene varios elementos de una o varias tablas.                                                                                      | Hasta 100 elementos |
| **Query**                     | Recupera todos los elementos que coinciden con una clave de partición (y, opcionalmente, una condición sobre la clave de ordenación). | —                   |
| **Scan**                      | Lee todos los elementos de una tabla o de un índice secundario.                                                                       | —                   |
| **UpdateItem**                | Modifica uno o más atributos de un elemento.                                                                                          | —                   |
| **DeleteItem**                | Elimina un elemento de una tabla.                                                                                                     | —                   |
| **BatchWriteItem** (eliminar) | También se usa para eliminar varios elementos por lotes.                                                                              | Hasta 25 elementos  |

## DynamoDB Streams API

Operaciones para capturar y consumir los cambios sobre los elementos de una tabla — ver
[[8-dynamodb-streams|DynamoDB Streams]] para el concepto general.

| API                  | Qué hace                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **ListStreams**      | Obtiene la lista de streams asociados a una tabla.                                                                     |
| **DescribeStream**   | Recupera información sobre un stream específico.                                                                       |
| **GetShardIterator** | Obtiene un iterador que permite leer los registros del stream desde una posición específica.                           |
| **GetRecords**       | Recupera los registros del stream (usando el shard iterator), incluyendo inserciones, actualizaciones y eliminaciones. |

## Transactions API

Permite agrupar varias operaciones en una única operación **todo o nada** (atómica): o tienen éxito
todas las operaciones incluidas, o fallan todas. Es especialmente útil cuando hace falta garantizar la
integridad de los datos a través de múltiples elementos — por ejemplo, en transacciones financieras.

También aquí hay dos formas de trabajar: con **PartiQL** o con las **APIs transaccionales clásicas**.

| API                    | Qué hace                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **ExecuteTransaction** | Operación por lotes en PartiQL: realiza una operación transaccional con múltiples acciones sobre distintos elementos y tablas. |
| **TransactWriteItems** | Realiza atómicamente varias operaciones de escritura (put, update, delete) sobre varios elementos de una o varias tablas.      |
| **TransactGetItems**   | Recupera varios elementos de una o varias tablas como parte de una única transacción atómica.                                  |
