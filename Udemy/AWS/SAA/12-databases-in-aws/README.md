# Bases de datos en AWS

## Elección de bases de datos en AWS según el caso de uso

Elegir la base de datos adecuada es fundamental para optimizar el **rendimiento**, **costos**, **escalabilidad** y **mantenimiento** de una solución. AWS ofrece una amplia gama de bases de datos especializadas, cada una diseñada para resolver problemas distintos.

---

### Preguntas clave para elegir una base de datos

Antes de decidir qué base de datos utilizar, se deben considerar:

| Pregunta                                                   | Ejemplo de implicación                             |
| ---------------------------------------------------------- | -------------------------------------------------- |
| ¿Predomina la **lectura o escritura**?                     | Lectura intensiva → ElastiCache, DAX               |
| ¿La carga es constante o **fluctúa durante el día**?       | Fluctuante → DynamoDB on-demand o serverless RDS   |
| ¿Cuánto **crecerán los datos** y por cuánto tiempo?        | Alto volumen → Redshift, S3, Glacier               |
| ¿Qué tan importantes son la **latencia y el rendimiento**? | Tiempo real → DynamoDB, ElastiCache                |
| ¿Cuántos usuarios simultáneos habrá?                       | Escalabilidad horizontal → NoSQL, Aurora           |
| ¿Cómo se accede a los datos? (consultas, joins, etc.)      | Joins complejos → RDS o Aurora                     |
| ¿Qué **modelo de datos** necesitas?                        | Estructurado → RDBMS, Semi/no estructurado → NoSQL |
| ¿Necesitas **esquema estricto o flexibilidad**?            | Rígido → RDBMS, Flexible → DynamoDB, DocumentDB    |
| ¿Qué **nivel de durabilidad** requieren los datos?         | Ledger inmutable → QLDB                            |
| ¿Cuáles son los **costos de licencia** aceptables?         | AWS maneja opciones de código abierto o gestionado |

---

### Categorías y opciones de bases de datos en AWS

#### 📘 Relacionales (SQL / OLTP)

| Servicio          | Descripción                                           | Casos de uso                             |
| ----------------- | ----------------------------------------------------- | ---------------------------------------- |
| **Amazon RDS**    | Motor relacional gestionado (MySQL, Postgres, etc.)   | Aplicaciones tradicionales, OLTP         |
| **Amazon Aurora** | Compatible con MySQL/Postgres, escalable y serverless | Alta disponibilidad, lecturas intensivas |

✔️ **Ideal para**: consultas SQL complejas, joins, esquemas rígidos, integridad referencial

---

#### 📙 NoSQL (clave-valor, documentos, grafos, etc.)

| Servicio                  | Tipo                                  | Casos de uso                                                |
| ------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| **DynamoDB**              | Clave-valor / documento (JSON)        | Apps móviles, IoT, ecommerce, gaming                        |
| **ElastiCache**           | Memoria en caché (Redis, Memcached)   | Caching, sesiones, contadores en tiempo real                |
| **DocumentDB**            | Documentos (JSON, compatible MongoDB) | Apps con datos flexibles tipo documento                     |
| **Keyspaces (Cassandra)** | Wide-column                           | IoT, telemetría, grandes volúmenes con baja latencia        |
| **Neptune**               | Grafos                                | Redes sociales, recomendaciones, relaciones entre entidades |

✔️ **Ideal para**: escalabilidad horizontal, datos semi/no estructurados, baja latencia

---

#### 📗 Almacenamiento de objetos

| Servicio      | Descripción                             | Casos de uso                      |
| ------------- | --------------------------------------- | --------------------------------- |
| **Amazon S3** | Almacén de objetos duradero y escalable | Archivos, backups, big data, logs |

✔️ **Ideal para**: datos estáticos, acceso vía SDK/HTTP, almacenamiento masivo

---

#### 📕 Almacenes de datos / analítica

| Servicio            | Descripción                                 | Casos de uso                             |
| ------------------- | ------------------------------------------- | ---------------------------------------- |
| **Amazon Redshift** | Data warehouse SQL para grandes volúmenes   | BI, dashboards, informes empresariales   |
| **Athena**          | Consultas SQL sobre datos en S3             | Exploración ad hoc, sin infraestructura  |
| **EMR**             | Framework de big data (Hadoop, Spark, etc.) | Procesamiento de logs, ML, ETL complejas |

✔️ **Ideal para**: análisis masivo, consultas sobre datos históricos, informes complejos

---

#### 📓 Casos especializados

| Servicio              | Tipo / Propósito                      | Casos de uso                                   |
| --------------------- | ------------------------------------- | ---------------------------------------------- |
| **Amazon OpenSearch** | Búsquedas e indexación de texto libre | Logs, búsqueda full-text, observabilidad       |
| **Amazon Neptune**    | Base de datos de grafos               | Relaciones complejas, motores de recomendación |
| **Amazon QLDB**       | Ledger inmutable y verificable        | Auditorías, registros financieros              |
| **Amazon Timestream** | Series temporales                     | IoT, métricas, datos con timestamp             |

✔️ **Ideal para**: necesidades específicas como trazabilidad, búsquedas, datos temporales

---

### Comparación rápida

| Tipo de base de datos | Servicios principales                        | Mejor para...                          |
| --------------------- | -------------------------------------------- | -------------------------------------- |
| Relacional (SQL)      | RDS, Aurora                                  | Integridad, joins, estructura rígida   |
| NoSQL                 | DynamoDB, DocumentDB, Keyspaces, ElastiCache | Escalabilidad, flexibilidad, velocidad |
| Grafos                | Neptune                                      | Relaciones complejas entre datos       |
| Temporal              | Timestream                                   | Datos por tiempo, series de métricas   |
| Objetos               | S3                                           | Archivos, blobs, medios, backups       |
| Analítica             | Redshift, Athena, EMR                        | Informes masivos, consultas históricas |
| Ledger                | QLDB                                         | Inmutabilidad, auditoría               |
| Búsqueda              | OpenSearch                                   | Indexación, búsqueda full-text         |

---

### Conclusión

Para elegir correctamente una base de datos en AWS, es esencial entender el **modelo de acceso**, el **tipo de datos**, la **carga esperada**, la **frecuencia de acceso**, la **latencia requerida** y el **modelo de crecimiento**. AWS proporciona una solución específica para cada necesidad, desde bases relacionales tradicionales hasta servicios para analítica, búsqueda o IoT. La clave está en alinear la elección con los **requisitos técnicos y de negocio** del sistema.

## Amazon RDS (Relational Database Service) en detalle

Amazon RDS es un servicio gestionado que facilita la creación, operación y escalado de bases de datos relacionales en la nube. Ofrece alta disponibilidad, seguridad, backups automáticos y administración simplificada sin tener que preocuparse por la infraestructura subyacente.

---

### Motores compatibles

RDS soporta múltiples motores de bases de datos:

| Motor          | Características destacadas                                   |
| -------------- | ------------------------------------------------------------ |
| **PostgreSQL** | Open source avanzado, extensiones como PostGIS               |
| **MySQL**      | Muy popular, gran ecosistema                                 |
| **MariaDB**    | Fork de MySQL, open source, mayor flexibilidad de licencias  |
| **Oracle**     | Licencia BYOL o incluida, soporte para PL/SQL, RAC limitado  |
| **SQL Server** | Licencia BYOL o incluida, integra con Windows Server, .NET   |
| **RDS Custom** | Entorno personalizado con acceso a SO, para workloads legacy |

---

### Tipos de instancias y almacenamiento

#### Instancias

- Se selecciona una instancia EC2 subyacente con memoria, CPU y red adaptadas al caso de uso
- Categorías comunes:

  - **T3/T4g** (burstable, dev/test)
  - **M** (balanceado)
  - **R** (optimizadas para memoria)
  - **X/HighMem** (uso intensivo de memoria para Oracle o SAP)

#### Almacenamiento (volúmenes EBS)

- **GP3** (propósito general)
- **IO1/IO2** (IOPS provisionadas, para cargas críticas)
- Tamaño mínimo de 20 GB, escalable automáticamente si se habilita

