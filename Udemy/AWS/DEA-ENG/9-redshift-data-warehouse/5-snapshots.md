# Amazon Redshift Snapshots

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es una snapshot?

Una **snapshot** es una **copia de seguridad puntual (point-in-time backup)** de un cluster.

- Redshift almacena las snapshots internamente en **buckets de S3**.
- Se utiliza una **conexión cifrada (SSL)** para ello.

Las snapshots se pueden tomar de dos formas: **automáticas** o **manuales**.

## Snapshots automatizadas

- Están **activadas por defecto** al crear un cluster.
- Redshift toma automáticamente una **snapshot incremental**, que registra los cambios respecto a
  la última snapshot automatizada.
- Se toman según lo que ocurra **primero** de estos dos criterios:
  - Cada **8 horas**.
  - Cada **5 GB por nodo** de cambios de datos.
- Existe un **tiempo mínimo de 15 minutos** entre snapshots automatizadas, incluso si el umbral de
  5 GB/nodo se alcanza antes.
- **Periodo de retención**: **1 día** por defecto, configurable.

## Snapshots manuales

- Se pueden tomar en **cualquier momento**, manualmente.
- Por defecto se **conservan indefinidamente**.
- El periodo de retención se puede **modificar** editando la propia snapshot.

## Compartir datos entre regiones y cuentas

Redshift permite **compartir datos directamente entre clusters**, sin necesidad de copiarlos
manualmente:

- No hace falta descargar los datos a un bucket de S3 y copiarlos a un nuevo cluster, ni hacer una
  copia de snapshot entre regiones.
- El **data sharing** se puede hacer:
  - Entre clusters de la **misma cuenta de AWS**.
  - Entre clusters de **distintas cuentas de AWS**.
  - Incluso cuando el cluster está en una **región diferente**.

> ⚠️ El **data sharing** entre clusters es la alternativa recomendada frente a copiar snapshots
> manualmente entre regiones/cuentas — es más directo y no requiere pasos intermedios por S3.

## Resumen: snapshots automáticas vs. manuales

| Característica | Automáticas | Manuales |
| ------------------------ | ------------------------------------------ | ------------------------------------ |
| **Activación** | Por defecto, al crear el cluster | Bajo demanda, en cualquier momento |
| **Tipo** | Incremental | — |
| **Frecuencia** | Cada 8h o cada 5 GB/nodo (lo que ocurra primero, mín. 15 min entre snapshots) | Manual |
| **Retención por defecto** | 1 día (configurable) | Indefinida (configurable) |
