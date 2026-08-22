# Amazon SQS (Simple Queue Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon SQS** es un servicio de **cola de mensajes** gestionado: almacena mensajes temporalmente
mientras se mueven entre distintas aplicaciones o microservicios, de forma **fiable** y
**escalable**.

- Habilita el **procesamiento asíncrono**: distintas partes del sistema pueden funcionar de forma
  independiente.
- Útil para **sistemas distribuidos**, **microservicios** y **aplicaciones serverless**.

## Cómo funciona

- Los **productores** envían mensajes a la cola; los **consumidores** los recuperan y procesan.
- Los mensajes **no** se almacenan en un único servidor: se guardan de forma **redundante** en
  varios servidores dentro de SQS, lo que aporta **durabilidad** y **disponibilidad** — los
  mensajes siguen siendo accesibles aunque algún servidor sufra downtime.

### El papel del consumidor: borrado de mensajes

- Es responsabilidad del **consumidor** borrar el mensaje de la cola tras procesarlo, marcándolo
  como gestionado.
- Si el mensaje no se borra a tiempo (por un error del proceso o un fallo del sistema), vuelve a
  hacerse **visible** en la cola una vez expira el **tiempo de espera de visibilidad**
  (*visibility timeout*), lo que puede provocar que se reintente su procesamiento.

> ⚠️ El borrado de mensajes tras su procesamiento es clave para la integridad del sistema — un
> mensaje no borrado a tiempo puede procesarse más de una vez.

## Tipos de cola

| Tipo | Rendimiento | Orden garantizado | Duplicados |
| ------------- | -------------------------------------------------------------- | -------------------- | -------------------------------------- |
| **Standard** | Muy alto (gran número de transacciones/segundo) | No — best effort, pero no garantizado | Posibles (entrega **at-least-once**) |
| **FIFO** | Hasta 300 mensajes/segundo (con batching), hasta 3000 sin batching | Sí — orden exacto | No (entrega **exactly-once**) |

- **Standard**: adecuada cuando se necesita procesamiento muy rápido y alto rendimiento, y se puede
  tolerar que los mensajes lleguen desordenados o duplicados.
- **FIFO**: adecuada cuando el orden estricto y la ausencia de duplicados son importantes, a costa
  de menor rendimiento.

## SQS vs. Kinesis Data Streams

| Aspecto | SQS | Kinesis Data Streams |
| ------------------------ | -------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Propósito principal | **Mensajería**: desacoplar componentes de la aplicación para que funcionen de forma independiente (escalabilidad y tolerancia a fallos). | **Streaming de datos en tiempo real** a gran escala: ingesta de datos, procesamiento inmediato. |
| Retención de datos | Hasta **14 días**. | Por defecto **24 horas**, configurable hasta **365 días**. |
| Escalado | Automático, según el volumen de mensajes — sin gestión manual. | Orden de registros garantizado **dentro de un shard**, no entre shards; entrega **at-least-once**. |

> En resumen: **SQS** es para la **gestión de mensajes** entre componentes; **Kinesis Data
> Streams** es para el **procesamiento e ingesta de flujos de datos** en tiempo real.
