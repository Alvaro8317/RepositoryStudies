# Aplicaciones de desacoplamiento

## Visibilidad de mensajes en SQS y su impacto en la competencia entre consumidores

Cuando múltiples consumidores están leyendo mensajes desde una cola de Amazon SQS (Simple Queue Service), existe una mecánica esencial que regula cómo se reservan temporalmente esos mensajes para evitar colisiones o procesamientos duplicados: el **tiempo de espera de visibilidad** (_Visibility Timeout_).

### ¿Cómo funciona?

- Cuando un consumidor lee (sondea) un mensaje de la cola, **ese mensaje se vuelve invisible para los demás consumidores** durante un periodo definido: el **visibility timeout**.
- Por defecto, este tiempo es de **30 segundos**, pero puede ajustarse desde **0 segundos hasta 12 horas** dependiendo de la necesidad.

### ¿Qué pasa si no se procesa a tiempo?

- Si **el consumidor no elimina el mensaje antes de que el tiempo expire**, el mensaje se **vuelve visible nuevamente** y **otro consumidor puede leerlo y procesarlo**, provocando un **reprocesamiento o duplicado**.
- Esto **no garantiza exclusividad de procesamiento**, por lo que **las aplicaciones deben ser idempotentes** (es decir, procesar el mismo mensaje más de una vez no debe causar efectos secundarios no deseados).

### Ejemplo ilustrativo (con plastilina mental)

Imagina que tienes una bandeja de cartas (la cola SQS) y varios niños curiosos (consumidores) que pueden leer una carta para jugar con ella:

- Cuando un niño toma una carta (mensaje), se la guarda por 30 segundos. Durante ese tiempo, **nadie más puede verla**.
- Si el niño no termina de jugar con ella y **no la guarda en una caja (delete)** dentro de ese tiempo, la carta regresa a la bandeja y **otro niño puede tomarla**.
- Si un niño se distrae o se queda dormido, la carta tarda más en volver, y se **retrasan todos los demás**.

### Problemas comunes y cómo mitigarlos

| Problema                        | Causa                                   | Solución                                                                 |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| Mensajes duplicados             | Timeout muy corto y procesamiento lento | Aumentar el visibility timeout dinámicamente                             |
| Procesamiento lento o bloqueado | Timeout alto y consumidor colgado       | Usar _heartbeat_, monitoreo o reducir timeout con retries                |
| Trabajo perdido                 | El consumidor falla y no se reintenta   | Configurar un DLQ (Dead Letter Queue) para aislar mensajes problemáticos |

### Ejemplo con código (usando SDK de AWS en Python con Boto3)

```python
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/mi-cola'

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    VisibilityTimeout=45,  # override temporal al default
    WaitTimeSeconds=10
)

for message in response.get('Messages', []):
    print(f"Procesando: {message['Body']}")
    # Después de procesar
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
```

### Meme sugerido (para ilustrar conceptos en la clase)

**Nombre del meme**: _"Dog in burning room – This is fine"_

**Uso**: Mostrar cómo un sistema con visibility timeout muy alto y consumidores colgados sigue esperando como si nada, mientras los mensajes se acumulan en la cola.

## Long Polling en SQS para optimizar la eficiencia del consumo de mensajes

Cuando un consumidor intenta recibir mensajes de una cola en Amazon SQS, puede usar **Short Polling** o **Long Polling** para hacerlo. El **Long Polling** es la opción más eficiente, y deberías conocerla bien porque es pregunta fija de examen SAA.

### ¿Qué es el Long Polling?

Es una técnica en la que el consumidor le dice a SQS:
**"Ey, si no tienes mensajes ahora, espera un rato antes de responderme."**

Esto reduce las llamadas vacías (sin mensajes) y, por tanto, disminuye:

- Costos por llamadas a la API.
- Carga innecesaria en la red o en tus lambdas/eventos.

### Comparativa rápida

| Característica          | Short Polling           | Long Polling                         |
| ----------------------- | ----------------------- | ------------------------------------ |
| Tiempo de espera        | 0 segundos              | Entre 1 y 20 segundos                |
| ¿Devuelve siempre algo? | Sí, aunque esté vacío   | No, si no hay mensajes en el timeout |
| Uso de recursos         | Alto                    | Bajo                                 |
| Nivel de activación     | Solo vía API            | API o configuración de la cola       |
| ¿Recomendado?           | No (excepto casos edge) | Sí, por defecto                      |

