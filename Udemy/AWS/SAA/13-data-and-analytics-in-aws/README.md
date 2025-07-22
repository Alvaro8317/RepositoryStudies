# Datos y analíticas en AWS

## Amazon Athena: servicio serverless para análisis interactivo de datos en S3 mediante SQL

**Amazon Athena** es un servicio **serverless** que permite **consultar datos directamente en S3 usando SQL estándar (ANSI)**, sin necesidad de mover los datos ni configurar servidores. Es ideal para análisis ad hoc, inteligencia empresarial, dashboards, e integración con servicios como **Amazon QuickSight, Metabase o Redash**.

---

### Características principales

| Característica             | Descripción                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- |
| **Serverless**             | No requiere infraestructura, solo se paga por los datos analizados            |
| **Consulta directa en S3** | Analiza archivos en formatos abiertos                                         |
| **SQL estándar (ANSI)**    | Lenguaje familiar, sin necesidad de aprender APIs específicas                 |
| **Precio**                 | **\$5 USD por TB escaneado**, con recomendaciones para reducir costos         |
| **Integración**            | Compatible con **QuickSight**, **Glue**, **Lake Formation**, **Lambda**, etc. |

---

### Formatos de archivos soportados

| Formato       | Descripción                                                |
| ------------- | ---------------------------------------------------------- |
| **CSV, JSON** | Comunes, pero menos eficientes en tamaño y velocidad       |
| **Parquet**   | Columnar, comprimido, ideal para ahorrar escaneo           |
| **ORC**       | Columnar, eficiente en almacenamiento y procesamiento      |
| **Avro**      | Binario, útil para registros estructurados y serialización |

> 💡 **Recomendación:** usa formatos columnar **Parquet u ORC** para mejorar el rendimiento y reducir costos.

---

### Costos y optimización

- **\$5 por TB de datos escaneados**
- **Buenas prácticas para reducir el volumen escaneado:**

  - Comprimir archivos (Gzip, Snappy)
  - Usar formatos columnar
  - **Particionar directorios en S3**: estructura como
    `s3://mi-bucket/logs/year=2024/month=07/day=18/`
  - Usar archivos grandes de **más de 128 MB** para minimizar overhead

---

### Integración con AWS Glue

- **Glue Data Catalog**: almacena metadatos de bases y tablas
- **Glue ETL jobs**: transforma datos (ej. convertir JSON → Parquet)
- Athena consulta los datos usando los metadatos del **Glue catalog**

---

### Consultas federadas

Athena permite **consultar datos fuera de S3**, accediendo a múltiples fuentes de datos mediante conectores (que se ejecutan en Lambda):

| Fuente                         | Descripción                                                |
| ------------------------------ | ---------------------------------------------------------- |
| **DynamoDB**                   | Consulta directa sobre tablas NoSQL                        |
| **RDS / Aurora**               | Consulta SQL relacional distribuida                        |
| **CloudWatch Logs**            | Consultas sobre logs históricos almacenados                |
| **ElasticSearch / OpenSearch** | Consultas sobre índices de búsqueda                        |
| **Google BigQuery / Redshift** | (Mediante conectores o JDBC)                               |
| **Sistemas personalizados**    | Puedes crear tus propios conectores para cualquier backend |

---

### Almacenamiento de resultados

- Todos los resultados de las consultas de Athena se almacenan automáticamente en un bucket de S3 configurado (por defecto en `aws-athena-query-results`)
- Puedes configurar el bucket de resultados en cada ejecución

---

### Casos de uso comunes

| Caso de uso                         | Justificación                                                         |
| ----------------------------------- | --------------------------------------------------------------------- |
| **Análisis de registros (logs)**    | Consultar logs de **VPC Flow Logs**, **ELB logs**, **S3 Access Logs** |
| **Dashboard e informes BI**         | Integración nativa con **Amazon QuickSight**, Metabase, etc.          |
| **Data Lake exploratorio**          | Consultas puntuales sobre grandes volúmenes de datos                  |
| **Auditoría y cumplimiento**        | Explorar logs y cambios en CloudTrail desde S3                        |
| **Consulta distribuida (federada)** | Usar SQL para consultar múltiples fuentes sin mover datos             |

---

### Comparación rápida: Athena vs otras opciones

| Característica       | **Athena**               | **Redshift Spectrum**     | **EMR + Hive/Presto**        |
| -------------------- | ------------------------ | ------------------------- | ---------------------------- |
| Infraestructura      | Serverless               | Requiere clúster Redshift | Se debe aprovisionar clúster |
| Lenguaje             | SQL                      | SQL                       | SQL                          |
| Formatos soportados  | Parquet, ORC, JSON, etc. | Similar                   | Similar                      |
| Costo                | \$5/TB                   | Depende del clúster       | Por hora                     |
| Curva de aprendizaje | Baja                     | Media                     | Alta                         |
| Velocidad            | Alta si bien optimizado  | Alta                      | Alta si bien configurado     |

---

### Resumen técnico

