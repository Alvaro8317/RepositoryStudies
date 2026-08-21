# Amazon OpenSearch Service

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon OpenSearch Service** es un motor de búsqueda **totalmente gestionado** — antes conocido
como **Amazon Elasticsearch Service** (renombrado a OpenSearch).

Incluye además **OpenSearch Dashboards**, una herramienta para visualización de datos en tiempo
real sobre los datos almacenados en OpenSearch.

## Casos de uso

- **Análisis de datos en tiempo real**: analizar logs o métricas de aplicaciones para entenderlas
  mejor.
- **Dashboards**: visualizaciones, gráficos y tablas a partir de los datos — puede actuar como
  backend de herramientas de BI.
- **Búsqueda**: capacidad de búsqueda como núcleo del servicio.

## Características clave

- Modelo de precios **pay-per-use**: solo se paga por los recursos usados.
- Servicio **totalmente gestionado**: AWS gestiona mantenimiento, configuración, seguridad,
  hardware y actualizaciones de software.
- Puede desplegarse como clústeres gestionados o como una opción **serverless** (sin gestionar en
  absoluto la arquitectura subyacente).
- **Escalable**: se pueden añadir o quitar recursos sin interrumpir el servicio.

> ⚠️ Por defecto (fuera de la opción serverless) el escalado **no es automático** — hay que ajustar
> la configuración manualmente para escalar, salvo que se use la arquitectura serverless.

- Integraciones: **AWS Lambda** (ejecutar código), **Kinesis** (streaming en tiempo real), **S3**
  (almacenamiento de datos).
- Alta disponibilidad: despliegue **multi-AZ**.
- Snapshots automatizados para poder recuperar datos de fechas anteriores.
- Monitorización integrada con **CloudWatch** y **CloudTrail**.

## OpenSearch vs. CloudWatch Logs / CloudWatch Metrics

Es fácil confundirlos porque ambos sirven para monitorizar y consultar logs/métricas, pero
resuelven necesidades distintas:

| Aspecto | CloudWatch (Logs + Metrics) | OpenSearch |
| --- | --- | --- |
| Propósito principal | Monitorización **nativa** de servicios AWS: métricas operativas, logs y alarmas | Motor de **búsqueda y analítica de propósito general** sobre cualquier tipo de dato (logs, texto libre, documentos de negocio...) |
| Origen de los datos | Generado automáticamente por servicios AWS, o enviado vía agentes/SDK | Cualquier fuente — logs de CloudWatch, aplicaciones, dispositivos IoT, datos de negocio, etc. — normalmente ingestado vía Kinesis Data Firehose, Logstash, agentes, etc. |
| Capacidad de búsqueda | Limitada: **CloudWatch Logs Insights** permite consultas tipo query sobre logs, pero no es un motor de búsqueda full-text | Motor de **búsqueda full-text** avanzado (basado en Lucene): relevancia, agregaciones complejas, fuzzy search, etc. |
| Retención/almacenamiento | Retención configurable por log group; pensado para operación a corto/medio plazo | Pensado para almacenar y analizar grandes volúmenes de datos a más largo plazo, organizados en índices con shards/réplicas |
| Visualización | CloudWatch Dashboards (básico) | **OpenSearch Dashboards**, mucho más rico para exploración interactiva |
| Gestión de infraestructura | Totalmente gestionado, sin clúster que administrar | Servicio gestionado, pero con clúster/nodos configurables (o la opción serverless) |

> ⚠️ En la práctica, no suelen usarse el uno en lugar del otro, sino **juntos**: CloudWatch Logs
> captura los logs de forma nativa, y desde ahí se pueden exportar a OpenSearch (por ejemplo, vía
> una **suscripción de CloudWatch Logs** hacia Kinesis Data Firehose o directamente a OpenSearch)
> para obtener búsquedas más potentes, dashboards más ricos, o correlacionar esos logs con datos
> que no son de AWS.

## Componentes de datos

| Componente    | Descripción                                                                                                                                                                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Documento** | Una única pieza de información — comparable a una fila de una tabla o un registro de una base de datos. Tiene siempre un **ID único** para localizarlo.                                                                                                                             |
| **Tipo**      | Concepto de versiones antiguas de OpenSearch/Elasticsearch (previo a la 7.0), usado junto con un índice para dar estructura a los documentos. Ya no se usa desde la 7.0, pero puede seguir apareciendo en aplicaciones antiguas.                                                    |
| **Índice**    | Comparable a una base de datos: agrupa documentos similares y define su esquema (estructura/campos). Se pueden tener varios índices para distintos casos de uso (ej. uno para clientes, otro para productos), cada uno con su propia configuración de rendimiento y almacenamiento. |

