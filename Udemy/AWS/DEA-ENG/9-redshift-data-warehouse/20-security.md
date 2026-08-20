# Redshift: seguridad

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Redshift ofrece varios mecanismos para gestionar la seguridad del data warehouse.

## Credenciales

- Los usuarios que quieren acceder a Redshift siempre deben **autenticarse**, normalmente con
  **usuario y contraseña**.

## Integración con IAM

- **IAM** está totalmente integrado con Redshift.
- Permite controlar **quién puede realizar qué acciones** sobre los recursos de Redshift (ej.
  crear o modificar un clúster).

## VPC

- Redshift **siempre se despliega dentro de una VPC**, aislando el data warehouse de la Internet
  pública.
- Se puede configurar y usar una **VPC propia y específica**.

## Cifrado del clúster

- Los clústeres pueden **cifrarse**, especialmente recomendable si los datos son sensibles.
- El cifrado se gestiona mediante **AWS Key Management Service (KMS)**, ya sea con:
  - Claves gestionadas por **AWS**, o
  - Claves **gestionadas por el cliente**.

## Grupos de seguridad del clúster

- Por defecto, un clúster de Redshift recién creado es **inaccesible para todo el mundo** — un
  estado de **confianza cero**: sin configuración explícita, no se permite ninguna conexión de
  red entrante.
- Para habilitar el acceso entrante, el clúster debe estar asociado a un **grupo de seguridad**,
  que actúa como un **firewall virtual** controlando el tráfico entrante y saliente.
- Mediante reglas en el grupo de seguridad, se puede conceder acceso desde **IPs específicas** u
  otros **recursos de AWS**.

> ⚠️ Un clúster de Redshift no es accesible por defecto — hay que asociarlo explícitamente a un
> grupo de seguridad para permitir cualquier conexión entrante.

## Cifrado en tránsito

- La conexión entre el **cliente y el clúster** se puede cifrar mediante **SSL**, garantizando
  que los datos estén protegidos en tránsito.

## Cifrado de los datos cargados (COPY)

Al subir archivos de datos a S3 para cargarlos en tablas de Redshift, se pueden cifrar de dos
formas:

- **Cifrado del lado del servidor (server-side encryption)**: S3 se encarga del descifrado.
- **Cifrado del lado del cliente (client-side encryption)**: el propio comando `COPY` de Redshift
  descifra los datos mientras carga la tabla.

## Control de acceso granular

- Redshift soporta **control de acceso a nivel de columna** y **seguridad a nivel de fila**
  (row-level security), para restringir qué datos concretos puede ver cada usuario.
