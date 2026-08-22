# Amazon CloudWatch

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es CloudWatch?

**CloudWatch** es el servicio de **monitorización** de AWS: da visibilidad sobre el
**rendimiento** y la **salud operativa** de aplicaciones y recursos, **en tiempo real**.

- Permite reunir métricas y recopilarlas en **dashboards**: una colección de métricas centralizada
  en un mismo sitio.
- Es un servicio **global**: se pueden ver las métricas **independientemente de la región**, sin
  necesidad de cambiar de región para consultarlas.

## Métricas

Una **métrica** es un conjunto de **puntos de datos** — valores numéricos que se usan para medir
recursos y aplicaciones.

- Las métricas ayudan a entender **cuánto se está usando** un recurso y **qué tan saludable**
  está.
- Ejemplo típico: el **porcentaje de utilización de CPU** de una instancia EC2, para medir su
  salud, uso y rendimiento.
- Muchos servicios de AWS proporcionan métricas **por defecto** y **sin coste adicional**, para
  supervisar la salud, el rendimiento y la utilización de los recursos.

### Componentes de una métrica

| Componente | Descripción |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Namespace** | Contenedor que **agrupa métricas relacionadas**, para organizarlas y categorizarlas (por ejemplo, según su fuente/servicio o propósito). Convención habitual: `AWS/<servicio>` (ej. `AWS/EC2`), o algo propio como `mi-empresa/produccion`. |
| **Timestamp** | Momento en el que se tomó la medida. |
| **Dimensiones** | Pares **clave-valor** asociados a una métrica, que aportan **profundidad adicional**. Ej. para una instancia EC2: `InstanceId`, `InstanceType`, `ImageId`. Permiten ver los datos de una instancia específica o comparar varias instancias entre sí. |
| **Estadísticas** | Datos **agregados** de la métrica durante un periodo determinado (ej. la utilización **media** de CPU de una instancia EC2 en ese periodo). |
| **Periodo (Period)** | Intervalo de tiempo asociado a una estadística — determina con qué frecuencia se agregan/comprueban los datos. |
| **Resolución** | Nivel de detalle (granularidad) de los datos de la métrica. |

### Resolución: estándar vs. alta

- **Resolución estándar**: un punto de datos **cada minuto** (comportamiento por defecto).
- **Alta resolución**: registra métricas con granularidad de **hasta 1 segundo**.

> ⚠️ Las **métricas** son el concepto más fundamental de CloudWatch — namespace, dimensiones,
> estadísticas, periodo y resolución son los componentes clave a entender a nivel conceptual antes
> de ver funcionalidades más avanzadas como los **metric streams** (siguiente clase).

## CloudWatch Metric Streams

**CloudWatch Metric Streams** permite transmitir **continuamente** las métricas de CloudWatch
hacia otros destinos (por ejemplo, **S3** o servicios de terceros), ofreciendo una alimentación
casi en **tiempo real** de las métricas de los recursos monitorizados.

- Son similares a los **Kinesis Data Streams** en el sentido de que también transmiten datos (en
  este caso, métricas) como un flujo continuo, tanto hacia otros servicios de AWS como hacia
  destinos de terceros.
- Por debajo, usan **Kinesis Data Firehose** para entregar las métricas a los distintos destinos.

### Flujo de funcionamiento

1. Las métricas se ingieren en un **Metric Stream**, que las envía a **Kinesis Data Firehose**.
2. Firehose entrega los datos a los destinos configurados — por ejemplo, **OpenSearch**,
   **Redshift** o buckets de **S3**.
3. Esos destinos suelen ofrecer, además, capacidades de **análisis** sobre los datos recibidos.

> En esencia: se crea un metric stream y se dirige hacia un delivery stream de **Amazon Data
> Firehose**, que se encarga de entregarlo al destino final.

### Formas de configurar un Metric Stream