| Elemento                     | Valor                                           |
| ---------------------------- | ----------------------------------------------- |
| Tipo de servicio             | Consulta serverless sobre datos en S3           |
| Lenguaje de consulta         | ANSI SQL (extendido)                            |
| Coste                        | \$5 por TB escaneado                            |
| Formatos recomendados        | Parquet, ORC                                    |
| Compresión soportada         | Sí (gzip, snappy, zlib, etc.)                   |
| Glue integration             | Sí, para catálogos y ETL                        |
| Consultas federadas          | Sí, con conectores en Lambda                    |
| Almacenamiento de resultados | Automáticamente en S3                           |
| Escenarios ideales           | Logs, análisis ad hoc, dashboards BI, data lake |

---

**Amazon Athena** es la solución ideal cuando se necesita ejecutar **consultas SQL directamente sobre datos almacenados en S3**, sin levantar infraestructura ni cargar los datos a un motor de base de datos. Su flexibilidad, escalabilidad y facilidad de integración lo hacen una herramienta poderosa para análisis en data lakes.

## Amazon Redshift: almacén de datos OLAP a escala de petabytes, basado en PostgreSQL

**Amazon Redshift** es un **almacén de datos OLAP (procesamiento analítico en línea)** totalmente gestionado por AWS, optimizado para realizar consultas analíticas complejas sobre grandes volúmenes de datos. A diferencia de PostgreSQL tradicional (OLTP), Redshift está diseñado para cargas de trabajo de análisis intensivo, **10 veces más rápido que otras soluciones de data warehouse**, y escala a **petabytes** con consultas paralelizadas en múltiples nodos.

---

### Arquitectura de Redshift

| Componente            | Función                                                               |
| --------------------- | --------------------------------------------------------------------- |
| **Nodo líder**        | Recibe las consultas SQL, planifica, coordina y agrega los resultados |
| **Nodos de cómputo**  | Ejecutan la consulta en paralelo y devuelven los resultados al líder  |
| **Clúster**           | Conjunto de nodos Redshift que funciona como una unidad               |
| **Redshift Spectrum** | Permite consultar directamente datos en S3 sin cargarlos al clúster   |

---

### Características principales de redshift

| Característica                            | Descripción                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------ |
| **Basado en PostgreSQL**                  | Usa una versión modificada, pero **no es OLTP**, sino OLAP                           |
| **Almacenamiento en columnas**            | Mejora el rendimiento de escaneo y reduce el tamaño de los datos                     |
| **Motor de procesamiento paralelo (MPP)** | Divide las consultas en subprocesos ejecutados en paralelo                           |
| **Escala a petabytes**                    | Capacidad de escalar horizontalmente grandes volúmenes de datos                      |
| **Consultas SQL estándar**                | Compatibilidad con SQL para agregaciones, joins, análisis complejos                  |
| **Integración con BI**                    | Compatible con **QuickSight, Tableau, Looker, Power BI**, etc.                       |
| **Pago por uso**                          | Basado en instancias aprovisionadas; opción de **instancias reservadas** para ahorro |

---

### Comparación OLTP vs OLAP

| Característica | **OLTP (ej. RDS PostgreSQL)**         | **OLAP (Redshift)**                        |
| -------------- | ------------------------------------- | ------------------------------------------ |
| Uso principal  | Transacciones rápidas (insert/update) | Análisis de grandes volúmenes de datos     |
| Ejemplo        | Aplicaciones web, ecommerce           | Business Intelligence, informes ejecutivos |
| Consultas      | Cortas, frecuentes                    | Largas, con joins y agregaciones           |
| Almacenamiento | Por filas                             | Por columnas                               |
| Rendimiento    | Bajo en cargas analíticas complejas   | Alto con consultas masivas                 |

---

### Snapshots y recuperación ante desastres

| Tipo de snapshot          | Descripción                                                              |
| ------------------------- | ------------------------------------------------------------------------ |
| **Automáticas**           | Cada 8 horas, cada 5 GB o según cronograma; retención de **1 a 35 días** |
| **Manuales**              | Persisten hasta ser eliminadas                                           |
| **Almacenamiento**        | En **Amazon S3**, incrementales (solo guardan cambios)                   |
| **Restauración**          | Se pueden restaurar a un nuevo clúster                                   |
| **Copias entre regiones** | Se pueden copiar automáticamente snapshots a **otra región** para DR     |

---

### Carga de datos en Redshift

| Método de carga           | Descripción                                                    |
| ------------------------- | -------------------------------------------------------------- |
| **COPY desde S3**         | Alta eficiencia, recomendado para cargas masivas               |
| **Kinesis Data Firehose** | Ingesta automatizada en tiempo casi real                       |
| **JDBC/ODBC**             | Para cargas desde aplicaciones o herramientas de terceros      |
| **Redshift Data API**     | Para invocar operaciones SQL sin mantener conexión persistente |

> 🔸 **Insertar datos en masa es más eficiente** que múltiples inserts pequeños. Siempre que sea posible, agrupa en lotes.

---

### Redshift Spectrum: consulta sobre datos en S3

| Característica              | Detalles                                                                      |
| --------------------------- | ----------------------------------------------------------------------------- |
| **No carga previa**         | Permite ejecutar consultas directamente sobre datos en S3                     |
| **Requiere clúster activo** | Necesita que exista un clúster Redshift activo para ejecutar la consulta      |
| **Usa Glue Catalog**        | Define los metadatos de las tablas externas en Glue o en el catálogo de datos |
| **Soporta formatos**        | Parquet, ORC, Avro, CSV, JSON                                                 |
| **Escala automáticamente**  | Utiliza miles de nodos en segundo plano para la ejecución                     |

