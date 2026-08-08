# Amazon EFS (Elastic File System)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es Amazon EFS?

**Amazon EFS** (Elastic File System) ofrece almacenamiento de archivos **totalmente elástico y sin
servidor**, pensado para **compartir archivos**.

- No es necesario aprovisionar ni gestionar la capacidad de almacenamiento ni el rendimiento subyacente:
  AWS lo gestiona automáticamente.
- **Alta disponibilidad**: los datos se replican en varias **zonas de disponibilidad** dentro de una misma
  región.
- **Elástico y escalable**: se amplía y reduce automáticamente según la carga de trabajo, lo que también
  ayuda a ahorrar costes (cuando no se necesita capacidad, esta se reduce).

## EFS vs. EBS

La gran diferencia frente a **EBS** es que un volumen EBS solo puede conectarse a **una** instancia EC2 a
la vez, mientras que un sistema de archivos EFS puede montarse en **múltiples instancias EC2
simultáneamente**.

- Esto permite usar EFS como un **sistema de archivos compartido**, facilitando la colaboración y el
  acceso concurrente a los mismos archivos desde distintas instancias EC2.

## Compatibilidad

- Utiliza el protocolo **NFS v4.1**, lo que le da una amplia compatibilidad.
- Es **totalmente compatible con el estándar POSIX**: expone el conjunto de llamadas API y operaciones de
  archivo típicas de sistemas Unix, lo que facilita portar aplicaciones entre distintos sistemas operativos
  basados en Unix.
- Soporta hasta **1000 clientes NFS** conectados simultáneamente.

## Precios

Modelo de **pago por consumo**, sin costes iniciales:

- Se paga en función del **almacenamiento** utilizado y de la **transferencia de datos**.

## Seguridad

- Los datos se cifran, y se puede usar **KMS** para crear y gestionar las propias claves de cifrado.
- KMS permite además **rotar** las claves y **eliminarlas automáticamente**.

## Clases de almacenamiento

| Clase                      | Detalle                                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| **Standard**               | Replicación de datos entre múltiples zonas de disponibilidad. Alta disponibilidad.                 |
| **IA (Infrequent Access)** | Para datos a los que se accede con poca frecuencia. Más económico.                                 |
| **One Zone-IA**            | Igual que IA, pero los datos **no** se replican entre zonas de disponibilidad, solo dentro de una. |

> ⚠️ Las clases **IA** y **One Zone-IA** son opciones de ahorro de costes para datos de acceso poco
> frecuente o sin requisitos de alta disponibilidad multi-AZ.

## Modos de rendimiento (Performance modes)

| Modo                | Uso recomendado                                                                                                                              | Escalado                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **General Purpose** | La mayoría de los casos de uso (ej. gestión de contenido web). Baja latencia, buen rendimiento general.                                      | Automático, según la cantidad de datos almacenados.               |
| **Max I/O**         | Cargas de trabajo con mayores exigencias de IOPS y rendimiento agregado (ej. análisis de big data, procesamiento intensivo, bases de datos). | Manual: hay que aprovisionar la capacidad de caudal (throughput). |

## Modos de throughput

| Modo                            | Uso recomendado                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Bursting (ráfaga)**           | Patrones de acceso impredecibles o puntuales, usando créditos de ráfaga acumulados para picos cortos de rendimiento.  |
| **Provisioned (aprovisionado)** | Rendimiento constante y predecible; se aprovisiona una cantidad específica de throughput para el sistema de archivos. |
