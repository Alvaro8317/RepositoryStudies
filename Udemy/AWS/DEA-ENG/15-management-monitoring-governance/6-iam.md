# AWS IAM (Identity and Access Management)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**IAM** se utiliza para gestionar el **acceso** y los **permisos** dentro de una cuenta de AWS.
Se apoya en cuatro conceptos fundamentales:

| Concepto | Descripción |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Usuarios** | Identidades con credenciales propias para acceder a la cuenta; se les asignan permisos (políticas). |
| **Grupos** | Agrupan usuarios para gestionar sus permisos de forma conjunta, sin tener que adjuntar políticas a cada usuario individualmente. |
| **Roles** | Tienen políticas adjuntas y pueden ser **asumidos** por identidades (usuarios, grupos) o por **servicios** de AWS (ej. una función Lambda que necesita realizar acciones). |
| **Políticas** | Documentos **JSON** que definen explícitamente qué acciones están permitidas (o denegadas). |

## Usuarios

Por defecto, un usuario recién creado **no tiene acceso a nada** — hay que concederle permisos
explícitamente para las acciones concretas que necesite. Esto sigue el **principio de mínimo
privilegio**: sin acceso por defecto, se concede solo lo necesario.

### Tipos de usuario

| Tipo | Descripción |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Root user** | El propietario de la cuenta, creado al darla de alta. Tiene acceso **sin restricciones** a todo. Pensado únicamente para la **configuración inicial** de la cuenta (no hay otros usuarios todavía) — **no debe usarse** en entornos productivos ni para el trabajo diario, por su acceso ilimitado. |
| **Usuario IAM (estándar)** | Usuario creado dentro de IAM, con sus propias credenciales. Solo puede acceder a lo que se le permita explícitamente mediante políticas adjuntas (directamente o vía grupo). |
| **Usuario federado** | Usuario externo autenticado a través de un **proveedor de identidad externo** (identity provider), en lugar de tener credenciales nativas de IAM. |

> ⚠️ El **root user** solo debe usarse para la configuración inicial de la cuenta — para el uso
> diario, siempre se deben crear usuarios IAM estándar con permisos acotados al principio de mínimo
> privilegio.

## Grupos

Los **grupos** organizan usuarios para gestionar sus permisos de forma más sencilla: las políticas
se adjuntan al grupo, y todos los usuarios que pertenecen a él **heredan** esos permisos.

- Un usuario puede pertenecer a **varios grupos** a la vez — en ese caso, hereda la **combinación**
  de las políticas de todos esos grupos.
- Ejemplo: los grupos `dev` y `test` tienen políticas propias adjuntas; un usuario que pertenece
  al grupo `dev` hereda automáticamente los permisos definidos en las políticas de ese grupo.

## Roles

Un **rol** tiene una o varias políticas adjuntas, y puede ser **asumido** por:

- **Identidades**: usuarios o grupos (ej. un rol de "ingeniero de datos" que distintas personas
  pueden asumir).
- **Servicios de AWS**: por ejemplo, una función Lambda necesita un **rol de ejecución**
  (*execution role*) que defina qué se le permite hacer. El servicio asume el rol definido al
  configurarse, y solo puede realizar las acciones que ese rol permite.

Este mecanismo se conoce como **control de acceso basado en roles** (*role-based access
control*), y es muy común en AWS.

> ⚠️ Si los permisos del rol no están correctamente configurados, el servicio que lo asume
> fallará al intentar realizar acciones no permitidas — por ejemplo, una función Lambda sin los
> permisos adecuados en su rol de ejecución no podrá acceder a los recursos que necesita.

## Políticas

Una **política** es un documento en formato **JSON** que define permisos: qué acciones están
**permitidas** o **denegadas**, sobre qué recursos, y bajo qué **condiciones**. Se adjuntan a
usuarios, grupos o roles.

### Estructura de una política (ejemplo)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:Get*", "s3:List*"],
      "Resource": "*"
    }
  ]
}
```

| Elemento | Descripción |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| **Version** | Versión del lenguaje de políticas de IAM (la más reciente es `2012-10-17`). |
| **Statement** | Una o varias declaraciones de permiso. |
| **Effect** | `Allow` o `Deny`. |
| **Action** | La(s) acción(es) afectadas — admite comodines (`*`). Ej. `s3:Get*` cubre cualquier acción que empiece por `Get` (`GetObject`, `GetBucketLocation`, etc.). |
| **Resource** | A qué recurso(s) se aplica — `*` significa "todos los recursos" (ej. todos los buckets de S3). |

### Políticas gestionadas (managed) vs. en línea (inline)

| Tipo | Descripción | Reutilizable |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------- |
| **Managed policy** | Existe como entidad **independiente**, gestionada de forma centralizada; se puede asignar a varios usuarios/grupos/roles. | Sí |
| **Inline policy** | Está **directamente vinculada** a un usuario, grupo, rol o recurso específico (ej. escrita directamente sobre un bucket). No existe de forma independiente. | No |

Dentro de las **managed policies** hay dos variantes:

| Variante | Descripción |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **AWS managed policy** | Creada y mantenida por **AWS**, pensada para casos de uso comunes (ej. acceso de lectura a S3); AWS las actualiza a medida que introduce nuevos servicios/funcionalidades. |
| **Customer managed policy** | Creada por el propio usuario/cuenta; da más flexibilidad y control para definir exactamente qué acciones, recursos y condiciones se permiten. |

### Políticas basadas en identidad vs. basadas en recursos

| Tipo | Se define en... | Descripción |
| -------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Identity-based policy** | La identidad (usuario, grupo o rol) | Define qué puede hacer esa identidad. Puede ser managed (AWS o customer) o inline. |
| **Resource-based policy** | El propio recurso (ej. un bucket S3) | Define quién puede acceder a ese recurso. Solo existe como política **inline** — se adjunta directamente al recurso; no todos los recursos la soportan (S3 sí, por ejemplo, mediante *bucket policies*). |

### Trust policy (política de confianza)

Caso especial de política basada en recursos, asociada a un **rol**: define qué entidad (cuenta,
usuario o servicio) puede **asumir** ese rol (acción `sts:AssumeRole`).

**Caso de uso típico — acceso entre cuentas (cross-account):** un recurso en la Cuenta A (ej. una
instancia EC2) necesita ser accedido por la Cuenta B.

1. En la Cuenta A se define un **rol** con permisos de acceso a esa instancia EC2.
2. Por defecto, la Cuenta B **no puede asumir** ese rol.
3. Se configura una **trust policy** en el rol que declara explícitamente a la Cuenta B como
   entidad de confianza autorizada a asumirlo.
4. La Cuenta B puede entonces asumir el rol y acceder al recurso.

> ⚠️ Alternativa: si el recurso lo soporta, también se puede lograr el mismo acceso entre cuentas
> definiendo directamente una **resource-based policy** sobre el propio recurso (ej. una bucket
> policy en S3) — pero no todos los recursos permiten este tipo de política, por lo que los
> **roles + trust policy** son la vía más general para el acceso entre cuentas.
