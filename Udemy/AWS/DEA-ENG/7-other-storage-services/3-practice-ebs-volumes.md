# Práctica: Crear y adjuntar volúmenes EBS

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

**Volumes** es una funcionalidad dentro de **EC2** (no un servicio independiente), pensada
específicamente para crear y gestionar volúmenes EBS asociados a instancias EC2.

## Crear la instancia EC2

Antes de crear un volumen adicional, se lanza una instancia EC2 básica:

- **Sistema operativo**: Ubuntu.
- **Tipo de instancia**: `t2.micro` (dentro de la capa gratuita).
- **Key pair**: obligatorio para poder conectarse a la instancia desde el equipo local.
- Al configurar el almacenamiento, además del **volumen raíz**, se puede añadir un **volumen
  adicional** directamente desde el asistente de lanzamiento (ej. tipo **gp2**, tamaño **4 GB**).

## Crear un volumen EBS de forma independiente

En **EC2 → Volumes → Create volume**:

- Se elige el **tipo** de volumen (ej. gp2) y el **tamaño** (ej. 4 GB).
- Es obligatorio elegir la **Availability Zone**: debe coincidir exactamente con la de la instancia
  EC2 a la que se quiera adjuntar el volumen (se puede comprobar la AZ de la instancia en su detalle).

> ⚠️ Un volumen recién creado solo puede adjuntarse a instancias que estén en su **misma Availability
> Zone**. Un volumen en otra AZ (por ejemplo, de una instancia ya terminada) ni siquiera aparece como
> opción al intentar adjuntarlo a una instancia en una AZ distinta.

## Adjuntar el volumen a la instancia

1. En **Volumes**, seleccionar el volumen recién creado (estado **available**, "not in use").
2. **Attach volume** → elegir la instancia EC2 (debe estar en la misma AZ) y el **nombre de
   dispositivo** (ej. `/dev/sdd`).
3. Tras adjuntarlo, el volumen pasa a estado **in-use**.

## Delete on Termination en la práctica

Al revisar el almacenamiento de la instancia (**Storage** tab), se ven los distintos volúmenes
adjuntos y su configuración de **Delete on Termination**:

- El **volumen raíz** tiene este atributo activado (`Yes`) **por defecto**.
- Los volúmenes **adicionales** adjuntados aparte tienen este atributo desactivado (`No`) por defecto.

### Demostración: terminar la instancia

Al terminar (**Terminate**) la instancia:

- El **volumen raíz** se elimina automáticamente junto con la instancia (comportamiento por defecto
  en una instancia respaldada por EBS).
- Los **volúmenes adicionales** (con Delete on Termination desactivado) **permanecen** disponibles en
  **Volumes** tras la terminación, y hay que eliminarlos **manualmente** si ya no se necesitan
  (escribiendo `delete` para confirmar la eliminación).

### Configuración avanzada al crear un volumen

Al lanzar una nueva instancia (o añadir un volumen desde el asistente), la sección **Advanced** de la
configuración de almacenamiento permite ajustar, volumen por volumen:

- **Delete on Termination** (activado/desactivado).
- **Tipo de volumen**.
- **IOPS**.
- **Cifrado**.

## Conclusión

Esta práctica confirma el comportamiento de `Delete on Termination` visto en la teoría: se define por
volumen (root vs. adicionales) al crear/adjuntar el volumen, con el volumen raíz eliminándose por
defecto al terminar la instancia y los volúmenes adicionales sobreviviendo hasta que se borran de
forma explícita.
