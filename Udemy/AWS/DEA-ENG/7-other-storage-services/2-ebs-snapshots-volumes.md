# EBS: Snapshots, tipos de volumen y configuración

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## EBS Snapshots

Una **snapshot** de EBS es la captura del estado de un volumen en un **punto específico en el
tiempo**, y funciona como copia de seguridad de sus datos.

### Cómo funcionan

- **Copias de seguridad incrementales**: solo se guardan los bloques que han cambiado desde la última
  snapshot, lo que reduce el coste de almacenamiento y mejora la eficiencia.
- Operan a **nivel de bloque**: capturan todos los bloques de datos, los metadatos y los ajustes de
  configuración asociados al volumen.
- Antes de crear la snapshot, AWS garantiza la **consistencia de los datos** pausando temporalmente las
  operaciones de I/O en el volumen, para generar una imagen coherente del punto en el tiempo. Todo esto
  lo gestiona AWS automáticamente.
- Se almacenan en **Amazon S3**, lo que aporta durabilidad mediante la replicación de los datos entre
  múltiples **Availability Zones** dentro de una región.
- Se **comprimen automáticamente** (reduciendo aún más el coste de almacenamiento) y se **cifran en
  reposo** — se puede usar **AWS KMS** para gestionar las claves de cifrado.

### Gestión del ciclo de vida

AWS permite definir **políticas de ciclo de vida** para las snapshots, automatizando tareas como:

- **Retención**.
- **Eliminación**.
- **Copia** a otras regiones.

### Recuperación de datos

- Se pueden crear **nuevos volúmenes EBS a partir de una snapshot**, restaurando el volumen a un
  estado anterior.
- Las snapshots se pueden **copiar a otra región**, generando redundancia o permitiendo adjuntar un
  volumen equivalente a una instancia EC2 en esa otra región.

> El coste de las snapshots es bastante bajo para conservación de datos a largo plazo, pero conviene
> vigilar su uso y aplicar políticas de retención (gestión del ciclo de vida) para optimizar el coste,
> ya que se factura según la cantidad de datos almacenados en S3.

## Aprovisionamiento de capacidad

Al crear un volumen se especifica el **tamaño en GB** (capacidad total) y, según el tipo de volumen,
características adicionales como las **IOPS**.

### Tipos de volumen

| Tipo                                | Ejemplos                  | Uso recomendado                                                                                                   |
| ----------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **SSD de uso general**              | gp2, gp3                  | Buen equilibrio entre precio y rendimiento; adecuado para la mayoría de las cargas de trabajo.                    |
| **IOPS provisionadas SSD**          | io1, io2                  | Aplicaciones intensivas en I/O que necesitan rendimiento **consistente y predecible**, o sensibles a la latencia. |
| **HDD optimizado para rendimiento** | st1                       | Cargas de trabajo de acceso frecuente y secuencial, a menor coste.                                                |
| **HDD frío / magnético**            | sc1, standard (magnético) | Acceso poco frecuente; opción más económica cuando no se necesita alto rendimiento.                               |

> Se puede migrar directamente de **gp2** a **gp3** (nueva generación): en gp3 las IOPS y el
> throughput se configuran de forma **independiente** del tamaño del volumen, permitiendo obtener mejor
> rendimiento a menor coste sin necesidad de aprovisionar más almacenamiento. La actualización es
> fluida — solo hay que ajustar rendimiento e IOPS deseados.

Con **IOPS provisionadas**, se puede ajustar el número de IOPS según los requisitos de lectura/escritura
específicos de la aplicación.

### Tamaño del volumen y rendimiento

Aumentar el tamaño de un volumen (especialmente en SSD de uso general, ej. gp2) puede mejorar
indirectamente el rendimiento: los volúmenes más grandes suelen tener un **rendimiento base más alto**
y pueden sostener una **tasa de I/O más alta** durante más tiempo.

## Monitorización

Se pueden supervisar los volúmenes EBS con **Amazon CloudWatch**, revisando métricas como:

- Volumen de operaciones de lectura/escritura.
- **Latencia**.
- **Longitud de cola** (queue length).

Este monitoreo ayuda a identificar posibles **cuellos de botella** y a optimizar los recursos.

## Delete on Termination

> ⚠️ Detalle relevante para el examen.

El atributo **Delete on Termination** determina si un volumen EBS debe **eliminarse automáticamente**
cuando la instancia EC2 asociada se **termina**:

- **Activado**: el volumen se elimina automáticamente al terminar la instancia — útil para ahorrar
  costes cuando el volumen solo tiene sentido mientras existe esa instancia.
- **Desactivado**: el volumen se conserva de forma independiente, aunque la instancia EC2 asociada se
  termine.

Esta opción se especifica normalmente al **lanzar** la instancia EC2 desde la consola, y también se
puede **modificar** posteriormente en una instancia EC2 ya existente.