---

### Casos de uso ideales

| Caso de uso                        | Justificación                                                           |
| ---------------------------------- | ----------------------------------------------------------------------- |
| **Inteligencia empresarial (BI)**  | Agregaciones, visualizaciones, análisis masivo con SQL                  |
| **Dashboards ejecutivos**          | Uniones de múltiples fuentes para visualización                         |
| **Consultas analíticas complejas** | Join de millones de registros, filtros, ventanas temporales             |
| **Informes diarios/semanales**     | Optimización por almacenamiento columnar                                |
| **Integración con Data Lakes**     | Con **Spectrum**, puedes consultar archivos en S3 como si fueran tablas |

---

### Redshift vs Athena

| Característica          | **Redshift**                                       | **Athena**                   |
| ----------------------- | -------------------------------------------------- | ---------------------------- |
| Tipo de servicio        | OLAP Data Warehouse                                | Consulta serverless sobre S3 |
| Rendimiento             | Mejor en consultas complejas con joins y agregados | Bueno para análisis ad hoc   |
| Persistencia de datos   | Almacenamiento interno                             | Usa S3 directamente          |
| Costo                   | Por hora por nodo (o reservadas)                   | \$5/TB de datos escaneados   |
| Particionamiento        | Manual, por diseño de tablas                       | Mediante carpetas en S3      |
| Requiere clúster activo | Sí                                                 | No                           |

---

### Resumen técnico de Redshift

| Elemento                   | Valor                                              |
| -------------------------- | -------------------------------------------------- |
| Tipo de base de datos      | OLAP (almacén de datos analítico)                  |
| Arquitectura               | Clúster (nodo líder + nodos de cómputo)            |
| Almacenamiento             | Columnar                                           |
| Motor de consultas         | MPP (Massively Parallel Processing)                |
| Redshift Spectrum          | Consulta datos externos directamente desde S3      |
| Rendimiento                | Alta velocidad en consultas complejas              |
| Integración con BI         | QuickSight, Tableau, Power BI, etc.                |
| Carga de datos recomendada | COPY desde S3 o KDF                                |
| Seguridad                  | IAM, VPC, KMS, SSL                                 |
| Snapshots                  | Automáticas y manuales, retención de hasta 35 días |
| Disaster Recovery          | Snapshots replicables a otra región                |

---

**Amazon Redshift** es la opción recomendada para **cargas analíticas pesadas**, integración con herramientas de BI y **consultas complejas sobre grandes volúmenes de datos estructurados**, con opciones para interactuar tanto con datos internos como externos (en S3) gracias a **Redshift Spectrum**. Es una solución robusta para construir **data warehouses empresariales a escala**.

## Amazon OpenSearch: motor de búsqueda y análisis distribuido

**Amazon OpenSearch** (anteriormente Elasticsearch Service) es un servicio gestionado que permite realizar búsquedas avanzadas, coincidencias parciales y análisis sobre grandes volúmenes de datos en tiempo real. A diferencia de bases como DynamoDB, OpenSearch permite búsquedas no estructuradas en **cualquier campo**.

---

### Casos de uso frecuentes

- Análisis de logs y monitoreo
- Búsqueda textual avanzada (por ejemplo, en aplicaciones web)
- Visualización de métricas y dashboards en tiempo real
- Combinación con bases de datos transaccionales para búsquedas secundarias

---

### Comparación conceptual DynamoDB vs OpenSearch

| Característica       | **DynamoDB**                          | **OpenSearch**                                       |
| -------------------- | ------------------------------------- | ---------------------------------------------------- |
| Tipo de base         | NoSQL (claves-valor/documentos)       | Motor de búsqueda distribuido                        |
| Consulta por campo   | Solo por **clave primaria o índices** | Por cualquier campo, soporta coincidencias parciales |
| Lenguaje de consulta | Propietario, basado en expresiones    | DSL propio (no SQL estándar)                         |
| Uso típico           | Lectura rápida por clave              | Búsqueda textual, análisis y agregaciones            |
| Escalado             | Serverless, bajo demanda              | Clúster de instancias                                |
| Complementariedad    | Se usa como almacenamiento principal  | Se complementa con otra BD (como DynamoDB)           |

---

### Ingesta de datos en OpenSearch

| Fuente de datos          | Mecanismo de ingesta                        |
| ------------------------ | ------------------------------------------- |
| **DynamoDB Streams**     | Stream → Lambda → OpenSearch                |
| **Kinesis Data Streams** | KDS → Lambda (transformación) → OpenSearch  |
| **Kinesis Firehose**     | KDF → OpenSearch (sin necesidad de Lambda)  |
| **CloudWatch Logs**      | Filtro de suscripción → Lambda → OpenSearch |
| **AWS IoT**              | IoT → Kinesis / Lambda → OpenSearch         |

---

### Seguridad

