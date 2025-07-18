# Contenedores en AWS

## Resumen de Docker y su gestión de contenedores en AWS

### ¿Qué es Docker?

Docker es una plataforma de código abierto que permite **crear, empaquetar, distribuir y ejecutar aplicaciones** dentro de contenedores. Un **contenedor** es una unidad ligera y portátil que incluye el código, bibliotecas, dependencias y configuraciones necesarias para ejecutar una aplicación, asegurando que se ejecute de forma **consistente en cualquier entorno**.

- Los contenedores comparten el mismo sistema operativo host, lo que los hace más **eficientes y rápidos** que las máquinas virtuales.
- Se definen a través de **Dockerfiles**, que especifican cómo construir la imagen del contenedor.

---

### ¿Dónde se almacenan las imágenes en Docker?

Las imágenes Docker pueden almacenarse y recuperarse desde **repositorios de imágenes** (registries). Existen dos principales:

- **Docker Hub**: registro público por defecto de Docker

  - Puede contener repositorios **públicos** (visibles para todos) o **privados** (acceso restringido)

- **Amazon Elastic Container Registry (ECR)**: servicio de AWS para almacenamiento seguro y privado de imágenes de contenedor

  - Integra con servicios como ECS, EKS y Fargate
  - Soporta autenticación con IAM

---

### Repositorios públicos vs privados

| Tipo de repositorio | Descripción                                                      |
| ------------------- | ---------------------------------------------------------------- |
| **Público**         | Cualquiera puede acceder a la imagen (ej. `nginx`, `node`)       |
| **Privado**         | Acceso controlado por autenticación, usado para imágenes propias |

**Ejemplo**:

- Imagen pública: `docker pull nginx`
- Imagen privada en ECR: requiere autenticación con AWS CLI o IAM roles

---

### Docker vs Máquinas Virtuales

| Característica         | **Docker (Contenedores)**                        | **Máquinas Virtuales (VMs)**                        |
| ---------------------- | ------------------------------------------------ | --------------------------------------------------- |
| Arranque               | Rápido (segundos)                                | Lento (minutos)                                     |
| Tamaño                 | Ligero (MBs)                                     | Pesado (GBs)                                        |
| Aislamiento            | A nivel de proceso (comparten el kernel)         | Total (sistema operativo independiente)             |
| Eficiencia de recursos | Alta (menos overhead)                            | Menor (requiere más CPU/RAM)                        |
| Portabilidad           | Muy alta (misma imagen en cualquier host Docker) | Limitada por el hipervisor o sistema operativo      |
| Uso típico             | Microservicios, pipelines, apps en contenedor    | Aplicaciones legacy, entornos completos, servidores |

---

### Gestión de contenedores en AWS

AWS ofrece varias opciones para ejecutar y administrar contenedores:

| Servicio        | Descripción                                                               |
| --------------- | ------------------------------------------------------------------------- |
| **Amazon ECS**  | Orquestador de contenedores propio de AWS, fácil de usar y bien integrado |
| **Amazon EKS**  | Servicio de Kubernetes administrado, para quienes ya usan Kubernetes      |
| **AWS Fargate** | Ejecución de contenedores **sin administrar servidores** (serverless)     |
| **Amazon ECR**  | Registro privado para almacenar imágenes Docker dentro de AWS             |

**Resumen por caso de uso**:

- **ECS**: ideal si quieres usar herramientas de AWS directamente sin complejidad adicional
- **EKS**: recomendado si ya usas o necesitas Kubernetes
- **Fargate**: elimina la necesidad de provisionar y escalar instancias EC2 para contenedores
- **ECR**: almacenamiento de imágenes Docker, integrado con ECS, EKS y Fargate

---

**Ejemplo flujo completo**:

1. Crear imagen Docker localmente
2. Subirla a **Amazon ECR**
3. Ejecutar contenedor desde esa imagen usando **ECS o EKS**
4. Si usas **Fargate**, no necesitas preocuparte por servidores EC2, solo defines la tarea y AWS se encarga del resto

