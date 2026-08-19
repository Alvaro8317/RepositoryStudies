# AWS Secrets Manager

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS Secrets Manager?

**AWS Secrets Manager** es el servicio diseñado para **gestionar, recuperar y almacenar secretos**.

- Un **secreto** es principalmente **datos confidenciales**, como:
  - **Credenciales de bases de datos** (ej. **RDS**, **Redshift**).
  - **Claves de API**.
  - **Tokens de acceso**.
- Los secretos se **almacenan cifrados**.
- Cuenta con **integraciones incorporadas** con otros servicios, lo que facilita el acceso a los
  secretos desde ellos.
- Permite definir **políticas de grano fino (fine-grained policies)** para controlar exactamente
  **quién puede acceder** a cada secreto.
- Soporta **rotación automática** de secretos, configurable mediante un **horario (schedule)** —
  sin necesidad de modificar el código de la aplicación.

## Recuperación segura de secretos

- Los secretos se recuperan mediante **llamadas a la API**.
- Esto evita tener que **codificar en texto plano (hardcode)** credenciales o claves dentro de la
  aplicación.

> ⚠️ Los secretos **nunca** deben quedar en texto plano dentro del código — para eso existe Secrets
> Manager.

## Integración con CloudTrail

- Secrets Manager se integra con **CloudTrail**, lo que permite registrar:
  - Todos los **accesos** a los secretos.
  - El **historial de rotación**.
- Esto aporta más detalle a las **pistas de auditoría (audit trails)**, útil para **cumplimiento
  (compliance)** y **supervisión**.

## Replicación de secretos entre regiones (cross-region)

Un secreto puede **replicarse en varias regiones**. Es útil cuando se necesita acceder al secreto
desde varias regiones, o para reducir el riesgo de tener el secreto concentrado en una única
región.

### Funcionamiento

1. El secreto existe primero en una región, donde se le llama el **secreto primario (primary
   secret)**.
2. Desde la configuración del secreto, se **habilita la replicación**.
3. Al habilitarla, se pueden **añadir regiones adicionales** donde se quiere que el secreto esté
   disponible — el secreto se **replica** en cada una de esas regiones.
4. Para el **cifrado**, es obligatorio usar una **customer managed key** (clave gestionada por el
   cliente): solo con este tipo de clave se puede modificar la **política de la clave** para
   permitir su uso también desde las regiones de destino. Esto funciona igual que la replicación de
   claves de KMS entre regiones — la clave replicada en la región destino se llama **clave de
   réplica (replica key)**.

### Promoción de una réplica a secreto independiente

- Un secreto replicado se puede **promover** a un **secreto independiente** en su región.
- A partir de ese momento, se convierte en un **nuevo secreto primario**: se puede modificar de
  forma independiente y, a su vez, replicarse de forma independiente a otras regiones.

### Qué se replica

- El **ARN se mantiene consistente** entre regiones — lo único que cambia es el indicador de
  región.
- También se replican:
  - Los **datos del secreto cifrados**.
  - Las **etiquetas (tags)**.
  - Las **políticas**.
  - La configuración de **rotación**, si está habilitada en el secreto primario.
- Cualquier **actualización** del secreto primario se **propaga automáticamente** a sus réplicas.

## Compartir secretos entre cuentas (cross-account)

A diferencia de la replicación entre regiones, compartir un secreto entre cuentas **no lo
replica**: simplemente se **concede acceso** mediante políticas, manteniendo un único secreto.

### Funcionamiento

1. Sobre el secreto (en la cuenta propietaria), se **concede acceso** a una identidad de otra
   cuenta (ej. cuenta B) adjuntando una **política de recursos (resource policy)**.
2. Además, hay que permitir que la identidad de la cuenta B pueda usar la **clave KMS** para
   **descifrar** el secreto — si no, aunque tenga acceso al secreto, no podría leerlo.
3. Por esto, también aquí es obligatorio usar una **customer managed key**: es la única que permite
   modificar su política para dar acceso a otra cuenta (una AWS managed key no se puede editar).

> ⚠️ Tanto para la **replicación entre regiones** como para **compartir entre cuentas**, Secrets
> Manager exige una **customer managed key**, porque solo ese tipo de clave permite modificar su
> política para extender el acceso (a otra región o a otra cuenta).