- **Autenticación y acceso**: integración con **IAM** y **Amazon Cognito**
- **Cifrado en tránsito**: TLS
- **Cifrado en reposo**: usando **AWS KMS**
- **Control de acceso**: políticas finas por índice y por usuario
- **OpenSearch Dashboards**: interfaz visual incluida para explorar los datos

---

### Ejemplos de patrones de arquitectura

#### 🔹 Patrón 1: DynamoDB + OpenSearch para búsquedas

```plaintext
Usuario → API Gateway → Lambda → DynamoDB
                               ↳ DynamoDB Streams → Lambda → OpenSearch
```

- Las operaciones CRUD se hacen sobre DynamoDB
- Los cambios son replicados a OpenSearch para permitir búsquedas avanzadas

---

#### 🔹 Patrón 2: CloudWatch Logs → OpenSearch

```plaintext
CloudWatch Logs → Filtro de suscripción → Lambda → OpenSearch
```

- Los logs de la aplicación son procesados por Lambda y enviados a OpenSearch

---

#### 🔹 Patrón 3: Ingesta vía Kinesis + transformación

```plaintext
Kinesis Data Streams → Lambda (transforma) → OpenSearch
```

o

```plaintext
Kinesis Data Firehose → Lambda (opcional) → OpenSearch
```

- Para análisis en tiempo casi real, con escalado automático

---

### Ventajas y consideraciones

| Ventaja                                 | Consideración                                    |
| --------------------------------------- | ------------------------------------------------ |
| Búsquedas rápidas y por cualquier campo | Requiere mantenimiento de clúster                |
| Dashboards integrados                   | No es serverless (se pagan nodos por hora)       |
| Complementa bases como DynamoDB         | No reemplaza un motor de almacenamiento primario |
| Integración con servicios de ingesta    | No soporta SQL estándar                          |

---

### Resumen técnico de OpenSearch

| Elemento             | Descripción                                                     |
| -------------------- | --------------------------------------------------------------- |
| Servicio gestionado  | Sí                                                              |
| Compatibilidad       | OpenSearch API y Dashboards                                     |
| Lenguaje de consulta | DSL de OpenSearch (no SQL)                                      |
| Escalado             | Manual o automático en clústeres gestionados                    |
| Seguridad            | IAM, Cognito, TLS, KMS, control por índice                      |
| Integraciones        | Lambda, KDF, KDS, IoT, CloudWatch, DynamoDB                     |
| Visualización        | OpenSearch Dashboards                                           |
| Casos de uso ideales | Logs, monitoreo, análisis de eventos, búsqueda textual flexible |

---

**Amazon OpenSearch** es ideal cuando necesitas **búsquedas flexibles, análisis avanzado y visualización en tiempo real**, y se complementa comúnmente con bases como **DynamoDB** o servicios de streaming como **Kinesis** para habilitar arquitecturas observables, rápidas y escalables.

## Amazon EMR: Clústeres Hadoop y procesamiento de Big Data en AWS

**Amazon EMR (Elastic MapReduce)** es un servicio gestionado que permite crear clústeres de procesamiento distribuido de big data utilizando frameworks como Apache **Hadoop**, **Spark**, **Flink**, **Hive**, **HBase**, **Presto** y más. Es ideal para cargas de trabajo que requieren procesamiento de grandes volúmenes de datos como **ETL**, **aprendizaje automático**, **indexación web** o **análisis de logs**.

---

### Características principales de EMR

- **Administración simplificada**: EMR se encarga del **aprovisionamiento**, **configuración**, **parcheo** y **escalado automático** del clúster.
- **Integración con instancias Spot** para reducción de costos.
- Se puede ejecutar clústeres en **EC2**, **EKS**, **Fargate** o **Outposts**.
- Compatible con almacenamiento en **S3** (como data lake), **HDFS**, **EMRFS** y **Glue Data Catalog**.

---

### Arquitectura del clúster EMR

| Rol del nodo       | Función principal                                                                |
| ------------------ | -------------------------------------------------------------------------------- |
| **Nodo maestro**   | Coordina el clúster: gestiona la distribución de tareas, monitorea, maneja HDFS. |
| **Nodo central**   | Ejecuta tareas y almacena datos intermedios en HDFS. Puede haber varios.         |
| **Nodo de tareas** | Ejecuta tareas de procesamiento únicamente. No mantiene estado. Puede ser Spot.  |

> 🔹 _Los nodos de tareas son opcionales y típicamente usados como instancias Spot para tareas transitorias y económicas._

---

### Opciones de compra de instancias EC2

| Tipo de instancia | Características principales                                          |
| ----------------- | -------------------------------------------------------------------- |
| **Bajo demanda**  | Pago por hora, fiable, no se termina inesperadamente                 |
| **Reservadas**    | Compromiso de 1 o 3 años, ahorro significativo, para cargas estables |
| **Spot**          | Muy económicas, pueden interrumpirse, ideales para nodos de tarea    |

---

### Tipos de clúster

| Tipo de clúster       | Descripción                                                           |
| --------------------- | --------------------------------------------------------------------- |
| **De larga duración** | Persiste para múltiples trabajos o sesiones interactivas              |
| **Transitorio**       | Se termina automáticamente tras finalizar el trabajo (ideal para ETL) |

---

### Integraciones comunes