## Amazon ECS: Tipos de lanzamiento, IAM roles y almacenamiento compartido

### Tipo de lanzamiento EC2 en Amazon ECS

El modo de lanzamiento **EC2** en Amazon ECS permite ejecutar tareas en instancias EC2 administradas por el usuario:

- Se deben **provisionar, mantener y escalar manualmente** las instancias EC2 del clúster
- Cada instancia EC2 debe tener instalado y en ejecución el **agente ECS**
- AWS se encarga de iniciar y detener los contenedores definidos en las **tareas ECS**
- Se recomienda usar **Auto Scaling Groups** para administrar el grupo de instancias

**Componentes clave**:

- **Perfil de instancia EC2**: proporciona permisos para que el **agente ECS**:

  - Registre la instancia al clúster ECS
  - Envíe logs a CloudWatch
  - Descargue imágenes desde Amazon ECR
  - Acceda a secretos desde Secrets Manager

---

### Tipo de lanzamiento Fargate en Amazon ECS

El modo de lanzamiento **Fargate** es completamente **serverless**:

- No se gestionan instancias EC2, AWS se encarga de toda la infraestructura
- Solo se define una **definición de tarea** que describe:

  - Imagen del contenedor
  - CPU y memoria
  - Variables de entorno, secretos, puertos, etc.

- Ideal para ejecutar contenedores con mínima gestión operativa

---

### IAM y control de acceso en ECS

| Tipo de rol                                         | ¿Dónde se define?                 | ¿Qué permite?                                                                |
| --------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------- |
| **Perfil de instancia EC2**                         | Asociado a instancias del clúster | Permite al agente ECS realizar llamadas a la API de ECS                      |
| **Rol de ejecución de tarea (task execution role)** | En la definición de tarea         | Permite extraer imágenes de ECR, acceder a Secrets Manager o CloudWatch Logs |
| **Rol de tarea (task role)**                        | En la definición de tarea         | Permite que el código del contenedor acceda a servicios AWS específicos      |

**Ejemplo**:

- Una tarea ECS puede tener acceso a DynamoDB, S3 o Parameter Store a través de su **rol de tarea**.
- Ese acceso no depende del perfil de instancia EC2 (si se usa EC2), ni del rol de ejecución.

---

### Integración con balanceadores de carga

ECS se integra nativamente con:

- **Application Load Balancer (ALB)**:

  - Ideal para aplicaciones web HTTP/HTTPS
  - Soporta enrutamiento por path y host
  - Integración directa con ECS para exponer tareas como servicios

- **Network Load Balancer (NLB)**:

  - Diseñado para tráfico TCP/UDP de alto rendimiento
  - Útil para microservicios que requieren baja latencia o protocolos no HTTP

**ECS registra automáticamente** las tareas en el balanceador usando Target Groups.

---

### Almacenamiento compartido con Amazon EFS

Amazon ECS permite montar sistemas de archivos EFS (Elastic File System) en tareas:

- Compatible tanto con **tipo EC2** como con **Fargate**
- Permite compartir datos entre múltiples tareas incluso si se ejecutan en **diferentes zonas de disponibilidad**
- Ideal para casos como procesamiento de archivos, carga de recursos compartidos, o persistencia entre ejecuciones

**Ventajas de Fargate + EFS**:

- Completamente **serverless**
- Sin necesidad de administrar instancias EC2 o NFS manualmente

> 🔸 **Amazon S3 no puede montarse como un sistema de archivos** en ECS, ya que no es un filesystem POSIX. En cambio, debe accederse mediante SDK/API o herramientas como `aws s3 cp` dentro del contenedor.

---

### Resumen por tipo de lanzamiento