---

### Autoescalado de almacenamiento

- **El almacenamiento puede escalar automáticamente** en función del crecimiento del volumen de datos
- No requiere downtime
- Hasta 64 TB por instancia (depende del motor y tipo)

---

### Alta disponibilidad y réplicas

| Función                  | Descripción                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| **Multi-AZ**             | Replica sincrónica en otra zona de disponibilidad; failover automático |
| **Read Replicas**        | Réplicas de solo lectura para balancear carga y escalar lecturas       |
| **Aurora Read Replicas** | Hasta 15 réplicas, latencia de milisegundos                            |

---

### Seguridad

| Función             | Descripción                                              |
| ------------------- | -------------------------------------------------------- |
| **IAM**             | Permite autenticar usuarios y roles sin usar contraseñas |
| **Security Groups** | Controlan acceso de red a las instancias                 |
| **KMS**             | Cifrado en reposo con claves gestionadas                 |
| **SSL/TLS**         | Cifrado en tránsito entre cliente y base de datos        |
| **Secrets Manager** | Almacena credenciales cifradas para bases de datos       |

---

### Backup, recuperación y mantenimiento

- **Backups automáticos**:

  - Punto de restauración hasta **35 días**
  - Incluye logs de transacciones para recuperación a un punto exacto en el tiempo

- **Snapshots manuales**:

  - Permanecen hasta que se eliminan explícitamente

- **Mantenimiento gestionado**:

  - AWS puede aplicar parches y actualizaciones durante ventanas configurables

---

### Autenticación con IAM y Secrets Manager

- RDS permite usar **IAM** para autenticar conexiones a **MySQL y PostgreSQL**
- Con **Secrets Manager**, se puede:

  - Rotar credenciales automáticamente
  - Integrar fácilmente con Lambda, ECS, EC2, etc.

---

### RDS Custom

- Opción para workloads que requieren acceso a sistema operativo, por ejemplo:

  - Aplicaciones legacy que instalan componentes del lado del SO
  - Bases de datos de terceros altamente personalizadas

---

### Casos de uso ideales

| Caso de uso                            | Por qué RDS es adecuado                                     |
| -------------------------------------- | ----------------------------------------------------------- |
| Aplicaciones OLTP                      | Alto rendimiento y transacciones concurrentes               |
| Sistemas con integridad referencial    | Soporte para claves foráneas, triggers, constraints         |
| Aplicaciones con consultas SQL         | RDS soporta SQL completo con joins, funciones y más         |
| Apps que requieren alta disponibilidad | Multi-AZ y réplicas de lectura aseguran disponibilidad      |
| Arquitecturas seguras y escalables     | IAM, KMS, VPC, SG, backups automáticos, escalado de storage |

---

### Resumen técnico

| Funcionalidad                   | Detalle                                                    |
| ------------------------------- | ---------------------------------------------------------- |
| Motores soportados              | PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, RDS Custom |
| Tamaño máximo de almacenamiento | Hasta 64 TB (escalado automático opcional)                 |
| Alta disponibilidad             | Multi-AZ con failover                                      |
| Réplicas de lectura             | Sí (dependen del motor)                                    |
| Cifrado                         | En tránsito (SSL), en reposo (KMS), por cliente (opcional) |
| Backup                          | Automático (hasta 35 días), snapshots manuales             |
| Autenticación IAM               | Compatible con MySQL y PostgreSQL                          |
| Integración                     | Secrets Manager, CloudWatch, Lambda, CloudTrail, VPC       |

---

Amazon RDS es ideal para cargas de trabajo relacionales que requieren **transacciones consistentes**, **alta disponibilidad**, **seguridad robusta**, y **mínima gestión operativa**, manteniendo compatibilidad con los motores más populares.

## Amazon Aurora: base de datos relacional optimizada para la nube

**Amazon Aurora** es un motor de base de datos relacional desarrollado por AWS que ofrece el rendimiento y disponibilidad de bases de datos comerciales con la simplicidad y rentabilidad de las bases de datos open source. Aunque **no es open source**, **es compatible a nivel de API con MySQL y PostgreSQL**.

---

### Compatibilidad de motores

| Compatibilidad        | Detalle                                      |
| --------------------- | -------------------------------------------- |
| **Aurora MySQL**      | Compatible con MySQL 5.6, 5.7, 8.0           |
| **Aurora PostgreSQL** | Compatible con PostgreSQL 11, 12, 13, 14, 15 |

Esto permite migrar aplicaciones existentes con mínimos cambios en el código.

---

### Arquitectura de Aurora: separación de cómputo y almacenamiento

#### 📦 Almacenamiento distribuido (storage layer)

- Totalmente gestionado y desacoplado del cómputo
- Almacena los datos en **6 réplicas** distribuidas en **3 zonas de disponibilidad (AZs)**
- Es **auto-reparable** y **autoescalable** hasta **128 TB**
- Capaz de tolerar la pérdida de:

  - 2 copias sin afectar la escritura
  - 3 copias sin afectar la lectura

#### 🧠 Cómputo (database instances)

- Se despliega un **clúster Aurora** con al menos una **instancia escritora**
- Se pueden añadir hasta **15 réplicas de solo lectura** con latencia inferior a 100 ms
- Aurora detecta fallos y realiza **failover automático** a una réplica

---

### Endpoints personalizados

Aurora proporciona distintos **puntos finales (endpoints)** para optimizar el uso de las instancias:

| Endpoint             | Función                                                |
| -------------------- | ------------------------------------------------------ |
| **Cluster endpoint** | Dirige al nodo principal (escritura)                   |
| **Reader endpoint**  | Balancea carga entre réplicas de solo lectura          |
| **Custom endpoint**  | Se puede crear para agrupar un subconjunto de réplicas |

---

### Alta disponibilidad y replicación global

| Funcionalidad           | Descripción                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------- |
| **Multi-AZ**            | Alta disponibilidad con failover automático entre instancias                          |
| **Read replicas**       | Hasta 15 réplicas por región                                                          |
| **Aurora Global**       | Replica en varias regiones (hasta 5), con **16 réplicas de lectura** cada una         |
| **Aurora Multi-Master** | Escrituras en múltiples nodos en una misma región (alta disponibilidad activa-activa) |

---

### Características avanzadas

| Funcionalidad               | Descripción                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| **Aurora Serverless v2**    | Escalado automático fino por segundos (ideal para cargas intermitentes) |
| **Aurora Global Database**  | Replicación entre regiones para apps globales                           |
| **Aurora Machine Learning** | Invoca modelos de **SageMaker o Comprehend** desde SQL                  |
| **Aurora Database Cloning** | Crea clones instantáneos del clúster sin copiar físicamente los datos   |
| **Zero-downtime patching**  | Aplicación de parches sin interrupciones (en Serverless v2)             |

---

### Seguridad, backups y mantenimiento

- **Cifrado en tránsito (SSL/TLS)** y en reposo (**KMS**)
- Integración con **IAM** para autenticación
- Compatibilidad con **Secrets Manager**
- **Copias de seguridad automáticas** y restauración punto en el tiempo
- Snapshots manuales
- Mantenimiento programado y gestionado por AWS

---

### Comparación con RDS tradicional

| Característica              | **Aurora**                                | **RDS (MySQL/Postgres)**               |
| --------------------------- | ----------------------------------------- | -------------------------------------- |
| Escalabilidad de lectura    | Hasta 15 réplicas con <100 ms de latencia | 5 réplicas con mayor latencia          |
| Almacenamiento              | Automático, distribuido y resiliente      | EBS en una sola zona de disponibilidad |
| Rendimiento                 | Hasta 5× (MySQL) / 3× (PostgreSQL)        | Limitado al motor estándar             |
| Compatibilidad multi-región | Aurora Global Database                    | Requiere configuraciones complejas     |
| Esquema de cobro            | Por instancia y por I/O                   | Por instancia y volumen                |
| Serverless                  | Sí (v1 y v2)                              | Solo en RDS para Aurora                |

---

### Casos de uso ideales para aurora