- **S3**: Fuente/destino de datos con **EMRFS**
- **Glue Data Catalog**: Para metadatos y descubrimiento de datos
- **Athena / Redshift / QuickSight**: Como herramientas de análisis sobre los resultados
- **IAM**: Control de acceso granular
- **CloudWatch**: Para logs y métricas del clúster
- **Auto Scaling**: Horizontal o manual para nodos Core y Task

---

### Casos de uso

- Procesamiento de **grandes volúmenes de datos** (ETL, batch)
- **Aprendizaje automático** con Spark MLlib
- **Transformación de datos** para data lakes
- **Análisis interactivo** con Presto
- **Indexación y análisis de logs** para motores de búsqueda

---

### Comparación con otros servicios

| Servicio   | Enfoque principal                      | Diferencia clave                                         |
| ---------- | -------------------------------------- | -------------------------------------------------------- |
| **Athena** | Consultas ad-hoc SQL sobre datos en S3 | Totalmente serverless, sin gestión de clústeres          |
| **Glue**   | ETL serverless                         | Menor control, ideal para cargas más simples             |
| **EMR**    | Procesamiento big data personalizado   | Mayor control, elección de frameworks, escalado flexible |

---

### Resumen técnico de EMR

| Elemento                | Valor                                               |
| ----------------------- | --------------------------------------------------- |
| Frameworks soportados   | Hadoop, Spark, Hive, HBase, Flink, Presto, etc.     |
| Nodos del clúster       | Maestro, Centrales, Tareas (opcional, spot)         |
| Tipos de instancias     | Bajo demanda, reservadas, spot                      |
| Almacenamiento de datos | S3 (EMRFS), HDFS, Glue Data Catalog                 |
| Escalabilidad           | Auto Scaling con políticas o manual                 |
| Ejecución               | Larga duración o transitoria                        |
| Costo                   | Pago por hora/segundo de las instancias del clúster |
| Seguridad               | IAM, KMS, VPC, SG, cifrado en tránsito y en reposo  |

---

**EMR** es una solución altamente flexible y potente para procesar grandes volúmenes de datos con tecnologías de código abierto, manteniendo el control de infraestructura, frameworks y coste. Ideal para empresas que requieren personalización avanzada en su arquitectura de datos distribuida.

## Amazon QuickSight: Análisis empresarial visual e inteligente con AWS

**Amazon QuickSight** es un servicio de inteligencia empresarial (BI) totalmente gestionado, que permite crear **paneles interactivos (dashboards)** y realizar análisis ad hoc sobre datos provenientes de diversas fuentes. Se destaca por su **alta escalabilidad**, **motor de machine learning**, y modelo de **precios por sesión**, lo que lo hace ideal tanto para usuarios ocasionales como frecuentes.

---

### Características clave

- **Motor SPICE (Super-fast, Parallel, In-memory Calculation Engine)**: Motor de computación en memoria que permite análisis rápidos sobre millones de filas sin cargar repetidamente los datos desde la fuente.
- **Machine Learning integrado**: Detección de anomalías, predicciones, generación automática de insights con lenguaje natural (NLQ).
- **Modelo serverless y escalable**: No requiere infraestructura, y escala automáticamente para miles de usuarios simultáneos.
- **Pago por sesión**: En edición Enterprise, se paga por cada sesión iniciada (útil para usuarios que consultan ocasionalmente).

---

### Casos de uso típicos

- Análisis de datos empresariales (ventas, marketing, operaciones)
- Creación de dashboards interactivos y visuales
- Monitoreo de KPIs en tiempo real
- Análisis ad hoc con capacidad de filtrar, segmentar y explorar

---

### Integración con fuentes de datos

QuickSight se conecta fácilmente a una variedad de servicios de AWS y fuentes externas:

| Fuente de datos en AWS | Fuente externa                   |
| ---------------------- | -------------------------------- |
| RDS                    | Salesforce                       |
| Aurora                 | Jira                             |
| Redshift               | Archivos CSV, JSON, TSV          |
| Athena                 | Bases de datos SQL y NoSQL       |
| S3                     | Servidores locales mediante ODBC |
| Timestream             |                                  |

---

### Ediciones disponibles

| Edición        | Características principales                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| **Standard**   | Ideal para análisis individual. Sin control granular de seguridad ni usuarios corporativos.   |
| **Enterprise** | Soporte para usuarios/grupos, control de acceso a nivel de fila/columna, integración con SSO. |

> 🔐 _Solo en edición Enterprise se puede aplicar CLS (Column-Level Security) y RLS (Row-Level Security)._

---

### Usuarios y grupos en QuickSight

- Se definen dentro del entorno de QuickSight, **no dependen de IAM**.
- Se pueden asignar permisos a nivel de dashboard, dataset, carpeta o columna.
- Soporta integración con directorios corporativos (SSO) mediante SAML 2.0.

---

### Conceptos clave

| Elemento      | Descripción                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| **Dataset**   | Fuente de datos preparada para análisis. Puede ser directa o SPICE.         |
| **Analysis**  | Vista editable en la que se crean gráficos, filtros y cálculos.             |
| **Dashboard** | Vista de solo lectura de un análisis, compartible con otros usuarios.       |
| **SPICE**     | Motor en memoria, permite mayor velocidad y disponibilidad offline parcial. |
| **Visual**    | Gráfico individual dentro de un análisis o dashboard.                       |