| Característica             | **ECS con EC2**                        | **ECS con Fargate**                         |
| -------------------------- | -------------------------------------- | ------------------------------------------- |
| Gestión de infraestructura | Manual (instancias EC2)                | Automática (sin servidores)                 |
| Escalado                   | Con Auto Scaling Group                 | Escalado automático por definición de tarea |
| Instalación del agente ECS | Necesario                              | No requerido                                |
| IAM: perfil de instancia   | Sí (para que el agente ECS funcione)   | No aplica                                   |
| IAM: rol de tarea          | Sí, definido en la definición de tarea | Sí                                          |
| Integración con ALB/NLB    | Sí                                     | Sí                                          |
| Compatibilidad con EFS     | Sí                                     | Sí                                          |
| Uso de S3 como filesystem  | No (solo vía API o SDK)                | No (igual)                                  |

## Jerarquía y componentes clave en Amazon ECS

Amazon Elastic Container Service (ECS) está estructurado en niveles que permiten organizar, ejecutar y escalar contenedores en AWS. A continuación se describe la jerarquía y el propósito de cada elemento principal.

---

### 1. **Clúster (Cluster)**

- Es el **nivel más alto** de agrupación lógica.
- Un clúster ECS es un conjunto de recursos donde se ejecutan las tareas y servicios.
- Puede contener:

  - Instancias **EC2** registradas al clúster (modo EC2)
  - Tareas **Fargate** (no requieren instancias físicas visibles)

**Ejemplo**: un clúster llamado `producción` puede contener múltiples servicios y tareas corriendo en EC2 y/o Fargate.

---

### 2. **Definición de tarea (Task Definition)**

- Es la **plantilla** o blueprint que define **cómo debe ejecutarse** un contenedor (o varios).
- Especifica:

  - Imagen del contenedor (Docker image)
  - CPU y memoria
  - Variables de entorno, puertos, volúmenes
  - IAM roles (task role y execution role)
  - Puntos de montaje EFS, secretos de Secrets Manager o Parameter Store

- Se pueden definir **múltiples contenedores** dentro de una misma tarea (por ejemplo, app + sidecar)

**Nota**: No ejecuta nada por sí sola, solo es una plantilla.

---

### 3. **Tarea (Task)**

- Es una **instancia en ejecución** de una definición de tarea.
- Puede lanzarse:

  - Manualmente (una sola vez)
  - Como parte de un servicio (mantiene disponibilidad continua)

- Se ejecuta sobre recursos del clúster según el **tipo de lanzamiento**:

  - **EC2**: sobre instancias administradas por el usuario
  - **Fargate**: sin servidores

**Ejemplo**: lanzar una tarea `procesar-carga` que lee un lote de datos y termina.

---

### 4. **Servicio (Service)**

- Es un **componente de larga duración** que garantiza que un número específico de tareas esté **siempre ejecutándose**.
- Supervisa y reemplaza tareas que fallan.
- Permite:

  - Integrarse con **ALB/NLB**
  - Escalar automáticamente con CloudWatch o Application Auto Scaling

- El servicio lanza tareas basadas en una task definition y un **proveedor de capacidad**.

---

### 5. **Proveedor de capacidad (Capacity Provider)**

- Determina **cómo y dónde** se ejecutarán las tareas de un servicio.
- Existen dos tipos:

  - **Fargate** y **Fargate Spot**
  - **EC2 Auto Scaling Groups** (vinculados al clúster)

- Se puede usar **estrategia mixta** para balancear costos y disponibilidad, ej. 80% Fargate Spot, 20% Fargate

**Ejemplo**: un servicio puede decir “lanza mis tareas en Fargate, y si es posible, usa Spot para ahorrar”.

---

### 6. **Roles IAM en ECS**

