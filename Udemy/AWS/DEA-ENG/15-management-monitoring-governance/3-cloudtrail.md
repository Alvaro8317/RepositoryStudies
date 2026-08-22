# AWS CloudTrail

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**AWS CloudTrail** es una herramienta de **auditoría y gobernanza**: registra toda la actividad
que tiene lugar dentro de una cuenta de AWS, en forma de **eventos**.

- Está **activado por defecto** en todas las cuentas.
- Ejemplos de actividad registrada: iniciar sesión en la cuenta de AWS, lanzar una instancia EC2,
  crear un bucket S3, etc.

## Tipos de eventos

Un **evento** es el registro de una actividad realizada en la cuenta — acciones ejecutadas a
través de la consola de AWS, el SDK, o la CLI, por un usuario, un rol o un servicio.

| Tipo de evento | También conocido como | Descripción | Registrado por defecto |
| -------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| **Management events** | Operaciones del **control plane** | Información sobre operaciones de **gestión** realizadas sobre recursos de la cuenta — ej. iniciar sesión, lanzar una instancia EC2, crear un bucket S3. | Sí |
| **Data events** | Operaciones del **data plane** | Información sobre operaciones realizadas **sobre/en** un recurso — suelen ser de **alto volumen**. Ej. acceso a nivel de objeto en un bucket S3 (subidas, descargas, borrados), consultas a bases de datos RDS. | No — hay que habilitarlos explícitamente |
| **Insight events** | — | Detectan **actividad inusual**: patrones anómalos en llamadas a la API o tasas de error inusuales en la cuenta. Se registran en un prefijo/carpeta distinto dentro del bucket de destino del trail. | No — hay que habilitarlos explícitamente, y solo se registran cuando CloudTrail detecta una desviación respecto al patrón de uso habitual (baseline) |

> ⚠️ Los **data events** (ej. acceso a objetos de S3) pueden habilitarse para un bucket concreto o
> para todos los buckets de la cuenta, según el nivel de detalle de auditoría necesario.

## Event history

**Event history** ofrece un registro **visible, consultable e inmutable** de los últimos **90
días** de actividad de management events en una región de AWS.

- Disponible **automáticamente** al crear la cuenta, **sin coste adicional**.

## Trails (rutas de seguimiento)

Un **trail** captura los registros de eventos de actividad y los almacena en un **bucket S3**
especificado por el usuario — también se puede integrar la entrega a **CloudWatch Logs**.

### Tipos de trail

| Tipo | Alcance | Notas |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Multi-región (multi-region)** | Aplica a **todas las regiones**: registra eventos en cada región y entrega los archivos de log al bucket S3 especificado. | Es la opción **por defecto** al crear un trail desde la **consola**. Si se añade una región nueva a la cuenta después de crear el trail, se incluye automáticamente. |
| **Región única (single-region)** | Aplica solo a **una región** específica. | Es la opción **por defecto** al crear un trail vía **CLI/API**. Se puede alternar entre single-region y multi-region usando la CLI. |
| **Organizacional (organization trail)** | Registra eventos de **todas las cuentas** de una organización de AWS Organizations. | Debe crearse desde la **cuenta de gestión** o una **cuenta de administrador delegado**. Puede aplicar a todas las regiones o solo a la región actual. |

> Para los tres tipos de trail, el bucket S3 de destino puede estar en **cualquier región** — no
> hay restricción geográfica sobre dónde se almacenan los logs.

### Múltiples trails por región

Se pueden crear **varios trails en una misma región** — útil, por ejemplo, cuando distintos grupos
(desarrolladores, responsables de seguridad, auditores) necesitan su propia copia de los archivos
de log.

> ⚠️ Límite: hasta **5 trails por región**. Un trail **multi-región** cuenta como un único trail
> por cada región a la que aplica.

## CloudTrail Lake

**CloudTrail Lake** es un **data lake gestionado** para capturar, almacenar y analizar la
actividad de usuarios y de API — típicamente con fines de **auditoría** o **seguridad**.

- Los eventos se ingieren en CloudTrail Lake mediante **channels** (canales).

### Tipos de channel

| Tipo | Descripción |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Integraciones con fuentes fuera de AWS** | Ingiere eventos de fuentes externas a AWS — por ejemplo, socios (*partners*) externos integrados con CloudTrail, o fuentes personalizadas. Al configurar el channel se elige dónde almacenar los eventos recibidos; si la fuente es un socio, se le proporciona el **ARN del channel**, y la **política de recursos** del channel es lo que le permite enviar eventos a través de él. |
| **Service-linked channels** (vinculados a un servicio) | Creados automáticamente por servicios de AWS, configurados para recibir eventos de forma automática. Pueden consultarse y modificarse desde la consola de CloudTrail o la CLI. |

> CloudTrail Lake permite un análisis profundo de los eventos, y se puede combinar con
> **EventBridge** creando reglas que respondan a eventos concretos de CloudTrail.
