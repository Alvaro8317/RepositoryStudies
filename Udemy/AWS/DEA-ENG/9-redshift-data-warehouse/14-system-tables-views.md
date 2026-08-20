# Redshift: tablas y vistas del sistema

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

No es posible (ni necesario) cubrir cada tabla y vista del sistema individualmente, pero conviene
tener una visión general de las **categorías** y algunos **ejemplos importantes**, ya que pueden
aparecer en el examen.

## Qué son y para qué se usan

- Contienen **metadatos** sobre el funcionamiento del sistema — no son datos de negocio.
- Se usan sobre todo para **tareas administrativas**: obtener información, supervisar la salud del
  clúster y mejorar el rendimiento de las consultas.
- Ejemplo de uso: ver todas las **consultas en ejecución** en un momento dado.
- Se consultan igual que cualquier otra tabla o vista, con `SELECT` estándar.

> ⚠️ No todas son accesibles para cualquier usuario: algunas están reservadas para el personal de
> AWS (fines de diagnóstico), otras solo son visibles para **superusuarios**, y otras están
> disponibles para todos los usuarios.

## Categorías

Redshift organiza sus tablas y vistas de sistema en varios prefijos. Muchas de las **vistas** (`SVV`,
`SVL`, `SVCS`) hacen referencia a **tablas** subyacentes (`STL`, `STV`), solo que presentan los datos
de forma más organizada y fácil de consultar. Por eso, a veces hay **información solapada** entre
distintas vistas — no siempre hay una separación clara de casos de uso.

| Prefijo                         | Qué contiene                                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **SVV** (system view)           | Información sobre **objetos de base de datos** (tablas, columnas, tablas/columnas externas).                                      |
| **SYS**                         | Vistas para **monitorizar consultas y uso de carga de trabajo**, tanto en clústeres aprovisionados como en workgroups serverless. |
| **STL** (system table log)      | Datos tomados de los **logs generados en el clúster**, formateados como vistas útiles para diagnosticar problemas.                |
| **STV** (system table snapshot) | **Instantáneas** de los datos actuales del sistema.                                                                               |
| **SVCS**                        | Detalles de consultas tanto del **clúster principal** como de los **clústeres de concurrency scaling**.                           |
| **SVL**                         | Vistas que referencian tablas **STL**, con **joins** adicionales para que la información sea más fácil de entender.               |

## SVV — objetos de base de datos

- Devuelven una **unión** de todos los objetos de un tipo determinado junto con información
  relacionada.
- Ejemplos:
  - **`SVV_TABLES`**: unión de todas las tablas (incluye también tablas externas).
  - **`SVV_COLUMNS`**: unión de todas las columnas (incluye también columnas de tablas externas).

## SYS — monitorización de consultas y workloads

- Se usan para supervisar consultas y uso de carga de trabajo, tanto en **clústeres
  aprovisionados** como en **workgroups serverless**.
- Ejemplos:
  - **`SYS_QUERY_HISTORY`**: muestra los detalles de las consultas de usuario — cada fila
    representa una consulta, con estadísticas adicionales.
  - **`SYS_QUERY_DETAIL`**: versión aún más detallada de la anterior.

## STL — logs del sistema

- Provienen de los archivos de log generados en el clúster, formateados para que los
  administradores puedan consultarlos y diagnosticar problemas.
- Ejemplos:
  - **`STL_ALERT_EVENT_LOG`**: registra alertas cuando el **optimizador de consultas** identifica
    condiciones que podrían indicar problemas de rendimiento — muy útil como punto de partida para
    detectar oportunidades de optimización.
  - **`STL_VACUUM`**: estadísticas de filas y bloques de las tablas que han sido objeto de
    [`VACUUM`](7-vacuum.md).

## STV — instantáneas del sistema

- Contienen una **instantánea** de los datos actuales del sistema en un momento dado.
- Ejemplo:
  - **`STV_EXEC_STATE`**: información sobre las consultas y los pasos de consulta que se están
    ejecutando **activamente** en los nodos de cómputo — útil para diagnosticar problemas en curso.

## SVCS — consultas en clúster principal y concurrency scaling

- Detalles de consultas ejecutadas tanto en el **clúster principal** como en los **clústeres de
  concurrency scaling** (la función que añade capacidad adicional al clúster automáticamente
  cuando aumenta la carga de consultas).
- Ejemplo:
  - **`SVCS_QUERY_SUMMARY`**: información general sobre la ejecución de una consulta. Su
    información se solapa parcialmente con `SYS_QUERY_HISTORY` / `SYS_QUERY_DETAIL`.

> ⚠️ AWS recomienda usar las vistas **`SYS_QUERY_HISTORY`** / **`SYS_QUERY_DETAIL`** en lugar de
> `SVCS_QUERY_SUMMARY`, ya que están formateadas de forma más fácil de usar y entender.

## SVL — vistas legibles sobre tablas STL

- Referencian tablas `STL`, añadiendo `JOIN`s para hacer el acceso más sencillo que consultar las
  tablas `STL` directamente.
- Ejemplo:
  - **`SVL_USER_INFO`**: información sobre los usuarios de la base de datos, bien organizada.
