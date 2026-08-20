# AWS Lake Formation: permisos y seguridad

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

[Lake Formation](1-lake-formation.md) **centraliza la gestión del acceso a los datos**: en lugar
de gestionar permisos por separado en cada servicio, las políticas de seguridad se definen y
aplican **desde el propio Lake Formation**, de forma consistente en un único lugar.

Esto aplica a distintos servicios donde pueden residir los datos: buckets de **S3**, el **Glue
Data Catalog**, **RDS**, etc. Por ejemplo, se puede especificar directamente una ubicación de S3
como fuente en Lake Formation y configurar ahí mismo la seguridad de ese bucket.

Lake Formation permite controlar el acceso a distintos niveles de granularidad:

- Nivel de **base de datos**.
- Nivel de **tabla**.
- Nivel de **fila**, **columna** o incluso **celda** (mediante *data filtering*).

## Data filtering: seguridad a nivel de fila, columna y celda

El **data filtering** permite un control de acceso muy fino sobre los datos almacenados en las
tablas — no solo quién accede a una base de datos o tabla, sino **qué filas y columnas concretas**
puede ver cada usuario.

| Tipo                      | Qué controla                                                                       | Ejemplo de uso                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Row-level security**    | Qué **filas** de una tabla puede ver un usuario, según políticas basadas en roles. | Usuarios de distintos departamentos solo ven las filas de su propio departamento.                                                                            |
| **Column-level security** | Qué **columnas** de una tabla puede ver un usuario.                                | Restringir el acceso a columnas sensibles con información personal identificable (**PII**).                                                                  |
| **Cell-level security**   | Combina row-level y column-level security a la vez.                                | Pensar en la tabla como una cuadrícula: se restringe simultáneamente a qué filas **y** columnas se accede, determinando exactamente qué celdas son visibles. |

> ⚠️ La seguridad a nivel de celda **no es una función independiente**: es la combinación de
> aplicar seguridad a nivel de fila y de columna sobre la misma tabla.

## LF-Tags (control de acceso basado en etiquetas)

En un data lake grande, el número de tablas y usuarios crece muy rápido, y gestionar permisos uno
a uno se vuelve difícil de escalar. Para ello, Lake Formation ofrece **LF-Tag-Based Access
Control (LF-TBAC)** — control de acceso basado en atributos/etiquetas.

- Los administradores de datos crean **etiquetas LF (LF-Tags)** basadas en alguna clasificación de
  los datos (ej. `departamento`, `ubicación`).
- Esas etiquetas se **adjuntan** a los recursos del Glue Data Catalog (bases de datos, tablas,
  columnas).
- Los permisos se definen en función de esas etiquetas, en lugar de nombrar cada recurso
  individualmente — los administradores pueden **asignar y revocar** permisos a escala usando las
  LF-Tags.

## Integración con IAM

Lake Formation se integra con **IAM** para la gestión de identidad y permisos — roles, permisos
específicos, etc., igual que en el resto de servicios de AWS.

## Data sharing entre cuentas

Lake Formation simplifica compartir recursos del Data Catalog (bases de datos o tablas) tanto
**dentro de una cuenta** como **entre distintas cuentas de AWS**, mediante dos mecanismos:

- **Recursos con nombre (named resources)**: un recurso específico (ej. una tabla o base de
  datos) identificado por un **nombre único** dentro de Lake Formation y el Glue Data Catalog.
  Los permisos se conceden o revocan según ese nombre.
- **LF-Tags**: para un acceso más granular, usando las mismas etiquetas descritas arriba.

También se pueden compartir tablas del Data Catalog junto con **data filters**, de forma que el
acceso quede restringido a nivel de fila y celda incluso para el recurso compartido.

### AWS Resource Access Manager (RAM)

La integración con **AWS RAM** es clave para gestionar los permisos entre cuentas:

1. El recurso se comparte mediante una **invitación de RAM**.
2. La cuenta receptora **acepta** la invitación — el recurso pasa a estar disponible en esa cuenta,
   donde su administrador puede controlarlo y autorizarlo.
3. Para que servicios de consulta como **Athena** o **Redshift** puedan acceder al recurso
   compartido, es necesario crear un **resource link**: un enlace que apunta al recurso
   compartido (ej. una base de datos o tabla), y que permite a los usuarios de la cuenta receptora
   consultarlo.

> ⚠️ Aceptar la invitación de RAM no es suficiente por sí solo para consultar el recurso desde
> Athena/Redshift — hace falta además crear el **resource link** correspondiente en la cuenta
> receptora.

## Problemas habituales al compartir datos

- **Problemas de RAM**: los permisos no se propagan correctamente entre cuentas.
- **Problemas de rol de IAM**: el rol o su política no están bien configurados, y no permiten que
  el rol asumido (assumed role) haga lo que necesita hacer.
