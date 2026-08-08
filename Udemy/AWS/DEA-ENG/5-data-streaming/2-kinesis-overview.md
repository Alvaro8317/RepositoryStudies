# Amazon Kinesis — Visión General

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon Kinesis?

**Amazon Kinesis** no es un único servicio, sino una **colección de servicios** que gestionan
diferentes aspectos del flujo (streaming) de datos: ingesta, entrega y análisis en tiempo real.

## Servicios de la familia Kinesis

### Kinesis Data Streams

- Se encarga de la **ingesta** de datos en streaming.
- Pensado para **grandes volúmenes de datos**, de forma muy **dinámica y escalable**, incluyendo la
  capacidad de absorber **picos** en el flujo de datos.
- Es el primer paso: hay que **capturar** los datos antes de poder ingerirlos.
- Se profundizará en este servicio en la próxima clase.

### Kinesis Firehose

- Servicio **totalmente gestionado (fully managed)**.
- Su función es **entregar** los datos de streaming a diferentes **destinos**, por ejemplo:
  - **Amazon S3**
  - **Amazon Redshift**
- El objetivo es llevar los datos a un lugar de **almacenamiento más permanente**, desde donde luego
  se pueden analizar o procesar de otras formas.

### Managed Apache Flink (antes Kinesis Data Analytics)

- Permite **analizar los datos en tiempo real**.
- Soporta análisis complejos mediante **consultas SQL estándar** sobre datos en streaming.
- Útil siempre que haya un requisito de **análisis complejo en tiempo real**.
- Puede recibir datos tanto desde **Kinesis Data Streams** como desde **Kinesis Firehose**.

> ⚠️ Managed Apache Flink es el **nuevo nombre** de lo que antes se llamaba **Kinesis Data
> Analytics** — es importante reconocer ambos nombres, ya que la documentación y el examen pueden
> referirse al servicio de cualquiera de las dos formas.

## Casos de uso típicos

| Caso de uso                         | Descripción                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Dispositivos IoT**                | Generan datos en tiempo real que se capturan para almacenarlos, procesarlos o analizarlos.                                             |
| **Seguridad / detección de fraude** | Datos muy sensibles al tiempo: se necesita detectar anomalías, problemas de seguridad o transacciones fraudulentas de forma inmediata. |
| **Comportamiento del cliente**      | Por ejemplo, en un sitio web, donde se quiere reaccionar al comportamiento del usuario tan rápido como sea posible.                    |

En general, Amazon Kinesis es la opción a considerar siempre que se necesite realizar **procesamiento
o análisis de datos en tiempo real** mediante streaming.

## Kinesis Data Streams vs colas y otros servicios de eventos

Es fácil confundir Kinesis Data Streams (KDS) con otros servicios de mensajería/eventos de AWS. La
diferencia central es **modelo de cola vs modelo de log**:

- **SQS (cola):** un mensaje se entrega y se **borra** una vez procesado. Pensado para el patrón
  *competing consumers* (varios workers se reparten el trabajo de una misma cola, cada mensaje lo
  procesa uno solo). Sin replay: una vez borrado, desaparece.
- **KDS / Kafka (log distribuido):** los datos se escriben en un **log ordenado y persistente**,
  dividido en particiones (shards en KDS, partitions en Kafka). Los consumidores no borran nada al
  leer, solo avanzan un puntero/offset (checkpointing) — esto permite que **múltiples consumidores
  independientes** lean el mismo dato a su propio ritmo, y es la base de la replayability.

### KDS vs Kafka

Son prácticamente el mismo modelo conceptual (shard ≈ partition), pero con diferencias prácticas:

| Aspecto               | Kinesis Data Streams                     | Kafka (o Amazon MSK)                                   |
| --------------------- | ---------------------------------------- | ------------------------------------------------------ |
| Gestión               | Nativo de AWS, fully/semi-managed        | Open source; MSK lo gestiona parcialmente en AWS       |
| Integración           | Directa con Firehose, Lambda, Flink, IAM | Requiere más configuración/conectores propios          |
| Ecosistema            | Más limitado, atado a AWS                | Muy amplio (Kafka Connect, Kafka Streams, multi-cloud) |
| Portabilidad          | Solo AWS                                 | Portable entre nubes/on-premise                        |
| Complejidad operativa | Menor                                    | Mayor (incluso con MSK)                                |

### KDS y arquitecturas orientadas a eventos (EDA)

KDS puede servir como backbone de una **arquitectura orientada a eventos (EDA)**, en el mismo rol que
cumpliría Kafka. Pero AWS ofrece varios servicios para EDA, cada uno con garantías distintas:

| Servicio AWS    | Modelo                                             | ¿Replay?                 | Uso típico en EDA                                                                            |
| --------------- | -------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------- |
| **SNS**         | Pub/sub, *fire-and-forget*                         | No                       | Notificar a varios suscriptores algo puntual (fan-out simple)                                |
| **EventBridge** | Event bus con reglas de enrutado y schema registry | No (retención muy corta) | Enrutar eventos entre servicios/SaaS según su tipo/contenido                                 |
| **SQS**         | Cola punto a punto                                 | No                       | Desacoplar y repartir trabajo entre workers                                                  |
| **KDS / Kafka** | Log ordenado y particionado                        | **Sí**                   | Streaming de eventos de alto volumen, múltiples consumidores independientes, reprocesamiento |

> ⚠️ Lo que hace a KDS particularmente apto para EDA "serio" es el **log persistente y replayable**:
> permite que distintos servicios consuman el mismo flujo de eventos de forma independiente, sin
> coordinarse entre sí. SNS/EventBridge son más para *enrutar/notificar* eventos puntuales; KDS es más
> para *transmitir* un flujo continuo que varios consumidores necesitan procesar (y potencialmente
> reprocesar).
