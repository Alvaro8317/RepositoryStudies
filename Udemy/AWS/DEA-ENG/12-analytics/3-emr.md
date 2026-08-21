# Amazon EMR (Elastic MapReduce)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon EMR** (Elastic MapReduce) simplifica la ejecución de frameworks de **big data** — como
**Hadoop** o **Apache Spark** — en AWS de forma **gestionada**. Permite procesar y analizar
grandes cantidades de datos con gran rapidez, distribuyéndolos en un **clúster de servidores**.

Es especialmente útil para tareas de procesamiento complejas sobre grandes volúmenes de datos:
transformaciones de datos, análisis predictivo, procesamiento en tiempo real, etc.

- Soporta múltiples frameworks además de Hadoop: **Apache Spark**, **Presto**, **Flink**, entre
  otros — se elige el framework deseado y EMR lo instala durante la configuración del clúster.
- Permite configurar y escalar clústeres de procesamiento de datos **rápidamente** y gestionarlos
  de forma sencilla, reduciendo el overhead operativo tradicionalmente asociado a este tipo de
  infraestructura.

## EMR vs. Glue

Aunque ambos sirven para procesar/transformar datos, EMR y Glue tienen casos de uso distintos:

- **Glue** es más sencillo de usar y suele ser la opción por defecto para la mayoría de casos de
  uso, cuando se busca una solución simple.
- **EMR** es más adecuado cuando:
  - Hay cargas de trabajo de **procesamiento a escala de petabytes** — en esos casos, Glue podría
    no tener suficiente rendimiento.
  - Ya existen recursos **on-premises** que se quieren migrar, por ejemplo un **Hive Metastore**
    propio — es más fácil migrarlo y seguir usándolo en EMR de forma gestionada en la nube.

## Precios

- Se cobra **por hora**, según las **instancias EC2** subyacentes utilizadas por el clúster.

## Seguridad

EMR ofrece varias capas de seguridad:

- **IAM** integrado para la gestión de usuarios.
- **Amazon VPC** para aislar la red del clúster.
- **Cifrado con AWS KMS**:
  - **En reposo**: los datos almacenados en los nodos del clúster se cifran.
  - **En tránsito entre nodos**: los datos que se mueven entre los nodos del clúster también se
    cifran.
  - **En tránsito hacia/desde otros servicios** (ej. S3, DynamoDB): mediante **SSL/TLS**.

## Hadoop: la base de EMR

EMR se originó y se basa principalmente en **Hadoop**, un framework open source para el
**almacenamiento y procesamiento distribuido** de grandes volúmenes de datos, con dos componentes
principales:

| Componente                                | Función                                                                                                                          |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **HDFS** (Hadoop Distributed File System) | Almacenamiento: divide los datos en **bloques** y los distribuye entre varios nodos del clúster, con acceso de alto rendimiento. |
| **MapReduce**                             | Modelo de procesamiento: procesa esos grandes conjuntos de datos de forma **distribuida y en paralelo** sobre el clúster.        |

## Otros frameworks soportados: Spark, Presto y Flink

Además de Hadoop, EMR permite instalar y ejecutar otros frameworks de big data sobre el mismo
clúster gestionado:

- **Apache Spark**: framework de procesamiento distribuido **in-memory**, generalmente más rápido
  que MapReduce porque minimiza las lecturas/escrituras a disco entre pasos. Soporta procesamiento
  **batch** y **streaming** (vía micro-batches), consultas SQL (**Spark SQL**), machine learning
  (**MLlib**) y procesamiento de grafos (**GraphX**). Es una opción muy habitual para ETL y
  analítica a gran escala.
- **Presto** (y su fork **Trino**): motor de consultas **SQL distribuido**, optimizado para
  consultas **interactivas de baja latencia** sobre grandes volúmenes de datos — incluso a través
  de múltiples fuentes de datos (S3, HDFS, bases de datos relacionales, etc.) sin necesidad de
  mover los datos primero. No es un motor de almacenamiento, solo de consulta.
- **Apache Flink**: framework de procesamiento en **streaming** diseñado desde el origen para
  **baja latencia** y procesamiento en tiempo real (a diferencia de Spark, que nació batch-first y
  añadió streaming después mediante micro-batching). También soporta procesamiento batch.

| Framework | Enfoque principal                          | Uso típico                                        |
| --------- | ------------------------------------------ | ------------------------------------------------- |
| Spark     | Batch + streaming (micro-batch), in-memory | ETL, analítica general, machine learning          |
| Presto    | Consultas SQL interactivas distribuidas    | Analítica ad-hoc sobre múltiples fuentes de datos |
| Flink     | Streaming nativo de baja latencia          | Procesamiento en tiempo real, event-driven        |

- Al crear el clúster de EMR se elige qué framework(s) instalar; EMR se encarga de aprovisionarlos
  y configurarlos sobre los nodos del clúster.

## Arquitectura del clúster: tipos de nodo