---

### Seguridad y gobernanza

- Cifrado en tránsito y en reposo con **KMS**
- Control de acceso por usuario, grupo, dataset, carpeta
- **RLS/CLS** para ocultar datos según perfil del usuario
- **Auditoría y logs** mediante CloudTrail

---

### Comparación con otras herramientas BI

| Herramienta             | Descripción breve                                       |
| ----------------------- | ------------------------------------------------------- |
| **Athena + QuickSight** | Análisis sobre datos en S3 usando SQL y visualizaciones |
| **Redshift + Tableau**  | Análisis OLAP con herramienta externa más avanzada      |
| **Glue + QuickSight**   | Transformación ETL + visualización final                |

---

### Ventajas principales

- Sin servidor, sin necesidad de infraestructura
- Alta escalabilidad
- Integración nativa con todo el ecosistema de AWS
- Pago por uso en Enterprise
- Motor SPICE para consultas rápidas
- Ideal para dashboards empresariales compartidos con usuarios no técnicos

---

QuickSight es la solución nativa de AWS para **analítica visual, rápida y empresarial**, ideal para organizaciones que desean tener **información accionable sin gestionar infraestructura de BI**.

## AWS Lake Formation: Centralización de acceso y creación eficiente de lagos de datos

**Lake Formation** es un servicio completamente gestionado que permite configurar, proteger y administrar un **lago de datos** de forma rápida y sencilla, centralizando tanto los datos como los controles de acceso para múltiples servicios de análisis.

---

### Propósito principal de Lake Formation

- Facilita la creación de un **Data Lake** en AWS sobre Amazon S3, combinando datos estructurados y no estructurados.
- Automatiza pasos clave del proceso como:

  - Descubrimiento de datos
  - Limpieza y transformación
  - Ingesta
  - Deduplicación

- Permite implementar **controles de acceso granulares** (columna, fila, tabla) desde un solo lugar, incluso para múltiples consumidores (Athena, Redshift Spectrum, EMR, QuickSight, etc.).

---

### Relación con AWS Glue

- **Lake Formation se basa en AWS Glue**:

  - Reutiliza Glue Crawlers para descubrir esquemas
  - Comparte el **Glue Data Catalog** como fuente de metadatos
  - Puede ejecutar Glue Jobs para transformación de datos

- Agrega una **capa adicional de control de acceso centralizado** y avanzado que Glue por sí solo no ofrece.

---

### Control de acceso centralizado

Antes de Lake Formation, los permisos debían configurarse en múltiples niveles:

| Nivel      | Ejemplo de control de acceso                 |
| ---------- | -------------------------------------------- |
| IAM        | Permisos por usuario/rol a nivel de servicio |
| S3         | Políticas de bucket y objetos                |
| Athena     | Acceso por base de datos o tabla             |
| QuickSight | Seguridad por conjunto de datos              |

Lake Formation permite **centralizar todo esto** con políticas que controlan:

- Acceso a **tablas o columnas específicas**
- Visibilidad condicional para diferentes usuarios
- Permisos compartidos entre cuentas (con cross-account access)
- Visibilidad basada en contexto o atributos

---

### Ejemplo: Seguridad a nivel de columna

Supón que tienes una tabla de empleados con las siguientes columnas:

- `id`, `nombre`, `departamento`, `salario`

Puedes usar Lake Formation para definir que:

- El equipo de RRHH vea todos los campos
- El equipo financiero solo vea `id`, `departamento`, `salario`
- Otros usuarios solo vean `id` y `departamento`

Esto se hace sin necesidad de duplicar tablas o datasets.

---

### Principales ventajas

| Ventaja                                                 | Descripción                                                     |
| ------------------------------------------------------- | --------------------------------------------------------------- |
| **Totalmente gestionado**                               | No requiere aprovisionamiento de servidores                     |
| **Centralización de permisos**                          | Acceso detallado por columna, fila, tabla, base de datos        |
| **Integración nativa**                                  | Compatible con Glue, Athena, Redshift Spectrum, EMR, QuickSight |
| **Soporte para datos estructurados y no estructurados** | Permite analizar todo tipo de fuentes                           |
| **Escenarios multi cuenta**                             | Permite compartir recursos entre cuentas con control detallado  |

---

### Flujo general con Lake Formation

1. **Crear el Data Lake** sobre S3.
2. **Ingerir los datos** usando Glue ETL, Glue Crawlers o servicios de streaming como Kinesis.
3. **Catalogar los datos** en el Glue Data Catalog.
4. **Aplicar políticas de acceso** a través de Lake Formation.
5. **Analizar los datos** con Athena, Redshift Spectrum, EMR o QuickSight con los permisos ya gestionados.

---

### Casos de uso frecuentes de LakeFormation

- Centralizar el acceso a datos para múltiples equipos o unidades de negocio
- Definir accesos diferenciales para datos sensibles (ej. cumplimiento GDPR)
- Compartir datasets entre cuentas AWS sin duplicar datos
- Mejorar la gobernanza de datos en entornos analíticos complejos

