# AWS KMS (Key Management Service)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es AWS KMS?

**AWS KMS** (**Key Management Service**) es el servicio que ayuda a **crear y gestionar claves de
cifrado (encryption keys)** usadas para cifrar y descifrar datos.

- Cada vez que ciframos datos en AWS (ej. un bucket de **S3**, un volumen **EBS**, una base de
  datos), **KMS trabaja por detrás** para generar y gestionar esas claves.
- Dependiendo del **tipo de clave** utilizada, podemos ver la clave en la consola de KMS y, en
  algunos casos, gestionarla y modificar sus propiedades.
- También se puede acceder a las claves mediante **llamadas a la API**, no solo a través de la
  integración automática de otros servicios.

## Casos de uso

- **Cifrado de datos en reposo**: buckets de S3, bases de datos, volúmenes EBS.
- **Cifrado de credenciales/secretos**: en vez de guardar credenciales en texto plano (por ejemplo
  en variables de entorno o directamente en el código), se cifran con KMS y se descifran mediante
  llamadas a la API cuando se necesitan.
- **Cumplimiento (compliance)**: muchas normativas exigen que los datos estén cifrados y que el uso
  de las claves quede auditado.

> ⚠️ **CloudTrail** está integrado con KMS: todo el uso de las claves queda registrado (cuándo se
> usó, cómo se usó). Esto es clave para fines de auditoría y cumplimiento.

## Tipos de claves: simétricas vs. asimétricas

### Clave simétrica (symmetric key)

- Es el tipo de clave **por defecto** y la forma más sencilla de cifrar datos.
- Se usa **la misma clave** tanto para **cifrar** como para **descifrar**.
- Muy **eficiente** y **segura**, por lo que es adecuada para **grandes volúmenes de datos**.
- Usa el estándar **AES** con claves de **256 bits**.
- Soporta tanto **cifrado en reposo (at rest)** como **cifrado en tránsito (in transit)**.

### Clave asimétrica (asymmetric key)

- Consiste en un **par de claves**:
  - **Clave pública** (descargable): se usa para **cifrar** los datos.
  - **Clave privada**: se usa para **descifrar** los datos.
- Útil cuando se necesita **compartir datos de forma segura** con terceros, o para operaciones de
  **firma y verificación (sign/verify)**.
- Usa los estándares **RSA** y **ECC**.

## Propiedad de la clave: AWS owned, AWS managed y customer managed keys

| Tipo de clave                   | ¿Quién la crea/gestiona?                | ¿Visible en KMS? | ¿Auditable con CloudTrail? | ¿Se puede configurar (políticas, rotación, etc.)?   |
| ------------------------------- | --------------------------------------- | ---------------- | -------------------------- | --------------------------------------------------- |
| **AWS owned keys**              | AWS, compartida entre múltiples cuentas | No               | No                         | No — control total de AWS                           |
| **AWS managed keys**            | AWS, pero creada en nuestra cuenta      | Sí               | Sí                         | No — AWS controla rotación y políticas              |
| **Customer managed keys (CMK)** | El propio usuario/cliente               | Sí               | Sí                         | Sí — control total (políticas, rotación, acceso...) |

### AWS owned keys

- No se crean en nuestra cuenta: son **totalmente invisibles y gestionadas por AWS**, y se
  comparten entre **múltiples cuentas** (son propiedad del servicio, no del cliente).
- No hay acceso a la clave, ni a sus políticas, ni a su ciclo de vida.
- No es posible auditarlas con CloudTrail ni gestionarlas.
- Buena opción cuando **no** se necesita auditoría ni gestión de la clave; mala opción si hay
  requisitos de cumplimiento que exigen auditar el uso de la clave.

### AWS managed keys

- Se crean y gestionan en nombre del usuario, **dentro de la cuenta del cliente**, específicas para
  cada servicio.
- Son visibles en KMS: se pueden ver la clave y sus políticas, y se pueden **auditar** con
  CloudTrail.
- No se puede controlar la **rotación** ni el resto de políticas — eso lo sigue gestionando AWS.
- Buena opción cuando se necesita auditoría, pero no control total sobre la clave.

### Customer managed keys (CMK)

- Las crea, posee y gestiona el propio usuario.
- **Control total** sobre la clave: quién tiene acceso, las políticas, cómo y cuándo se rota, cómo
  se cifra, etc.
- Opción recomendada cuando se necesita **control completo** sobre el ciclo de vida de la clave.

## Tareas habituales en KMS

- **Crear una clave**: desde la consola, el CLI o el SDK, eligiendo si es **simétrica** o
  **asimétrica**.
- **Configurar políticas** de acceso (solo disponible con customer managed keys).
- **Rotación de claves (key rotation)**: por seguridad, para no cifrar demasiados datos durante
  demasiado tiempo con la misma clave. AWS gestiona toda la complejidad de este proceso; según el
  tipo de clave, la rotación puede ser automática o configurable por el usuario.

## Rotación de claves (key rotation)

- Es una **buena práctica de seguridad**: si una clave se ve comprometida, el impacto es menor
  cuanto menos tiempo lleve en uso (menos datos cifrados con esa misma clave).
- AWS gestiona toda la complejidad de la rotación por detrás, incluso cuando se rota manualmente.
- Según el tipo de clave:
  - **AWS managed keys**: se rotan **automáticamente**, normalmente **una vez al año**, sin
    intervención del usuario.
  - **Customer managed keys**: la rotación es **responsabilidad del usuario** — hay que
    configurarla manualmente, no ocurre por defecto.