### ¿Cómo se activa?

- **A nivel de cola**: puedes configurar que **todas las peticiones de receive_message usen long polling por defecto** (ideal si tienes varios consumidores o una integración fija).
- **A nivel de API**: usando el parámetro `WaitTimeSeconds` al hacer la llamada `receive_message`.

### Ejemplo con Python (Boto3)

```python
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/mi-cola'

# Long polling activado por 15 segundos
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=15
)

for message in response.get('Messages', []):
    print(f"Llegó mensaje: {message['Body']}")
```

### ¿Por qué es tan importante?

Porque si usas **Short Polling** en colas que rara vez tienen mensajes (como las triggeradas por eventos), **terminas llamando a la API como loco para recibir... nada.** Literalmente estás pagando por recibir aire.

### Analogía tipo plastilina

**Short Polling**: Es como si cada 2 segundos abrieras la nevera para ver si mágicamente apareció una pizza.
**Long Polling**: Le dices a tu mamá: “Avísame cuando llegue la pizza”, y mientras tanto haces otra cosa útil.

### Meme sugerido

**Nombre del meme**: _"Waiting Skeleton"_

**Uso**: Mostrar al consumidor con short polling esperando a que llegue un mensaje que nunca llega, mientras gasta recursos en cada intento. Ideal para reforzar por qué el long polling es _mejor en casi todos los casos_.

## Integración de Amazon SQS con Auto Scaling Group para procesar cargas variables

Amazon SQS (Simple Queue Service) puede integrarse eficazmente con un Auto Scaling Group (ASG) para manejar cargas de trabajo variables y desacoplar componentes de una arquitectura distribuida.

### Uso de métricas de CloudWatch para escalar instancias EC2

Es posible configurar una cola SQS para que sirva como fuente de eventos que desencadenen el escalado de instancias EC2 dentro de un ASG. Amazon CloudWatch puede monitorear la métrica `ApproximateNumberOfMessagesVisible`, que representa la cantidad de mensajes en la cola que aún no han sido procesados. Cuando esta métrica supera un umbral predefinido, se activa una alarma (`CloudWatch Alarm`) que incrementa el número de instancias EC2 en el ASG.

Esto permite que el sistema escale automáticamente en función del volumen de trabajo en la cola.

**Ejemplo**:

- Si tienes una aplicación de procesamiento de imágenes y la cola SQS acumula muchos mensajes (cada uno representando una imagen por procesar), la métrica en CloudWatch lo detecta y dispara una alarma.
- El ASG lanza nuevas instancias EC2 para que más consumidores estén disponibles y vacíen la cola más rápidamente.

### Prevención de pérdida de transacciones en flujos de alta carga

En escenarios donde la carga de trabajo es muy alta, puede haber riesgo de pérdida de transacciones si las instancias EC2 no escalan a tiempo o si el sistema de procesamiento se satura.

**Solución**: Utilizar SQS como _búfer de escritura_ hacia una base de datos. De esta manera:

- Las instancias EC2 reciben las transacciones, las colocan en una cola SQS (infinitamente escalable).
- Un grupo de consumidores (por ejemplo, procesos en EC2 o containers en ECS) extrae los mensajes de la cola y los escribe en la base de datos de forma controlada.

Esto permite absorber picos de carga sin perder datos, ya que SQS garantiza la entrega (al menos una vez) de los mensajes.

### Desacoplamiento entre frontend y backend con SQS

SQS es ideal para desacoplar componentes, como el frontend y el backend de una aplicación.

**Ejemplo práctico**:

1. Un usuario envía un formulario en una aplicación web (frontend).
2. El frontend no realiza una operación sincrónica con el backend. En lugar de eso, envía un mensaje JSON a una cola SQS con los datos del formulario.
3. El backend, completamente desacoplado, consume los mensajes de la cola SQS y procesa la información (ej. enviar un correo, guardar en una base de datos, generar una factura).

**Ventajas**:

- El frontend no depende del tiempo de respuesta del backend.
- El backend puede fallar temporalmente o escalar independientemente.
- Se puede controlar el ritmo de procesamiento (throttling) sin perder solicitudes.

**Código JSON ejemplo del mensaje enviado por el frontend**:

```json
{
  "nombre": "Alvaro",
  "email": "alvaro@example.com",
  "mensaje": "Hola, quiero información del producto X"
}
```

