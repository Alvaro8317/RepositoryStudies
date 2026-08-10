# Atributos proyectados en índices secundarios

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Un [[6-secondary-indexes|índice secundario]] (LSI o GSI) se construye **proyectando atributos**: los
atributos de la tabla base se **copian** al índice para poder construir la clave secundaria y servir
las consultas directamente desde allí. Se puede elegir qué atributos proyectar — hasta un máximo de
**20 atributos por índice**.

## Las tres opciones de proyección

| Opción        | Qué copia al índice                                                 | Coste de almacenamiento | Cuándo usarla                                                                                                        |
| ------------- | ------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **ALL**       | Todos los atributos del item                                        | El más alto             | Patrón de acceso impredecible, o cuando se necesita máximo rendimiento en lectura para cualquier atributo            |
| **KEYS_ONLY** | Solo los atributos clave (partition key + sort key) del item        | El más bajo             | Solo se necesita **localizar** items rápidamente por clave, para luego consultar el item completo aparte             |
| **INCLUDE**   | Las claves + una lista específica de atributos adicionales elegidos | Intermedio              | Patrón de acceso **predecible**, con atributos concretos que se consultan con frecuencia (ej. categoría, fabricante) |

### ALL

- Copia **todos** los atributos del item al índice.
- Da el mejor rendimiento posible en lectura, ya que cualquier atributo está disponible directamente
  desde el índice sin tener que consultar la tabla base.
- Simplifica el diseño — no hace falta prever qué atributos se necesitarán.
- Coste: mayor uso de almacenamiento, al duplicar todos los atributos en el índice.

### KEYS_ONLY

- Copia únicamente los **atributos clave** del item.
- Es la opción más **económica en almacenamiento**.
- Útil cuando la aplicación solo necesita localizar rápidamente las claves de los items, para después
  recuperar el item completo por separado si hace falta.

### INCLUDE

- Copia las claves más una **lista explícita** de atributos adicionales necesarios para la aplicación.
- Buen equilibrio entre rendimiento y eficiencia de almacenamiento, cuando el patrón de acceso es
  **predecible** — se sabe de antemano qué atributos se van a consultar con frecuencia (ej. `categoria`,
  `fabricante` en el ejemplo de [[6-secondary-indexes]]).

## Siguiente paso

Para hacer seguimiento de los cambios que ocurren en una tabla (inserciones, actualizaciones,
eliminaciones), DynamoDB ofrece los **DynamoDB Streams** — se tratan en la siguiente lección.