## Políticas de acceso (key policies)

- Gestionan **quién puede acceder y usar** una clave de KMS.

| Tipo de política                      | Descripción                                                                                                                                                                                                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Política de clave por defecto**     | Se aplica automáticamente al crear una clave; da acceso completo al **usuario root** de la cuenta de AWS.                                                                                                                                                      |
| **Políticas IAM**                     | Permiten conceder acceso a más usuarios/roles; el administrador de la cuenta mantiene acceso ilimitado.                                                                                                                                                        |
| **Políticas de clave personalizadas** | Control **granular** e independiente de IAM: se define exactamente qué puede hacer cada usuario/rol con una clave específica (ej. quién puede cifrar, descifrar o rotar la clave). Útil en organizaciones con requisitos de seguridad/normativa más estrictos. |

## Precios de KMS

| Concepto                                              | Coste                                                      |
| ----------------------------------------------------- | ---------------------------------------------------------- |
| **Customer managed key**                              | $1 / mes por clave                                         |
| **AWS managed keys** / **AWS owned keys**             | Gratis                                                     |
| **Llamadas a la API**                                 | $0.03 por cada 10 000 solicitudes                          |
| **Rotación de claves**                                | Gratis (tanto para AWS managed como customer managed keys) |
| **Uso de una clave desde otra región** (cross-region) | $0.01 por cada 10 000 solicitudes                          |

> ⚠️ Una clave de KMS siempre es **específica de una región**. Usarla desde una región distinta a
> donde está almacenada tiene un coste adicional por las solicitudes entre regiones.

## Uso interregional de claves (cross-region)

Una clave de KMS se crea siempre en una **región concreta** y solo puede usarse en esa región. Esto
tiene implicaciones importantes en operaciones que cruzan regiones — por ejemplo, copiar un
**snapshot de un volumen EBS** cifrado de una región a otra:

1. **Snapshot en la región de origen**: el volumen EBS está cifrado con una clave (AWS managed o
   customer managed). Al crear el snapshot, se cifra con **esa misma clave** — no hay problema
   porque sigue en la misma región.
2. **Copia del snapshot a la región de destino**: al copiarlo, hay que elegir qué clave usar en la
   región destino (la clave por defecto de esa región o una customer managed key) — es una clave
   **completamente distinta** a la de la región de origen, sin ninguna relación con ella.
   - Durante la transferencia, los datos permanecen cifrados en todo momento: AWS **descifra** el
     snapshot con la clave de la región de origen y lo **vuelve a cifrar** con la clave de la
     región de destino, de forma automática.
3. **Creación del volumen en la región de destino**: una vez el snapshot está disponible ahí, se
   crea el nuevo volumen EBS a partir de él. El volumen queda cifrado con la clave especificada
   durante la copia — o, si no se especificó ninguna, con la clave por defecto de EBS de la región
   destino.

## Claves multi-región (multi-Region keys)

- Son un **conjunto de claves independientes** que existen en varias regiones, pero comparten el
  **mismo material de clave (key material)** y el **mismo Key ID**, por lo que se pueden usar de
  forma intercambiable — como si fueran la misma clave replicada.
- Con ellas se pueden **cifrar datos en una región y descifrarlos en otra**, sin necesidad de volver
  a cifrarlos ni hacer llamadas entre regiones.
- **No son claves globales**: cada una sigue viviendo en su propia región y hay que **gestionarla de
  forma independiente** (alias, etiquetas, políticas, grants...) en cada región.
- Funcionamiento: se crea una **clave primaria** en la primera región y luego se **replica** a una o
  varias regiones adicionales seleccionadas.

### Casos de uso de claves multi-región

- **Backup y disaster recovery**: cifrar/descifrar datos sin interrupción entre regiones, incluso si
  hay un corte en una de ellas.
- **Gestión global de datos**: empresas con datos distribuidos en múltiples regiones pueden usar la
  clave multi-región como si fuera una única clave local en cada región, sin latencia adicional.
- **Firma entre regiones**: aplicaciones con capacidades de firma (**sign/verify**) entre regiones,
  usando **claves asimétricas** multi-región.

## Uso entre cuentas (cross-account)

- A veces es necesario **compartir una clave entre distintas cuentas de AWS** — por ejemplo, backups
  cifrados o servicios compartidos gestionados de forma centralizada en una cuenta pero usados desde
  varias cuentas.
- Esto **solo es posible con customer managed keys**, ya que son las únicas cuyas **políticas de
  clave** se pueden modificar para dar acceso a otras cuentas (con una AWS managed key no se pueden
  editar las políticas).

### Ejemplo: compartir un volumen EBS cifrado entre la cuenta A y la cuenta B

1. En la **cuenta A** (origen), se cifra el volumen EBS con una **customer managed key**, cuya
   política se configura para conceder acceso de cifrado/descifrado a la **cuenta B**.
2. Se crea un **snapshot** de ese volumen cifrado en la cuenta A, y se modifican los permisos del
   snapshot para que la **cuenta B** también tenga acceso a él.
3. Desde la cuenta B, se **copia el snapshot compartido**, seleccionando durante la copia una clave
   gestionada por la propia **cuenta B** para volver a cifrarlo (mayor control y seguridad).
4. Con el snapshot ya re-cifrado, se **crea el volumen EBS** en la cuenta B a partir de él — el
   volumen usa la clave de la cuenta B.
5. Finalmente, ese volumen se puede **adjuntar a una instancia EC2** en la cuenta B.
