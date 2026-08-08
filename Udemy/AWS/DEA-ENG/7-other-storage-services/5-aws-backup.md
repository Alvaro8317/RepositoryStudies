# AWS Backup

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Backup?

**AWS Backup** permite configurar y administrar copias de seguridad desde un **único lugar
centralizado**.

- Se pueden crear **políticas de backup** y aplicarlas a distintos servicios de AWS: instancias **EC2**,
  **Amazon RDS**, **Amazon EFS**, etc.
- Todo se gestiona de forma centralizada desde AWS Backup, sin necesidad de configurar copias de seguridad
  por separado en cada servicio.

## Planes de backup (Backup plans)

El proceso de copia de seguridad se **automatiza** mediante **planes de backup**, que definen:

- **Frecuencia** de las copias de seguridad (diaria, semanal, mensual, etc.).
- **Periodo de retención**: cuánto tiempo se conservan.

Esta automatización garantiza que las copias se realicen de forma periódica **sin intervención manual**.

- También es posible copiar los backups a **otras regiones** de AWS e incluso a **otras cuentas** de AWS,
  algo especialmente útil para escenarios de **recuperación ante desastres (disaster recovery)**.

## Restauración

AWS Backup ofrece un proceso sencillo de **restauración**, que permite recuperar:

- Archivos individuales.
- Directorios.
- Sistemas completos.

> ⚠️ Lo que se puede restaurar exactamente depende del **servicio** sobre el que se creó la copia de
> seguridad y de la naturaleza del backup.

## Conformidad, seguridad y monitorización

- Permite establecer normas de **retención** y de **ciclo de vida** de las copias de seguridad para cumplir
  requisitos de conformidad (compliance).
- Se integra con **IAM**, permitiendo controlar quién puede acceder a las copias de seguridad y
  administrarlas.
- Ofrece un **dashboard** para monitorizar el estado de los backups y ver informes detallados, útil para
  confirmar que las copias se completaron correctamente o detectar problemas.

## Flujo básico de uso

1. Definir un **plan de backup**: frecuencia deseada y periodos de retención.
2. Configurar los **recursos** que se quieren incluir en la copia de seguridad.
3. Supervisar las copias de seguridad desde la **consola de gestión**.

AWS Backup almacena los datos en un **bucket interno de S3** asignado específicamente para este servicio.

## Backup Vault

Un **backup vault** (bóveda de backup) es un **contenedor donde se almacenan las copias de seguridad de
forma segura**.

- Se pueden crear varias bóvedas para organizar las copias de seguridad según distintos criterios:
  departamento, aplicación, necesidades específicas de cumplimiento, etc.

## AWS Backup Vault Lock

**Vault Lock** mejora la seguridad y el cumplimiento de las copias de seguridad permitiendo aplicar
**salvaguardas inmutables** sobre los backups almacenados en una bóveda.

- Útil para requisitos regulatorios donde se necesita **inmutabilidad de los datos**, protegiéndolos frente
  a eliminación o alteración accidental o maliciosa.
- Una vez que se aplica el lock a una bóveda, la política se vuelve **inmutable durante el periodo
  especificado**: nadie —ni siquiera el usuario root— puede alterar o eliminar los puntos de recuperación
  almacenados antes de que expire ese periodo.

> ⚠️ Vault Lock es especialmente relevante en sectores como el **financiero** o **sanitario**, donde se
> exige integridad y seguridad estricta de los datos almacenados.

### Modos de Vault Lock

| Modo           | Detalle                                                                                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compliance** | La política del vault **no puede modificarse ni eliminarse** mientras dure el periodo de bloqueo. Cumplimiento estricto.                                    |
| **Governance** | Permite a roles de IAM específicos **gestionar y actualizar** las políticas del vault, pero sigue protegiendo los puntos de recuperación frente al borrado. |
