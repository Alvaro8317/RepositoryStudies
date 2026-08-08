# Práctica: Crear un plan de backup en AWS Backup

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En el servicio **AWS Backup** se gestionan de forma centralizada y automatizada las copias de
seguridad. Desde el panel izquierdo se accede a las principales secciones: **dashboard** (estado de las
copias realizadas), **backup plans** y **backup vaults**.

## Backup vaults

En **Backup vaults** ya existe por defecto una bóveda (`Default`). También es posible crear una nueva
bóveda propia, eligiendo una **clave de cifrado** específica y un nombre.

## Crear un plan de backup

Se puede crear un plan desde varios sitios de la consola (dashboard, backup vaults, etc.), pero lo más
directo es ir a **Backup plans → Create backup plan**.

Opciones para definir el plan:

- **Start with a template**: usa reglas predefinidas (ej. "Daily, Weekly, Monthly, 5-year retention"),
  que luego se pueden seguir personalizando.
- **Build a new plan**: exactamente las mismas opciones, pero partiendo de cero.
- **Define with JSON**: la misma configuración expresada en JSON.

### Configurar una regla de backup (ejemplo: regla diaria)

Al elegir una plantilla con varias reglas (ej. diaria, semanal, mensual), cada regla se puede editar
por separado. Para la regla **diaria**:

- **Frequency**: diaria.
- **Backup vault**: en cuál se almacena (ej. la bóveda `Default`).
- **Backup window**: ventana horaria en la que se ejecuta el backup; se puede dejar la de por defecto o
  ajustarla a horas de baja actividad (ej. de madrugada).
- **Lifecycle**: cuándo mover el backup de almacenamiento en caliente a almacenamiento en frío, para
  ahorrar costes cuando ya es menos probable que se necesite.
- **Retention period**: tiempo total de conservación (puede ser indefinido). En el ejemplo se configuró
  en **35 días**.
- **Copy to another region**: posibilidad de copiar el backup a otra región (ej. Canadá) e incluso a
  otra **cuenta** y bóveda de destino, útil para recuperación ante desastres.

> ⚠️ Un plan de backup puede combinar **varias reglas** (ej. diaria con retención corta + mensual con
> retención más larga) para conseguir la estrategia global deseada.

Tras configurar la regla, se guarda y queda reflejada dentro del plan (en el ejemplo, nombrado
`backup-plan-test`).

## Asignar recursos al plan (resource assignment)

Una vez creado el plan, hay que definir qué recursos se van a respaldar mediante una **asignación de
recursos**:

- **IAM role**: se puede usar un rol por defecto (creado automáticamente si no existe) o uno específico
  ya configurado.
- **Resource types**: se puede incluir **todos los tipos** de recursos, o filtrar a un tipo concreto
  (ej. **S3**).
- Dentro de un tipo, se puede **incluir** un recurso específico (ej. un bucket S3 concreto) o
  **excluir** recursos concretos del filtro.
- También se puede filtrar por **tags**: por ejemplo, incluir solo los recursos cuya etiqueta
  `Department` sea igual a `Marketing`.

Se pueden crear **varias asignaciones de recursos** dentro del mismo plan.

## Resultado

El plan de backup queda compuesto por:

1. Las **reglas** (cuándo se ejecutan los backups y las normas de lifecycle/retención).
2. Las **asignaciones de recursos** (qué se respalda).

Desde el plan también se pueden consultar los **backup jobs** ejecutados.

## Limpieza

Al finalizar la práctica se eliminan los recursos creados, en este orden:

1. La **resource assignment** (escribiendo su nombre para confirmar).
2. El **backup plan** completo (`backup-plan-test`, escribiendo su nombre para confirmar).