**Backend (consumidor)**:
Una función Lambda o un worker en EC2 consume el mensaje, valida y guarda los datos en DynamoDB o RDS, y envía un correo de respuesta.

## Servicios de Amazon Kinesis para procesamiento en tiempo real de flujos de datos

Amazon Kinesis es una plataforma completamente administrada que permite recopilar, procesar y analizar datos en tiempo real, facilitando la toma de decisiones inmediata basada en eventos. Es ideal para aplicaciones que requieren análisis de datos de flujo continuo, como monitoreo, detección de fraudes, análisis de comportamiento del usuario y más.

### Casos de uso comunes para la ingesta de datos

Amazon Kinesis permite la ingesta de datos desde múltiples fuentes, incluyendo:

- Registros de aplicaciones (logs)
- Métricas de infraestructura y aplicaciones
- Secuencias de clics en sitios web (clickstreams)
- Dispositivos IoT (sensores, cámaras, etc.)
- Redes sociales, eventos de juegos online, logs de seguridad

### Componentes principales de Kinesis

#### Kinesis Data Streams (KDS)

- Servicio para la recopilación y procesamiento de flujos de datos personalizados.
- Los datos se dividen en _shards_ (fragmentos) que permiten la lectura paralela.
- Los consumidores pueden leer los datos con una latencia de milisegundos.
- Se puede integrar con AWS Lambda, Kinesis Client Library (KCL), o aplicaciones personalizadas en EC2.
- Los datos se almacenan por defecto durante 24 horas (extensible hasta 7 días).

**Ejemplo**: Una aplicación que registra los movimientos de los usuarios en una web de e-commerce envía estos eventos a Kinesis Data Streams. Una función Lambda procesa cada evento para alimentar en tiempo real una tabla de recomendaciones.

#### Kinesis Data Firehose

- Servicio de entrega automática de flujos de datos a destinos como Amazon S3, Redshift, OpenSearch o un endpoint HTTP.
- No requiere administrar shards ni consumidores, es completamente administrado.
- Admite transformación de datos en vuelo mediante funciones Lambda.
- Ideal para almacenamiento, archivado y análisis posterior.

**Ejemplo**: Enviar los logs de acceso de una aplicación web directamente a Amazon S3 para su análisis con Amazon Athena o Redshift.

#### Kinesis Data Analytics

- Servicio para consultar y procesar flujos de datos en tiempo real usando SQL.
- Permite aplicar ventanas de tiempo, agregaciones, filtros, joins y más sin necesidad de escribir código Java o Python.
- Se puede conectar directamente a Data Streams o Firehose como fuente.

**Ejemplo**: Calcular el promedio móvil de temperatura de sensores IoT cada 5 minutos, y emitir alertas si supera un umbral.

#### Kinesis Video Streams

- Servicio especializado para la ingesta, almacenamiento y análisis de video en tiempo real.
- Compatible con flujos de video en vivo de cámaras, drones, dispositivos IoT, etc.
- Los datos pueden ser consumidos por aplicaciones de procesamiento de imágenes o machine learning (ej. detección de objetos con Rekognition).

**Ejemplo**: Un sistema de videovigilancia que transmite video desde cámaras IP a Kinesis Video Streams y usa Amazon Rekognition para detectar movimiento o caras.

### Comparación general de los componentes

| Servicio       | Enfoque principal                          | Latencia     | Destinos compatibles                        | Administración |
| -------------- | ------------------------------------------ | ------------ | ------------------------------------------- | -------------- |
| Data Streams   | Procesamiento personalizado                | Milisegundos | Lambda, EC2, KCL                            | Parcial        |
| Data Firehose  | Entrega automática a destinos              | \~1 minuto   | S3, Redshift, OpenSearch, HTTP              | Total          |
| Data Analytics | Procesamiento con SQL                      | Segundos     | Streams, Firehose                           | Total          |
| Video Streams  | Ingesta y análisis de video en tiempo real | Varía        | ML, almacenamiento, procesamiento de frames | Total          |

## Arquitectura y funcionamiento de Amazon Kinesis Data Firehose (KDF) para entrega de datos en tiempo casi real

Amazon Kinesis Data Firehose (KDF) es un servicio completamente gestionado que permite capturar, transformar y entregar flujos de datos casi en tiempo real a destinos como almacenamiento, análisis o monitoreo.