---

**Lake Formation** permite una gestión moderna de lagos de datos con enfoque en **gobernanza, escalabilidad y control de acceso granular**, sin la necesidad de procesos manuales complicados o desarrollos personalizados.

## Kinesis Data Analytics para SQL y Apache Flink

**Kinesis Data Analytics (KDA)** es un servicio totalmente gestionado y serverless que permite procesar y analizar flujos de datos en tiempo real mediante SQL o Apache Flink, sin necesidad de administrar servidores o clústeres.

---

### Kinesis Data Analytics con SQL

- **Enfocado a desarrolladores que usan SQL**
- Permite escribir sentencias SQL estándar para realizar:

  - Agregaciones en tiempo real
  - Ventanas de tiempo (tumbling, sliding, session)
  - Filtros y proyecciones de datos
  - Enriquecimiento de datos

#### Fuentes de datos

- Kinesis Data Streams (KDS)
- Kinesis Data Firehose (KDF)

#### Destinos posibles

- Kinesis Data Streams
- Kinesis Data Firehose

#### Características destacadas

| Característica                      | Descripción                                                              |
| ----------------------------------- | ------------------------------------------------------------------------ |
| **Enriquecimiento de datos**        | Posible mediante archivos de referencia alojados en S3                   |
| **Escalado automático**             | Adapta automáticamente la capacidad a la carga                           |
| **Pago por consumo real**           | Solo se cobra por los recursos utilizados                                |
| **Transformaciones en tiempo real** | Los resultados se pueden enviar a otros servicios para consumo inmediato |

#### Ejemplo de flujo con SQL

```text
Kinesis Data Stream (fuente)
   ↓
Kinesis Data Analytics con SQL
   - SELECT sensor_id, AVG(temp) OVER 1 MINUTE ...
   - JOIN con archivo CSV en S3
   ↓
Kinesis Firehose (destino) → S3, Redshift, OpenSearch
```

---

### Kinesis Data Analytics con Apache Flink

- Permite ejecutar **aplicaciones personalizadas en streaming** utilizando:

  - Java
  - Scala
  - SQL

#### Capacidades de Flink

- Procesamiento **estadoful** de eventos
- Tolerancia a fallos (checkpoints, backup)
- **Computación paralela** y en clúster
- **Programación avanzada** (por ejemplo, uniones, ventanas personalizadas, patrones de eventos con CEP)

#### Orígenes y destinos

| Tipo         | Servicios compatibles                                        |
| ------------ | ------------------------------------------------------------ |
| **Orígenes** | Kinesis Data Streams, Amazon MSK, Apache Kafka (no Firehose) |
| **Destinos** | Kinesis Data Streams, MSK, S3, Redshift, etc.                |

> 🔴 **Importante:** Apache Flink **no puede leer desde Kinesis Data Firehose**, ya que este no expone un stream legible en tiempo real.

#### Flujo con Flink

```text
MSK / KDS (origen)
   ↓
Kinesis Data Analytics con Apache Flink (código Java/Scala)
   ↓
Kinesis Data Streams / S3 / Redshift / OpenSearch (destino)
```

#### Características adicionales

- Aplicaciones resilientes con backups automáticos
- Integración con métricas y logs de CloudWatch
- Procesamiento con **baja latencia y alta capacidad de paralelismo**

---

### Comparación rápida entre SQL y Apache Flink

| Característica          | SQL                           | Apache Flink                     |
| ----------------------- | ----------------------------- | -------------------------------- |
| Lenguaje                | SQL estándar                  | Java, Scala, SQL (Flink SQL)     |
| Complejidad             | Baja                          | Alta (pero más flexible)         |
| Escenarios recomendados | Filtros, agregaciones simples | Procesamiento complejo, patrones |
| Escalado automático     | Sí                            | Sí                               |
| Enriquecimiento con S3  | Sí                            | Sí                               |
| Lectura desde Firehose  | ✅                            | ❌                               |
| Latencia                | Baja                          | Muy baja                         |

---

### Casos de uso comunes de KDS

- **SQL**: detección de anomalías en sensores IoT, cálculo de KPIs en tiempo real, agregaciones por ventana.
- **Flink**: procesamiento de logs, detección de fraudes, correlación de eventos, machine learning en streaming.

---

**Kinesis Data Analytics**, ya sea con **SQL o Apache Flink**, es una solución robusta para ejecutar análisis en tiempo real directamente sobre flujos de datos, con gran integración en el ecosistema de AWS y adecuada tanto para casos simples como para arquitecturas complejas de streaming.

### Comparación entre Amazon Kinesis Data Streams (KDS) y Amazon MSK (Managed Streaming for Apache Kafka)

