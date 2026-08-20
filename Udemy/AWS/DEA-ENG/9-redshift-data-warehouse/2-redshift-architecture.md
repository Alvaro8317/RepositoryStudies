# Arquitectura de Redshift: clusters

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es un cluster?

Un **cluster** es el **componente central** de la infraestructura de Redshift: es lo que **ejecuta
las cargas de trabajo**.

- Ejecuta el **motor de Redshift** y contiene **una o varias bases de datos**.
- El **rendimiento** del almacén de datos depende directamente de **cómo se configure el cluster**.
- Ofrece **replicación y copias de seguridad continuas**, lo que mejora la **disponibilidad** y
  garantiza la **durabilidad** de los datos.
- Es un **cluster distribuido** con **recuperación automática**: cuando un componente falla, se
  **sustituye automáticamente**.

## Componentes del cluster

Un cluster de Redshift está formado principalmente por dos tipos de componentes:

- **Nodo líder (leader node)**.
- **Nodos de computación (compute nodes)**.

### Nodo líder (leader node)

- Se **aprovisiona automáticamente** cuando el cluster tiene **dos o más nodos de computación**.
- Es el que se **comunica con el cliente**, normalmente mediante una conexión **ODBC** o **JDBC**.
- **Coordina** los nodos de computación y gestiona toda la **comunicación externa** con el cliente.
- **Agrega los resultados** de todos los nodos de computación antes de devolverlos a la aplicación
  cliente.
- Desarrolla el **plan de ejecución** de la consulta: la serie de pasos necesarios para obtener los
  resultados de consultas complejas.
- A partir de ese plan de ejecución:
  1. **Compila el código** necesario.
  2. **Distribuye el código compilado** a los nodos de computación.
  3. **Asigna a cada nodo de computación una porción de los datos** sobre la que trabajar.

> ⚠️ Redshift implementa **ciertas funciones SQL exclusivamente en el nodo líder**. Una consulta
> que use alguna de esas funciones **debe ejecutarse solo en el nodo líder** — si hace referencia a
> algo almacenado en los nodos de computación (por ejemplo, una tabla), **devolverá un error**.

### Nodos de computación (compute nodes)

- Son los que **ejecutan realmente la carga de trabajo** de las consultas.
- Cada nodo de computación tiene su propia **memoria, CPU y almacenamiento en disco dedicados**.
- Ejecutan los **planes de ejecución de consultas** que reciben del nodo líder y **transmiten datos
  entre ellos** para resolver esas consultas.
- La **capacidad de cómputo** se puede aumentar o disminuir de dos formas (combinables):
  - Cambiando el **número de nodos**.
  - Cambiando el **tipo de nodo**.
- La combinación de número y tipo de nodo es lo que determina el **rendimiento del cluster**.

## Opciones de despliegue: serverless vs. provisioned

Al crear una nueva instancia de Redshift hay dos opciones:

| Opción                         | Cuándo usarla                                                                                                                           |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon Redshift Serverless** | Cuando el almacén de datos necesita **escalar automáticamente** según la demanda — útil si la carga de trabajo es **más impredecible**. |
| **Cluster provisioned**        | Da **más control** sobre la configuración — más adecuado para cargas de trabajo **predecibles o estables**.                             |

> ⚠️ La elección entre serverless y provisioned depende sobre todo de qué tan **predecible** sea la
> carga de trabajo: automática y flexible (serverless) frente a control total y estabilidad
> (provisioned).
