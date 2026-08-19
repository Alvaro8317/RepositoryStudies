# AWS Transfer Family

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Transfer Family?

**AWS Transfer Family** es un servicio **totalmente gestionado** que facilita la transferencia segura de
archivos hacia y desde los servicios de almacenamiento de AWS.

- Usa protocolos estándar de transferencia de archivos:
  - **SFTP** (SSH File Transfer Protocol).
  - **FTPS** (FTP sobre SSL, para seguridad).
  - **FTP** (File Transfer Protocol).
- Pensado para empresas que **intercambian archivos con frecuencia** de forma segura con socios o
  clientes — por ejemplo, para migrar o sincronizar datos como parte de su estrategia.

## Características principales

- **Totalmente gestionado:** AWS se encarga del escalado, la disponibilidad y el mantenimiento de la
  infraestructura de transferencia.
- **Integración con S3 y Amazon EFS:** permite almacenar y acceder a archivos directamente desde estos
  servicios.
- **Personalizable:**
  - Enrutamiento DNS configurable.
  - Métodos de autenticación de usuarios ajustables — la autenticación puede vincularse a sistemas
    existentes como **roles IAM**.
  - Distintos mecanismos de control de acceso.
- Permite construir flujos de transferencia de archivos **sin modificar las aplicaciones existentes ni
  gestionar servidores de transferencia** propios, reduciendo así los gastos operativos.
- **Modelo de precios pay-per-use:** solo se paga por la transferencia de archivos y la gestión de
  usuarios; no hace falta aprovisionar ni mantener servidores físicos ni infraestructura propia.

## Casos de uso

- **Distribución de datos:** empresas que distribuyen datos globalmente a socios o equipos internos de
  forma segura.
- **Automatización de backups:** copiar datos automáticamente a **S3** o **EFS**, obteniendo una
  solución de almacenamiento segura y duradera conectada a un mecanismo de transferencia de archivos
  seguro.

## Resumen

AWS Transfer Family es una solución **flexible y escalable** para organizaciones que buscan agilizar su
proceso de transferencia de archivos manteniendo altos niveles de **seguridad y cumplimiento**, gracias a
su integración nativa con otros servicios de AWS.
