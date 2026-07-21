# Práctica: Ingesta con estado usando Job Bookmarks

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En esta práctica se implementa una **ingesta de datos stateful** en el ETL Job creado anteriormente,
habilitando los **Job Bookmarks** de AWS Glue. El objetivo es comprobar que, tras una primera ejecución,
solo se procesan los archivos **nuevos** en ejecuciones posteriores (carga incremental), sin volver a
cargar lo que ya se procesó.

## Habilitar Job Bookmarks

En los detalles del job (Job details) está la opción **Job bookmarks**, que especifica cómo Glue procesa
los marcadores de trabajo cuando el job se ejecuta:

- **Enable**: al activarse, Glue recuerda los datos ya procesados en ejecuciones anteriores (el estado de
  lo que se ha cargado y lo que no). Si se modifica o se añaden filas en un archivo **ya existente**,
  también se detecta y se reprocesa gracias a los bookmarks.
- **Pause**: se sigue actualizando la información de estado, pero sin aplicar la lógica de carga
  incremental en esa ejecución.
- **Disable**: la información de estado se ignora por completo.

> ⚠️ Para que los bookmarks funcionen desde el principio, hay que habilitarlos **antes** de la primera
> ejecución y volver a cargar el primer archivo desde cero. Si se activan después de haber ejecutado el
> job sin bookmarks, no habrá información de estado almacenada de esas ejecuciones previas.

## Preparar el escenario

1. **Vaciar el bucket destino**: seleccionar todos los objetos generados en ejecuciones anteriores y
   eliminarlos permanentemente (confirmando la eliminación).
2. **Vaciar la carpeta origen** (`documents`), donde había dos archivos, y dejarla vacía.
3. Guardar el job con los **Job bookmarks habilitados**. En este punto todavía no hay información de
   estado almacenada, ya que solo se genera después de la primera ejecución.

## Primera ejecución: solo el primer archivo

1. Subir únicamente el **primer archivo** a la carpeta origen en S3.
2. Ejecutar el job. Al finalizar (unos 2 minutos), Glue actualiza la información de estado, recordando
   que ese archivo ya se ha cargado.
3. Consultar el destino: deberían aparecer **11 filas**.

## Segunda ejecución: carga incremental del segundo archivo

1. Subir el **segundo archivo** a la misma carpeta origen (sin tocar el primero).
2. Volver a ejecutar el mismo job.
3. Consultar el destino con la misma query (sin `LIMIT` ni `ORDER BY`): el resultado esperado son
   **21 registros** (11 + 10 del segundo archivo), **no 32**, que sería el total si el primer archivo se
   hubiera vuelto a cargar por completo.

Al obtener exactamente 21 registros se confirma que Glue **no reprocesó el primer archivo**, sino que
únicamente cargó los datos nuevos del segundo archivo.

## Conclusión

Con los Job Bookmarks habilitados se ha implementado con éxito una **ingesta de datos con estado**: el
job de Glue recuerda qué archivos ya procesó y, en cada ejecución posterior, solo carga los datos
incrementales (nuevos o modificados), evitando reprocesar información ya cargada.
