# Kubernetes y Amazon EKS (Elastic Kubernetes Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Kubernetes?

**Kubernetes** es una plataforma **open source** diseñada para automatizar el despliegue, la gestión y
el escalado de aplicaciones en contenedores.

- Agrupa uno o varios ordenadores (máquinas virtuales o físicas) en un **cluster**, que ejecuta las
  cargas de trabajo en contenedores.
- Fue creado originalmente por **Google**, pero hoy lo mantiene una comunidad global de colaboradores.
- Facilita el despliegue y la gestión de aplicaciones complejas en contenedores **a gran escala**,
  proporcionando un marco para ejecutarlas y gestionarlas dentro de un cluster.
- Es adecuado para cargas de trabajo de distintos tamaños y estilos — de ahí su gran adopción.
- **No es nativo de la nube**: no fue diseñado originalmente para ella, aunque puede ejecutarse en un
  entorno cloud.

## ¿Qué es Amazon EKS?

**Amazon EKS** es un servicio de **Kubernetes gestionado** que permite ejecutar Kubernetes en la nube de
AWS o también en un centro de datos on-premise.

- Se integra con otros servicios de AWS:
  - **Elastic Load Balancing**
  - **Amazon VPC** (para ejecutar en un entorno aislado)
  - **IAM** (control de acceso)
  - **Amazon CloudWatch** (logging y métricas)
  - **AWS CloudTrail**
- Garantiza **alta disponibilidad** desplegando las instancias del **control plane** en varias zonas de
  disponibilidad dentro de una región.
- Es **escalable**: permite escalar los clusters hacia arriba y hacia abajo según la demanda de la
  aplicación, pudiendo añadir o eliminar nodos de trabajo de forma dinámica sin interrumpir la
  aplicación.
- Aprovecha las características de seguridad integradas de AWS: aislamiento de red vía VPC, control de
  acceso vía IAM, y cifrado de datos en tránsito y en reposo.
- Se integra con **CloudWatch** para monitorizar clusters y aplicaciones.

## Arquitectura: dos componentes principales

### Control plane

- Servicio que **gestiona el cluster de Kubernetes**: toma las decisiones del cluster, por ejemplo qué
  nodo debe ejecutar qué carga de trabajo.
- Está compuesto por múltiples nodos que ejecutan el software de Kubernetes.
- Es responsable de la **gestión y orquestación** de los distintos componentes del cluster.
- Normalmente habría que gestionarlo uno mismo (lo cual es complejo), pero con **Amazon EKS está
  totalmente gestionado**: AWS se encarga del aprovisionamiento, escalado y mantenimiento de los
  componentes del control plane.

### Worker nodes (nodos de trabajo)

- Proporcionan la **potencia de cálculo** necesaria para ejecutar las aplicaciones en contenedores:
  máquinas físicas o virtuales con la CPU, memoria y almacenamiento necesarios, todo orquestado por
  Kubernetes.

En Amazon EKS existen los siguientes tipos de nodos:

| Tipo de nodo            | Descripción                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AWS Fargate**         | Motor de cómputo **serverless** para contenedores; AWS gestiona toda la infraestructura subyacente. Solo hay que especificar los requisitos de la aplicación.                                                      |
| **Karpenter**           | Lanza recursos de cómputo del tamaño adecuado en respuesta a los cambios de carga de la aplicación. Adecuado para contenedores con requisitos de disponibilidad muy altos.                                         |
| **Managed node groups** | Amazon EKS crea y gestiona las instancias EC2 por el usuario: se usan instancias EC2, pero gestionadas por AWS.                                                                                                    |
| **Self-managed nodes**  | Control total sobre las instancias EC2 del cluster: el usuario gestiona todo, incluidos escalado y mantenimiento. Útil cuando se necesita personalización y control total, a cambio de asumir esa responsabilidad. |