| Rol                   | ¿Dónde se aplica?             | Propósito principal                                                                    |
| --------------------- | ----------------------------- | -------------------------------------------------------------------------------------- |
| **Execution Role**    | En la definición de tarea     | Permite a ECS **extraer imágenes** de ECR, enviar logs a CloudWatch, acceder a Secrets |
| **Task Role**         | En la definición de tarea     | Permite a los **contenedores acceder** a otros servicios AWS (DynamoDB, S3, etc.)      |
| **EC2 Instance Role** | En instancias EC2 del clúster | Permite al **agente ECS** registrar y comunicar las tareas con ECS                     |

---

### Diferencias entre **Tarea** y **Servicio**

| Característica       | **Tarea (Task)**                                      | **Servicio (Service)**                                        |
| -------------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| Persistencia         | Temporal                                              | Continua (se reinicia si falla)                               |
| Control de escala    | No (es manual)                                        | Sí, mantiene el número deseado de tareas                      |
| Balanceador de carga | No se puede registrar directamente                    | Sí, se puede asociar con ALB o NLB                            |
| Casos de uso         | Procesamiento por lotes, tareas puntuales             | Microservicios, APIs, workers que deben estar siempre activos |
| Invocación           | Manual o programada (ej. EventBridge, Step Functions) | Permanente, administrado por ECS                              |

---

### Jerarquía resumida

```textplain
CLUSTER
│
├── TASK DEFINITION (plantilla)
│    ├── Execution Role
│    └── Task Role
│
├── SERVICE (gestiona tareas en ejecución)
│    ├── Tipo de lanzamiento (EC2 / Fargate)
│    ├── Proveedor de capacidad
│    └── Auto Scaling / Load Balancer opcional
│
└── TASK (instancia ejecutada de la definición)
```

---

### Ejemplo práctico

Un clúster `producción` contiene:

- Un **servicio** llamado `api-web` con tipo de lanzamiento **Fargate**
- Este servicio ejecuta tareas con definición `api:2`, expuestas a un **ALB**
- Cada tarea tiene un **task role** que le permite acceder a DynamoDB
- El **execution role** permite obtener secretos de Secrets Manager y logs en CloudWatch
- El **capacity provider** mezcla 80% Fargate Spot y 20% Fargate para optimizar costo y disponibilidad

## Escalado automático en Amazon ECS: tareas vs infraestructura

Amazon ECS permite escalar tanto el **número de tareas** que ejecutan los servicios como la **infraestructura subyacente** (instancias EC2), dependiendo del tipo de lanzamiento. El escalado puede ser reactivo (basado en métricas), por pasos, por objetivos o programado.

---

### Escalado automático de servicios ECS (número de tareas)

El **escalado automático del servicio ECS** ajusta el número **deseado de tareas** en un servicio, utilizando **AWS Application Auto Scaling**.

#### Tipos de políticas de escalado

1. **Seguimiento de objetivo (Target Tracking Scaling)**
   Ajusta automáticamente el número de tareas para mantener una métrica en un valor deseado.
   **Ejemplo**: mantener el 60 % de uso promedio de CPU.

2. **Escalado por pasos (Step Scaling)**
   Define umbrales y acciones explícitas.
   **Ejemplo**: si CPU > 70 % durante 5 min, aumenta 2 tareas.

3. **Escalado programado (Scheduled Scaling)**
   Define cambios de capacidad basados en horarios.
   **Ejemplo**: aumentar tareas a 10 todos los días a las 9 a. m.

#### Métricas comunes de escalado

- **Utilización de CPU promedio**
- **Utilización de memoria promedio**
- **Recuento de solicitudes por destino** (usando Application Load Balancer)
- Métricas personalizadas (por ejemplo, mensajes en cola SQS)

---

### Escalado de infraestructura con Auto Scaling Group (ASG)

Cuando se utiliza el tipo de lanzamiento **EC2**, también es necesario escalar las instancias subyacentes. Aquí entra en juego el **ASG del clúster ECS**, que gestiona las instancias EC2.

- El ASG puede aumentar o reducir el número de instancias EC2 en función de:

  - Métricas como CPU, memoria, espacio en disco
  - Número de tareas en espera por recursos
  - Programación o escalado manual

