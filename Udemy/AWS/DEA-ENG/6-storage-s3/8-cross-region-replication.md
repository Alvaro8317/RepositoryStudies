# Cross-Region Replication (CRR) en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Cross-Region Replication** consiste en copiar y sincronizar automáticamente los datos de un bucket
de S3 (**bucket de origen**) hacia otro bucket ubicado en una **región completamente distinta**
(**bucket de destino**). Todo el contenido nuevo que se añade al bucket de origen se replica y
mantiene sincronizado con el bucket de destino.

## Beneficios

- **Disaster recovery** — si ocurre una interrupción regional (ej. una caída del centro de datos de
  una región completa), los datos siguen disponibles en la región de destino gracias a esta
  redundancia adicional.
- **Rendimiento / latencia reducida** — al tener los datos también en la región donde están la
  mayoría de los usuarios, se reduce la latencia de acceso.
- **Mayor disponibilidad y durabilidad** — la redundancia adicional entre regiones protege frente a
  cortes temporales, manteniendo los datos accesibles.

## Casos de uso

### Disaster recovery

Ejemplo: una empresa de salud tiene datos críticos en la región de Sídney y habilita CRR hacia un
bucket en la región de Tokio. Si ocurre una interrupción regional en Sídney, los datos siguen
disponibles en Tokio gracias a esta capa adicional de redundancia — la empresa queda protegida frente
al fallo.

### Reducción de latencia

Ejemplo: una empresa de gaming con sede en Estados Unidos, pero cuya mayoría de usuarios está en
Europa, replica sus datos a un bucket de S3 en la UE. Esto acerca los datos a los jugadores europeos,
reduce los tiempos de acceso y mejora la experiencia de uso.

## Coste

Al igual que [[7-versioning]], CRR conlleva un **coste adicional de almacenamiento** (se duplican los
datos en otra región) y, además, un **coste de transferencia de datos** entre regiones. Por eso no
conviene replicar todos los datos de forma indiscriminada — hay que ser selectivo.

### Qué evaluar antes de replicar

- **Importancia del dato para disaster recovery** — identificar qué datos son críticos y de los que
  depende la recuperación ante desastres.
- **Aplicaciones que requieren tiempos de respuesta rápidos** — identificar a qué datos acceden con
  frecuencia usuarios de otras regiones; solo tiene sentido replicar hacia esas regiones.
- **Requisitos específicos de disponibilidad** — por ejemplo, archivos multimedia que deben estar
  siempre accesibles se benefician de esta capa adicional.
- **Balance coste-beneficio** — con volúmenes de datos grandes, el coste crece rápido; hay que
  equilibrarlo frente al beneficio real.
- **Requisitos normativos** — en sectores como finanzas o salud, a veces la replicación entre
  regiones es obligatoria por cumplimiento (compliance), igual que ocurre con el versionado.

## Mecanismo de funcionamiento

- Se configura mediante **reglas y políticas de replicación** en el bucket de origen.
- Una vez habilitada, AWS replica automáticamente cada nuevo objeto que se añade al bucket de origen.

> ⚠️ La replicación funciona **solo en una dirección**: de origen a destino. Si se añade un objeto
> directamente en el bucket de destino, **no** se replica de vuelta al bucket de origen.

> ⚠️ Por defecto, **borrar un objeto en el bucket de origen no lo borra en el bucket de destino**.
> Esto no es un descuido — es precisamente lo que permite que CRR sirva como protección ante
> borrados accidentales, además de como disaster recovery.

- Es **obligatorio activar [[7-versioning]]** tanto en el bucket de origen como en el de destino para
  poder habilitar la replicación entre regiones.
