# AWS Snow Family

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es la Snow Family?

La **Snow Family** son **dispositivos físicos** de AWS diseñados para transferir grandes cantidades de
datos, especialmente en entornos con **conectividad limitada**.

- Cuando hay que mover grandes volúmenes de datos pero el ancho de banda disponible es limitado (o
  simplemente llevaría demasiado tiempo transferirlos por Internet), se usa un dispositivo físico: los
  datos se cargan en el dispositivo, y este se envía de vuelta a AWS para completar la carga — **sin
  pasar los datos por Internet**.
- Algunos dispositivos (**Snowball Edge** y **Snowcone**) ofrecen, además de transferencia de datos,
  **cómputo y almacenamiento local**, permitiendo ejecutar aplicaciones directamente en el dispositivo y
  procesar los datos localmente antes de enviarlos a la nube (**edge computing**).
- Todos los dispositivos vienen equipados con:
  - **Cifrado en reposo y en tránsito**, usando **AWS KMS** para las claves de cifrado.
  - Resistencia a manipulación (tamper-resistant).
  - Diseño robusto para soportar entornos adversos (plantas industriales, ubicaciones al aire libre,
    minería, zonas remotas, etc.).

## Tipos de dispositivo

### Snowcone

- El dispositivo **más pequeño y portátil** de la familia: cabe en una mochila estándar y pesa unos
  **2 kg**.
- Ofrece **8 TB** de almacenamiento utilizable.
- Diseñado para almacenamiento, transferencia de datos y **edge computing** en lugares con
  conectividad limitada.
- Incluye el **agente DataSync**, que facilita el proceso de transferencia de datos.
- Se ejecuta sobre **AWS IoT Greengrass** y puede ejecutar funciones de **AWS Lambda**, permitiendo
  procesar datos y ejecutar aplicaciones localmente incluso sin conexión.

### Snowball Edge

- Diseñado para transferir **grandes cantidades de datos** entre la nube y ubicaciones locales; también
  ofrece capacidades de edge computing.
- Existen dos versiones:

| Versión               | Almacenamiento | Enfoque                                                                                                     |
| --------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| **Storage Optimized** | Hasta 80 TB    | Prioriza el espacio de almacenamiento, para mover y almacenar grandes volúmenes de datos.                   |
| **Compute Optimized** | Hasta 42 TB    | Menos almacenamiento, pero con más potencia de cómputo, para procesar datos directamente en el dispositivo. |

- Los datos se cifran tanto en tránsito como en el propio dispositivo.
- Está construido para soportar entornos difíciles (fuera de un datacenter típico), útil para
  recopilar y procesar datos localmente en zonas remotas.

### Snowmobile

- Un **centro de datos portátil** alojado en un contenedor de ~15 metros, transportado en camión.
- Puede albergar hasta **100 PB** de datos — pensado para las mayores migraciones de datos posibles.
- Los datos se cargan en el camión, que se conduce de vuelta a las instalaciones de AWS, donde se
  descargan y se suben a la nube del cliente.
- Se usa cuando hay que transferir **más de 10 PB** de datos, un volumen que ya no resulta práctico
  mover con múltiples dispositivos Snowball.

## Flujo de trabajo

1. Se solicita el dispositivo desde la **AWS Management Console**, eligiendo el tipo según las
   necesidades de transferencia de datos y/o edge computing (cantidad de datos, destino, caso de uso).
2. AWS prepara y envía el dispositivo, ya configurado con seguridad y software listos para usar.
3. Al recibirlo, se conecta a los servidores/sistemas de almacenamiento locales y se gestiona mediante la
   interfaz **AWS OpsHub**, tanto para transferir datos como (en Snowcone/Snowball Edge) para configurar
   tareas de edge computing.
4. Una vez transferidos los datos, el dispositivo se empaqueta de forma segura y se devuelve a AWS.
5. AWS conecta el dispositivo a su red y sube los datos de forma segura a los servicios de destino (ej.
   **S3**, **Amazon Glacier**), manteniendo el cifrado durante todo el proceso.

## Cuándo usar cada dispositivo

| Volumen de datos              | Dispositivo recomendado                                       |
| ----------------------------- | ------------------------------------------------------------- |
| Hasta 8 TB                    | **Snowcone**                                                  |
| 8–24 TB                       | **Snowcone** (límite) → considerar Snowball Edge si se supera |
| Hasta 42 TB (con más cómputo) | **Snowball Edge – Compute Optimized**                         |
| Hasta 80 TB                   | **Snowball Edge – Storage Optimized**                         |
| Más de 10 PB                  | **Snowmobile**                                                |

> ⚠️ La elección del dispositivo depende principalmente de dos factores: la **cantidad de datos** a
> transferir y si se necesita **potencia de cómputo** (edge computing) además de almacenamiento.