- Aplicaciones críticas que requieren **alta disponibilidad**
- Servicios globales con **réplicas en múltiples regiones**
- Cargas intermitentes o variables que se beneficien de **Aurora Serverless**
- Sistemas OLTP con alta **concurrencia y rendimiento**
- Aplicaciones que desean escalar sin rediseñar su backend relacional

---

### Resumen técnico de Aurora

| Aspecto                    | Valor                                        |
| -------------------------- | -------------------------------------------- |
| Compatibilidad             | PostgreSQL y MySQL (a nivel de API)          |
| Almacenamiento máximo      | 128 TB                                       |
| Réplicas                   | Hasta 15 por región, 16 por región en global |
| Tiempo de recuperación     | < 30 segundos (failover automático)          |
| Serverless disponible      | Sí (v1 y v2)                                 |
| Clonado de base de datos   | Sí, instantáneo                              |
| Machine Learning integrado | Sí (con SQL → SageMaker/Comprehend)          |
| Escalado automático de I/O | Sí, con base en uso real                     |

---

Aurora combina lo mejor de RDS con una arquitectura de almacenamiento distribuido, resiliente y escalable, ideal para cargas **críticas, modernas y globales** que buscan **desempeño, simplicidad operativa y disponibilidad sin compromiso**.

## Amazon ElastiCache en detalle: Redis y Memcached como servicios gestionados

**Amazon ElastiCache** es un servicio administrado que proporciona almacenamiento en memoria de alta velocidad utilizando los motores **Redis** y **Memcached**. Actúa como una capa de caché para reducir la latencia, aliviar carga en bases de datos y mejorar la escalabilidad de aplicaciones.

---

### Motores disponibles

| Motor         | Características principales                                               |
| ------------- | ------------------------------------------------------------------------- |
| **Redis**     | Soporte para clustering, persistencia, replicación, estructuras avanzadas |
| **Memcached** | Cache simple, sin persistencia, multi-thread, distribuido automáticamente |

> Redis es más **avanzado y flexible**, mientras que Memcached es más **ligero y simple**

---

### Arquitectura y provisión

- ElastiCache es similar a RDS en cuanto a administración:

  - Se **aprovisionan nodos** (instancias EC2 específicas para memoria)
  - Se **asignan grupos de parámetros**, mantenimiento, copias, etc.

- Redis soporta:

  - **Cluster mode enabled** (sharding automático de datos)
  - **Multi-AZ con failover** (replicación automática)
  - Hasta **5 réplicas de lectura por shard**

- Memcached no soporta clustering ni replicas

---

### Almacenamiento y rendimiento

- **Almacenamiento en RAM**: no persistente por defecto (aunque Redis permite snapshots y AOF)
- Latencia: **sub-milisegundos**, ideal para respuestas ultra rápidas
- Capacidad: basada en el tamaño de memoria de los nodos EC2 seleccionados

---

### Seguridad en Elasticaché

| Mecanismo               | Descripción                                                   |
| ----------------------- | ------------------------------------------------------------- |
| **IAM y VPC**           | Control de acceso a instancias ElastiCache                    |
| **Grupos de seguridad** | Control de tráfico de red                                     |
| **KMS**                 | Cifrado en reposo (solo Redis con cluster mode deshabilitado) |
| **Cifrado en tránsito** | TLS opcional entre cliente y servidor Redis                   |
| **Redis AUTH**          | Autenticación por contraseña a nivel de cliente Redis         |

---

### Mantenimiento y copias

- **Backups automáticos** en Redis (snapshots)
- Mantenimiento programado (como parches de seguridad)
- Escalado vertical (cambio de tamaño de nodo)
- Escalado horizontal (clustering Redis)

---

### Requisitos para uso en aplicaciones

- **No utiliza SQL**, las operaciones son específicas del motor (Redis/Memcached)
- Requiere cambios en el **código de la aplicación** para:

  - Insertar, obtener y borrar elementos desde la caché
  - Determinar **estrategias de invalidación** o expiración
  - Implementar patrones como **cache-aside**, **write-through** o **lazy-loading**

---

### Casos de uso típicos

| Caso de uso                              | Descripción                                                     |
| ---------------------------------------- | --------------------------------------------------------------- |
| **Caché de resultados de base de datos** | Almacenar respuestas frecuentes para evitar consultas repetidas |
| **Datos de sesión**                      | Guardar tokens, sesiones de usuarios, contadores temporales     |
| **Colas o sistemas de puntuación**       | Redis soporta listas, conjuntos ordenados, pub/sub, etc.        |
| **Throttle o rate-limiting**             | Implementación rápida con expiración de claves                  |
| **Gaming / leaderboard**                 | Uso de estructuras como sorted sets                             |

---

### Comparación rápida entre Redis y Memcached

| Característica       | **Redis**                           | **Memcached**          |
| -------------------- | ----------------------------------- | ---------------------- |
| Persistencia         | Opcional (snapshots, AOF)           | No                     |
| Replicación          | Sí (Multi-AZ, réplicas de lectura)  | No                     |
| Clustering           | Sí (sharding)                       | No (escala manual)     |
| Autenticación        | Redis AUTH                          | No                     |
| Cifrado              | En tránsito y en reposo             | No                     |
| Estructuras de datos | Complejas (listas, sets, hashes...) | Solo clave-valor plano |
| Multi-thread         | No (Redis es single-thread)         | Sí                     |

---

### Resumen técnico de elasticaché

| Funcionalidad             | Valor                                         |
| ------------------------- | --------------------------------------------- |
| Latencia                  | Sub-milisegundos                              |
| Escalabilidad             | Vertical y horizontal (Redis Cluster)         |
| Réplicas                  | Hasta 5 por shard (solo Redis)                |
| Cifrado                   | TLS, KMS, Redis AUTH                          |
| Backup y snapshots        | Sí (Redis)                                    |
| Mantenimiento gestionado  | Sí                                            |
| Tipos de instancias       | Basado en instancias EC2 (memoria optimizada) |
| Integración con VPC y IAM | Sí                                            |

---

### Conclusión de elasticaché

Amazon ElastiCache es ideal para cargas de trabajo que requieren **respuesta inmediata**, especialmente en casos donde los datos se consultan repetidamente y pueden mantenerse en memoria. **Redis** es recomendado para la mayoría de los casos por su **flexibilidad, replicación y clustering**, mientras que **Memcached** es útil para soluciones más simples o legadas. Ambos ayudan a descargar trabajo de bases de datos primarias y a reducir costos operativos por lecturas intensas.

## Amazon DynamoDB en detalle: base de datos NoSQL clave-valor y documentos totalmente gestionada

**Amazon DynamoDB** es una base de datos **NoSQL propietaria de AWS** orientada a claves-valor y documentos. Está diseñada para ofrecer **latencia de milisegundos de un solo dígito** a cualquier escala, con disponibilidad y durabilidad garantizadas. Es ideal para aplicaciones web, móviles, IoT y serverless que requieren alta velocidad, flexibilidad de esquema y escalabilidad automática.

---

### Características principales

| Característica                   | Descripción                                                               |
| -------------------------------- | ------------------------------------------------------------------------- |
| **Modelo de datos**              | Clave-valor o documento (tipo JSON)                                       |
| **Latencia**                     | Milisegundos de un solo dígito, incluso en cargas altas                   |
| **Gestión**                      | Totalmente gestionado, sin servidores, sin patching manual                |
| **Esquema**                      | Flexible: solo se define clave primaria, resto de atributos son dinámicos |
| **Disponibilidad y durabilidad** | Alta disponibilidad Multi-AZ por defecto                                  |

---

### Modos de capacidad

| Modo                        | Descripción                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| **Capacidad aprovisionada** | Se definen RCU/WCU (unidades de lectura y escritura); autoescalado opcional |
| **Capacidad bajo demanda**  | Escala automáticamente sin configuración previa; paga solo por uso          |

> Ideal para cargas impredecibles o nuevas aplicaciones en etapa inicial

---

### Lectura y escritura desacopladas

- **Lectura y escritura** se manejan por separado en términos de capacidad
- Lecturas consistentes: eventual o **consistente fuerte**
- Puede escalar operaciones de escritura sin afectar el rendimiento de lectura y viceversa

