# Amazon RDS (Relational Database Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**RDS** (*Relational Database Service*) es un servicio de base de datos relacional **totalmente
gestionado** en el que se pueden alojar los motores de base de datos habituales (MySQL, PostgreSQL,
etc.) sin tener que gestionar la infraestructura subyacente.

### El problema que resuelve

Montar y mantener una base de datos relacional por cuenta propia implica, entre otras cosas:

- Aprovisionar un servidor (físico o máquina virtual).
- Instalar y configurar el motor de base de datos.
- Configurar seguridad: firewall, control de acceso.
- Garantizar rendimiento y alta disponibilidad (por ejemplo, con réplicas).
- Mantenimiento continuo: parches, actualizaciones, copias de seguridad.

RDS se encarga de toda esta gestión, permitiendo centrarse en el desarrollo de la aplicación en vez
de en la administración de la base de datos.

## Ventajas

- **Escalable**, al apoyarse en la infraestructura subyacente de AWS.
- **Fiable y rentable**, ya que AWS gestiona la administración por completo.
- Soporta los **motores de base de datos relacional más comunes** (MySQL, PostgreSQL, y otros).
- **Integración sencilla** con el resto de servicios de AWS relevantes.
- Aprovisionamiento y gestión de la infraestructura con solo unos clics, manteniendo el mismo motor
  de base de datos con el que ya se esté familiarizado.

En el contexto de big data no es el servicio más central, al ser una base de datos relacional, pero
es habitual **migrar datos desde RDS** hacia servicios analíticos como **Redshift** u otros.

## Seguridad

- **VPC**: se puede desplegar la base de datos dentro de una **Virtual Private Cloud** propia, con
  grupos de seguridad de tráfico entrante/saliente totalmente configurables, para un entorno aislado.
- **Cifrado de datos**: añade una capa adicional de protección — si alguien accede a los datos sin
  autorización, no podrá leerlos al estar cifrados.
- **Copias de seguridad, parches y recuperación**: gestionados por AWS, ahorrando tiempo y esfuerzo.
  - Se puede usar **AWS Backup** como servicio centralizado para automatizar todas las copias de
    seguridad, o crear copias manuales.
  - Las copias de seguridad se pueden usar para restaurar la base de datos de forma fiable y
    eficiente, con gestión centralizada en AWS Backup.
- **IAM**: integración con IAM para definir roles, usuarios y permisos, implementando control de
  acceso a la base de datos de forma sencilla.