### Flujo general de datos en Kinesis Data Firehose

#### Productores

KDF puede recibir datos desde múltiples fuentes:

- Aplicaciones personalizadas mediante AWS SDK
- AWS IoT
- Amazon Kinesis Data Streams (KDS)
- Agentes como Kinesis Agent o herramientas externas (Fluent Bit, Fluentd)

#### Transformación de datos

- Puede integrar una **función AWS Lambda** para transformar los datos antes de ser entregados
- Permite **conversión automática** a formatos como JSON, Parquet o ORC
- Soporta compresión (GZIP, Snappy, ZIP) y cifrado antes del almacenamiento

#### Entrega a destinos

- **Amazon S3**
- **Amazon Redshift**
- **Amazon OpenSearch Service (antes Elasticsearch)**
- **Destinos personalizados mediante HTTP**
- **Herramientas de monitoreo**: Datadog, Splunk, New Relic, MongoDB

Todos los datos, incluidos los **registros fallidos**, pueden ser enviados a un bucket de S3 como respaldo.

#### Características adicionales

- **Escritura por lotes**: latencia mínima de **60 segundos** o **1 MB** de datos acumulados
- **Escalado automático** sin configuración de shards
- **No se almacenan datos** en Firehose, la entrega es directa al destino
- **Pago por volumen de datos procesados**
- **Formato flexible** y soporte para transformación y compresión

---

## Comparación entre Kinesis Data Streams (KDS) y Kinesis Data Firehose (KDF)

| Característica                  | Kinesis Data Streams (KDS)                                     | Kinesis Data Firehose (KDF)                              |
| ------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------- |
| Tipo de servicio                | Plataforma de streaming personalizada                          | Servicio de entrega de datos totalmente gestionado       |
| Codificación                    | Requiere código personalizado para producción y consumo        | No requiere programación para entrega básica             |
| Latencia                        | En tiempo real (milisegundos)                                  | Casi en tiempo real (mínimo 60 segundos o 1 MB de datos) |
| Almacenamiento de datos         | Hasta 365 días                                                 | No almacena datos                                        |
| Escalado                        | Manual (modo aprovisionado) o automático (modo bajo demanda)   | Escalado automático                                      |
| Destinos de entrega             | Requiere consumidores personalizados o Firehose                | S3, Redshift, OpenSearch, Datadog, Splunk, HTTP, etc.    |
| Transformación de datos         | Con código propio o funciones intermedias                      | Integración con Lambda para transformación en vuelo      |
| Reintentos y registros fallidos | El consumidor debe manejarlos                                  | Automáticamente almacenados en S3 como fallback          |
| Soporte de repetición (replay)  | Sí, mediante secuencia y duración de retención                 | No, datos no pueden reproducirse                         |
| Pago                            | Por shard y volumen de datos                                   | Por volumen de datos entregados                          |
| Gestión del servicio            | Parcialmente gestionado (se gestiona capacidad y consumidores) | Totalmente gestionado y sin servidor                     |

---

**Resumen**:

- **KDS** es ideal para **procesamiento personalizado en tiempo real** con control sobre la lógica, la retención y la secuencia.
- **KDF** es ideal para **entrega simple, automática y escalable** de datos a sistemas de análisis o almacenamiento sin preocuparse por la infraestructura.

## Comparación entre Amazon SQS y Amazon Kinesis Data Streams (KDS)

Amazon SQS y Kinesis Data Streams son servicios de colas/mensajería que permiten desacoplar aplicaciones distribuidas, pero están diseñados para diferentes tipos de cargas, casos de uso y patrones de procesamiento.