---

### TTL y caché

- Cada ítem puede tener un **Time To Live (TTL)** para eliminar automáticamente registros expirados
- Puede funcionar como reemplazo de **ElastiCache** para ciertas aplicaciones de caché clave-valor de baja latencia

---

### Integraciones y procesamiento avanzado

| Funcionalidad                  | Descripción                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **DynamoDB Streams**           | Registra cambios en la tabla (insert/update/delete)                   |
| **Lambda triggers**            | Procesa eventos de Streams sin necesidad de infraestructura           |
| **DAX (DynamoDB Accelerator)** | Caché en memoria gestionado, latencia en microsegundos                |
| **Transacciones**              | Lecturas y escrituras atómicas en una o más tablas                    |
| **Backups y PITR**             | Copias automáticas hasta 35 días (Point-in-Time Recovery)             |
| **Exportación a S3**           | Se puede exportar PITR a S3 sin consumir RCU                          |
| **Tablas globales**            | Replicación multirregional activa-activa (lectura/escritura en todas) |

---

### Seguridad y control de acceso

| Mecanismo               | Descripción                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **IAM**                 | Autenticación y autorización granular a nivel de tabla, ítem, acción |
| **Cifrado en reposo**   | Automático mediante **AWS KMS**                                      |
| **Cifrado en tránsito** | Conexión cifrada con TLS                                             |
| **Integración con VPC** | VPC Endpoints para acceso privado desde subredes internas            |

---

### Arquitectura sin servidor

DynamoDB se integra fácilmente en arquitecturas **serverless**:

- Compatible con **API Gateway + Lambda**
- No requiere servidores, escalado o parches
- Soporte completo para **monitorización con CloudWatch**

---

### Ventajas para desarrolladores

- No requiere diseño de esquemas estrictos
- Ideal para desarrollos ágiles con cambios frecuentes en estructura
- Escalable horizontalmente sin rediseño
- Soporta patrones como **single-table design**

---

### Limitaciones

| Limitación                 | Detalle                                           |
| -------------------------- | ------------------------------------------------- |
| **Sin lenguaje SQL**       | Se usa PartiQL (consulta tipo SQL limitada)       |
| **Joins no soportados**    | No hay operaciones relacionales                   |
| **Tamaño máximo por ítem** | 400 KB                                            |
| **Índices secundarios**    | Requieren planificación y limitan la flexibilidad |

---

### Casos de uso ideales de DynamoDB

| Caso de uso                      | Razón                                                     |
| -------------------------------- | --------------------------------------------------------- |
| Aplicaciones **serverless**      | Integración directa con Lambda, escalado automático       |
| Almacenamiento **clave-valor**   | Tiempo real, baja latencia, TTL por ítem                  |
| Juegos online, IoT, apps móviles | Altas tasas de escritura, necesidad de baja latencia      |
| Apps multi-región                | Tablas globales con replicación activa-activa             |
| Sistemas de eventos              | Conexión con Streams y procesamiento asíncrono con Lambda |
| Control de acceso granular       | IAM a nivel de tabla, ítem o acción                       |

---

### Resumen técnico de DynamoDB

| Característica      | Valor                                                   |
| ------------------- | ------------------------------------------------------- |
| Latencia            | Milisegundos de un solo dígito                          |
| Modos de capacidad  | Aprovisionado (con autoscaling) o bajo demanda          |
| Almacenamiento      | Escalable automáticamente sin límite práctico           |
| Transacciones       | Sí, ACID                                                |
| TTL                 | Sí, por ítem                                            |
| Streams             | Sí, integración con Lambda                              |
| Copias de seguridad | PITR hasta 35 días, backups manuales y exportación a S3 |
| Tablas globales     | Sí, hasta 16 regiones activas                           |
| Seguridad           | IAM, KMS, VPC, cifrado en tránsito y reposo             |
| Caché               | DAX (lecturas en microsegundos)                         |

---

### Comparación general: DynamoDB vs ElastiCache vs RDS

| Característica      | **DynamoDB**             | **ElastiCache**   | **RDS**                   |
| ------------------- | ------------------------ | ----------------- | ------------------------- |
| Modelo de datos     | Clave-valor / documentos | Clave-valor       | Relacional                |
| SQL                 | ❌                       | ❌                | ✅                        |
| Escalado automático | ✅                       | Limitado          | Limitado (excepto Aurora) |
| Persistencia        | ✅                       | Opcional (Redis)  | ✅                        |
| Carga típica        | Mixta lectura/escritura  | Lectura intensiva | Transaccional (OLTP)      |
| Latencia            | Milisegundos             | Microsegundos     | Milisegundos              |

---

**Amazon DynamoDB** es ideal para arquitecturas modernas, sin servidor, que necesitan **escalabilidad instantánea, latencia baja y operación sin mantenimiento**, sacrificando cierta flexibilidad relacional a cambio de **rendimiento masivo y simplicidad operacional**.

## Amazon S3 en detalle: almacenamiento de objetos escalable, duradero y seguro

**Amazon S3 (Simple Storage Service)** es un servicio de almacenamiento **clave-valor orientado a objetos**, totalmente **serverless**, diseñado para almacenar y recuperar cualquier cantidad de datos desde cualquier lugar en la web, con **escalabilidad infinita**, **alta durabilidad (99.999999999%)** y **bajo costo**.

---

### Características generales

| Característica               | Detalle                                                            |
| ---------------------------- | ------------------------------------------------------------------ |
| **Modelo de datos**          | Clave (nombre del objeto) – valor (contenido del archivo)          |
| **Tamaño máximo por objeto** | Hasta **5 TB**                                                     |
| **Mínimo recomendado**       | No óptimo para objetos muy pequeños o millones de archivos <100 KB |
| **Durabilidad**              | 11 nueves (99.999999999%)                                          |
| **Alta disponibilidad**      | A través de múltiples zonas de disponibilidad                      |
| **Serverless**               | No hay instancias, ni mantenimiento, escala automáticamente        |

---

### Casos de uso ideales de S3

- Almacenamiento de archivos estáticos (PDF, JPG, HTML, JS, etc.)
- Backup y archivado de información
- Big Data y machine learning (logs, datasets)
- Distribución de contenido vía CloudFront
- **Alojamiento de sitios web estáticos**
- Carga de archivos en apps móviles/web
- Registro de logs de acceso o auditoría
- Recuperación ante desastres

---

### Capacidades de almacenamiento y niveles de clase

| Clase de almacenamiento     | Uso recomendado                                                          |
| --------------------------- | ------------------------------------------------------------------------ |
| **S3 Standard**             | Datos accedidos frecuentemente                                           |
| **S3 Intelligent-Tiering**  | Cambia automáticamente entre frecuencias de acceso                       |
| **S3 Standard-IA**          | Acceso infrecuente pero con disponibilidad inmediata                     |
| **S3 One Zone-IA**          | Similar al anterior, pero en una sola AZ (más barato, menos durabilidad) |
| **S3 Glacier**              | Archivos archivados, recuperación entre minutos y horas                  |
| **S3 Glacier Deep Archive** | Archivado a largo plazo, recuperación en horas                           |

---

### Funcionalidades clave

| Funcionalidad                | Descripción                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| **Versionado**               | Mantiene versiones anteriores de objetos modificados o eliminados |
| **Ciclo de vida**            | Políticas para mover o eliminar objetos automáticamente           |
| **Cifrado**                  | SSE-S3, SSE-KMS, SSE-C, cifrado del lado del cliente, TLS         |
| **Replicación**              | CRR / SRR (Cross/ Same Region Replication)                        |
| **MFA Delete**               | Protege contra eliminaciones accidentales                         |
| **S3 Access Logs**           | Registro detallado de accesos al bucket                           |
| **CORS**                     | Control de acceso desde dominios cruzados (Cross-Origin Requests) |
| **S3 Object Lock**           | Inmutabilidad para cumplimiento normativo                         |
| **S3 Object Lambda**         | Personaliza el contenido en tiempo real (por ejemplo, anonimizar) |
| **S3 Select**                | Consultas SQL parciales sobre objetos CSV, JSON o Parquet         |
| **S3 Batch Operations**      | Procesamiento masivo de objetos (copiar, etiquetar, restaurar)    |
| **S3 Transfer Acceleration** | Mejora rendimiento de cargas desde ubicaciones remotas            |
| **Carga multiparte**         | Carga paralela de archivos grandes (>100MB)                       |
| **Eventos de S3**            | Invocación automática de funciones Lambda, SQS, SNS               |

