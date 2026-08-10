# Práctica: Configurar Cross-Region Replication en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: crear un bucket de origen y uno de destino en regiones distintas, configurar una
regla de [[8-cross-region-replication|Cross-Region Replication]] entre ambos y comprobar en la
consola su comportamiento (unidireccional, sin replicar borrados).

## Creación de los buckets

### Bucket de origen

- Se crea en una región concreta (ej. `us-west-2`) con un nombre único (sufijo numérico aleatorio).
- El resto de ajustes se dejan por defecto, salvo uno: **hay que habilitar Versioning en el momento
  de la creación**. Sin esto, la replicación no funcionará (ver [[8-cross-region-replication]]).

### Bucket de destino

- Se crea en una **región distinta** a la del bucket de origen (ej. `us-east-1`), para obtener la
  capa adicional de redundancia y disponibilidad que ofrece CRR.
- A propósito, en esta práctica se crea **sin habilitar Versioning**, para comprobar más adelante que
  la consola bloquea la replicación hasta que se active.

## Crear la regla de replicación

Dentro del bucket de origen, en la pestaña **Management → Replication rules → Create replication
rule**:

1. **Nombre de la regla** (ej. `replication-test`).
2. **Estado**: habilitada (Enabled) por defecto.
3. **Ámbito (scope)**: se puede limitar por prefijo o etiquetas, igual que en las Lifecycle Rules (ver
   [[5-practice-lifecycle-rules]]). En esta práctica se aplica a **todos los objetos**.
4. **Bucket de destino**: se selecciona el bucket creado antes.
   > ⚠️ Si el bucket de destino no tiene Versioning habilitado, la consola muestra un error: la
   > replicación **requiere** que el versionado esté activado en el destino. Se puede habilitar desde
   > ahí mismo, sin salir del asistente.
5. **Rol IAM**: se puede elegir uno existente o dejar que la consola cree uno nuevo para este
   propósito.
6. **Replication Time Control (RTC)**: opcional, acelera la velocidad de la replicación a cambio de
   una tarifa adicional. No se habilita en esta práctica.
7. Al guardar, aparece la opción de **replicar objetos ya existentes** en el bucket (por defecto, la
   replicación **solo** aplica a objetos nuevos a partir de ahora, no a los que ya estuvieran en el
   bucket). Como el bucket está vacío, se elige no replicar objetos existentes.

## Comprobaciones

- **Replicación de un objeto nuevo**: al subir un archivo al bucket de origen, aparece en el bucket
  de destino en cuestión de segundos (casi en tiempo real; el tiempo depende del tamaño del archivo).
- **Solo funciona en una dirección**: subir un archivo directamente al bucket de destino **no** lo
  replica de vuelta al bucket de origen, incluso esperando y refrescando la consola.
- **Los borrados no se replican por defecto**: al eliminar el objeto en el bucket de origen, sigue
  disponible en el bucket de destino aunque se refresque después de un rato.

## Eliminar marcadores de borrado (delete markers)

En **Management → (regla) → Edit**, dentro de **Additional replication options**, existe una opción
para replicar también los **delete markers** hacia el bucket de destino (es decir, sí propagar los
borrados). En esta práctica se deja **desactivada**, ya que el objetivo es usar CRR como protección
adicional para disaster recovery — precisamente lo que se pierde si los borrados también se
replican.

## Gestión de la regla

Desde **Management → Replication rules**, la regla creada se puede **editar**, **deshabilitar** o
**eliminar** en cualquier momento mediante el menú **Actions**.