## Arquitectura: nodos, clústeres, dominios y shards

### Nodos

Un **nodo** es una instancia individual en ejecución dentro de OpenSearch (el "servidor"). Todo
nodo forma parte de un **clúster**, almacena una porción de los datos y participa en el
procesamiento (indexación de nuevos datos, ejecución de consultas de búsqueda).

Tipos de nodo:

| Tipo de nodo    | Función                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Data node**   | Almacena los datos y ejecuta operaciones de búsqueda y agregaciones.                                                  |
| **Master node** | Gestiona el funcionamiento del clúster: rastrea qué nodos lo componen y decide cómo distribuir los datos entre ellos. |
| **Client node** | Gestiona las solicitudes de búsqueda entrantes y agrega los resultados de los distintos nodos (orquestación).         |

### Clúster y dominio

- Un **clúster** es un conjunto de uno o varios nodos (normalmente varios) que trabajan juntos para
  almacenar y gestionar los datos — aumenta capacidad y disponibilidad: si un nodo falla, otro nodo
  del clúster puede asumir su carga sin pérdida de datos ni downtime.
- **Dominio**: término que usa AWS para referirse a todo el clúster de OpenSearch — el hardware y
  toda la configuración/ajustes asociados.

### Shards

- Los datos de un clúster se distribuyen entre los nodos en forma de **shards** — la unidad
  fundamental de almacenamiento, comparable a **particiones** de un índice.
- Cada índice se divide en varios shards, distribuidos por el clúster; esto permite ejecutar
  operaciones en paralelo a través de varios shards, haciendo la recuperación de datos más
  eficiente.

> ⚠️ El concepto de shard es similar al de **shard en Kinesis Data Streams**.

Dos tipos de shard:

| Tipo de shard     | Función                                                                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Primary shard** | Shard principal — aquí se escriben los datos por primera vez. Su número se especifica al crear el índice; gestiona lectura y escritura.                                                                                              |
| **Replica shard** | Copia de un primary shard. Aporta redundancia (tolerancia a fallos) y puede mejorar el rendimiento de lectura ("réplicas de lectura"). Solo gestiona lecturas, no escrituras. Su número se puede ajustar después de crear el índice. |

- Cada **documento** se somete a un hash y se asigna a un shard específico, por lo que los datos
  quedan distribuidos por todo el clúster; cada shard puede residir en cualquier nodo (según
  configuración y balanceo de carga).
- Cada shard funciona como un **mini motor de búsqueda independiente**, lo que permite a OpenSearch
  gestionar operaciones de búsqueda en paralelo de forma eficiente.

## Gestión y acceso a los datos

De forma práctica, hay tres acciones principales para gestionar y acceder a los datos en
OpenSearch:

1. **Crear un índice**: un índice es el análogo a una base de datos — la colección donde se
   almacenan los documentos. Al crearlo se define su estructura mediante **settings** y
   **mappings**:
   - *Settings*: parámetros como el número de **shards** y de **réplicas**.
   - *Mappings*: ajustes específicos por campo — tipos de datos, tokenización, etc.

   Estos ajustes afectan directamente al rendimiento de búsqueda y a cómo se distribuyen los datos
   en el clúster, por lo que es importante definirlos bien desde el principio.

2. **Añadir o actualizar documentos**: cada documento tiene un **ID**, que puede definirse
   explícitamente o dejar que OpenSearch lo genere automáticamente. Los documentos se pueden
   insertar/actualizar uno a uno, o en **procesos por lotes (bulk)** — más eficiente cuando se
   trabaja con grandes volúmenes de datos.

3. **Buscar**: la acción principal del servicio, para recuperar datos. Incluye desde búsquedas
   simples de palabras clave (ej. buscar todos los documentos que contengan el nombre o la
   categoría de un producto) hasta consultas más complejas sobre varios campos a la vez. Se puede
   hacer tanto mediante llamadas a la **API** como desde la interfaz de **OpenSearch Dashboards**,
   de forma más visual.

## Configuración: rendimiento, seguridad y fiabilidad

- **Dominios**: simplifican la gestión del clúster agrupando todo (hardware, configuración,
  software) en una única unidad manejable. Cada dominio se puede personalizar — número de
  instancias, tipo de instancia, opciones de almacenamiento, etc.
- **Nodos master dedicados**: importantes para la estabilidad del clúster, especialmente en
  producción. Se encargan de las tareas de gestión del clúster (crear/eliminar índices, rastrear
  qué nodos lo componen), sin manejar datos ni consultas de búsqueda — así el clúster sigue
  funcionando con fluidez incluso bajo alta carga.
