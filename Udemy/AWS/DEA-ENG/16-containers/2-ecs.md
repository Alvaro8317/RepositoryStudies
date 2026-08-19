# Amazon ECS (Elastic Container Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon ECS?

**Amazon ECS** es un servicio de **orquestación de contenedores totalmente gestionado** en AWS.

- Simplifica el proceso de implantación: permite ejecutar imágenes Docker en la nube de AWS,
  encargándose de todas las partes de la gestión de contenedores.
- Puede configurarse para **escalar automáticamente** (up/down) en función de la carga de trabajo.
- Ofrece **alta disponibilidad y escalabilidad**, apoyándose en configuraciones multi-AZ.
- Incluye **características de seguridad integradas**: integración con **roles IAM** y **AWS Secrets
  Manager**, útil para asegurar la aplicación en contenedores y proteger datos sensibles.
- Se integra tanto con servicios de AWS como con herramientas de terceros, por ejemplo:
  - **Elastic Load Balancing**
  - **Elastic Container Registry (ECR)**
  - **CloudWatch**

## Conceptos fundamentales

### Task Definition (definición de tarea)

- Es el **"proyecto" o manual de instrucciones** de la aplicación.
- Contiene todos los parámetros de configuración necesarios:
  - Imagen Docker a usar.
  - Requisitos de CPU y memoria.
  - Configuración de red.
  - Otras dependencias del contenedor.
- ECS sigue esta definición para ejecutar la aplicación.

### Cluster

- Es un **grupo de recursos informáticos** donde se ejecutan y gestionan los contenedores.
- Toda aplicación en contenedores se despliega **dentro de un cluster**, ya sea como una tarea
  independiente (ej. un batch job) o como un servicio.
- Los recursos de cómputo del cluster pueden ser:
  - Instancias **EC2**.
  - Infraestructura **serverless** con **AWS Fargate**.
- Es el punto de gestión centralizado de las tareas y servicios: engloba potencia de cálculo,
  configuración de red, etc.

### Task vs. Service

| Concepto    | Descripción                                                                                                                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Task**    | Instancia de una task definition; uno o más contenedores que se ejecutan según esas especificaciones. Ideal para trabajos de **corta duración**.                                                                                                          |
| **Service** | Ejecuta y mantiene un número determinado de instancias de una task definition **simultáneamente** en el cluster. Ideal para aplicaciones de **larga duración** o microservicios (ej. un servidor web) que requieren monitorización y escalado constantes. |

> ⚠️ Diferencia clave: si una **task** independiente falla, no hay ningún mecanismo integrado que la
> reemplace automáticamente — hay que reiniciarla manualmente. En cambio, un **service** sí reemplaza
> automáticamente las tareas fallidas, garantizando que la aplicación siga ejecutándose de forma
> continua.

- Las tareas también pueden programarse (schedule) e iniciarse/terminarse dinámicamente según las
  demandas de carga de trabajo.
- Un service es, en esencia, una abstracción de alto nivel que gestiona las tareas por el usuario.

### Container Agent (agente de contenedor)

- Es un **daemon ligero** que se ejecuta en cada instancia EC2 dentro del cluster.
- Actúa como **puente de comunicación** entre el plano de control de ECS y la instancia de contenedor
  subyacente.
- Responsabilidades:
  - Obtener las task definitions.
  - Iniciar y detener los contenedores.
  - Informar del estado de salud (health status) de los contenedores a ECS.

## Próximos temas

En la siguiente clase se profundizará en los **tipos de lanzamiento (launch types)** de ECS — EC2 vs.
Fargate — y en algunas configuraciones importantes asociadas.
