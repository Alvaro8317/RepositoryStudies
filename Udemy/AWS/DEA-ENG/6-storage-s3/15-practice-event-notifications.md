# Práctica: Notificaciones de Eventos en S3 con SNS

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: configurar un bucket para que, al subir un archivo, se envíe una notificación de
evento a un **topic de SNS**, que a su vez envía un email a través de una suscripción. Ver la teoría en
[[14-event-notifications]].

## Objetivo

1. Subir un archivo a un bucket de S3.
2. Que esto dispare una **notificación de evento** hacia un **topic de SNS**.
3. Que el topic de SNS, mediante una **suscripción por email**, notifique al usuario.

## Paso 1 — Crear el bucket

- Se crea un bucket nuevo (ej. `prueba-de-notificaciones-de-eventos-...`), dejando el resto de la
  configuración por defecto.
- En **Properties** del bucket se copia el **ARN** — se necesita más adelante para la política de
  acceso del topic SNS.

## Paso 2 — Crear el topic de SNS

- En la consola de **SNS**, crear un topic de tipo **Standard**.
- Por defecto, un topic **no permite** que ningún origen externo (como un bucket de S3) le envíe
  notificaciones — hay que configurar explícitamente una **política de acceso (access policy)** que lo
  permita.
- En la sección **Advanced** de la política de acceso, se define una policy que concede permiso a S3
  para publicar en el topic, especificando:
  - **`SourceArn`** → el ARN del bucket de S3.
  - **`SourceAccount`** → el ID de la cuenta de AWS propietaria del bucket.

> ⚠️ Si al guardar la configuración de notificaciones en S3 aparece el error **"Unable to validate the
> following destination configurations"**, revisar la access policy del topic SNS: probablemente falta
> el campo **`Resource`** (el ARN del propio topic SNS) en la policy — sin él, SNS no reconoce que la
> policy aplica a ese topic.

## Paso 3 — Suscribirse al topic

- Crear una **suscripción (subscription)** sobre el topic, con protocolo **Email** y la dirección de
  correo deseada.
- AWS envía un email de confirmación — hay que **confirmar la suscripción** desde ese correo antes de
  que empiecen a llegar notificaciones.

## Paso 4 — Configurar la notificación de evento en el bucket

- En el bucket, ir a **Properties → Event notifications** y crear una nueva notificación.
- Tipo de evento: **`s3:ObjectCreated:*`** (todos los métodos de creación de objetos — put, post, etc.,
  sin distinguir cuál se usó). No se aplica filtro de prefijo/sufijo en este ejemplo.
- Destino: **SNS topic** → seleccionar el topic creado en el paso 2.

> Alternativa mencionada pero no usada en esta práctica: en vez de enviar directamente a un topic SNS
> o cola SQS, el bucket también permite enrutar las notificaciones a **Amazon EventBridge**, útil
> para configuraciones más complejas (múltiples reglas/destinos).

## Paso 5 — Probar

- Subir un archivo cualquiera al bucket (ej. un JSON).
- Casi de inmediato debería llegar un email a la dirección suscrita, confirmando que S3 → SNS →
  Email funcionó correctamente.

## Resumen del flujo

`Subida de archivo a S3` → `Notificación de evento (ObjectCreated:*)` → `Topic SNS` →
`Suscripción por email` → `Email recibido`