| Característica                          | **Kinesis Data Streams (KDS)**                                 | **Amazon MSK (Kafka)**                                           |
| --------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Naturaleza**                          | Servicio propietario de AWS                                    | Plataforma de streaming basada en Apache Kafka (open source)     |
| **Administración**                      | Totalmente gestionado                                          | Totalmente gestionado                                            |
| **Modelo de datos**                     | Flujos con **shards** (fragmentos)                             | **Temas con particiones**                                        |
| **Particiones**                         | Shards se pueden dividir o fusionar dinámicamente              | Particiones son fijas; solo se pueden **agregar**, no eliminar   |
| **Protocolo**                           | Propietario de AWS (SDK, KPL/KCL)                              | Compatible con protocolo Kafka (producers/consumers estándar)    |
| **Tamaño máximo de registro**           | **1 MB por registro**                                          | **1 MB por defecto**, pero **configurable**                      |
| **Retención de datos**                  | De **1 a 365 días**                                            | Configurable desde horas hasta días o indefinido                 |
| **Reproducción de datos (replay)**      | Soportado, gracias al almacenamiento inmutable                 | Soportado mientras los datos estén retenidos                     |
| **Ordenación**                          | Garantizada dentro de un shard por clave de partición          | Garantizada dentro de una partición                              |
| **Escalado**                            | Manual (modo aprovisionado) o automático (modo on-demand)      | Basado en número de particiones y tamaño del clúster             |
| **Integración con otros servicios AWS** | Alta (Lambda, Firehose, Analytics, etc.)                       | Media (requiere más configuración, uso de conectores Kafka)      |
| **Cifrado en tránsito**                 | TLS                                                            | TLS o plaintext (ambos disponibles)                              |
| **Cifrado en reposo**                   | KMS                                                            | KMS o AWS-managed keys con EBS                                   |
| **VPC**                                 | Compatible con endpoints VPC                                   | Se implementa dentro de una VPC multi-AZ                         |
| **Tolerancia a fallos**                 | Sí (alta disponibilidad por diseño del servicio)               | Sí (multi-AZ con recuperación automática de brokers y ZooKeeper) |
| **Costo y complejidad de operación**    | Menor complejidad, menos flexible                              | Mayor control y flexibilidad, mayor complejidad operativa        |
| **Uso recomendado**                     | Integración rápida y sencilla con AWS, análisis en tiempo real | Migración desde Kafka, integración con herramientas Kafka        |

---

### Conclusiones

- **KDS** es ideal si necesitas una solución _nativa de AWS_, más fácil de usar, con integración profunda con otros servicios y suficiente para la mayoría de escenarios de streaming estándar.
- **MSK** es ideal si ya usas **Apache Kafka**, necesitas _compatibilidad completa con su ecosistema_, o requieres configuraciones más personalizadas (como modificar tamaño de mensaje, retención, replicación, etc.).

Ambas opciones permiten transmitir, almacenar y procesar flujos de datos, pero **KDS prioriza simplicidad** y **MSK prioriza compatibilidad y flexibilidad**.

### Arquitectura Serverless para un Pipeline de Ingesta de Big Data

#### 1. **Recopilación de datos en tiempo real (IoT Core → Kinesis Data Streams)**

- Los dispositivos IoT envían datos continuamente.
- **AWS IoT Core** actúa como gateway seguro y administrado.
- Los datos se enrutan directamente a **Kinesis Data Streams (KDS)** para procesarlos en tiempo real.

#### 2. **Transformación y almacenamiento (KDS → Firehose → Lambda → S3)**

- **Kinesis Data Firehose** toma los datos desde KDS.
- Aplica una función **Lambda para transformación en tiempo de ejecución** (por ejemplo, limpieza o enriquecimiento de datos).
- Firehose entrega los datos transformados a un **bucket S3**.

#### 3. **Procesamiento adicional (SQS → Lambda → Athena → S3 Reportes)**

- Se puede añadir una **cola SQS** para desacoplar el procesamiento.
- Una **Lambda** actúa como consumidor de SQS, y lanza **consultas en Athena** usando SQL para procesar los datos almacenados en S3.
- Athena puede generar resultados en otro bucket **S3 de reportes**.

#### 4. **Visualización y almacenamiento analítico (QuickSight / Redshift)**

- Los datos procesados y almacenados en S3 pueden:
  - Ser consultados directamente desde **Amazon QuickSight** para dashboards e informes interactivos.
  - O ser cargados a **Amazon Redshift** como almacén de datos OLAP para consultas analíticas más complejas y agregaciones de grandes volúmenes.

---

### Diagrama resumen

```plaintext

Dispositivos IoT
↓
AWS IoT Core
↓
Kinesis Data Streams
↓
Kinesis Data Firehose
↓ → (opcional) → SQS → Lambda → Athena → S3 (reportes)
Lambda (transformación)
↓
S3 (raw / staging)
↓
QuickSight / Redshift
```

---

### Características Clave del Pipeline

| Componente            | Rol                                                    |
| --------------------- | ------------------------------------------------------ |
| IoT Core              | Recepción de datos de sensores / dispositivos          |
| KDS                   | Canalización de datos en tiempo real                   |
| Firehose              | Transformación básica + entrega a S3                   |
| Lambda                | Transformación personalizada / procesamiento disparado |
| SQS                   | Desacoplamiento del procesamiento                      |
| Athena                | Consultas ad hoc en S3 con SQL                         |
| S3                    | Almacenamiento centralizado, staging y resultados      |
| QuickSight / Redshift | Visualización de datos / análisis profundo             |

---

Este enfoque es **completamente serverless**, escalable y optimizado para escenarios de big data en tiempo real con transformación, análisis y visualización.