---

### Seguridad en S3

| Mecanismo                      | Descripción                                                             |
| ------------------------------ | ----------------------------------------------------------------------- |
| **IAM policies**               | Controlan acceso por usuario/rol                                        |
| **Bucket policies**            | Controlan acceso a nivel de bucket                                      |
| **ACL (Access Control Lists)** | Controles heredados más granulados (menos recomendados)                 |
| **Access Points**              | Permiten gestionar acceso a subconjuntos de datos                       |
| **Object Lock / WORM**         | Protección legal o de cumplimiento (Write Once Read Many)               |
| **Cifrado en reposo**          | SSE-S3 (AWS gestiona claves), SSE-KMS (clave del cliente en KMS), SSE-C |
| **Cifrado en tránsito**        | TLS                                                                     |
| **MFA Delete**                 | Elimina objetos/versiones solo si se proporciona MFA                    |

---

### Automatización y eventos

- S3 puede **publicar eventos** hacia:

  - **Lambda**: ejecutar código sin servidores (e.g., redimensionar imagen)
  - **SQS**: colas para flujos asincrónicos
  - **SNS**: notificaciones por correo o HTTP

---

### Optimización de rendimiento

| Optimización                    | Beneficio                                                        |
| ------------------------------- | ---------------------------------------------------------------- |
| **Carga multiparte**            | Aumenta rendimiento para archivos grandes (>100 MB)              |
| **Transfer Acceleration**       | Usando edge locations de CloudFront para acelerar transferencias |
| **Naming aleatorio de objetos** | Mejora distribución de acceso                                    |
| **S3 Select**                   | Extrae solo los campos necesarios de archivos grandes            |

---

### Arquitecturas comunes usando S3

- **Web estático**: CloudFront + S3 como origen
- **Procesamiento de datos**: S3 → Lambda/EMR → Redshift/Athena
- **Backup automatizado**: ciclo de vida + replicación + Glacier
- **Carga directa de archivos desde frontend**: firmado con pre-signed URLs y autenticación con Cognito

---

### Resumen técnico de S3

| Característica           | Valor                                             |
| ------------------------ | ------------------------------------------------- |
| Tamaño máximo de objeto  | 5 TB (recomendado: carga multiparte para >100 MB) |
| Capacidad total          | Ilimitada                                         |
| Versionado               | Sí                                                |
| Cifrado                  | SSE-S3, SSE-KMS, SSE-C, TLS                       |
| Replicación              | Cross Region o Same Region                        |
| Clases de almacenamiento | Standard, IA, Glacier, etc.                       |
| Eventos                  | Lambda, SNS, SQS                                  |
| Consultas directas       | S3 Select (CSV, JSON, Parquet)                    |
| Automatización           | Ciclos de vida, batch operations, eventos         |

---

**Amazon S3** es el componente central de muchas arquitecturas modernas en AWS. Ofrece un equilibrio entre **durabilidad, rendimiento, seguridad y costos**, sirviendo como el punto de origen ideal para cargas estáticas, backup, big data, almacenamiento de medios y arquitecturas sin servidor.

## Amazon DocumentDB en detalle: base de datos documental compatible con MongoDB

**Amazon DocumentDB (con compatibilidad MongoDB)** es un servicio de base de datos documental completamente gestionado, diseñado para almacenar, consultar e indexar documentos en formato **BSON (Binary JSON)**. Es ideal para aplicaciones que utilizan el modelo de documentos flexible y dinámico típico de MongoDB, pero desean beneficiarse de la escalabilidad, seguridad y disponibilidad gestionada que ofrece AWS.

---

### Principales características

| Característica      | Descripción                                                       |
| ------------------- | ----------------------------------------------------------------- |
| **Modelo de datos** | Documento BSON (Binary JSON)                                      |
| **Compatibilidad**  | API compatible con MongoDB (versiones 3.6, 4.0, 5.0)              |
| **Despliegue**      | Similar a Aurora: clúster con almacenamiento y cómputo separados  |
| **Gestión**         | Totalmente gestionado por AWS                                     |
| **Escalabilidad**   | Almacén crece automáticamente en incrementos de 10 GB hasta 64 TB |
| **Rendimiento**     | Optimizado para millones de solicitudes por segundo               |

---

### Arquitectura de Amazon DocumentDB

#### Separación de cómputo y almacenamiento

- Instancias de base de datos **no almacenan datos localmente**
- Almacenamiento distribuido **separado y compartido** entre réplicas
- El almacenamiento es automáticamente:

  - **Replicado en 3 AZ**
  - **Tolerante a fallos**
  - **Autoescalable** hasta **64 TB**

#### Replicación y disponibilidad

| Función                 | Descripción                                                    |
| ----------------------- | -------------------------------------------------------------- |
| **Multi-AZ**            | Replica automáticamente en 3 zonas de disponibilidad           |
| **Failover automático** | Cambia a réplica en caso de fallo del nodo primario            |
| **Read replicas**       | Hasta 15 réplicas para escalar lectura sin degradar escrituras |

---

### Compatibilidad con MongoDB

- **API compatible**, permite migrar fácilmente desde MongoDB sin rediseñar la aplicación
- No se ejecuta MongoDB “puro”, por lo tanto **no es 100 % compatible**
- No admite todos los operadores y funciones avanzadas de MongoDB (e.g., change streams, map-reduce complejos)

---

### Seguridad y cifrado

| Mecanismo     | Descripción                                           |
| ------------- | ----------------------------------------------------- |
| **VPC**       | Despliegue dentro de redes privadas                   |
| **IAM**       | Control de acceso granular con políticas              |
| **KMS**       | Cifrado en reposo                                     |
| **TLS**       | Cifrado en tránsito                                   |
| **Auditoría** | Integra con CloudTrail para registrar llamadas de API |

---

### Backups, restauración y mantenimiento

- **Backups automáticos** con retención configurable (hasta 35 días)
- **Snapshots manuales** exportables o restaurables
- **Restauración punto en el tiempo** (PITR)
- Mantenimiento gestionado con parches programables

---

### Escalado y rendimiento

- **Almacenamiento autoescalable** hasta 64 TB
- Soporta hasta **15 réplicas de lectura**
- Admite escalado vertical (cambiar tipo de instancia)
- Diseñado para cargas de trabajo con millones de solicitudes por segundo

---

### Casos de uso típicos de documentDB

| Caso de uso                     | Por qué DocumentDB es adecuado                                   |
| ------------------------------- | ---------------------------------------------------------------- |
| Aplicaciones que usan MongoDB   | Migración con mínima fricción (misma API y drivers)              |
| Catálogos de productos          | Datos semi-estructurados con campos dinámicos                    |
| Aplicaciones móviles y juegos   | Almacenamiento flexible para perfiles, progreso, configuraciones |
| Contenido generado por usuarios | Posts, comentarios, formularios con estructuras no rígidas       |
| Apps serverless con API Gateway | Se integra bien con Lambda para patrones CRUD dinámicos          |

---

### Diferencias clave: DocumentDB vs MongoDB autogestionado

| Característica         | **Amazon DocumentDB**               | **MongoDB en EC2 / Atlas**                 |
| ---------------------- | ----------------------------------- | ------------------------------------------ |
| Administración         | Totalmente gestionado               | Autogestionado o gestionado por terceros   |
| Almacenamiento         | Separado, escalado automático       | Local (EBS), necesita configuración        |
| Alta disponibilidad    | 3 AZ por defecto                    | Requiere configuración manual o de clúster |
| Backups y PITR         | Sí                                  | Manual en EC2, nativo en Atlas             |
| Compatibilidad MongoDB | Parcial (API compatible)            | Total (MongoDB nativo)                     |
| Integración con AWS    | Profunda: IAM, KMS, VPC, CloudTrail | Limitada (a menos que se use Atlas en AWS) |

