# AWS DataSync

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS DataSync?

**AWS DataSync** está diseñado para facilitar el movimiento de **grandes cantidades de datos**, sin
necesidad de escribir scripts ni gestionar configuraciones de red complejas.

- Su objetivo principal es transferir **archivos y datos de sistemas de archivos**.
- Automatiza y acelera la transferencia:
  - Entre sistemas de almacenamiento **on-premise** y servicios de AWS.
  - **Entre servicios de AWS** (no solo on-premise ↔ cloud).
- **Preserva permisos y metadatos de los archivos**:
  - Los permisos originales de control de acceso, establecidos en el origen, se mantienen al mover los
    archivos al destino.
  - Los metadatos (timestamps, información de propiedad, atributos adicionales) también se conservan —
    importante para archivos o aplicaciones que dependen de ellos.

> ⚠️ Si el ancho de banda de red en el entorno local es limitado, se puede considerar usar **AWS
> Snowcone** (parte de la [[1-snow-family|Snow Family]]), que incluye el software de DataSync integrado
> para acelerar la transferencia desde el entorno local hacia la nube.

## Características principales

- **Alta velocidad:** puede transferir datos hasta **10 veces más rápido** que los métodos
  tradicionales, gracias a un protocolo de red específico y técnicas de transferencia paralela.
- **Transferencias programadas (scheduled):** útil para backups periódicos o tareas de sincronización
  recurrentes.

> ⚠️ DataSync **no soporta transferencias continuas** — si se necesita sincronización continua, hay que
> configurar un schedule que se ejecute con la periodicidad deseada.

- **Integración con servicios de almacenamiento de AWS:**
  - **Amazon S3**
  - **Amazon EFS** (Elastic File System)
  - **Amazon FSx for Windows File Server**
  - Permite copiar tanto los datos como sus metadatos entre almacenamiento on-premise y estos servicios.

## Cómo funciona

1. **Instalar el agente de DataSync** en un servidor del entorno local (necesita acceso al sistema de
   archivos **NFS** o **SMB**) — solo aplica si la transferencia parte de on-premise.
2. **Configurar una tarea de DataSync** en la AWS Management Console, definiendo:
   - El **origen** (ej. path NFS/SMB) y el **destino** (recurso de AWS).
   - Parámetros adicionales: validación de datos, limitación de ancho de banda (throttling), y
     programación (ej. transferencias en horas valle para minimizar el impacto en la red).
3. **Transferencia:** los datos se transfieren dentro de una **conexión TLS** (cifrados), usando un
   protocolo propio optimizado para transferencias a alta velocidad por Internet, con **compresión** de
   datos para reducir el uso de ancho de banda y acelerar la transferencia.
4. **Escritura en destino:** al llegar al entorno de AWS, DataSync escribe los datos en el servicio
   elegido (S3, EFS o FSx). Cada servicio maneja los datos de forma distinta, pero DataSync se asegura
   de que el **formato de los datos y los permisos** se apliquen correctamente en cada caso.

Esta configuración permite aprovechar tanto la infraestructura de almacenamiento local existente como la
escalabilidad, durabilidad y características avanzadas de los servicios de AWS.