> 🔸 **Importante**: el **ASG de ECS (capacidad)** es diferente al **ASG de EC2 clásico**. Aunque ambos usan la misma tecnología, el ASG de ECS está vinculado a un **proveedor de capacidad ECS**.

---

### Proveedor de capacidad ECS

- Un **Capacity Provider** define cómo ECS obtiene la infraestructura para ejecutar tareas.
- Puede vincularse a:

  - Un **ASG** (para tipo de lanzamiento EC2)
  - **Fargate** o **Fargate Spot** (para serverless)

**Ventajas de usar un proveedor de capacidad con ASG**:

- ECS puede **detectar automáticamente** si faltan recursos
- Puede iniciar nuevas instancias EC2 automáticamente cuando se necesitan más tareas
- Compatible con **escalado administrado por ECS** (Managed Scaling)

---

### Relación general entre escalados

| Escalado                          | ¿Qué escala?           | ¿Cuándo se usa?                                 |
| --------------------------------- | ---------------------- | ----------------------------------------------- |
| **Auto Scaling del servicio ECS** | Número de tareas       | Siempre (Fargate o EC2)                         |
| **ASG de EC2 clásico**            | Instancias EC2         | Solo cuando se usa tipo de lanzamiento EC2      |
| **Managed ECS Capacity Provider** | Vincula ECS con un ASG | Escalado automático basado en demanda de tareas |
| **Fargate**                       | Automático, sin ASG    | No se requiere escalado de infraestructura      |

---

### Ejemplo práctico de ECS

- Un servicio ECS ejecuta contenedores `web` con 2 tareas mínimas.
- Tiene una política de **target tracking** que mantiene el uso de CPU por debajo del 60 %.
- Cuando aumenta el tráfico web, ECS escala automáticamente el número de tareas a 5.
- Las tareas requieren más recursos de cómputo, así que el **capacity provider** escala el ASG y lanza más instancias EC2 para alojarlas.
- Todo el proceso es automático gracias a la integración entre ECS, Application Auto Scaling y el ASG.

## Resumen de Amazon ECR (Elastic Container Registry)

Amazon ECR es un **registro de contenedores privado y administrado** que permite almacenar, compartir y gestionar imágenes de Docker de forma segura y altamente disponible dentro del ecosistema de AWS.

---

### Características principales

- **Registro privado** de imágenes Docker y OCI (Open Container Initiative)
- **Integración directa** con:

  - **Amazon ECS**
  - **Amazon EKS**
  - **AWS Fargate**
  - **AWS CodeBuild / CodePipeline**

- **Respaldado internamente por Amazon S3**, aunque no expuesto directamente como bucket

  - Alta durabilidad y disponibilidad del almacenamiento

---

### Seguridad y control de acceso

- Control de acceso granular mediante **IAM policies**

  - Se puede permitir o restringir acceso por repositorio, usuario, cuenta o rol

- Soporte para **cifrado en reposo** con **AWS KMS**
- **Cifrado en tránsito** usando HTTPS
- Compatibilidad con **escaneo de vulnerabilidades** de imágenes mediante Amazon Inspector o herramientas nativas
- Posibilidad de habilitar **escaneo automático al push**

---

### Funciones comunes

- **Push/Pull de imágenes**:

  ```bash
  aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
  docker build -t mi-imagen .
  docker tag mi-imagen <account>.dkr.ecr.<region>.amazonaws.com/mi-repositorio
  docker push <account>.dkr.ecr.<region>.amazonaws.com/mi-repositorio
  ```

- **Autenticación automática** con ECS, EKS y CodeBuild usando **roles IAM** (sin necesidad de hacer login manual)

---

### Beneficios

