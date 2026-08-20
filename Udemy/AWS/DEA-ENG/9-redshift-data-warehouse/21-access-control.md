# Redshift: control de acceso (usuarios, grupos y roles)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## IAM vs. control de acceso dentro de Redshift

- **IAM** se sigue usando, pero principalmente para **autenticar** a los usuarios cuando se
  conectan a un clúster de Redshift — no sustituye al control de acceso interno de Redshift.
- Los **roles y permisos sobre objetos específicos** (tablas, esquemas de base de datos, etc.) se
  definen y gestionan **dentro de Redshift**: crear y gestionar usuarios, grupos y roles, y
  conceder privilegios, se hace con **comandos SQL**.

## Usuarios y grupos

- Un **grupo** puede contener **múltiples usuarios**.
- Un usuario puede pertenecer a **varios grupos** a la vez — en ese caso, hereda los privilegios
  de **todos** los grupos a los que pertenece.
- Flujo típico:
  1. Crear un usuario con su contraseña (esto crea el login).
  2. Crear un grupo (opcional, si no existe ya).
  3. Añadir el usuario al grupo con `ALTER GROUP ... ADD USER ...`.
  4. Conceder permisos al grupo (ej. `GRANT USAGE ON SCHEMA ...`, `GRANT SELECT ON ...`).
- Los grupos existen sobre todo por **conveniencia de gestión**: organizar permisos por grupo y
  luego simplemente añadir/quitar usuarios de esos grupos, en lugar de asignar permisos a cada
  usuario individualmente.

> ⚠️ Una limitación importante de los grupos: un grupo **no puede contener a otro grupo**. No es
> posible anidar grupos dentro de grupos.

## Roles (RBAC)

En 2022, AWS introdujo **RBAC (Role-Based Access Control)** en Redshift, que sí permite una
estructura **jerárquica**.

- Funciona de forma similar a los grupos: se define un **rol** (ej. `data_analyst`), se le
  asignan **permisos**, y luego el rol se **concede a usuarios**.
- La diferencia clave frente a los grupos: un **rol se puede conceder a otro rol**. El rol que
  recibe la concesión **hereda todos los permisos** del rol concedido — permitiendo construir una
  **jerarquía de roles**.
- Los roles concedidos a otros roles siguen pudiéndose volver a conceder a usuarios, propagando
  toda la jerarquía de permisos heredados.

> ⚠️ A diferencia de los grupos, los roles sí soportan anidamiento: un rol puede heredar los
> permisos de otro rol, y ese rol combinado se puede conceder a un usuario o a otro rol.

### Ejemplo con SQL

```sql
-- Crear un rol
CREATE ROLE finance;

-- Conceder permisos al rol
GRANT USAGE ON SCHEMA finance_schema TO ROLE finance;
GRANT SELECT ON ALL TABLES IN SCHEMA finance_schema TO ROLE finance;

-- Conceder el rol a un usuario
GRANT ROLE finance TO usuario;

-- Anidar roles: el rol "hr" hereda todos los permisos del rol "finance"
GRANT ROLE finance TO ROLE hr;
```

> ⚠️ En general, AWS recomienda usar **roles** en lugar de grupos para organizar el control de
> acceso — los grupos siguen existiendo, pero en la práctica los roles los sustituyen gracias a
> su capacidad de anidamiento jerárquico.

## Control de acceso de grano fino

Además de los permisos tradicionales (`GRANT SELECT` sobre una tabla o esquema), Redshift también
ofrece **control de acceso de grano fino** — seguridad a nivel de fila, de columna y enmascaramiento
de datos — tratado en detalle en [22-fine-grained-access-control.md](22-fine-grained-access-control.md).
