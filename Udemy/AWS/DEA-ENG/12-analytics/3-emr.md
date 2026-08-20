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