| Ventaja                        | Descripción                                                             |
| ------------------------------ | ----------------------------------------------------------------------- |
| **Alta integración**           | Totalmente conectado con ECS, EKS, Fargate, CodeBuild, etc.             |
| **Seguridad nativa de AWS**    | IAM, KMS, CloudTrail, VPC endpoints                                     |
| **Escaneo de seguridad**       | Detección automática de vulnerabilidades en imágenes                    |
| **Eliminación automática**     | Se pueden definir políticas de retención para limpiar imágenes antiguas |
| **Replicación entre regiones** | Compatible con replicación automática entre regiones                    |

---

### Ejemplo de flujo típico con ECS

1. Desarrollador construye una imagen Docker y la sube a **ECR**
2. ECS (Fargate o EC2) extrae la imagen desde ECR al lanzar una tarea
3. IAM controla qué tareas o servicios pueden acceder a qué repositorios
4. El ciclo puede integrarse con CI/CD (CodePipeline, GitHub Actions, etc.)

---

### Conclusión

Amazon ECR es el componente ideal para gestionar imágenes de contenedores en AWS de forma segura, escalable y completamente integrada con los servicios de ejecución como **ECS, EKS y Fargate**, sin la necesidad de configurar infraestructura adicional para el registro.

## Resumen de Amazon EKS (Elastic Kubernetes Service)

Amazon EKS es un servicio administrado que permite ejecutar clústeres de **Kubernetes** en AWS sin tener que instalar ni operar el plano de control (control plane).

- Compatible con versiones upstream de Kubernetes
- Totalmente gestionado, seguro y escalable
- Se puede usar con instancias EC2, Fargate o nodos en local (con EKS Anywhere)

---

### Tipos de nodos en EKS

Los **nodos** son los recursos de cómputo donde se ejecutan los **pods** (contenedores). EKS admite múltiples tipos de nodos:

| Tipo de nodo          | Descripción                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **EC2 Managed Nodes** | Nodos EC2 administrados por AWS con actualizaciones automáticas de AMI    |
| **Self-managed EC2**  | Nodos EC2 administrados por el usuario (más control, más responsabilidad) |
| **Fargate**           | Nodos serverless: no se administran instancias, cada pod corre aislado    |

---

### Soporte de Fargate en EKS

- Permite ejecutar **pods directamente sin gestionar nodos EC2**
- Ideal para cargas pequeñas, tareas intermitentes o entornos dev/test
- Los pods en Fargate requieren **definiciones específicas en perfiles Fargate**
- Limitaciones: no admite DaemonSets, ni acceso a volúmenes persistentes EBS/EFS directamente

---

### Volúmenes persistentes y almacenamiento en EKS

Kubernetes en EKS utiliza **StorageClass** para definir tipos de almacenamiento dinámico. AWS ofrece compatibilidad con varios backends a través del estándar **CSI (Container Storage Interface)**.

#### Componentes

- **PersistentVolume (PV)**: recurso de almacenamiento en el clúster
- **PersistentVolumeClaim (PVC)**: solicitud de almacenamiento por parte de un pod
- **StorageClass**: define el tipo de almacenamiento a aprovisionar dinámicamente

#### Almacenamientos compatibles

| Tipo de almacenamiento | Descripción                                                  | CSI requerido |
| ---------------------- | ------------------------------------------------------------ | ------------- |
| **Amazon EBS**         | Volúmenes de bloque persistentes por zona AZ                 | Sí            |
| **Amazon EFS**         | Sistema de archivos compartido entre múltiples pods y nodos  | Sí            |
| **Amazon FSx**         | Sistemas de archivos avanzados (Lustre, Windows File Server) | Sí            |

---

### Ejemplos de uso

- **EBS**: para bases de datos por pod (como PostgreSQL o MongoDB con almacenamiento local por zona)
- **EFS**: para almacenamiento compartido entre múltiples pods, ideal para CMS, apps multiinstancia
- **FSx for Lustre**: para procesamiento de archivos de alto rendimiento (ej. genomics, renderizado)
- **FSx for Windows File Server**: para aplicaciones Windows legacy que requieren SMB

