# Amazon MSK (Managed Streaming for Apache Kafka)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es?

**Amazon MSK** es la versión **totalmente gestionada** de **Apache Kafka** en AWS. Igual que Kinesis
Data Streams, permite construir aplicaciones de streaming con productores y consumidores, pero
basadas en el ecosistema y las herramientas de **Kafka** en lugar del modelo propio de Kinesis.

## Durabilidad y disponibilidad

Los mensajes se replican automáticamente entre los distintos **brokers** del clúster y entre
diferentes **zonas de disponibilidad (Availability Zones)**. Esto aporta:

- **Protección frente a pérdida de datos** — el mismo mensaje vive en varias copias.
- **Alta disponibilidad y durabilidad**.
- **Recuperación rápida** ante fallos de un broker o de una zona de disponibilidad, sin interrumpir
  el flujo de datos.

## Configuración y límites

Una de las diferencias clave frente a Kinesis Data Streams es la **flexibilidad de configuración**:

| Aspecto | Kinesis Data Streams | Amazon MSK |
| ------- | --------------------- | ----------- |
| Tamaño máximo de mensaje | **1 MB** (fijo) | Configurable, hasta **10 MB** |
| Nivel de personalización | Bajo — experiencia gestionada y sencilla | Alto — control granular sobre la configuración del clúster Kafka |

Esta mayor flexibilidad permite manejar mensajes más grandes y afinar otros parámetros del clúster
para optimizar el rendimiento según las necesidades específicas de la aplicación.

## Productores y consumidores

El modelo es el mismo concepto que en Kinesis:

- **Productores** — las fuentes del flujo de datos (aplicaciones, sensores, etc.) que envían datos a
  MSK.
- **Consumidores** — las aplicaciones o endpoints que leen y procesan esos datos.

MSK facilita que los datos fluyan de productores a consumidores para habilitar procesamiento en
tiempo real.

## Kinesis Data Streams vs. Amazon MSK

### Personalización vs. comodidad

- **Kinesis** — configuración más sencilla, experiencia más gestionada; ideal cuando no se necesita
  un ajuste fino de la configuración.
- **MSK** — control granular más fino, permite optimizaciones más complejas; preferible en escenarios
  más intrincados (ej. mensajes grandes, tuning de rendimiento específico).

### Organización de los datos

| | Kinesis Data Streams | Amazon MSK (Kafka) |
| --- | --------------------- | -------------------- |
| Unidad de organización | **Streams** divididos en **shards** | **Topics** divididos en **partitions** |
| Escalado | Se pueden **dividir (split) o fusionar (merge)** shards según necesidad | Escalar implica **añadir particiones** |

> ⚠️ En Kafka/MSK, una vez añadidas particiones a un topic **no se pueden eliminar**. Esto hace la
> organización más rígida que en Kinesis (donde los shards sí se pueden fusionar) y requiere más
> gestión.

### Control de acceso

**Cifrado en tránsito** — similar en ambos servicios:

- Ambos soportan **cifrado TLS** en tránsito.
- Ambos soportan **cifrado KMS**.
- MSK además permite la opción de **texto sin formato (plaintext)**, es decir, sin cifrado.

**Autenticación y autorización** — aquí sí difieren bastante:

- **Kinesis** — modelo simplificado: usa **políticas de IAM** tanto para autenticación como para
  autorización.
- **MSK** — ofrece **tres modelos** distintos:
  1. **TLS mutuo (mutual TLS)** para autenticación, combinado con **Kafka ACLs** para autorización a
     nivel de topic.
  2. **Usuario/contraseña (SASL/SCRAM)** para autenticación, también apoyado en **Kafka ACLs**.
  3. **Control de acceso vía IAM** — autenticación y autorización integradas con IAM, aprovechando el
     ecosistema de AWS de forma más simplificada.

## ¿Cuándo usar cada uno?

- **Kinesis Data Streams** — cuando se prioriza una configuración y gestión más sencillas, y los
  mensajes están dentro del límite de **1 MB**. Es la opción más fácil de usar e integrar.
- **Amazon MSK** — cuando se necesita un control más detallado de la configuración del clúster, o los
  mensajes superan el límite de 1 MB de Kinesis. Aporta más flexibilidad, a costa de mayor
  complejidad y gestión.
