# Amazon Athena — Consultas federadas (Federated Queries)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son las consultas federadas?

Las **consultas federadas (federated queries)** son una funcionalidad avanzada de Athena que permite
ejecutar **SQL estándar** sobre datos que **no están en S3**, sino en otras fuentes de datos:

- Fuentes de datos **relacionales**.
- Fuentes de datos **no relacionales**.
- **Almacenes de objetos**.
- Incluso **fuentes de datos personalizadas** creadas por el usuario.

El beneficio principal es tener una única interfaz — **Athena** — desde la que consultar datos que
viven en sistemas completamente distintos, sin tener que moverlos ni replicarlos primero.

## Conectores de datos federados

Para lograr esto, Athena usa **fuentes de datos federadas (data source connectors)**: piezas de código
que traducen entre la fuente de datos de destino y el motor de consultas de Athena.

> Se puede pensar en cada conector como una **extensión del motor de consultas de Athena**.

- Existen **conectores preconfigurados** para fuentes comunes.
- También se pueden **personalizar** o crear conectores propios.

### Fuentes soportadas por conectores preconfigurados

| Fuente de datos            | Tipo                                       |
| -------------------------- | ------------------------------------------ |
| **Amazon CloudWatch Logs** | Logs                                       |
| **Amazon DynamoDB**        | No relacional                              |
| **Amazon DocumentDB**      | No relacional (documentos)                 |
| **Amazon RDS**             | Relacional                                 |
| **Otras fuentes JDBC**     | Relacional (ej. **MySQL**, **PostgreSQL**) |

## Caso de uso típico

Las consultas federadas son útiles para **análisis ad hoc**: cuando se necesita combinar datos de
varias fuentes rápidamente, sin construir un proceso ETL completo.

Ejemplo: revisar el historial completo de un cliente combinando datos de distintos sistemas:

- **Historial de compras** e información de productos → almacenados en **RDS**.
- **Perfil detallado del cliente** → en otra fuente de datos.
- **Interacciones del usuario** → almacenadas en **DynamoDB**.

En vez de consultar cada sistema por separado, una consulta federada permite combinar todas esas
fuentes en una sola consulta SQL desde Athena.

> ⚠️ Las consultas federadas están pensadas para análisis rápidos y exploratorios, no para sustituir
> un pipeline ETL cuando se necesita procesamiento recurrente o a gran escala.
