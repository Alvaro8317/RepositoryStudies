# Amazon DocumentDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Amazon DocumentDB** es un servicio de base de datos **NoSQL** orientado a documentos, con un diseño
de esquema flexible — típico de las bases de datos NoSQL. Su característica clave es que es **totalmente
compatible con MongoDB**.

## Compatibilidad con MongoDB

**MongoDB** es un conocido sistema de base de datos NoSQL, muy usado para manejar documentos **JSON**
y estructuras de datos complejas. DocumentDB emula su funcionalidad:

- Se pueden usar las mismas **herramientas y drivers** de MongoDB.
- Soporta las mismas **consultas y estructuras de datos** de MongoDB.
- Por debajo, usa la **implementación propia de AWS**, no MongoDB real — pero de cara al cliente el
  comportamiento es equivalente, sin las complicaciones de configurar MongoDB por cuenta propia.

## Gestión y escalado

- Servicio **totalmente gestionado**: aprovisionamiento, parches y toda la infraestructura los
  gestiona AWS.
- **Escalado automático**: la capacidad aumenta o disminuye según cambia la carga de trabajo de la
  aplicación.

## Alta disponibilidad y durabilidad

Construido sobre la infraestructura de AWS para ser altamente disponible y duradero:

- Replica automáticamente **6 copias** de los datos en **3 Availability Zones** distintas.
- Realiza **copias de seguridad continuas** de los datos en **S3**.

## Seguridad

- **Cifrado en reposo** mediante **KMS**.
- **Cifrado en tránsito** mediante **TLS**.
- Integración con **IAM** para autenticación y autorización de base de datos.

## Precios

- Por **horas de instancia** en ejecución.
- Por **almacenamiento** consumido en S3.
- Por operaciones de **I/O** realizadas.
- Posibles **costes adicionales de almacenamiento de backup**.
