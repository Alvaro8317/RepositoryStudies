# Práctica: Ingesta basada en eventos con AWS Lambda y S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En esta práctica se implementa el caso de uso de [[1-lambda|ingesta basada en eventos]] visto en la
teoría: al subir un archivo a un bucket S3 **origen**, se dispara automáticamente una función **Lambda**
que mueve ese archivo a otro bucket S3 **destino**.

## Preparar el bucket origen

Se crea un nuevo bucket S3 que actuará como **fuente** (ej. `source-bucket-<sufijo>`), dejando el
resto de configuración por defecto. El bucket destino ya existía de una práctica anterior.

## Crear la función Lambda

En **Lambda → Create function → Author from scratch**:

- **Function name**: ej. `my-event-function`.
- **Runtime**: Python.
- **Execution role**: se crea un **rol nuevo** con los permisos básicos de Lambda (por defecto). Más
  adelante se le añaden permisos adicionales para poder escribir en otro bucket S3.

## Código de la función

Se usa un script Python sencillo (se puede generar incluso con ayuda de un LLM) que:

- Toma el **bucket y el archivo de origen** a partir de los datos del **evento** que dispara la
  función (no hace falta codificarlo a mano: vendrá del trigger S3 configurado más adelante).
- Copia/mueve el archivo al **bucket de destino**, cuyo nombre sí se indica de forma explícita en el
  código.

> Opcionalmente, si el rol de ejecución tiene los permisos necesarios, también se podría eliminar el
> archivo original tras copiarlo, o aplicar procesamiento adicional sobre los datos. En esta práctica se
> mantiene simple: solo se mueve el archivo.

## Añadir permisos al rol de ejecución

1. En **Configuration → Permissions** de la función, abrir el **rol** de ejecución (se abre en IAM en
   una pestaña nueva).
2. **Attach policies** → añadir una política de S3 (por simplicidad, en este entorno de práctica se usa
   **AmazonS3FullAccess**).

> ⚠️ En un entorno productivo conviene usar permisos más granulares (acceso restringido a
> buckets/prefijos concretos) en lugar de acceso completo a S3.

## Configurar el trigger (S3 event notification)

En la función Lambda, **Add trigger**:

- **Source**: S3.
- **Bucket**: el bucket **origen** creado al principio.
- **Event type**: se deja el valor por defecto, **All object create events** (también se podría
  limitar solo a `PUT`, u otros tipos de evento disponibles).
- Opcionalmente se puede añadir un **prefix** (por ejemplo, para limitarlo a una subcarpeta concreta) o
  un **suffix** (por ejemplo, para limitarlo a archivos `.csv`). En esta práctica se dejan ambos vacíos.
- Confirmar el aviso y **Add** el trigger.

El trigger queda visible tanto en **Configuration → Triggers** como en el diagrama general de la
función.

## Desplegar y probar

1. **Deploy** la función para activar el código.
2. Subir manualmente un archivo al **bucket origen** (drag & drop).
3. Tras uno o dos minutos, comprobar:
   - En **Monitor**, que aparece una nueva **invocación** de la función (duración, error count, etc.).
   - En el **bucket destino**, que el archivo ha llegado.

En la prueba realizada, la invocación tardó **menos de un segundo** y el archivo apareció en el bucket
destino en menos de un minuto, con **0 errores** y **1 invocación exitosa**.

## Conclusión

Con este flujo se ha configurado una función Lambda disparada por una **notificación de evento S3**
(`All object create events`), demostrando de forma práctica una **ingesta basada en eventos**: cualquier
archivo nuevo subido al bucket origen se mueve automáticamente al bucket destino sin intervención
manual adicional.
