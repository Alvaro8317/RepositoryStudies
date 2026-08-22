# Amazon EventBridge

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon EventBridge** es un servicio **serverless** que ayuda a enlazar diferentes partes de una
aplicación mediante **eventos**. Se utiliza para **gestionar** y **enrutar** eventos desde un
**productor** (donde se genera el evento) hacia un **objetivo** específico.

## ¿Qué es un evento?

Un **evento** es básicamente un **cambio de estado** en el entorno. Ejemplos:

- Una instancia **EC2** que cambia de `running` a `stopped`.
- Un **bucket S3** configurado para emitir un evento cuando se sube un archivo.

Un evento puede desencadenar otra acción — por ejemplo, la subida de un archivo dispara una función
**Lambda** que lo procesa. Este es un ejemplo básico de **arquitectura dirigida por eventos**
(*event-driven architecture*).

> EventBridge puede gestionar eventos generados por aplicaciones propias, por servicios de AWS o
> por software de terceros (SaaS).

## Componentes principales

| Componente             | Función                                                                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Event producers**    | Fuentes que generan los eventos: un servicio de AWS (ej. EC2), una aplicación personalizada o una aplicación SaaS de terceros. |
| **Event bus**          | El eje central por donde circulan los eventos: recibe los eventos y decide, según las reglas configuradas, hacia dónde reenviarlos. |
| **Rules** (reglas)     | Definidas en el event bus; determinan qué eventos deben enviarse a qué objetivo para su procesamiento.                    |
| **Targets** (objetivos) | Servicios/recursos que reciben el evento para procesarlo — por ejemplo, una función Lambda o un topic de SNS.             |

### Arquitectura desacoplada

Reaccionar a eventos mediante EventBridge habilita una **arquitectura desacoplada**: los distintos
componentes de la aplicación pueden funcionar de forma **independiente**.

**Ejemplo:** se sube un archivo a un bucket S3 (evento) → el evento llega al event bus → el event
bus comprueba las reglas configuradas → si hay coincidencia, el evento (junto con metadatos, como
el nombre del archivo) se envía al objetivo definido (ej. una función Lambda) → la Lambda se
dispara y procesa el archivo. Un mismo evento puede enviarse a **varios objetivos** a la vez (por
ejemplo, una notificación SMS y, además, un flujo de trabajo de Step Functions).

## Tipos de reglas

| Tipo de regla | Descripción |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Basada en patrón de evento** | Desencadena acciones según un **patrón de evento** específico, definido en JSON (estructura y valores concretos que interesan — ej. solo cierto tipo de archivo o cierta ruta de un bucket S3). Cuando un evento entrante coincide con el patrón, EventBridge lo enruta al objetivo definido. |
| **Basada en calendario** (*schedule*) | Envía eventos a intervalos de tiempo específicos hacia los objetivos definidos — por ejemplo, ejecutar una función Lambda periódicamente. |

## Tipos de event bus

| Tipo                     | Descripción                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| **Default event bus**    | Siempre disponible por defecto en la cuenta; recibe automáticamente eventos de los servicios de AWS. |
| **Custom event bus**     | Creado por el usuario; se especifica qué eventos debe recibir, para necesidades específicas.       |
| **Partner event bus**    | Permite recibir eventos de socios SaaS integrados con AWS.                                        |

## Schema Registry (registro de esquemas)

El **Schema Registry** permite **descubrir**, **gestionar** y **hacer evolucionar** los
**esquemas de eventos**.

- Un **esquema de evento** es un modelo que define la **estructura de los datos** de un evento
  (tipos de datos, campos, etc.), normalmente en formato **JSON** — asegura que todos los
  componentes de la arquitectura puedan interpretar correctamente los eventos que reciben.
- Proporciona un formato **estructurado y coherente** que productores y consumidores de eventos
  pueden seguir.

### Características

- **Descubrimiento de esquemas**: captura automáticamente la estructura de los eventos (de
  servicios de AWS, aplicaciones personalizadas o SaaS), eliminando la necesidad de examinar
  manualmente los datos de los eventos.
- **Generación de código**: genera automáticamente código en varios lenguajes para facilitar el
  manejo de eventos en las aplicaciones.
- **Seguimiento y gestión de versiones**: rastrea las actualizaciones de los esquemas a medida que
  evolucionan, garantizando compatibilidad tanto con formatos de datos antiguos como nuevos.
- **Compartición de esquemas**: permite tener esquemas comunes entre distintas cuentas/organización
  para un manejo uniforme y eficiente de los datos.

## Políticas basadas en recursos (Resource-based Policies)

EventBridge permite definir **políticas basadas en recursos** directamente sobre un recurso (por
ejemplo, un **event bus**) — sin necesidad de vincularlas a un usuario o rol IAM concreto. Esto
permite controlar, por ejemplo, quién puede **publicar eventos** en un event bus determinado.

Componentes de una política basada en recursos:

| Elemento      | Descripción                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------- |
| **Principal** | La cuenta de AWS (o, en algunos casos, usuario/rol) a la que se permite o deniega la acción.         |
| **Action**    | La acción concreta a permitir/denegar — por ejemplo, `events:PutEvents` (publicar eventos).          |
| **Resource**  | El **ARN** del recurso al que se adjunta la política — por ejemplo, el ARN del event bus.            |
| **Effect**    | `Allow` o `Deny`, según el permiso deseado.                                                          |

### Beneficios

- **Control descentralizado**: el acceso se gestiona directamente en el recurso, sin necesidad de
  centralizarlo mediante políticas de usuario/rol.
- **Acceso entre cuentas simplificado**: facilita que cuentas externas de AWS publiquen eventos en
  el event bus.
- **Granularidad**: permite afinar con detalle quién puede usar exactamente los recursos de
  EventBridge, mejorando la seguridad.
