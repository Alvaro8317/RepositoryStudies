# Amazon CloudWatch

## ¿Qué es?

CloudWatch permite realizar **monitoreo en tiempo real** de recursos y aplicaciones en AWS, proporcionando un conjunto de **métricas** para prácticamente todos los servicios de AWS.

- Se pueden usar las métricas que CloudWatch ofrece por defecto.
- También es posible crear **métricas personalizadas** propias para monitorizar aspectos específicos de una aplicación.

## Métricas destacadas

- **Utilización de CPU**
- **Networking:** tráfico de entrada y salida de red
- **Operaciones de disco:** lectura y escritura
- **Latencia**

Todas las métricas incluyen **timestamps** (marcas de tiempo), lo que permite saber exactamente en qué momento ocurrió cada evento/acción.

## Dashboards

CloudWatch permite crear **dashboards totalmente personalizados** para visualizar las métricas elegidas y controlar el estado de la aplicación **en tiempo real**.

## Integraciones con CloudWatch

| Componente                        | Qué se integra                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Instancias EC2**                | Registro de logs de la aplicación (imprescindibles para saber cómo funciona y detectar errores) |
| **Contenedores Docker (ej. ECS)** | Notificación de estado y logs de los contenedores                                               |
| **Bases de datos (ej. DynamoDB)** | Métricas de base de datos                                                                       |
| **Funciones Lambda**              | Las métricas pueden desencadenar la ejecución de código/funciones                               |
| **Alarmas**                       | Se activan al superar un umbral definido sobre una métrica                                      |

### Ejemplo de flujo con alarmas

1. Se monitoriza el uso de CPU de una instancia EC2.
2. Se define un **umbral** (ej. 80% de CPU).
3. Al superarlo, se **desencadena una alarma**.
4. La alarma puede disparar una acción, como **autoescalar** añadiendo más instancias EC2.

> Métricas → Alarmas → Escalado/Notificaciones: estos tres elementos son clave para la **escalabilidad** y **disponibilidad** de los sistemas en la nube.

## Monitorización detallada (Detailed Monitoring)

| Modo                              | Frecuencia de métricas | Coste           |
| --------------------------------- | ---------------------- | --------------- |
| **Estándar** (por defecto en EC2) | Cada **5 minutos**     | Incluido        |
| **Detallada**                     | Cada **1 minuto**      | Coste adicional |

- La monitorización detallada es útil, por ejemplo, cuando se necesita **escalar más rápido** un grupo de Auto Scaling.
- La **capa gratuita (Free Tier)** de AWS incluye **10 métricas** de monitorización detallada.
- Con un plan de pago se puede acceder a muchas más métricas.

## Nota importante: memoria en EC2

⚠️ El **uso de memoria de una instancia EC2 NO se envía por defecto a CloudWatch**.

Para poder visualizar la métrica de memoria es necesario **configurar una métrica personalizada** en la instancia correspondiente.

## Diagrama conceptual del flujo

```text
Instancia EC2
   │
   ├─► Recolección de métricas (CPU, estado de la instancia, eventos personalizados)
   │
   ├─► CloudWatch (métricas + logs + dashboards)
   │
   └─► Alarmas → Acciones (escalar, notificar usuarios, disparar Lambda, etc.)
```

## Idea clave

CloudWatch es uno de los servicios **más usados y recomendados** en cualquier arquitectura sobre AWS, ya que centraliza métricas, logs, eventos y alarmas, permitiendo tener visibilidad completa y reaccionar automáticamente ante cambios en el estado de los recursos.