| Característica                   | **Amazon SQS**                                                  | **Amazon Kinesis Data Streams (KDS)**                    |
| -------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| Tipo de servicio                 | Cola de mensajes (message queue)                                | Plataforma de streaming de datos                         |
| Modelo de mensajes               | Mensajes individuales con estructura simple (JSON, texto)       | Registros de datos estructurados para análisis/streaming |
| Orden garantizado                | Solo en FIFO queues                                             | Sí, para la misma clave de partición                     |
| Procesamiento                    | Pull-based: los consumidores extraen los mensajes               | Pull-based o push con Lambda                             |
| Retención de datos               | Máx. 14 días                                                    | Entre 1 y 365 días                                       |
| Capacidad de repetición (replay) | No (solo reintentos limitados)                                  | Sí, permite reprocesar desde un punto específico         |
| Escalabilidad                    | Automática (sin límite de throughput)                           | Modo aprovisionado (shards) o bajo demanda               |
| Latencia                         | Baja (milisegundos)                                             | Muy baja (milisegundos)                                  |
| Tamaño máximo de mensaje         | 256 KB                                                          | 1 MB por registro                                        |
| Orden en la entrega              | No garantizado en Standard, garantizado en FIFO                 | Garantizado por partición                                |
| Entrega de mensajes              | Al menos una vez (FIFO admite exactamente una vez)              | Al menos una vez                                         |
| Número de consumidores           | Escalable, pero cada consumidor procesa individualmente         | Múltiples consumidores pueden leer del mismo stream      |
| Casos de uso comunes             | Tareas asincrónicas, procesamiento en segundo plano, colas FIFO | Streaming en tiempo real, análisis de eventos, logs, IoT |
| Integración con otros servicios  | Lambda, ECS, SQS DLQ, Step Functions, etc.                      | Lambda, Firehose, Analytics, KCL, SDK                    |
| Seguridad                        | IAM, cifrado con KMS, VPC endpoints                             | IAM, cifrado con KMS, VPC endpoints                      |
| Costo                            | Basado en número de solicitudes y almacenamiento                | Basado en shards y volumen de datos                      |

---

### ¿Cuándo usar SQS?

- Procesos asincrónicos simples
- Comunicación entre microservicios desacoplada
- Procesamiento eventual con control de errores
- Uso de FIFO para mantener el orden (ej. transacciones bancarias)

**Ejemplo**: El frontend de una aplicación envía solicitudes de procesamiento a una cola FIFO y un backend con Lambda las atiende en orden.

---

### ¿Cuándo usar Kinesis Data Streams?

- Análisis de datos en **tiempo real**
- Casos de uso de **Big Data** o **IoT**
- Procesamiento **de eventos secuenciales** con múltiples consumidores simultáneos
- Necesidad de mantener una **ventana de retención larga** o **reprocesar eventos**

**Ejemplo**: Una empresa de videojuegos transmite en tiempo real los eventos de los jugadores (movimientos, compras, logros) a Kinesis, donde varias aplicaciones procesan esos datos para analítica, monitoreo en vivo y recomendaciones.

## Comparación entre Amazon SQS, SNS y Kinesis

Estos tres servicios permiten desacoplar componentes dentro de arquitecturas distribuidas, pero tienen propósitos, patrones y comportamientos distintos.

| Característica                           | **Amazon SQS**                                         | **Amazon SNS**                                   | **Amazon Kinesis Data Streams**                         |
| ---------------------------------------- | ------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------- |
| Modelo de comunicación                   | Cola de mensajes (punto a punto)                       | Publicación-suscripción (pub/sub)                | Streaming de datos en tiempo real                       |
| Tipo de flujo                            | Pull (los consumidores extraen los mensajes)           | Push (envía a los suscriptores automáticamente)  | Pull o push con Lambda                                  |
| Entrega                                  | A cada consumidor que lee de la cola                   | A todos los suscriptores del tema                | Múltiples consumidores pueden leer del stream           |
| Persistencia de mensajes                 | Sí, hasta 14 días                                      | No, los mensajes no se conservan                 | Sí, de 1 a 365 días (modo aprovisionado o bajo demanda) |
| Repetición de mensajes                   | No (una vez leídos y borrados, no se recuperan)        | No (solo notificación inmediata)                 | Sí, mediante secuencias y timestamps                    |
| Garantía de orden                        | Solo con FIFO queues                                   | No                                               | Sí, por clave de partición dentro del shard             |
| Escalado                                 | Automático, sin aprovisionar rendimiento               | Automático, sin aprovisionar rendimiento         | Manual (shards) o automático (modo bajo demanda)        |
| Fan-out (entrega a múltiples receptores) | Sí, con múltiples consumidores                         | Sí, nativo (hasta 12.5 millones de suscriptores) | Sí, fan-out reforzado con múltiples consumidores        |
| Número de destinatarios por mensaje      | Uno o varios (dependiendo del número de consumidores)  | Todos los suscriptores                           | Todos los consumidores simultáneamente                  |
| Soporte FIFO                             | Sí, en colas FIFO                                      | No directamente (solo a través de SQS FIFO)      | Sí, a nivel de partición                                |
| Casos de uso principales                 | Tareas asincrónicas, desacoplamiento, trabajos en cola | Notificaciones push, broadcast de eventos        | Big data, análisis de eventos, ETL, IoT, logs           |
| Tamaño máximo por mensaje                | 256 KB                                                 | 256 KB                                           | 1 MB por registro                                       |
| Retardo configurable (delay)             | Sí (individual o por cola)                             | No                                               | No                                                      |
| Integración común                        | Lambda, ECS, S3, Step Functions, SNS                   | SQS, Lambda, HTTP, email, SMS, mobile push       | Lambda, Firehose, Analytics, Glue, Redshift, S3         |
| Precio                                   | Por número de solicitudes y retención                  | Por número de publicaciones y tipo de destino    | Por número de shards y volumen de datos procesados      |

