# EBS vs EFS — Comparación y Repaso Final

> Resumen de cierre del módulo de almacenamiento en AWS, comparando **Amazon EBS** (Elastic Block Store) y **Amazon EFS** (Elastic File System).

## Amazon EBS — Puntos clave a recordar

- Un volumen EBS **solo puede adjuntarse a una instancia a la vez**, salvo que se use la característica **EBS Multi-Attach**.
- **Restricción de zona de disponibilidad (AZ):** tanto en el modo normal como en Multi-Attach, el volumen debe estar en la **misma AZ** que la(s) instancia(s) a la(s) que se adjunta.
- **Multi-Attach solo es compatible** con volúmenes de tipo **io1** e **io2 Block Express** (no con todos los tipos de volumen).
- **Migrar un volumen entre zonas de disponibilidad** requiere dos pasos:
  1. Crear un **snapshot** (instantánea) del volumen EBS.
  2. **Restaurar ese snapshot** en la zona de disponibilidad destino.
  - Después, el nuevo volumen puede adjuntarse a una instancia en esa nueva zona.
- **Volúmenes EBS root (raíz):** por defecto, **se terminan automáticamente cuando se termina la instancia EC2**.
  - ⚠️ Es un detalle que se suele olvidar y puede provocar pérdida de datos no intencionada. Conviene revisar y, si es necesario, cambiar este comportamiento antes de terminar una instancia.

## Amazon EFS — Puntos clave a recordar

- Permite adjuntar **múltiples instancias EC2**, incluso en **diferentes zonas de disponibilidad y diferentes regiones**, a un mismo sistema de archivos.
- **Alta disponibilidad y durabilidad**, con capacidad de **escalar a niveles muy altos**.
- Soporta uso **concurrente de miles de instancias EC2**.
- **Escalado automático** hacia arriba y hacia abajo según el uso: se paga solo por el espacio efectivamente utilizado.
- Es un servicio **serverless**: no requiere administrar infraestructura subyacente.
- **Limitación de compatibilidad:** actualmente solo disponible para **instancias Linux de tipo POSIX**.
- **Precio:** más elevado que EBS, por lo que conviene siempre evaluar el *pricing* antes de decidir la arquitectura.

## Comparación rápida

| Aspecto | Amazon EBS | Amazon EFS |
|---|---|---|
| Nº de instancias | 1 (o pocas con Multi-Attach) | Miles, de forma concurrente |
| Alcance | Ligado a una única AZ | Múltiples AZ / regiones |
| Escalado | Manual (tamaño fijo del volumen) | Automático (arriba y abajo) |
| Administración de infraestructura | Requerida | No requerida (serverless) |
| Compatibilidad de SO | Cualquiera compatible con EC2 | Solo Linux POSIX |
| Coste | Más económico | Más elevado |
| Migración entre AZ | Snapshot + restauración | No aplica (ya es multi-AZ) |
| Caso de uso típico | Disco de una sola instancia (ej. volumen raíz, BBDD local) | Almacenamiento compartido entre múltiples instancias |

## Idea clave para decidir

- Si el caso de uso implica **una sola instancia** (o pocas en la misma AZ) accediendo a un disco: **EBS**.
- Si el caso de uso implica **compartir archivos entre múltiples instancias**, posiblemente en distintas zonas o regiones: **EFS**.
- En ambos casos, **siempre evaluar el pricing** antes de tomar la decisión de arquitectura final.