- **Snapshots**: se toman automáticamente y se almacenan en **S3**, garantizando durabilidad y
  permitiendo restaurar el clúster a un estado anterior sin pérdida de datos. También se pueden
  iniciar **manualmente**, o programarse en un periodo/horario personalizado.

### Qué evitar

- **Usar OpenSearch como base de datos OLTP**: no está optimizado para integridad transaccional —
  para eso conviene una base de datos relacional.
- **Usar OpenSearch para consultas ad hoc pesadas**: aunque permite consultar datos, no es su caso
  de uso principal — para consultas ad hoc, **Athena** suele ser la mejor opción.
- **Crear demasiados shards por índice**: distribuir de más los datos para ganar paralelismo puede
  parecer buena idea, pero el exceso de shards aumenta el overhead de gestión y reduce el
  rendimiento.
- **Usar OpenSearch como almacén de datos único (primary data store)**: es un motor de indexación y
  búsqueda, no una base de datos diseñada para durabilidad e integridad transaccional. Lo
  recomendable es tener una base de datos fiable como almacenamiento primario, y sincronizar con
  OpenSearch solo los datos necesarios para búsqueda/analítica.

### Buenas prácticas de rendimiento

- Vigilar la **presión de memoria** (memory pressure) de la **JVM**: una asignación desequilibrada
  de shards puede sobrecargar unos y dejar otros infrautilizados.

> ⚠️ Tener **demasiados shards** puede, de forma contraintuitiva, **reducir** el rendimiento en vez
> de mejorarlo: el procesamiento distribuido consume memoria, y el overhead de gestión puede pesar
> más que el beneficio del paralelismo.

- Para aliviar la presión de memoria: borrar índices antiguos o no usados, y descargar (archivar)
  datos a un almacenamiento como **Amazon S3 Glacier** — esto reduce el número de shards activos y
  mejora el rendimiento del clúster.

## Seguridad

### Autenticación

Primera línea de defensa — verifica quién es el usuario/programa:

- **Autenticación nativa**: usuarios y roles definidos directamente dentro de OpenSearch.
- **Autenticación externa**: integración con sistemas como **Active Directory**, **Kerberos**,
  **SAML** y **OpenID Connect**.

### Autorización

Una vez autenticado, determina qué puede hacer ese usuario/programa:

- **RBAC (Role-Based Access Control)**: mecanismo principal — se definen roles y se asocian a
  usuarios y grupos.
- **ABAC (Attribute-Based Access Control)**: concede permisos en función de **atributos** del
  usuario.

### Cifrado

- **En tránsito**: OpenSearch proporciona cifrado **TLS** para todas las comunicaciones dentro del
  clúster.
- **En reposo**: proporcionado mediante **plugins** o herramientas de terceros.

### Registro de auditoría (audit logging)

- Los **audit logs** detallados ayudan a identificar y responder a posibles problemas de
  seguridad.
- Las opciones de configuración permiten especificar **qué eventos** se registran dentro de
  OpenSearch.

## OpenSearch Dashboards

**OpenSearch Dashboards** es la herramienta de visualización integrada en OpenSearch — viene
directamente incluida en el servicio, pero en cierto modo funciona también como una herramienta
independiente para explorar y visualizar los datos.

- Permite crear una amplia gama de visualizaciones: gráficos de líneas, de barras, circulares
  (pie), **mapas de calor (heatmaps)**, etc. — útil para hacer más comprensibles consultas
  complejas y agregaciones.
- Se pueden combinar varias visualizaciones en **dashboards personalizados**, totalmente
  configurables.
- Soporta elementos interactivos, como **filtros** y **drill-down**, para profundizar en los datos.

> ⚠️ Conceptualmente es similar a otras herramientas de dashboards como **Power BI**: se construyen
> gráficos y paneles a partir de una fuente de datos — en este caso, los datos almacenados en
> OpenSearch — para analizarlos y visualizarlos con más detalle.

## Tipos (niveles) de almacenamiento

Al crear índices en OpenSearch, los datos se pueden almacenar en distintos **niveles de
almacenamiento (storage tiers)**, según con qué frecuencia se accede a ellos y qué rendimiento se
necesita:

| Nivel | Dónde reside | Rendimiento / coste | Editable |
| --- | --- | --- | --- |
| **Hot storage** | Almacenamiento local de los nodos de datos estándar — instance store de EC2 o volúmenes **EBS** adjuntos a cada nodo | El más rápido; mayor coste | Sí |
| **UltraWarm** | Solución de caché sofisticada combinada con **Amazon S3** | Rendimiento intermedio; coste mucho menor que hot | Solo lectura (se puede mover a hot para editar) |
| **Cold storage** | **Amazon S3**, sin capacidad de cómputo asociada — los índices quedan "desconectados" | El de menor coste; datos inaccesibles hasta reconectar | No accesible directamente |