---

### Resumen técnico

| Componente                        | Detalle                                                       |
| --------------------------------- | ------------------------------------------------------------- |
| Tipo de cómputo                   | EC2, Fargate                                                  |
| Plano de control                  | Gestionado por AWS (alta disponibilidad, escalado automático) |
| Escalado automático               | Soporte para Cluster Autoscaler y Karpenter                   |
| CSI (Container Storage Interface) | Permite usar volúmenes dinámicos como EBS, EFS, FSx           |
| Acceso a storage                  | A través de PVC + StorageClass                                |
| Soporte multi-AZ                  | Sí, para pods y EFS (no para EBS directamente)                |

---

### Consideraciones

- Para usar **EBS**: el pod debe ejecutarse en la **misma zona de disponibilidad** donde fue creado el volumen
- Para usar **EFS**: ideal en **entornos multi-AZ y compartidos**
- Para **Fargate + almacenamiento persistente**, las opciones son **limitadas**; no se puede montar EBS directamente

---

Amazon EKS proporciona una plataforma robusta y flexible para ejecutar cargas de trabajo basadas en contenedores en Kubernetes, con soporte para múltiples tipos de nodos, almacenamiento dinámico y alto grado de integración con el ecosistema AWS.

## Diferencia entre **crear** un clúster de Amazon EKS y **registrar** un clúster en Amazon EKS

### 1. **Crear un clúster de EKS**

Significa aprovisionar un **clúster de Kubernetes totalmente administrado por AWS**, incluyendo su **plano de control (control plane)**.

#### Características de EKS creación

- AWS crea y gestiona el **control plane**: etcd, API server, controller manager, scheduler
- El control plane es **alta disponibilidad** y corre en **Multi-AZ**
- Se pueden usar nodos **EC2**, **Fargate** o ambos
- Configurable desde consola, CLI (`eksctl`) o IaC (CloudFormation, Terraform)

**Ejemplo de uso**:
Quieres una solución Kubernetes **completamente gestionada por AWS** y lista para producción, con soporte nativo para escalado, integración IAM, logging, etc.

---

### 2. **Registrar un clúster en EKS**

Significa **integrar un clúster de Kubernetes externo** (no creado por AWS) a la **consola de EKS** para **observabilidad y control unificado**, usando **Amazon EKS Connector**.

#### Características de EKS registro

- El clúster puede estar:

  - **On-premises**
  - En otra nube
  - Creado manualmente en EC2 (por ejemplo, usando `kubeadm`)
  - EKS Anywhere

- No es un control plane administrado por AWS
- AWS no gestiona ni cobra por el clúster (fuera de costos del Connector)
- Se puede usar para:

  - Visualizar nodos y workloads desde la consola de EKS
  - Integrar parcialmente con servicios AWS (monitoring, IAM, etc.)

**Ejemplo de uso**:
Tienes un clúster Kubernetes on-premises o en EC2 y deseas **centralizar la administración** desde la consola EKS sin migrarlo completamente.

---

### Comparación resumida

| Aspecto                        | **Crear un clúster EKS**                  | **Registrar un clúster EKS**                             |
| ------------------------------ | ----------------------------------------- | -------------------------------------------------------- |
| ¿Quién crea el control plane?  | AWS                                       | Usuario o externo                                        |
| ¿Dónde se ejecuta?             | En AWS, Multi-AZ gestionado               | Externo o autogestionado (on-prem, EC2, otra nube)       |
| ¿Gestión del plano de control? | AWS lo administra                         | El usuario lo administra                                 |
| ¿Costo por control plane?      | Sí (por hora)                             | No                                                       |
| ¿Se puede usar Fargate/EC2?    | Sí                                        | No (no está conectado a la infraestructura AWS)          |
| ¿Observabilidad desde consola? | Sí                                        | Sí (limitada, mediante EKS Connector)                    |
| ¿Casos de uso?                 | Arquitectura nativa en AWS con Kubernetes | Centralizar monitoreo de clusters externos (multi-cloud) |

