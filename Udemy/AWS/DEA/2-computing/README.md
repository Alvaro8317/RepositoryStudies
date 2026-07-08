# EC2 para Big Data y Procesadores Graviton

## Instancias EC2 en el sector del Big Data

Las instancias EC2 permiten **escalar recursos de cómputo de forma elástica** según la demanda de procesamiento de Big Data. En función del tipo de carga de trabajo, se recomienda usar un tipo de instancia u otro.

### 1. Instancias Spot

- **Ideales para tareas que toleran interrupciones.**
- Su precio depende del mercado, por lo que **pueden ser retiradas en cualquier momento**.
- Ofrecen el **coste económico más bajo** de las tres modalidades.
- **Caso de uso recomendado:** procesos con **puntos de control (checkpoints) frecuentes**, como cargas de trabajo de **Machine Learning**.

### 2. Instancias Reservadas

- Recomendadas para **clusters y bases de datos a largo plazo** (ej. una base de datos que sabes que vas a mantener más de un año).
- Ventajas: **estabilidad** y **reducción de costes** mediante grandes descuentos por la reserva.

### 3. Instancias bajo demanda (On-Demand)

- Se utilizan para **cargas de trabajo que no encajan** en los dos casos anteriores (ni tolerantes a interrupciones, ni de uso garantizado a largo plazo).
- Tienen el **precio más elevado** de las tres modalidades.
- Recomendación: siempre que sea posible, buscar alternativas (Spot o Reservadas) para reducir costes.

### Tabla comparativa

| Tipo de instancia | Tolerancia a interrupciones | Duración típica | Coste | Caso de uso Big Data |
|---|---|---|---|---|
| Spot | Alta (pueden interrumpirse) | Corta / variable | Más bajo | Machine Learning con checkpoints |
| Reservada | N/A (estable) | Largo plazo (+1 año) | Reducido por descuento | Clusters y bases de datos permanentes |
| On-Demand | Ninguna especial | Variable / puntual | Más alto | Cargas de trabajo que no encajan en las anteriores |

### Integraciones habituales de EC2 en arquitecturas de Big Data

- **Amazon S3** → almacenamiento
- **Amazon RDS y DynamoDB** → bases de datos
- **Amazon EMR** → procesamiento de datos distribuidos

---

## Procesadores AWS Graviton

**Graviton** es una familia de procesadores diseñada por AWS para ofrecer la mejor relación **precio/rendimiento** en cargas de trabajo que se ejecutan sobre instancias EC2.

### Casos de éxito mencionados

- **Fork Media:** logró reducir costes un **40%** ejecutando bases de datos sobre procesadores Graviton.
- **Datadog:** utilizó Graviton para **ofrecer más valor manteniendo los costes constantes**.

### Tipos de instancias con Graviton

Graviton está disponible en distintas familias de instancias EC2, según el propósito:

- **Propósito general**
- **Optimizadas para cómputo**
- **Optimizadas para memoria**
- **Optimizadas para almacenamiento**
- **Computación acelerada**

### Servicios de ingeniería de datos compatibles con Graviton

- **MSK** (Managed Streaming for Kafka)
- **RDS**
- **MemoryDB**
- **ElastiCache**
- **OpenSearch**
- **EMR**
- **Lambda**
- **Fargate**

### Idea clave

Cuando se busca **alto rendimiento con costes controlados**, los procesadores Graviton suelen ser una **muy buena opción** a considerar en el diseño de la arquitectura, tanto en EC2 como en los servicios de datos que dan soporte a Big Data.

C7, C6 son instancias que están optimizadas para cómputo con los procesadores AWS Graviton, que ofrecen un rendimiento superior al utilizar arquitectura basada en ARM.