- **Hot storage** (nivel por defecto): pensado para datos a los que se accede **con frecuencia** y
  que requieren recuperación instantánea — indexación activa, escritura activa, consultas activas.
  Ideal para análisis en tiempo real o logs recientes: cualquier escenario que necesite baja
  latencia.
- **UltraWarm**: forma más rentable de almacenar grandes volúmenes de datos a los que se accede
  **con menos frecuencia** y que no requieren el rendimiento de hot storage — ej. datos algo más
  antiguos o inmutables (logs que ya no se escriben). Es de solo lectura, pero un índice se puede
  **mover de vuelta a hot storage** para poder editarlo, y luego volver a UltraWarm.
- **Cold storage**: optimizado para datos a los que se accede **con poca frecuencia** o datos
  históricos — ej. requisitos de cumplimiento (compliance) que exigen conservar datos antiguos. Es
  la opción de **menor coste**, adecuada para archivado. Para acceder a estos datos hay que
  **reconectar** los índices a nodos UltraWarm; el proceso es relativamente rápido (acceso en
  cuestión de segundos).

> ⚠️ Los tres niveles forman un espectro de rendimiento vs. coste: **hot** (rápido, caro, editable)
> → **UltraWarm** (intermedio, más barato, solo lectura salvo que se mueva a hot) → **cold**
> (más barato, sin cómputo propio, requiere reconexión para acceder).

## Fiabilidad y eficiencia

### Replicación entre clústeres (cross-cluster replication)

- Función que permite **copiar y sincronizar datos de un clúster a otro**, aumentando la
  disponibilidad de los datos y sirviendo como opción de **recuperación ante desastres (DR)**.
- Si un clúster cae por un fallo de hardware, un problema de red u otra interrupción, el otro
  clúster replicado puede tomar el relevo sin perder acceso a los datos.
- Importante quando se necesita **alta disponibilidad** y no se puede permitir downtime.

### Gestión de índices (Index State Management, ISM)

- Automatiza el **ciclo de vida completo de un índice**, desde su creación hasta su eliminación,
  mediante **políticas** que actúan según criterios especificados.
- Muy útil combinado con los distintos [niveles de almacenamiento](#tipos-niveles-de-almacenamiento):
  en vez de decidir manualmente qué datos van a cada nivel, se puede automatizar el movimiento de
  índices entre hot, UltraWarm y cold storage según su antigüedad/uso.
- También permite automatizar acciones como eliminar índices antiguos, o pasarlos a un estado de
  solo lectura tras un periodo de tiempo determinado.

### Gestión de infraestructura

Aunque OpenSearch es un servicio totalmente gestionado, hay tres aspectos que siguen siendo
responsabilidad del usuario para mantener el sistema estable:

1. **Gestión de disco**: hay que determinar las necesidades mínimas de almacenamiento — quedarse
   sin espacio en disco es un problema común.
2. **Número de nodos master**: se recomienda tener al menos **tres nodos master dedicados** en un
   entorno de producción.
3. **Opción serverless**: si no se quiere gestionar la infraestructura en absoluto, está disponible
   la arquitectura **serverless** (ver siguiente sección).

## OpenSearch Serverless

Aunque OpenSearch ya es un servicio **totalmente gestionado**, eso no implica que sea serverless
por defecto: normalmente sigue siendo necesario decidir y ajustar la capacidad del clúster (número
de nodos, tipo de instancia, etc.) según cambien las necesidades. **OpenSearch Serverless** es la
opción que elimina también esa gestión de capacidad.

- No hay que gestionar el clúster: la capacidad **escala automáticamente** para ajustarse a la
  carga de trabajo, permitiendo centrarse en la ingeniería de datos en vez de en el mantenimiento
  de infraestructura.
- Reduce el overhead operativo de gestión.
- Modelo de pago **por uso**: solo se paga por lo que realmente se consume — puede ser más rentable
  para cargas de trabajo **variables**, ya que no hay coste cuando no hay uso.
- Se integra igual de bien con el resto de servicios de AWS al construir pipelines de datos —
  **Lambda** (ejecutar código), **S3** (almacenamiento), **Kinesis** (streaming), etc.

> ⚠️ OpenSearch Serverless es la opción recomendada cuando no es conveniente (o no se quiere)
> preocuparse por la gestión del clúster, y el objetivo es centrarse solo en las tareas de datos —
> con el beneficio adicional de ahorro de costes en cargas de trabajo variables.
