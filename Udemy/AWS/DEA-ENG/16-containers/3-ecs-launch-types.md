# ECS: Launch Types y Task Placement

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Launch Types (tipos de lanzamiento)

ECS ofrece tres tipos de lanzamiento diferentes:

| Launch Type  | Descripción                                                                                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EC2**      | Debes aprovisionar y mantener la infraestructura tú mismo: los contenedores se ejecutan en un cluster de instancias EC2 que gestionas.                            |
| **Fargate**  | Infraestructura **serverless** de AWS Fargate: ejecutas contenedores sin gestionar ninguna infraestructura subyacente.                                            |
| **External** | Permite ejecutar aplicaciones en contenedores en servidores propios o máquinas virtuales on-premise, registrados en el cluster ECS y gestionados de forma remota. |

### EC2

- Control total sobre la infraestructura: adecuado para cargas de trabajo grandes donde se quiere
  optimizar todo manualmente.
- Permite usar opciones específicas de EC2, como **Spot Instances** o tipos de instancia personalizados.
- Más complejo de gestionar, pero ofrece más opciones de personalización y control.

> ⚠️ Con el launch type EC2, el escaneo **no es automático**: toda la configuración de escalado y
> gestión de instancias corre por cuenta del usuario.

### Fargate

- No es necesario gestionar infraestructura EC2: AWS ejecuta las tareas basándose en los requisitos de
  **CPU y RAM** configurados, seleccionando automáticamente la cantidad de recursos necesaria.
- Es rápido y sencillo de configurar — suele ser la **opción recomendada o más utilizada** por su
  practicidad.
- Aprovisiona y **escala automáticamente** la infraestructura necesaria para ejecutar los contenedores.

### External

- Pensado para ejecutar contenedores en infraestructura propia (servidores locales o VMs) que se
  registra en el cluster ECS y se gestiona de forma remota.

## Task Placement (colocación de tareas)

> ⚠️ Task placement solo aplica al **launch type EC2**. Con Fargate no es necesario, ya que AWS gestiona
> la colocación de tareas automáticamente.

### Task Placement Strategies

Un algoritmo específico que selecciona en qué instancia se coloca (o de cuál se termina) una tarea,
controlando cómo se distribuyen las tareas entre las instancias de contenedor del cluster.

| Estrategia   | Descripción                                                                                                                       | Cuándo usarla                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Bin pack** | Empaqueta las tareas en las instancias con menor capacidad de CPU/memoria **disponible**, minimizando el desperdicio de recursos. | Cuando las tareas tienen requisitos de recursos variados y se quiere optimizar coste.       |
| **Spread**   | Reparte las tareas **uniformemente** entre las instancias del cluster, mejorando tolerancia a fallos y disponibilidad.            | Cuando las tareas tienen requisitos similares y se busca distribuirlas de forma equitativa. |
| **Random**   | Coloca las tareas de forma **aleatoria** entre las instancias del cluster.                                                        | Cuando no hay requisitos específicos de rendimiento o disponibilidad a considerar.          |

- Estas estrategias también pueden **combinarse** entre sí.

### Task Placement Constraints

Reglas que deben cumplirse para colocar una tarea en una instancia de contenedor. Si no se cumplen, la
tarea queda en estado **pendiente** y no se coloca.

| Restricción          | Descripción                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **distinctInstance** | Coloca la tarea en una instancia de contenedor **distinta**. Adecuado cuando se requiere un aislamiento fuerte.                                                   |
| **memberOf**         | Coloca la tarea en una instancia que satisface una expresión específica, escrita con el **cluster query language**, permitiendo agrupar instancias por atributos. |

### Proceso de colocación de una tarea

Cuando ECS coloca una tarea, sigue este orden:

1. Identifica qué instancias satisfacen los requisitos de **CPU, memoria y puerto**.
2. Identifica qué instancias satisfacen las **task placement constraints**.
3. Identifica qué instancias satisfacen la **task placement strategy**.

## Próximos temas

En la siguiente clase se hablará de los **roles de IAM** en el contexto de ECS.
