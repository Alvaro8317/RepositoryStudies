# Amazon SNS (Simple Notification Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon SNS** es un servicio de mensajería **pub/sub** (publicador/suscriptor) totalmente
gestionado: los mensajes se envían desde **editores** (*publishers*) a **temas** (*topics*), en
lugar de enviarse directamente a receptores específicos. Los **abonados** (*subscribers*) se
suscriben a esos temas y reciben solo los mensajes que les interesan.

- Permite **desacoplar** productores y consumidores de mensajes, haciendo el sistema más
  **flexible** y **escalable**.
- Pensado para desacoplar **microservicios**, **sistemas distribuidos** y **aplicaciones
  serverless**.
- Habilita mensajería push de **alto rendimiento**, de tipo **muchos a muchos**: varios editores
  envían mensajes que se distribuyen a varios abonados, permitiendo **procesamiento paralelo**.

Tipos de endpoint de abonado soportados: colas **SQS**, funciones **Lambda**, endpoints **HTTP/S**
(webhooks), **SMS**, correo electrónico, y más.

## Topics (temas)

Los **temas** son el núcleo de SNS: canales donde los editores publican mensajes que después se
envían a los abonados.

| Tipo de topic | Rendimiento | Orden garantizado | Duplicados | Uso recomendado |
| --------------------- | ----------------------- | -------------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| **Standard** | Muy alto (gran volumen de mensajes/segundo) | No | Posible (entrega **at-least-once**) | Aplicaciones donde el orden de los mensajes no es crítico. |
| **FIFO** | Hasta 300 transacciones/segundo | Sí — orden exacto de publicación | No (entrega **exactly-once**, deduplicación incorporada) | Flujos donde la secuencia importa mucho — ej. transacciones financieras. |

> ⚠️ La elección entre Standard y FIFO depende de si el **orden** y la ausencia de **duplicados**
> son críticos (FIFO) o si se prioriza el **rendimiento** (Standard).

## Patrones de mensajería

| Patrón | Descripción |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aplicación a aplicación (A2A)** | SNS se integra con servicios como Lambda, SQS, endpoints HTTP/S, etc. Permite el patrón **fan-out**: emitir un mismo mensaje a múltiples servicios simultáneamente para procesamiento paralelo (por ejemplo, extender notificaciones también a S3 o Redshift para análisis de datos). |
| **Aplicación a persona (A2P)** | Envía notificaciones directamente a personas vía SMS, email o apps móviles. Se puede **filtrar** según criterios específicos, para que los abonados solo reciban las notificaciones relevantes. |

## Formas de publicar mensajes

| Método | Descripción |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Publish (a un topic)** | Envía un mensaje a un topic; todos los abonados vinculados a ese topic lo reciben automáticamente. Útil para comunicar el mismo mensaje a varios abonados a la vez. |
| **Direct publish** (envío directo) | Envía el mensaje directamente a un abonado/dispositivo concreto, sin pasar por un topic. Útil para notificaciones personalizadas (ej. push móvil); el mensaje se adapta a cada destinatario y su estructura se define en **JSON**. |

> El método a elegir depende de si la comunicación va dirigida a **un individuo** concreto (direct
> publish) o a **una audiencia amplia** (publish a un topic).
