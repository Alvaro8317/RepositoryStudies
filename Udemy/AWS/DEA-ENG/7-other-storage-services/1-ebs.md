# Amazon EBS (Elastic Block Store)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es EBS?

**Amazon EBS** (Elastic Block Store) proporciona **almacenamiento de bloques duradero y escalable**
para instancias **EC2**. Ofrece almacenamiento persistente para distintos tipos de datos: archivos del
sistema operativo, datos de aplicaciones o bases de datos.

- Los volúmenes EBS están diseñados para **alta disponibilidad y durabilidad**: los datos se replican
  dentro de una **Availability Zone (AZ)**, protegiendo frente a fallos de hardware.
- Un volumen EBS se **adjunta (attach)** a una instancia EC2 concreta.

> ⚠️ Un volumen EBS solo puede adjuntarse a **una instancia EC2 a la vez** (no se puede compartir entre
> varias instancias simultáneamente). Sin embargo, una misma instancia sí puede tener **varios volúmenes**
> adjuntos, igual que una máquina física puede tener varios discos duros.

## Características principales

### Escalabilidad

La capacidad de almacenamiento se puede aumentar o reducir de forma **dinámica**, sin tiempo de
inactividad, para adaptarse a las necesidades cambiantes de la carga de trabajo.

### Durabilidad

La redundancia está incorporada, garantizando alta disponibilidad y protección frente a pérdida de
datos:

| Tipo de volumen        | Durabilidad   | Tasa de fallo anual |
| ---------------------- | ------------- | ------------------- |
| **io2 Block Express**  | 99.999%       | ~0.001%             |
| Otros tipos de volumen | 99.8% – 99.9% | ~0.1% – 0.2%        |

### Almacenamiento a nivel de bloque

Como indica su nombre, EBS trabaja a **nivel de bloque**, lo que da un control más granular sobre el
almacenamiento y el acceso a los datos — muy útil para adaptar el almacenamiento a las necesidades
específicas de cada instancia EC2.

### Almacenamiento persistente

Los datos se conservan aunque la instancia EC2 asociada se **detenga o finalice**, garantizando
disponibilidad, integridad y continuidad de los datos.

### EBS Snapshots

Las **instantáneas (snapshots)** permiten hacer copia de seguridad de los datos de un volumen y:

- Restaurar volúmenes al instante a partir de la snapshot.
- **Migrar** los datos a otra **Availability Zone**, otra **región**, o incluso a otra **cuenta de
  AWS**.

> ⚠️ Un volumen EBS está vinculado a una **Availability Zone** específica: no se puede desconectar de
> una instancia y conectar directamente a una instancia en otra AZ. Para moverlo a otra AZ, región o
> cuenta, es necesario pasar por una **snapshot**.

### Alto rendimiento

Existen distintos tipos de volumen adaptados a la carga de trabajo concreta:

- **SSD de uso general**.
- **IOPS provisionados (SSD)**.
- **HDD optimizado para rendimiento**.

### Cifrado

Los datos se pueden proteger mediante **cifrado**, tanto en reposo como en tránsito entre instancias.

### Precios

Modelo de **pago por uso**, con distintas opciones para optimizar el coste según las necesidades
específicas.

### Integración con EC2

Los volúmenes se pueden **adjuntar y separar** fácilmente de las instancias EC2, ofreciendo
almacenamiento flexible y fácil de gestionar.

## Cómo funciona

1. Se crea un **volumen EBS** con un tamaño y tipo específicos (ej. SSD de uso general).
2. Se **adjunta** el volumen a una instancia EC2.
3. La instancia accede al volumen como si fuera un **disco duro físico**: se puede formatear con un
   sistema de archivos y montar en un directorio, obteniendo así un sistema de archivos directamente
   adjunto a la instancia.
