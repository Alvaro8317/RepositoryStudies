# Amazon Keyspaces

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Apache Cassandra?

**Apache Cassandra** es una base de datos NoSQL de código abierto, de tipo **wide-column** (columna
ancha), diseñada para manejar grandes volúmenes de datos distribuidos en muchos servidores.

- Arquitectura **descentralizada**: todos los nodos son iguales (no hay un nodo maestro), lo que
  evita puntos únicos de fallo y facilita escalar horizontalmente añadiendo más nodos.
- Pensada para **alta disponibilidad** y tolerancia a fallos, replicando los datos entre nodos —
  incluso entre distintos centros de datos o regiones.
- Optimizada para un **throughput de escritura muy alto**, siendo habitual en casos de uso como
  series temporales, IoT o cualquier carga con grandes volúmenes de escritura.
- Usa su propio lenguaje de consulta, **CQL** (*Cassandra Query Language*), con una sintaxis similar
  a SQL pero adaptada al modelo de datos distribuido de Cassandra.

Mantener un clúster de Cassandra por cuenta propia implica gestionar nodos, parches, replicación y
escalado manualmente — precisamente lo que **Amazon Keyspaces** elimina al ofrecer esta misma
compatibilidad como servicio gestionado.

## Propósito

**Amazon Keyspaces** es un servicio de base de datos **NoSQL** totalmente gestionado, compatible con
**Apache Cassandra**. Para el examen basta con tener una visión general del servicio.

Es conceptualmente similar a [[../8-dynamo-db/1-dynamodb|DynamoDB]] (otra base de datos NoSQL), pero
mientras DynamoDB es el servicio NoSQL propietario de AWS, Keyspaces está pensado específicamente
para quien necesita **compatibilidad con Apache Cassandra**: permite reutilizar código de aplicación,
drivers de licencia Apache y herramientas ya existentes de Cassandra sin cambios.

## Gestión

Totalmente gestionado por AWS: aprovisionamiento, configuración, parches de hardware, replicación de
datos, escalado y copias de seguridad — todo se ajusta automáticamente según la carga de trabajo, sin
gestionar infraestructura subyacente.

## Alta disponibilidad y seguridad

- Replicación entre múltiples **Availability Zones**, aportando alta disponibilidad y durabilidad.
- Integración con **IAM** para autenticación y autorización.
- **Cifrado en reposo** mediante claves gestionadas por AWS.
- **Cifrado en tránsito** soportado.

## Modos de capacidad

Igual que en DynamoDB, existen dos formas de aprovisionar capacidad, con precios distintos:

| Modo | Cuándo usarlo | Coste |
| ------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **On-Demand** | Cargas de trabajo impredecibles o con picos puntuales | Se paga por el rendimiento de lectura/escritura consumido, más almacenamiento y backups — más caro pero más flexible |
| **Provisioned** | Cargas de trabajo predecibles y estables | Se aprovisiona una cantidad fija de rendimiento por adelantado — más barato en cargas estables |