| Opción | Descripción |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Uso de Firehose (personalizado)** | Configuración manual usando un delivery stream de Kinesis Data Firehose propio, con control total sobre el destino. |
| **Quick S3 setup** | Configuración rápida para transmitir directamente a **S3** — por defecto se crean automáticamente todos los recursos necesarios para el flujo. |
| **Quick AWS Partner setup** | Configuración rápida y simplificada, pensada para conectar con **socios de terceros** de AWS de forma sencilla. |

## CloudWatch Alarms

Las **alarmas** de CloudWatch se usan para **monitorizar métricas** y **desencadenar acciones**
cuando se supera un **umbral** (*threshold*) definido. Al crear una alarma se establece ese umbral
que la métrica supervisada no debería sobrepasar; cuando se supera, la alarma se dispara y entra
en acción.

### Tipos de alarma

| Tipo | Descripción |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **Alarma de métrica** | Controla una **única métrica**. Cuando esa métrica supera el umbral definido, la alarma pasa al estado `ALARM`. |
| **Alarma compuesta** | Controla los **estados de otras alarmas** (nivel superior). Se define mediante una **expresión de regla**; entra en estado `ALARM` únicamente cuando **todas** las condiciones de esa regla se cumplen. |

**Ejemplo:** una alarma de métrica que monitoriza la utilización de CPU de una instancia EC2, con
el umbral fijado en **80%** — al superarlo, se dispara la alarma y se ejecuta la acción asociada.

### Estados de una alarma

| Estado                  | Significado                                                                 |
| -------------------------- | -------------------------------------------------------------------------------- |
| **OK**                    | La métrica sigue **por debajo** del umbral definido.                            |
| **ALARM**                 | Se ha **superado** el umbral definido.                                          |
| **INSUFFICIENT_DATA**     | No hay datos suficientes para determinar el estado de la alarma.               |

### Acciones asociadas a una alarma

Cuando cambia el estado de una alarma, se pueden disparar distintas acciones, involucrando a otros
servicios:

- **Notificaciones vía Amazon SNS**: envío automático de email, SMS o notificaciones push a un
  administrador, o activación de un flujo de trabajo automatizado.
- **Acciones sobre instancias EC2**:
  - **Detener** la instancia — útil para reducir costes ante baja utilización.
  - **Terminar** la instancia — útil con instancias Spot o para eliminar instancias no saludables.
  - **Reiniciar** la instancia — útil si deja de responder.
- **Auto Scaling**: activar un grupo de Auto Scaling para escalar hacia dentro o hacia fuera.
- **AWS Lambda**: invocar una función para acciones personalizadas (ej. actualizar una base de
  datos, limpiar recursos, o cualquier otro flujo de trabajo a medida).
- **AWS Systems Manager Incident Manager**: crear automáticamente un **incidente** — un evento de
  alta prioridad que requiere atención y resolución inmediata.

## CloudWatch Logs

**CloudWatch Logs** permite supervisar y analizar los datos de registro (*logs*) de distintos
recursos y aplicaciones:

- Actúa como **repositorio centralizado**: recopila y consolida los logs de todas las fuentes del
  entorno de AWS en un mismo lugar.
- Permite **seguimiento y análisis en tiempo real**, para entender y reaccionar rápidamente ante
  problemas.

### Conceptos clave

| Concepto | Descripción |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Log stream** (flujo de registro) | Secuencia **cronológica** de eventos de registro procedentes todos de la **misma fuente** — por ejemplo, los eventos producidos por una única instancia EC2 o un único componente de aplicación. |
| **Log group** (grupo de registro) | Contenedor que agrupa uno o varios log streams — ayuda a **organizar y gestionar** los logs, por ejemplo separando distintas aplicaciones o capas de la infraestructura. |
| **Log event** (evento de registro) | Registro individual de actividad dentro de una aplicación o recurso; normalmente contiene un **timestamp** y un **payload** (ej. un informe de error u otra información relevante). |
| **Retention policy** (política de retención) | Define, **por log group**, durante cuánto tiempo se conservan los logs antes de borrarse automáticamente — ayuda a gestionar costes y a cumplir requisitos de retención de datos. |