---

### Casos prácticos de uso

- **SQS**: procesamiento desacoplado de tareas asincrónicas, sistemas en los que se quiere controlar el ritmo del procesamiento, colas FIFO para garantizar orden.

  **Ejemplo**: un backend genera tareas que son consumidas por workers en segundo plano (ej. procesamiento de imágenes).

- **SNS**: notificaciones en tiempo real, envío de eventos a múltiples servicios o usuarios, arquitectura tipo fan-out con integración simple.

  **Ejemplo**: un sistema de facturación publica un evento a SNS cuando una factura está lista; SNS reenvía esa notificación a una Lambda, a un webhook externo y a una cola SQS FIFO para procesamiento posterior.

- **Kinesis**: ingestión de grandes volúmenes de datos en tiempo real, análisis en vivo, procesamiento de flujos de eventos complejos o de IoT.

  **Ejemplo**: una aplicación de telemetría de flotas de camiones transmite posición GPS, temperatura y velocidad continuamente a un stream de Kinesis para análisis, alertas y archivado.

## Amazon MQ frente a SQS y SNS en entornos de mensajería en AWS

Amazon MQ es un servicio de mensajería administrado que facilita la migración de aplicaciones existentes basadas en **protocolos estándar** hacia AWS, mientras que **SQS y SNS** son servicios nativos de AWS diseñados para arquitecturas modernas en la nube.

---

### Compatibilidad con protocolos de mensajería

| Servicio      | Protocolos compatibles                        |
| ------------- | --------------------------------------------- |
| **Amazon MQ** | MQTT, AMQP, STOMP, OpenWire, WSS              |
| **SQS**       | Solo API AWS (AWS SDK, CLI, HTTP)             |
| **SNS**       | Solo API AWS (AWS SDK, CLI, HTTP, SMS, Email) |

Amazon MQ es ideal cuando necesitas soporte para **protocolos de mensajería tradicionales** utilizados en sistemas on-premises o aplicaciones legadas.

---

### Amazon MQ: funcionamiento y arquitectura

- Compatible con **Apache ActiveMQ** y **RabbitMQ**
- Utiliza una arquitectura basada en **brokers** (intermediarios de mensajes)
- Proporciona características de:

  - **Cola** (punto a punto)
  - **Tema** (publicación-suscripción)

- Incluye soporte para **retención de mensajes**, **garantía de entrega**, **ordenación**, y **transacciones**
- Integración con IAM, Amazon CloudWatch, KMS y VPC

---

### Alta disponibilidad con Multi-AZ

Amazon MQ puede desplegarse con replicación activa/pasiva en múltiples zonas de disponibilidad:

**Ejemplo de configuración Multi-AZ:**

- Un **broker activo** se ejecuta en **AZ1**
- Un **broker en espera** (standby) se ejecuta en **AZ2**
- Los mensajes y configuraciones se almacenan en **Amazon EFS**, montado en ambos brokers
- Si AZ1 falla, se produce una **conmutación por error automática** hacia AZ2, que reinicia el broker de respaldo con el mismo estado

---

### Comparación con SQS y SNS

