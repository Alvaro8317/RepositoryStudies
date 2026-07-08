# CloudWatch Logs

## ¿Qué es?

CloudWatch Logs permite **centralizar los logs** de aplicaciones y servicios en AWS, facilitando su **gestión y análisis en un mismo lugar**. Permite monitorizar logs **en tiempo real** para identificar y responder rápidamente a problemas.

Puede recoger logs de: aplicaciones, contenedores, funciones Lambda, instancias EC2, consultas DNS, y muchas fuentes más.

## Estructura básica

| Componente        | Descripción                                                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log Group**     | Contenedor que agrupa los logs de una aplicación/servicio. Se pueden tener múltiples Log Groups.                                                                                    |
| **Log Stream**    | Dentro de un Log Group, identifica los logs de una **instancia específica** (ej. un contenedor concreto dentro de un servicio con múltiples contenedores tendría su propio stream). |
| **Evento de log** | Cada registro individual, normalmente compuesto por un **timestamp** y un **mensaje** (los campos pueden variar según la configuración).                                            |

- Cada Log Group tiene **permisos** y una **retención definida** (tiempo configurable antes de que los logs se eliminen automáticamente).

## Flujo: filtros de métrica → métricas → alarmas

1. **Filtros de métrica:** procesan y analizan los logs en tiempo real, convirtiendo ciertos datos del log en **métricas**.
2. **Métricas:** valores numéricos extraídos a partir de los logs.
3. **Alarmas:** se pueden lanzar en función de esas métricas, desencadenando acciones posteriores (ej. notificar, escalar, ejecutar código).

> En resumen: Log Group → Filtro de métrica → Métrica → Alarma → Acción.

## Retención de logs

- Se puede definir un periodo de retención (ej. **30 días**) o configurar que los logs **nunca expiren**.

## Destinos de exportación de logs

Desde CloudWatch Logs, los registros se pueden enviar a otros servicios:

- **Amazon S3** (almacenamiento/exportación)
- **Kinesis Data Streams**
- **Kinesis Data Firehose**
- **AWS Lambda** (ejecución de código a partir de los eventos de log)

### Ejemplo de flujo completo

```text
Instancia EC2 (genera logs)
      │
      ▼
CloudWatch Logs (evento almacenado)
      │
      ├──► Exportación a S3
      │
      └──► Alarma → Amazon SNS (email al equipo técnico)
                  → AWS Lambda (acción automatizada)
```

## Fuentes comunes de logs en CloudWatch

- **Agente de CloudWatch Logs** / **Agente unificado de CloudWatch** (instalado en instancias EC2)
- **Elastic Beanstalk**
- **ECS** (contenedores Docker)
- **Funciones Lambda**
- **VPC Flow Logs**
- **API Gateway**
- **CloudTrail**
- **Route 53** (DNS)

## Filtrado y consultas

- **Expresiones de filtro:** permiten buscar patrones concretos dentro de los logs (ej. encontrar una IP específica, contar ocurrencias de errores, filtrar por nivel de log: error, warning, info, debug).
- Los **filtros de métrica** creados a partir de estas búsquedas pueden usarse para activar alarmas (ej. disparar una función Lambda o escalar instancias EC2).
- **CloudWatch Logs Insights:** permite consultar los logs de forma más avanzada y añadir esas consultas directamente a **CloudWatch Dashboards** para visualización centralizada.

## Exportación a Amazon S3

- Los datos de logs pueden tardar **hasta 12 horas** en estar disponibles para exportar a un bucket S3.
- La exportación **no es en tiempo real**; se realiza mediante:
  - Una **tarea de exportación** a través de la API (`CreateExportTask`).
  - O mediante **suscripciones a logs** para casos donde se necesite reaccionar a eventos.

## Filtros de suscripción (Subscription Filters)

- Permiten **enviar datos de CloudWatch Logs hacia otros servicios** en tiempo (casi) real: funciones Lambda, Kinesis, etc.
- Muy usados quando se quiere **suscribir múltiples servicios** a los mismos datos de logs para procesarlos de distintas formas.

### Centralización de logs entre cuentas

- Es habitual que, a medida que una empresa crece, se destine una **cuenta de AWS dedicada exclusivamente a centralizar logs**.
- Mediante **filtros de suscripción entre cuentas** (Cuenta A → Cuenta B), se pueden enviar los datos de CloudWatch Logs desde varias cuentas hacia una cuenta centralizada de gestión de logs.

## Idea clave

CloudWatch Logs tiene muchas funcionalidades (Log Groups/Streams, filtros de métrica, alarmas, exportación, Insights, suscripciones entre cuentas), pero la idea central es siempre la misma: **centralizar, analizar y reaccionar** ante los registros generados por las aplicaciones y servicios en AWS.