### CloudWatch Logs Insights

Permite **buscar y analizar interactivamente** los datos de los logs de CloudWatch: se escriben
**expresiones de consulta** para filtrar registros, crear visualizaciones y obtener información —
muy útil para diagnosticar problemas o entender el comportamiento del sistema.

### Envío de logs a otros servicios

| Destino | Uso típico |
| ------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **S3** | Retención a largo plazo / archivado de los datos de log. |
| **Kinesis Data Streams / Firehose** | Procesamiento en tiempo real de los datos de log, o carga hacia otros servicios/herramientas analíticas. |
| **Lambda** | Procesamiento personalizado de los logs o ejecución de acciones específicas basadas en su contenido. |

## Filtrado de logs: metric filters y subscription filters

Permiten **filtrar** los datos de log (por patrones o palabras concretas) antes de enviarlos a un
destino específico.

| Tipo de filtro | Descripción |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Metric filter** | Extrae datos de los eventos de log para crear **métricas personalizadas** a partir de ellos — permite obtener datos cuantitativos de logs (que por sí mismos no son cuantitativos) y habilitar monitorización adicional basada en su contenido. |
| **Subscription filter** | Transmite los datos de log a otros servicios **en tiempo real**. Una vez configurado sobre un log stream, todos los eventos entrantes que coincidan con el filtro se envían inmediatamente al destino especificado. |

Destinos habituales de un subscription filter:

- **Kinesis Data Firehose**: para cargar los datos en almacenes como S3, Redshift o Elasticsearch.
- **Kinesis Data Streams**: para seguir procesando los datos o aplicar análisis en tiempo real.
- **AWS Lambda**: para invocar una función que procese los datos de log.

**Flujo:** CloudWatch Logs → subscription filter (filtra los datos) → Kinesis Data Firehose /
Data Streams → destino final (ej. Lambda, S3).

### Acceso entre cuentas (cross-account)

Es habitual querer compartir logs generados en una cuenta con otra cuenta distinta (por ejemplo,
para aislar entornos y centralizar el análisis en una cuenta separada). Un patrón común usa un
**Kinesis Data Stream** en la cuenta de destino:

1. Crear el **Kinesis Data Stream** en la **cuenta de destino**.
2. Crear un **rol IAM** en la cuenta de destino que permita escribir en ese data stream.
3. Modificar la **política de recursos** del data stream para que la **cuenta de origen** pueda
   usarlo (escribir en él).
4. Configurar una **política de confianza** (*trust policy*) que permita a la cuenta de origen
   **asumir** ese rol IAM, para poder escribir en el Kinesis Data Stream.
5. Configurar un **subscription filter** en la **cuenta de origen** para filtrar qué logs se envían
   al Kinesis Data Stream.

> Este patrón habilita el acceso entre cuentas a logs generados en una cuenta y consumidos/
> analizados en otra.

## Agentes de logs: enviar logs desde EC2 / on-premises

> ⚠️ **EC2 no envía logs a CloudWatch de forma nativa.** Para enviar logs desde instancias EC2 (o
> servidores on-premises) a CloudWatch Logs hace falta instalar un **agente de logs**.

El agente es un proceso ligero e independiente que se instala directamente en la instancia/servidor
y recopila y transmite los datos de log a CloudWatch Logs casi en tiempo real.

| Agente | Estado | Capacidades |
| ----------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **CloudWatch Logs Agent** (antiguo) | Ya no recomendado | Solo recopila datos de **log**. Capacidades limitadas. |
| **CloudWatch Unified Agent** (nuevo) | **Recomendado** por AWS | Recopila logs **y** métricas a nivel de sistema (RAM, uso de CPU, uso de memoria, espacio en disco, etc.). Más eficiente, mejor rendimiento, menor uso de recursos, métricas personalizadas con resolución más fina, y mejor integración con otros servicios. |

> ⚠️ Para el examen: **usar siempre el Unified Agent**, no el CloudWatch Logs Agent antiguo — es
> la recomendación explícita de AWS.