---

### Comparación rápida: DocumentDB vs Aurora vs DynamoDB

| Característica        | **DocumentDB**                           | **Aurora**                       | **DynamoDB**                           |
| --------------------- | ---------------------------------------- | -------------------------------- | -------------------------------------- |
| Modelo de datos       | Documentos (BSON)                        | Relacional (SQL)                 | Clave-valor / documentos (JSON-like)   |
| Esquema               | Flexible                                 | Fijo / estructurado              | Flexible                               |
| SQL                   | ❌                                       | ✅                               | ❌ (PartiQL limitado)                  |
| Escalado              | Vertical + Réplicas                      | Vertical + Réplicas              | Horizontal automático                  |
| Serverless disponible | ❌ (no serverless)                       | ✅ (Aurora Serverless v2)        | ✅                                     |
| Uso típico            | Apps MongoDB-like, estructuras dinámicas | OLTP clásico, apps empresariales | Apps serverless, IoT, tráfico variable |

---

### Resumen técnico de DocumentDB

| Funcionalidad         | Valor                                                                   |
| --------------------- | ----------------------------------------------------------------------- |
| Compatibilidad        | MongoDB 3.6, 4.0, 5.0                                                   |
| Almacenamiento máximo | 64 TB                                                                   |
| Réplicas de lectura   | Hasta 15                                                                |
| Multi-AZ              | Sí, replicación automática en 3 zonas                                   |
| Backups automáticos   | Hasta 35 días con restauración PITR                                     |
| Cifrado               | En tránsito (TLS) y en reposo (KMS)                                     |
| Seguridad             | IAM, VPC, KMS, CloudTrail                                               |
| Rendimiento           | Millones de solicitudes por segundo (dependiendo del tipo de instancia) |

---

**Amazon DocumentDB** es una solución ideal para desarrolladores que desean la **flexibilidad del modelo documental de MongoDB** sin preocuparse por la administración de clústeres, backups, disponibilidad o escalado, todo con **integración nativa en el ecosistema AWS**.

## Amazon Neptune en detalle: base de datos gráfica totalmente gestionada y optimizada para relaciones complejas

**Amazon Neptune** es una **base de datos gráfica totalmente gestionada**, diseñada para almacenar, consultar y navegar eficientemente por conjuntos de datos altamente conectados. Permite representar relaciones complejas como las que se dan en redes sociales, motores de recomendación, fraudes financieros, y grafos de conocimiento.

---

### ¿Qué es una base de datos de grafos?

Una base de datos de grafos representa la información como:

- **Nodos (vértices)**: entidades como usuarios, productos, publicaciones
- **Relaciones (aristas)**: conexiones entre nodos (e.g., “amigo de”, “comentó”, “le gusta”)
- **Propiedades**: información adicional sobre nodos o relaciones

Esto permite modelar estructuras **más naturales y eficientes** que las bases relacionales para **consultas altamente relacionales**.

---

### Ejemplo: modelo de red social

```plaintext
[Usuario1] --amigo de--> [Usuario2]
   |                     |
  comenta            le gusta
   ↓                     ↓
[Publicación A]     [Publicación B]
      ↑
   tiene comentario
      ↓
  [Comentario C]
```

---

### Motores y lenguajes de consulta soportados

| Lenguaje       | Descripción                                                       |
| -------------- | ----------------------------------------------------------------- |
| **Gremlin**    | Lenguaje de Apache TinkerPop (traversal para grafos de propiedad) |
| **SPARQL**     | Lenguaje W3C para grafos RDF (datos semánticos)                   |
| **OpenCypher** | (Soporte en preview) Lenguaje usado en Neo4j                      |

> Permite elegir entre distintos **tipos de grafos** según el caso de uso: RDF (tripletas semánticas) o Property Graph (más estructurado y orientado a entidades)

---

### Características principales de **Neptune**

| Funcionalidad           | Descripción                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **Gestión**             | Servicio totalmente gestionado (infraestructura, parches, backups)       |
| **Alta disponibilidad** | Réplicas Multi-AZ, hasta **15 réplicas de lectura**                      |
| **Escalabilidad**       | Escala horizontalmente en lectura con réplicas                           |
| **Almacenamiento**      | Hasta **miles de millones de relaciones**                                |
| **Latencia**            | **Milisegundos de un solo dígito**, incluso con grafos grandes           |
| **Backups y PITR**      | Copias automáticas, snapshots y restauración a punto en el tiempo (PITR) |

---

### Casos de uso típicos de **Neptune**

| Caso de uso                  | Justificación                                                               |
| ---------------------------- | --------------------------------------------------------------------------- |
| **Redes sociales**           | Relaciones como amigos, seguidores, me gusta, comentarios                   |
| **Motores de recomendación** | Usuarios similares, productos relacionados, caminos en el grafo             |
| **Detección de fraudes**     | Rastrear conexiones sospechosas, patrones de transferencia complejos        |
| **Grafos de conocimiento**   | Representación semántica de entidades, inferencia y navegación de conceptos |
| **Gestión de identidades**   | Seguimiento de relaciones jerárquicas o de permisos                         |
| **Redes de suministro**      | Entidades, ubicaciones, proveedores, flujos logísticos                      |

---

### Arquitectura y alta disponibilidad

| Característica                          | Valor                                                |
| --------------------------------------- | ---------------------------------------------------- |
| **Réplicas de lectura**                 | Hasta 15                                             |
| **Multi-AZ**                            | Sí, con failover automático                          |
| **Cómputo separado del almacenamiento** | No directamente, pero lectura escalable vía réplicas |
| **Backup y restauración**               | Snapshots y PITR                                     |

---

### Seguridad e integración con AWS

- **IAM** para control de acceso y autenticación
- **VPC** para aislamiento de red
- **KMS** para cifrado en reposo
- **TLS** para cifrado en tránsito
- **CloudTrail** para auditoría de operaciones

---

### Comparación rápida con otras bases de datos

| Característica       | **Neptune**                      | **RDS**          | **DynamoDB**                        |
| -------------------- | -------------------------------- | ---------------- | ----------------------------------- |
| Tipo de datos        | Grafos                           | Relacional (SQL) | Clave-valor / documento             |
| Modelo de relaciones | Relaciones complejas nativas     | Por joins        | Limitadas                           |
| Lenguaje de consulta | Gremlin, SPARQL                  | SQL              | PartiQL (limitado)                  |
| Latencia             | Milisegundos                     | Milisegundos     | Milisegundos                        |
| Escalado de lectura  | Hasta 15 réplicas                | Sí (limitado)    | Sí (naturalmente distribuido)       |
| Caso de uso          | Relaciones complejas y dinámicas | OLTP clásico     | Apps serverless, IoT, rápido acceso |

---

### Resumen técnico de **Neptune**

| Funcionalidad         | Valor                                                      |
| --------------------- | ---------------------------------------------------------- |
| Lenguajes de consulta | Gremlin, SPARQL, OpenCypher (preview)                      |
| Almacenamiento        | Escala automáticamente (sin límite definido)               |
| Lecturas              | Hasta 15 réplicas                                          |
| Failover              | Automático en Multi-AZ                                     |
| Cifrado               | TLS, KMS                                                   |
| Integraciones AWS     | IAM, VPC, CloudTrail                                       |
| Disponibilidad        | Alta, con replicación entre AZ                             |
| Escenarios ideales    | Redes sociales, fraude, recomendaciones, grafos semánticos |

---

**Amazon Neptune** es ideal cuando necesitas consultar relaciones **complejas y profundas entre datos** a gran escala, y cuando el **modelo relacional o de clave-valor ya no es suficiente**. Ofrece un entorno altamente disponible, seguro y escalable para representar conocimiento, relaciones y estructuras de datos complejas de forma natural.

## Amazon Keyspaces (para Apache Cassandra): base de datos NoSQL escalable y totalmente gestionada

