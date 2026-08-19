# AWS Application Discovery Service

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es?

**AWS Application Discovery Service** ayuda a entender el propio **datacenter on-premise** antes de
migrar a AWS. Suele ser el **primer paso** de cualquier proyecto de migración: identificar dependencias
y configuraciones de servidores y bases de datos locales antes de planificar el traslado a la nube.

- Recopila información sobre servidores y bases de datos locales: especificaciones del servidor,
  dependencias, y métricas adicionales de uso.

## Formas de recolección de datos

| Método | Descripción |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Con agente** | Se instala un pequeño **agente de software** en los servidores (compatible con Windows y Linux), que recopila datos de configuración y de uso. |
| **Sin agente (Agentless)** | Se despliega un **Agentless Collector** mediante un archivo **OVA** a través de **VMware vCenter** — solo aplica a entornos con máquinas virtuales VMware. Permite recolectar automáticamente la información de todas las VMs de una vez, sin instalar un agente en cada una. |

## Uso de los datos recopilados

- Los datos recogidos se pueden **visualizar** para entender cómo es la infraestructura: servidores,
  bases de datos, su configuración, y métricas de utilización relevantes.
- Se pueden usar en la **consola de AWS Database Migration Service** para un análisis y una planificación
  más detallados de la migración.
- Se integra con **AWS Migration Hub**, que actúa como lugar centralizado donde se almacenan estos datos
  y se hace seguimiento del progreso de las migraciones.

> ⚠️ Entender bien la arquitectura on-premise (dependencias, configuración, métricas) mediante este
> servicio es clave para poder planificar y ejecutar con éxito la migración posterior.