---

**Resumen**:

- **Crear** = clúster administrado y hospedado por AWS
- **Registrar** = clúster externo que solo se vincula a la consola EKS para visibilidad y gestión parcial

## Resumen de AWS App Runner: despliegue simple de aplicaciones web y APIs

**AWS App Runner** es un servicio completamente administrado que permite implementar fácilmente aplicaciones web y APIs en contenedores sin necesidad de gestionar infraestructura, servidores o balanceadores de carga.

---

### Características principales

- **Despliegue directo desde código fuente o imagen de contenedor**

  - Repositorios compatibles: **GitHub**, **AWS CodeCommit**, o **Amazon ECR**
  - App Runner detecta el tipo de aplicación (Node.js, Python, Java, etc.) y la construye automáticamente

- **Despliegue sin servidores (serverless)**

  - No se necesitan instancias EC2, clústeres ECS o nodos Kubernetes

- **Escalado automático**

  - Escala la cantidad de instancias en función del tráfico de red entrante
  - También escala a cero si no hay tráfico (opcional)

- **Alta disponibilidad**

  - Despliegue multi-AZ automático
  - Balanceo de carga incluido por defecto, sin configuración manual

---

### Acceso a redes y servicios

- **Acceso a VPC**:

  - App Runner puede conectarse a recursos privados en una VPC como bases de datos, caches o servicios internos
  - Esto se logra creando una **conexión VPC** administrada

- **Conexión a servicios de AWS**:

  - Soporte para conectarse a:

    - **Bases de datos** (RDS, Aurora)
    - **Cachés** (ElastiCache)
    - **Colas** (SQS)
    - **Secrets Manager / Parameter Store** para gestionar secretos y variables

---

### Seguridad

- Control de acceso mediante **IAM roles de ejecución**
- HTTPS activado por defecto
- Soporte para políticas de tráfico de entrada y salida
- Integración con **AWS WAF**, **X-Ray** y **CloudWatch Logs**

---

### Flujo de trabajo típico

1. El desarrollador sube su código fuente a GitHub o su imagen a ECR
2. App Runner crea un servicio a partir del código/imágen
3. App Runner realiza el build y el despliegue automáticamente
4. El servicio es expuesto con un **endpoint HTTPS**
5. Escala automáticamente de acuerdo a la demanda

---

### Casos de uso comunes

| Caso de uso                    | Descripción                                                            |
| ------------------------------ | ---------------------------------------------------------------------- |
| **APIs REST y microservicios** | Despliegue fácil con escalado bajo demanda y sin gestión de servidores |
| **Aplicaciones web ligeras**   | Hosting de apps frontend/backend con build automático desde GitHub     |
| **Aplicaciones internas**      | Conexión segura a VPC para acceso a servicios backend privados         |
| **Prototipos o MVPs**          | Rápida iteración sin necesidad de aprovisionar infraestructura         |

---

### Comparación con servicios similares

| Servicio              | ¿Para qué sirve?                                   | Gestión infra | Escala automático     | Acceso a VPC |
| --------------------- | -------------------------------------------------- | ------------- | --------------------- | ------------ |
| **App Runner**        | Apps web / APIs serverless, auto-build/deploy      | No            | Sí                    | Sí           |
| **ECS + Fargate**     | Contenedores en producción, configuración flexible | Parcial       | Sí                    | Sí           |
| **EKS**               | Kubernetes administrado                            | Sí            | Sí (con herramientas) | Sí           |
| **Elastic Beanstalk** | Apps web tradicionales con EC2                     | Parcial       | Parcial               | Sí           |

---

**AWS App Runner** es ideal para desarrolladores que desean enfocarse en el código y olvidarse de la infraestructura, pero aún necesitan escalabilidad, seguridad, y la capacidad de integrarse con servicios del backend de AWS.