| Característica           | **Amazon MQ**                                 | **Amazon SQS**                                    | **Amazon SNS**                                |
| ------------------------ | --------------------------------------------- | ------------------------------------------------- | --------------------------------------------- |
| Tipo de servicio         | Broker administrado (ActiveMQ o RabbitMQ)     | Cola de mensajes totalmente gestionada            | Publicación-suscripción totalmente gestionado |
| Protocolos compatibles   | MQTT, AMQP, STOMP, OpenWire, WSS              | Solo API AWS                                      | Solo API AWS                                  |
| Arquitectura             | Basado en broker con estado                   | Serverless sin estado                             | Serverless sin estado                         |
| Escalado automático      | No, escalado limitado                         | Sí                                                | Sí                                            |
| Retención de mensajes    | Sí (configurable, depende del broker)         | Sí, hasta 14 días                                 | No (entrega inmediata)                        |
| Orden de mensajes        | Sí                                            | Solo en colas FIFO                                | No, excepto vía SQS FIFO                      |
| Persistencia             | Sí, mediante almacenamiento (EFS)             | Sí (controlado por visibilidad y borrado)         | No                                            |
| Tolerancia a fallos      | Sí, con Multi-AZ y failover                   | Alta disponibilidad nativa                        | Alta disponibilidad nativa                    |
| Casos de uso típicos     | Migración de apps que usan RabbitMQ/ActiveMQ  | Procesamiento asincrónico, trabajos en background | Notificaciones y arquitectura fan-out         |
| Administración necesaria | Sí (configuración del broker, monitoreo)      | No                                                | No                                            |
| Pago                     | Por hora de broker + almacenamiento + tráfico | Por solicitudes y almacenamiento                  | Por publicaciones y tipo de destinatarios     |

---

### Conclusión orientada a migración

- Si tu sistema actual ya usa **RabbitMQ, ActiveMQ** o protocolos como **AMQP**, **MQTT** o **STOMP**, **Amazon MQ** es la opción más directa para migrar con cambios mínimos.
- Si estás diseñando una arquitectura nativa en la nube, altamente escalable y sin administración, **SQS y SNS** son más adecuados.

## Problema de duplicación en consumidores de Amazon SQS: solución mediante ajuste del tiempo de visibilidad

Cuando múltiples consumidores reciben los **mismos mensajes** de una cola SQS y los procesan más de una vez, es probable que el **tiempo de espera de visibilidad** sea **menor que el tiempo de procesamiento**.

---

### ¿Qué es el tiempo de visibilidad (_Visibility Timeout_)?

Es el período durante el cual un mensaje, una vez leído por un consumidor, **queda oculto** para otros consumidores. Si el consumidor **no elimina** el mensaje antes de que expire este tiempo, el mensaje se vuelve visible de nuevo en la cola y **otro consumidor puede procesarlo**, causando **duplicación**.

---

### Escenario

- Cada consumidor recupera **10 mensajes**
- Cada mensaje se procesa en **1 minuto**
- El tiempo de visibilidad es menor a **60 segundos**

**Resultado**: El mensaje vuelve a estar disponible antes de ser eliminado, por lo que **otro consumidor lo recibe** y lo procesa de nuevo.

---

### Solución

**Aumentar el tiempo de visibilidad (`Visibility Timeout`)** a un valor **mayor que el tiempo de procesamiento real** de los mensajes.

#### Cómo hacerlo

- Desde la consola de Amazon SQS:

  - Ir a la cola → Configuración → _Visibility timeout_
  - Establecer un valor como **70 o 90 segundos**

- También se puede ajustar de forma dinámica por mensaje mediante la API:

  ```bash
  aws sqs change-message-visibility --queue-url <queue-url> --receipt-handle <handle> --visibility-timeout 90
  ```

---

### Consideraciones adicionales

- **No lo pongas excesivamente alto**: si el consumidor falla, el mensaje tardará más en ser reprocesado.
- **Utiliza la extensión dinámica del timeout** si el tiempo de procesamiento varía. Esto se puede hacer con:

  - AWS SDK (`ChangeMessageVisibility`)
  - [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html) para evitar mensajes vacíos y mejorar eficiencia

---

### Alternativas o complementos

- **SQS FIFO**: si el orden y la entrega única son críticos, puedes usar colas FIFO con `MessageGroupId`
- **Dead Letter Queue (DLQ)**: para capturar mensajes que fallan repetidamente

---

### Resumen

| Problema                                        | Solución recomendada                          |
| ----------------------------------------------- | --------------------------------------------- |
| Mensajes son leídos múltiples veces             | Aumentar el `Visibility Timeout`              |
| Tiempo de procesamiento > tiempo de visibilidad | Igualar o superar con el timeout adecuado     |
| Tiempo de procesamiento variable                | Ajustar visibilidad dinámicamente por mensaje |