Cada instancia dentro de un clúster de EMR es una instancia **EC2**, y dentro del clúster se le
llama **nodo**. Hay tres tipos de nodo:

| Tipo de nodo    | Función                                                                                                                                                                                   | Almacena datos | Obligatorio                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------- |
| **Master node** | Gestiona y coordina el clúster: distribuye datos y tareas entre el resto de nodos, monitoriza su estado/salud. No suele participar directamente en el almacenamiento ni el procesamiento. | No             | Sí — normalmente solo uno por clúster |
| **Core node**   | Almacenan los datos (vía HDFS) **y** ejecutan el procesamiento de las tareas (cálculos de big data, análisis, ML). Forman la "columna vertebral" del clúster.                             | Sí             | Sí                                    |
| **Task node**   | Opcional: aportan **potencia de cálculo adicional** para acelerar el procesamiento, sin almacenar datos. Útiles ante altos volúmenes de trabajo que hay que procesar en poco tiempo.      | No             | No (opcional)                         |

- Los datos se distribuyen en el almacenamiento local de los **core nodes**, y se procesan tanto
  por los **core nodes** como por los **task nodes**, coordinados por el **master node**.

### Tolerancia a fallos

- Si un nodo falla, sus tareas se **redistribuyen** entre los nodos restantes, garantizando que el
  procesamiento continúe sin pérdida de datos.
- Los datos almacenados en los core nodes se **replican en varios nodos**, evitando la pérdida de
  datos ante un fallo.

## Tipos de instancia / arquitectura de procesador

Al configurar un clúster, se puede elegir el tipo de nodo, el tipo de instancia EC2 y la
arquitectura del procesador:

| Arquitectura       | Descripción                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **x86**            | La opción tradicional — muy versátil, se adapta a una amplia gama de aplicaciones.                                                  |
| **Graviton** (ARM) | Ofrece un buen equilibrio entre cómputo, memoria y recursos de red, con un ahorro de coste potencial de hasta **20%** frente a x86. |

> ⚠️ Graviton no es solo una opción "más barata": mantiene un rendimiento comparable a x86 en la
> mayoría de cargas de trabajo, con la ventaja de reducir el coste.

## Tipos de clúster: transitorio vs. larga duración

Los clústeres de EMR se pueden configurar de dos formas, según los requisitos de las tareas de
procesamiento que deben gestionar:

- **Clúster transitorio (transient)**: agrupación **temporal**, creada solo para la duración de un
  trabajo concreto (o una serie de trabajos limitada). Una vez finalizado el trabajo, el clúster se
  **termina automáticamente**. Ideal para trabajos de **procesamiento por lotes (batch)** donde no
  se necesita el clúster disponible de forma constante — por ejemplo, un job ETL puntual o
  cualquier tarea programada que se completa de forma aislada.
- **Clúster de larga duración (long-running)**: diseñado para funcionar durante un **periodo
  prolongado**; no termina automáticamente al finalizar un trabajo. Más adecuado cuando se necesita
  **acceso y procesamiento continuos** — por ejemplo, ingesta continua de datos, procesamiento en
  tiempo real, o análisis de datos interactivo donde el usuario necesita consultar el clúster en
  cualquier momento.

## Opciones de almacenamiento

EMR ofrece varias opciones de almacenamiento, cada una adecuada para un caso de uso distinto:

| Tipo                                      | Descripción                                                                                                                                                          | Persiste tras terminar el clúster |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **HDFS** (Hadoop Distributed File System) | Almacenamiento tradicional de Hadoop: los datos residen en el **disco local** de cada nodo del clúster, con acceso de alta velocidad.                                | No                                |
| **EMRFS** (EMR File System)               | Implementación de HDFS que permite a los clústeres EMR almacenar datos directamente en **S3**.                                                                       | Sí                                |
| **Sistema de archivos local**             | Sistema de archivos regular de cada nodo, para datos **temporales específicos de ese nodo** (ej. datos intermedios de tareas MapReduce). No se comparte entre nodos. | No                                |
| **Volúmenes EBS**                         | Capacidad de disco adicional adjunta a los nodos (ej. SSDs para más rendimiento y flexibilidad de capacidad).                                                        | No                                |

> ⚠️ **HDFS, sistema de archivos local y volúmenes EBS son todos efímeros**: los datos ahí
> almacenados se pierden al terminar el clúster, salvo que se haga backup en otro almacenamiento
> (ej. S3). **EMRFS es la única opción que persiste** más allá de la vida del clúster, porque los
> datos residen en S3 — por eso es la opción recomendada para datos de entrada/salida que deben
> sobrevivir al clúster. Además, suele ser más rentable que almacenar grandes volúmenes de datos en
> HDFS local.
>
> Los volúmenes EBS en EMR se comportan distinto a EBS en instancias EC2 normales: aquí son
> **temporales** y se borran automáticamente cuando el clúster se termina.

## Escalabilidad

Los clústeres de EMR deben poder ampliarse o reducirse en función de la demanda, para adaptarse
dinámicamente a las necesidades de las tareas de procesamiento. Hay dos formas de hacerlo:

