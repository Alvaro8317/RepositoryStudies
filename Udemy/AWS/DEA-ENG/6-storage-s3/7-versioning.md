# Versionamiento en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Versioning** permite gestionar los cambios en los archivos guardando **múltiples versiones** del
mismo objeto, en lugar de sobrescribirlo cada vez que cambia.

- Permite **revertir a estados anteriores** en caso de borrado accidental o de modificaciones no
  deseadas.
- Forma parte de una estrategia de **recuperación ante desastres (disaster recovery)**.

## Beneficios

- **Restaurar datos a un punto concreto en el tiempo** — no solo recuperar el último estado, sino
  cualquier versión anterior guardada.
- **Garantiza integridad y consistencia** de los datos a lo largo del tiempo.
- **Requisito normativo** en sectores como finanzas o salud, donde hay que poder rastrear los cambios
  realizados sobre los datos.

## Mecanismo de funcionamiento

1. **Creación de versiones** — se crea una nueva versión cada vez que se hace un cambio sobre un
   archivo/documento.
2. **Identificación única** — cada versión queda identificada con un **número o código de versión**
   único.
3. **Versiones inmutables** — una vez creada, una versión **no se puede modificar**.

## Retos (challenges)

- **Mayor necesidad de almacenamiento**, especialmente relevante en data lakes que ya almacenan
  volúmenes de datos masivos.
- **No es un versionado incremental**: se guarda el **archivo completo** como una nueva versión (no
  solo el cambio/diferencia), lo que incrementa el coste de almacenamiento más rápido de lo que
  podría parecer a primera vista.
- **Complejidad adicional** para gestionar múltiples versiones (cuáles conservar, durante cuánto
  tiempo, etc.).

## El equilibrio (balancing act)

- Hay que encontrar el equilibrio entre los **beneficios** del versionado y el **coste de
  almacenamiento adicional** que conlleva.
- Las **políticas de ciclo de vida de los datos** ayudan a definir **periodos de retención** para las
  versiones anteriores — ver la sección siguiente y [[4-lifecycle-rules]].

## Implementación en Amazon S3

- El versionado se **activa por bucket** (Enable versioning).
- Una vez activado, S3 mantiene **múltiples versiones de un mismo objeto**, permitiendo revertir a
  versiones anteriores cuando haga falta.

> Esto conecta con lo visto en [[5-practice-lifecycle-rules]]: en un bucket **sin** versionado, una
> acción de expiración de una Lifecycle Rule **borra el objeto de forma permanente**. En un bucket
> **con** versionado, en cambio, esa misma expiración añade un **delete marker** y la versión que era
> la actual pasa a conservarse como **versión no actual (noncurrent version)** — no se pierde, solo
> deja de ser la versión "activa". Por eso las Lifecycle Rules también permiten definir acciones
> específicas para expirar/hacer la transición de esas **versiones no actuales**, que es precisamente
> el mecanismo para gestionar el periodo de retención mencionado arriba.

### Construir una estrategia

No hace falta activar el versionado para **todos** los datos — es una decisión que conviene tomar por
dataset, sopesando:

- La **criticidad** del dato (activar versionado para datasets críticos o sensibles).
- El **coste de almacenamiento adicional** que supone mantener varias versiones.
- Los **requisitos normativos** aplicables (algunos sectores lo exigen explícitamente).
