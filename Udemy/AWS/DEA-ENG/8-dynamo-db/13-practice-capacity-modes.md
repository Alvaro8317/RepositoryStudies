# Práctica: modos de capacidad de DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada en la consola demostrando cómo ver y cambiar el [[12-capacity-modes|modo de
capacidad]] de una tabla, y cómo configurar Auto Scaling.

## Ver el modo de capacidad de una tabla

- En el listado de tablas se puede ver directamente el modo de capacidad de cada una (ej.
  **Provisioned**).
- Dentro de una tabla, en **Additional settings**, se puede ver el detalle de cómo está configurada
  esa capacidad (unidades provisionadas, Auto Scaling, etc.).

## Cambiar el modo de capacidad

- El modo de capacidad de una tabla **siempre se puede cambiar después de creada** — no es una
  decisión fija al crear la tabla.
- Se cambia desde **Actions** → **Update settings**, en el resumen de la tabla, con **Edit** sobre la
  sección de capacidad.
- **Provisioned** — permite gestionar y optimizar costes asignando la capacidad específica por
  adelantado.
- **On-Demand** — se paga solo por lo que realmente se usa, pero a un precio bastante más alto
  (aproximadamente **el doble** que Provisioned). Conviene para demanda/carga de trabajo muy variable
  o difícil de planificar; si la carga es más estable y predecible, Provisioned sale más barato.

## Configurar Auto Scaling

Dentro de la configuración de capacidad (modo Provisioned), tanto para lectura como para escritura se
puede activar **Auto Scaling** y especificar:

- **Mínimo** y **máximo** de unidades de capacidad.
- **Target utilization** — el porcentaje de uso objetivo que Auto Scaling intentará mantener (ej. 70%).

> Existe también la opción de usar la misma configuración de capacidad de lectura para todos los
> **índices secundarios globales** de la tabla. Por defecto, esos índices tienen su propia
> configuración de capacidad dedicada; para heredar la de la tabla hace falta al menos el mismo número
> de unidades de capacidad que la tabla.

En la práctica se activa Auto Scaling solo para la **capacidad de lectura** (mínimo 1, máximo 10,
target 70%), dejando la escritura con capacidad fija provisionada.

## Verificar la actividad de Auto Scaling

- Tras guardar los cambios, en **Additional settings** se refleja que la capacidad de lectura ahora usa
  Auto Scaling, mientras que la de escritura sigue usando el valor fijo provisionado.
- En la sección de capacidad del **índice** también se pueden ver los eventos de Auto Scaling
  (**scaling activities**).
- Al no haber tráfico de lectura, Auto Scaling reduce automáticamente la capacidad hacia el **mínimo**
  configurado (en la práctica, a 1), ya que no hace falta más. Este ajuste no es instantáneo — puede
  tardar unos segundos en reflejarse tras refrescar la vista de actividad.
