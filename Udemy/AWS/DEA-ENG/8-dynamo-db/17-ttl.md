# TTL (Time to Live)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**TTL** (*Time to Live*) es una función que se puede activar en una tabla de DynamoDB para eliminar
automáticamente elementos una vez que alcanzan cierta antigüedad — útil para gestionar el ciclo de
vida de los datos y controlar el coste de almacenamiento sin borrar elementos manualmente.

## Cómo funciona

- Se activa TTL sobre un atributo de la tabla que contiene el **tiempo de expiración** de cada
  elemento.
- Ese atributo debe expresarse en formato **Unix epoch**: número de segundos transcurridos desde las
  00:00:00 UTC del 1 de enero de 1970.
- Cuando la marca de tiempo del elemento indica que ya ha pasado el tiempo de expiración, DynamoDB lo
  pone en cola automáticamente para su eliminación.

> ⚠️ Un elemento marcado como expirado **no se elimina de inmediato**: DynamoDB dispone de hasta
> **48 horas** desde la expiración para completar el borrado. Este margen hay que tenerlo en cuenta
> si se depende de que el borrado sea instantáneo.

## Coste

- El proceso de borrado por TTL **no consume capacidad de escritura provisionada** de la tabla — no
  se cobran WCU por esas eliminaciones.
- Esto lo convierte en un mecanismo de limpieza de datos obsoletos bastante rentable comparado con
  borrados manuales.

## Actualizaciones sobre elementos en cola de borrado

- Un elemento ya puesto en cola para eliminación por TTL **sigue pudiendo actualizarse** antes de que
  se borre definitivamente.
- Por ejemplo, se puede eliminar el atributo TTL de ese elemento para evitar que se borre — sigue
  siendo un elemento actualizable con normalidad hasta el momento del borrado real.

## Integración con DynamoDB Streams

Cuando el proceso de TTL elimina un elemento, esa eliminación también puede capturarse en
[[8-dynamodb-streams|DynamoDB Streams]] si están activados en la tabla:

- Aparece en el stream como una operación de tipo **eliminación** (`REMOVE`).
- Puede identificarse específicamente como un **borrado por TTL**, distinguiéndolo de una eliminación
  manual.
- Esto permite que procesos posteriores (por ejemplo, funciones **Lambda** consumiendo el stream)
  reaccionen a esas eliminaciones — por ejemplo, para archivar los datos en un almacenamiento más
  barato antes de perderlos definitivamente.
