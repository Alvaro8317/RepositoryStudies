# Políticas de Bucket en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

Una **Bucket Policy** es un conjunto de reglas que define **quién puede acceder** a los objetos de un
bucket de S3 y **qué acciones** puede realizar sobre ellos.

- Se define **a nivel de recurso**, dentro del propio bucket — no son roles/políticas IAM asociados a
  un usuario o servicio.
- Se configura como un **documento JSON**.
- Se gestiona desde la pestaña **Permissions** del bucket correspondiente.

## Estructura del documento

| Campo | Descripción |
| --- | --- |
| **Version** | Versión del lenguaje de políticas de IAM utilizado. |
| **Statement** | Contiene una o más reglas individuales. |
| **Effect** | `Allow` (permite la acción) o `Deny` (la rechaza). |
| **Principal** | A quién se le permite o deniega el acceso: una cuenta de AWS, un usuario IAM o un servicio de AWS. |
| **Action** | Qué acciones están permitidas o denegadas (ej. `s3:GetObject`, que permite descargar archivos). |
| **Resource** | Sobre qué bucket/objeto(s) aplica la regla. |
| **Condition** | (Opcional) Condición que debe cumplirse para que la declaración surta efecto. |

### Ejemplo de condiciones

- Restringir el acceso a un **rango de IPs** concreto.
- Exigir que la conexión use **HTTPS**.

## Bucket Policies vs. políticas IAM

| | **Bucket Policy** | **Política IAM** |
| --- | --- | --- |
| Dónde se adjunta | Al **recurso** (el bucket) | A una **identidad** (usuario, grupo o rol) |
| Quién puede ser el Principal | Cualquier cuenta, usuario o servicio de AWS — **incluso fuera de la cuenta propietaria** del bucket, o acceso público | Solo identidades **dentro de la propia cuenta** de AWS |
| Alcance | Un único bucket (y sus objetos) | Puede cubrir múltiples servicios/recursos a la vez |
| Caso de uso típico | Acceso **cross-account**, acceso público controlado, o centralizar reglas de acceso a un bucket concreto sin tocar IAM | Gestionar permisos de un usuario/rol a través de **varios** servicios de AWS |

Las Bucket Policies **no sustituyen** a IAM en general — ambos mecanismos coexisten y **se evalúan en
conjunto** para cada solicitud. La diferencia clave es que una Bucket Policy permite conceder (o
denegar) acceso a **principals externos a la cuenta** sin necesidad de crear un usuario/rol IAM para
ellos, algo que una política IAM por sí sola no puede hacer.

### Relación con el explicit deny

Cuando IAM evalúa una solicitud, combina **todas** las políticas aplicables — políticas IAM del
usuario/rol **y** la bucket policy del recurso — bajo esta lógica:

1. Si **cualquiera** de esas políticas contiene un **`Deny` explícito** que aplica a la solicitud, el
   acceso se deniega, **sin importar** que otra política (IAM o bucket policy) tenga un `Allow`.
2. Si no hay ningún `Deny` explícito, se concede el acceso si **al menos una** política tiene un
   `Allow` que aplica.
3. Si ninguna política concede acceso explícito, el resultado por defecto es **denegar** (deny
   implícito).

> ⚠️ Esto es justo lo que hace útiles a las Bucket Policies como mecanismo de control adicional: se
> puede usar un `Deny` explícito en la bucket policy para **bloquear** una acción (ej. exigir HTTPS,
> restringir por rango de IP) **incluso si** una política IAM del usuario permitiría esa misma acción.
> El `Deny` explícito siempre gana, venga de donde venga.
