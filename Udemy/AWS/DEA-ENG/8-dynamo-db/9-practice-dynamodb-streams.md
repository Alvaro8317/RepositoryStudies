# Práctica: DynamoDB Streams con Lambda

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada demostrando en la consola cómo habilitar un [[8-dynamodb-streams|stream]] en una tabla
y conectarlo a una función Lambda para procesar los cambios en tiempo real.

## Habilitar el stream en la tabla

- En la tabla, ir a **Exports and streams** → **DynamoDB stream details**.
- Por defecto está desactivado; se activa desde ahí (**Enable**).
- Al activarlo hay que elegir una de las cuatro opciones de `StreamViewType` vistas en
  [[8-dynamodb-streams]]. En la práctica se usa **New and old images**, para tener la vista más
  detallada de cada cambio.
- Una vez activado, cualquier cambio en la tabla (crear, modificar o eliminar items) queda registrado
  en el stream, aunque **por sí solo el stream no hace nada** con esos cambios — hace falta conectarlo
  a algo que los consuma (ej. una función Lambda).

## Crear y conectar la función Lambda

Desde la pestaña **Streams** de la tabla, se añade un **trigger**:

1. **Create a new trigger** → se puede conectar una función Lambda existente o crear una nueva desde
   cero (**Author from scratch**).
2. Se crea la función con runtime **Python** y el rol de ejecución por defecto (rol Lambda básico).
3. Código inicial de prueba: simplemente imprimir el evento recibido (`print(event)`), para poder
   inspeccionar en CloudWatch Logs qué contiene exactamente el payload que llega desde el stream.
4. Al configurar el trigger se define también el **batch size**: cuántos registros del stream deben
   acumularse antes de invocar la función. Con batch size = 1, la función se invoca con cada registro
   individual tan pronto como aparece.

> ⚠️ Crear la función Lambda con el rol de ejecución básico por defecto **no es suficiente** — ese rol
> solo incluye permisos para escribir logs en CloudWatch, no para leer del stream.

## Permisos necesarios para leer el stream

Al crear el trigger, este falla inicialmente porque el rol de la función no tiene permisos sobre el
stream. Las acciones necesarias son:

- `GetRecords`
- `GetShardIterator`
- `DescribeStream`
- `ListStreams`

Para solucionarlo:

1. Ir a la función Lambda → **Configuration** → **Permissions**, y abrir el rol de ejecución asociado.
2. **Attach policies** → buscar y añadir una política de DynamoDB (ej. acceso completo a DynamoDB) para
   cubrir esas acciones.

> Adjuntar acceso completo a DynamoDB es la vía rápida para la práctica; en un entorno real conviene
> restringir la política a solo esas cuatro acciones sobre el stream/tabla concretos (principio de
> mínimo privilegio).

Con los permisos añadidos, se puede volver a crear el trigger sin errores.

## Verificar que funciona

- Al hacer un cambio en la tabla (crear un item nuevo o modificar uno existente), la función Lambda se
  invoca automáticamente.
- En **Monitor** → **View CloudWatch logs** → dentro del log stream correspondiente, aparece el
  `event` impreso, con:
  - `eventName`: el tipo de operación (ej. `MODIFY` para una actualización).
  - `NewImage`: el estado del item **después** del cambio.
  - `OldImage`: el estado del item **antes** del cambio.

> Puede haber cierto retraso entre el cambio en la tabla y su aparición en los logs de CloudWatch — no
> es instantáneo. Si tras un cambio no se ve nada reflejado, conviene esperar un momento o hacer un
> cambio adicional antes de asumir que algo falla.

Este flujo (evento impreso en el log) es solo para verificar la conexión; en un caso real, la función
Lambda haría algo útil con `NewImage`/`OldImage` — por ejemplo, sincronizar el cambio con otro sistema,
enviarlo a otro servicio o transformarlo antes de guardarlo en otro lugar.