**Amazon Keyspaces** es un servicio de base de datos **NoSQL, serverless y totalmente gestionado**, compatible con **Apache Cassandra**, orientado a manejar cargas altamente escalables y con baja latencia. Ofrece disponibilidad y durabilidad mediante replicación en múltiples zonas de disponibilidad, ideal para datos como **IoT, series temporales, métricas, logs o telemetría**.

---

### Características principales de **Keyspaces**

| Característica          | Descripción                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Compatibilidad**      | Compatible con **CQL (Cassandra Query Language)**                          |
| **Modelo de datos**     | Clave-partición + Clave-clustering (similar a tablas relacionales simples) |
| **Arquitectura**        | Totalmente **serverless**, sin servidores que gestionar                    |
| **Gestión**             | Sin necesidad de administrar clústeres Cassandra ni replicación            |
| **Replicación**         | Replicación automática **en 3 zonas de disponibilidad (AZ)**               |
| **Latencia**            | Milisegundos de un solo dígito, incluso a escala masiva                    |
| **Modos de capacidad**  | **Aprovisionado con autoscaling** o **bajo demanda**                       |
| **Escalado automático** | Sí, vertical y horizontal sin intervención manual                          |

---

### Arquitectura técnica

- **Tablas y datos** replicados automáticamente en 3 AZ por región
- **Sin gestión de nodos ni clústeres**
- **Elasticidad completa**: escalar hasta millones de solicitudes por segundo
- Usa particiones y clustering para definir el orden físico y el acceso eficiente

---

### Lenguaje de consultas: CQL

- Compatible con muchas de las APIs y funciones del ecosistema Apache Cassandra
- Operaciones típicas:

  - `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`

- No admite joins ni subconsultas
- Ideal para consultas por **clave de partición**, y uso eficiente de índices secundarios

---

### Seguridad de **Keyspaces**

| Mecanismo         | Descripción                                                    |
| ----------------- | -------------------------------------------------------------- |
| **IAM**           | Control de acceso basado en roles y políticas                  |
| **KMS**           | Cifrado en reposo mediante AWS Key Management Service          |
| **TLS**           | Cifrado en tránsito                                            |
| **VPC Endpoints** | Acceso privado y seguro desde redes internas                   |
| **Auditoría**     | Integración con **CloudTrail** para seguimiento de operaciones |

---

### Resiliencia y respaldo

- Alta disponibilidad mediante replicación multi-AZ
- **Copia de seguridad automatizada** con restauración punto en el tiempo (PITR) de hasta **35 días**
- **Snapshots automáticos y manuales**

---

### Modos de capacidad de **Keyspaces**

| Modo              | Descripción                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| **Bajo demanda**  | Paga solo por las lecturas y escrituras utilizadas; ideal para cargas variables  |
| **Aprovisionado** | Se definen unidades de lectura/escritura (RCU/WCU); escalado automático opcional |

---

### Casos de uso ideales de **Keyspaces**

| Caso de uso                    | Justificación                                                |
| ------------------------------ | ------------------------------------------------------------ |
| **Datos de series temporales** | Alta tasa de escritura y lectura por tiempo (logs, sensores) |
| **Aplicaciones IoT**           | Dispositivos generando eventos en paralelo                   |
| **Catálogos o perfiles**       | Accesos rápidos y repetidos por clave                        |
| **Mensajería o métricas**      | Persistencia de eventos con acceso eficiente                 |
| **Historial de actividad**     | Seguimiento y análisis en sistemas distribuidos              |

---

### Comparación: Keyspaces vs DynamoDB vs Cassandra autogestionado

| Característica       | **Amazon Keyspaces**      | **Amazon DynamoDB**        | **Cassandra en EC2**        |
| -------------------- | ------------------------- | -------------------------- | --------------------------- |
| Modelo               | NoSQL basado en Cassandra | NoSQL propietario AWS      | NoSQL open source           |
| Lenguaje de consulta | CQL                       | API + PartiQL              | CQL                         |
| Serverless           | ✅                        | ✅                         | ❌                          |
| Gestión de clústeres | ❌                        | ❌                         | ✅                          |
| Escalado automático  | ✅                        | ✅                         | ❌ (requiere tuning manual) |
| PITR                 | ✅ (hasta 35 días)        | ✅ (hasta 35 días)         | ❌                          |
| Replicación multi-AZ | Sí                        | Sí                         | Opcional / compleja         |
| Integración AWS      | IAM, KMS, CloudTrail      | IAM, Lambda, Streams, etc. | Limitada                    |

---

### Resumen técnico de **Keyspaces**

| Funcionalidad        | Valor                                         |
| -------------------- | --------------------------------------------- |
| Lenguaje de consulta | CQL (compatible con Apache Cassandra)         |
| Escalado automático  | Sí, sin intervención manual                   |
| Modos de capacidad   | Bajo demanda y aprovisionado con autoscaling  |
| Almacenamiento       | Replicación 3x multi-AZ, sin límite práctico  |
| Copias de seguridad  | Sí, con PITR hasta 35 días                    |
| Seguridad            | IAM, KMS, TLS, VPC                            |
| Latencia             | Milisegundos, a cualquier escala              |
| Serverless           | Completamente                                 |
| Disponibilidad       | Alta (replicación automática en múltiples AZ) |

---

**Amazon Keyspaces** es ideal cuando se necesitan **consultas rápidas y estructuradas por clave de partición**, con **escalabilidad automática**, y sin preocuparse por la infraestructura de Apache Cassandra. Es especialmente útil para aplicaciones con **cargas impredecibles**, **picos temporales**, y modelos **de escritura intensiva**, como sensores IoT o datos temporales.

## Amazon QLDB (Quantum Ledger Database): base de datos inmutable y verificable para registros contables

**Amazon QLDB** es una **base de datos de libros contables (ledger database)** totalmente gestionada, diseñada para registrar cada cambio de forma **inmutable, ordenada y verificable criptográficamente**. Está pensada para aplicaciones donde la integridad del historial de datos es fundamental, como en **transacciones financieras, cadenas de suministro, registros de auditoría o sistemas legales**.

---

### ¿Qué es un ledger (libro contable)?

- Es un **registro cronológico** de transacciones que no pueden ser modificadas ni eliminadas
- Cada cambio en los datos es **registrado permanentemente**
- Se puede **verificar criptográficamente** la integridad del historial completo

> QLDB simula el funcionamiento de un libro mayor tradicional digitalmente y sin necesidad de una red distribuida

---

### Características clave de QLDB

| Característica                 | Descripción                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------ |
| **Totalmente gestionada**      | No requiere provisión ni administración de servidores                          |
| **Serverless**                 | Escala automáticamente con demanda, sin aprovisionamiento manual               |
| **Alta disponibilidad**        | Multi-AZ con replicación automática                                            |
| **Inmutabilidad**              | Una vez que se escribe un dato, **no puede ser eliminado ni sobrescrito**      |
| **Verificación criptográfica** | Cada registro está **encadenado con hashes SHA-256** para prueba de integridad |
| **Rendimiento**                | **2-3 veces más rápido que blockchain frameworks tradicionales**               |
| **Consulta SQL-like**          | Lenguaje propio: PartiQL (basado en SQL)                                       |

---

### Estructura de QLDB

- **Journal**: almacenamiento inmutable de transacciones, ordenadas cronológicamente
- **Ledger**: base de datos contable que contiene uno o más journals y tablas de datos
- **PartiQL**: lenguaje de consulta compatible con SQL para insertar, consultar y rastrear historial
- **Digest**: resumen criptográfico del estado actual del journal, se puede usar para auditorías

---

### Seguridad y gobernanza

| Funcionalidad        | Descripción                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| **IAM**              | Control de acceso basado en roles y usuarios                               |
| **KMS**              | Cifrado en reposo                                                          |
| **TLS**              | Cifrado en tránsito                                                        |
| **CloudTrail**       | Registro de acciones administrativas y operativas                          |
| **Auditoría nativa** | Registro completo y verificable del historial de cualquier cambio de datos |

---

### Diferencias entre QLDB y Amazon Managed Blockchain