- **Escalado manual**: se redimensiona el clúster manualmente, añadiendo o eliminando instancias.
  Da más control porque el proceso se ajusta exactamente como se necesite. Útil para cargas de
  trabajo muy predecibles, cuando se conocen bien los recursos necesarios.
- **Escalado automático**, con dos variantes:
  - **Escalado gestionado (managed scaling)**: EMR supervisa continuamente la carga de trabajo y
    las métricas del clúster, y ajusta automáticamente el número de instancias EC2 para adaptarse a
    la demanda, optimizando tanto coste como rendimiento. Totalmente automatizado — no requiere
    definir políticas propias.
  - **Escalado automático personalizado (custom automatic scaling)**: se definen políticas y reglas
    propias, con condiciones específicas basadas en métricas de **CloudWatch** (ej. utilización de
    CPU, uso de memoria) que activan la adición o eliminación de instancias. Da más control, pero
    requiere configurarlo manualmente.

> ⚠️ Lo más importante a entender es la diferencia entre **escalado gestionado** (automatizado por
> EMR, sin definir políticas) y **escalado automático personalizado** (políticas propias basadas en
> métricas de CloudWatch).

### Grupos de instancias vs. flotas de instancias

El escalado se aplica sobre **grupos de instancias (instance groups)** o **flotas de instancias
(instance fleets)**:

- **Grupo de instancias**: conjunto de instancias del mismo tipo por rol de nodo — un tipo de
  instancia para el grupo master, otro para el grupo core y otro para el grupo de tareas.
- **Flota de instancias**: permite mayor flexibilidad en los tipos de instancia usados dentro del
  clúster, incluyendo una combinación de instancias **Spot** y **On-Demand**, para tener más
  opciones de configuración y optimizar el coste.

**Ejemplo — grupo de instancias:** para el grupo **core** eliges un único tipo de instancia, por
ejemplo `m5.xlarge`. Todas las instancias que EMR añada a ese grupo (al escalar manualmente o vía
escalado gestionado) serán `m5.xlarge`, y todas se lanzan como **On-Demand** (o todas como Spot, si
así configuras el grupo).

**Ejemplo — flota de instancias:** para el grupo **core** defines varios tipos de instancia
posibles a la vez, por ejemplo `m5.xlarge`, `m5.2xlarge` y `r5.xlarge`, y le dices a EMR que use una
mezcla de **Spot** (para abaratar coste) y **On-Demand** (para garantizar una capacidad mínima
estable). EMR elige automáticamente entre esos tipos de instancia según disponibilidad y precio de
Spot en cada momento, en vez de depender de un único tipo fijo.

> ⚠️ El **escalado gestionado** está disponible tanto para grupos de instancias como para flotas de
> instancias. El **escalado automático personalizado** solo está disponible para **grupos de
> instancias**, no para flotas de instancias.

## Opciones de despliegue

Además del clúster "tradicional" sobre instancias EC2, EMR ofrece otras opciones de despliegue:

### EMR on EKS

- Permite ejecutar frameworks de big data open source sobre **Amazon EKS** (Elastic Kubernetes
  Service), aprovechando las capacidades de gestión de Kubernetes también para aplicaciones de big
  data.
- El usuario se centra solo en ejecutar sus cargas de trabajo analíticas; EMR on EKS construye,
  configura y gestiona los contenedores de la aplicación.
- Permite ejecutar aplicaciones basadas en EMR junto con otros tipos de aplicaciones en el mismo
  clúster EKS.
- Servicio totalmente gestionado: no es necesario aprovisionar ningún clúster por separado.
- Recomendable si ya se usa Kubernetes, o se busca más escalabilidad y simplicidad mediante
  contenedores.

### EMR Serverless

- Lleva la abstracción de infraestructura al máximo: **abstrae completamente** la gestión de todos
  los recursos de cómputo subyacentes — no hay interacción alguna con la arquitectura.
- Aprovisiona, configura y escala automáticamente todo el entorno de cómputo, y libera los recursos
  automáticamente al finalizar el trabajo, reduciendo costes.
- Puede **pre-inicializar recursos** para que las aplicaciones respondan rápidamente — útil para
  casos como análisis de datos interactivo.
- Ideal para cargas de trabajo variables/impredecibles donde gestionar recursos manualmente sería
  difícil, o cuando solo se quiere procesar datos sin preocuparse de la infraestructura subyacente.
- Modelo de pago **por uso**: solo se paga por los recursos usados mientras se ejecutan los
  trabajos — solución rentable para cargas de trabajo variables.

> ⚠️ EMR Serverless va un paso más allá que el escalado gestionado: con escalado gestionado (sobre
> un clúster EC2/EKS) la arquitectura subyacente sigue siendo visible e interactuable, aunque el
> escalado se automatice. Con EMR Serverless la infraestructura está **completamente abstraída** y
> no es visible en absoluto.