| Característica             | **Amazon QLDB**                                    | **Amazon Managed Blockchain**                    |
| -------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| **Descentralización**      | ❌ No                                              | ✅ Sí (Hyperledger Fabric, Ethereum)             |
| **Control**                | Centralizado (AWS administra todo)                 | Distribuido entre participantes                  |
| **Verificabilidad**        | Criptográfica (encadenamiento SHA-256)             | Criptográfica mediante consenso y bloques        |
| **Rendimiento**            | Alto (2-3× más rápido que blockchain)              | Más bajo por mecanismo de consenso               |
| **Uso típico**             | Libros contables internos, trazabilidad, auditoría | Finanzas descentralizadas, consorcios, contratos |
| **Complejidad operativa**  | Baja                                               | Alta (nodos, redes, permisos entre entidades)    |
| **Normativas financieras** | Compatible con entornos regulados centralizados    | Diseñado para entornos colaborativos             |

---

### Casos de uso ideales de QLDB

| Caso de uso                     | Motivo                                                                |
| ------------------------------- | --------------------------------------------------------------------- |
| **Historial financiero**        | Trazabilidad de transacciones, sin posibilidad de alteración          |
| **Cadena de suministro**        | Registro confiable de cambios de estado o propiedad                   |
| **Registros médicos/auditoría** | Rastrear y auditar cambios sin posibilidad de manipulación            |
| **Control de acceso/identidad** | Registrar accesos a recursos de forma inmutable                       |
| **Certificaciones o registros** | Garantizar autenticidad de certificados digitales, títulos o permisos |

---

### Resumen técnico de QLDB

| Funcionalidad                 | Valor                                                         |
| ----------------------------- | ------------------------------------------------------------- |
| Inmutabilidad                 | Sí, basada en journal criptográficamente encadenado           |
| Lenguaje de consulta          | PartiQL (estilo SQL)                                          |
| Rendimiento                   | Milisegundos de latencia, mejor que blockchains tradicionales |
| Cifrado                       | En tránsito (TLS) y en reposo (KMS)                           |
| Replicación Multi-AZ          | Sí, automáticamente                                           |
| Verificabilidad criptográfica | Digest + hashes encadenados (SHA-256)                         |
| Integración con AWS           | IAM, CloudTrail, KMS, VPC                                     |
| Serverless                    | Sí                                                            |

---

**Amazon QLDB** es la mejor opción cuando se necesita registrar cada modificación en una base de datos de manera **inmutable, rastreable y auditable**, sin la sobrecarga de administrar una red blockchain. Es ideal para organizaciones que requieren **confianza en los datos históricos sin ceder el control a un sistema descentralizado**.

## Amazon Timestream: base de datos de series temporales totalmente gestionada y optimizada para IoT y análisis en tiempo real

**Amazon Timestream** es un servicio de **base de datos de series temporales (time series)** **serverless, escalable y de alto rendimiento**, diseñado para almacenar, procesar y analizar grandes volúmenes de datos generados por **sensores, métricas, logs y eventos temporales**.

---

### Características clave

| Característica                       | Descripción                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| **Totalmente gestionada**            | No hay que aprovisionar, parchar ni escalar manualmente                      |
| **Serverless**                       | Escala automáticamente en función de la carga                                |
| **Altísimo rendimiento**             | Hasta **1000× más rápido y 1/10 del costo** comparado con bases relacionales |
| **Almacenamiento jerárquico**        | Datos recientes en **memoria**, históricos en **almacenamiento magnético**   |
| **Motor de consultas especializado** | Con funciones integradas para análisis de series temporales                  |
| **Seguridad**                        | Cifrado **en tránsito (TLS)** y **en reposo (KMS)**                          |
| **Escala masiva**                    | Almacena y analiza **billones de eventos por día**                           |

---

### Arquitectura de almacenamiento

Timestream organiza los datos en dos capas:

1. **Almacenamiento en memoria**

   - Para datos recientes y de acceso frecuente
   - Consultas ultrarrápidas

2. **Almacenamiento magnético**

   - Para datos históricos
   - Coste optimizado
   - Retención definida por política de tablas (por ejemplo: 1 semana en memoria, 1 año en disco)

---

### Lenguaje de consultas

- Usa una sintaxis SQL extendida con **funciones integradas para series temporales**, como:

  - `time_series()`, `bin()`, `approx_percentile()`, `rate()`, `interpolate_linear()`

- Permite agrupar por ventanas de tiempo (`GROUP BY bin(time, 5m)`), interpolar datos faltantes y detectar anomalías

---

### Integraciones nativas de entrada (Ingestion)

| Fuente de datos                         | Modo de integración             |
| --------------------------------------- | ------------------------------- |
| **AWS IoT Core**                        | Directo o mediante Lambda       |
| **Kinesis Data Streams (KDS)**          | Vía Lambda, Flink o Firehose    |
| **Amazon MSK (Kafka)**                  | Procesado con Lambda o Flink    |
| **Prometheus / Telegraf**               | Exportadores con soporte nativo |
| **IoT Analytics / SDKs personalizados** | Mediante REST o conexión JDBC   |

---

### Integraciones de salida (Visualización y análisis)

| Destino               | Uso                                                    |
| --------------------- | ------------------------------------------------------ |
| **Amazon QuickSight** | Dashboards en tiempo real                              |
| **Amazon SageMaker**  | Análisis predictivo y modelos ML con series temporales |
| **Grafana**           | Visualización con plugin nativo de Timestream          |
| **Conexiones JDBC**   | Herramientas de BI personalizadas                      |

---

### Casos de uso ideales de Timestream

| Caso de uso                      | Justificación                                                       |
| -------------------------------- | ------------------------------------------------------------------- |
| **IoT (sensores, dispositivos)** | Datos por segundo/minuto, alta ingestión y consultas rápidas        |
| **Métricas de infraestructura**  | CPU, memoria, disco, latencia — similares a Prometheus o CloudWatch |
| **Monitoreo de aplicaciones**    | Series temporales generadas por microservicios                      |
| **Detección de anomalías**       | Análisis de comportamiento y eventos atípicos                       |
| **Análisis de logs y eventos**   | Acceso optimizado a grandes cantidades de registros cronológicos    |

---

### Ventajas frente a bases de datos tradicionales

| Comparación               | **Timestream**                               | **Base de datos relacional (ej. RDS)**       |
| ------------------------- | -------------------------------------------- | -------------------------------------------- |
| Optimizado para tiempo    | ✅ Sí                                        | ❌ No                                        |
| Almacenamiento jerárquico | ✅ Memoria + disco por política              | ❌ Todo en un solo tipo de almacenamiento    |
| Escalado automático       | ✅                                           | ❌ Manual                                    |
| Serverless                | ✅                                           | ❌ No                                        |
| Consultas especializadas  | ✅ Funciones de series temporales            | ❌ Solo SQL estándar                         |
| Costo                     | ⚡ 1/10 del coste de soluciones relacionales | ❌ Más costoso para datos de alta frecuencia |

---

### Resumen técnico de Timestream

| Elemento              | Valor                                             |
| --------------------- | ------------------------------------------------- |
| Tipo de base de datos | Series temporales (NoSQL)                         |
| Serverless            | Sí                                                |
| Escalado automático   | Sí                                                |
| Almacenamiento        | Memoria (rápido) + magnético (económico)          |
| Seguridad             | TLS (en tránsito), KMS (en reposo)                |
| Motor de consultas    | SQL extendido con funciones temporales            |
| Retención configurada | Definida por política por tabla                   |
| Ingreso de datos      | IoT, Kinesis, Prometheus, Kafka, Telegraf, Lambda |
| Salida/análisis       | QuickSight, SageMaker, Grafana, JDBC              |

---

**Amazon Timestream** es ideal para escenarios donde se requiere **recoger, almacenar y consultar grandes volúmenes de datos en función del tiempo**, con la capacidad de escalar automáticamente, optimizar costos y ejecutar análisis complejos sin sacrificar rendimiento. Una excelente opción para IoT, monitoreo de sistemas y análisis en tiempo real.
