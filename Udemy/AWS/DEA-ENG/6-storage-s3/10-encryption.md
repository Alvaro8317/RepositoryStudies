# Encriptación en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

Los datos en S3 pueden protegerse mediante **encriptación** en dos momentos distintos:

- **En tránsito** — mientras se desplazan hacia/desde S3.
- **En reposo** — mientras están almacenados en disco en los data centers de S3.

## Cifrado en tránsito

- Se protege usando **SSL/TLS** (Secure Socket Layer / Transport Layer Security).
- El objeto se cifra en el cliente, se transporta de forma segura hasta S3 y se descifra allí.
- Si el bucket tiene configurado cifrado del lado del servidor, S3 vuelve a cifrar el objeto en ese
  punto antes de almacenarlo.

## Cifrado en reposo

- Puede aplicarse **del lado del servidor** o **del lado del cliente**.
- **Todos los buckets tienen cifrado en reposo activado por defecto** — S3 cifra los objetos antes de
  guardarlos y los descifra al descargarlos, de forma automática.

> ⚠️ El cifrado en reposo no es opcional ni algo que haya que activar manualmente: viene configurado
> por defecto en todo bucket de S3.

### Métodos de cifrado del lado del servidor

| Método | Quién gestiona las claves | Control adicional |
| --- | --- | --- |
| **SSE-S3** (claves gestionadas por S3) | Amazon (creación, almacenamiento, rotación) | Nivel básico, sin configuración extra |
| **SSE-KMS** (claves gestionadas con AWS KMS) | El usuario, integrado con KMS | Políticas de acceso, rotación, desactivación y borrado de claves |
| **Cifrado de doble capa (DSSE-KMS)** | El usuario, dos claves KMS independientes | Dos capas de cifrado; si una capa se ve comprometida, la segunda sigue protegiendo el dato |
| **SSE-C** (claves proporcionadas por el cliente) | El usuario, en su totalidad | Máximo control; AWS nunca almacena la clave |

#### SSE-S3 — claves gestionadas por S3

- Es la configuración de cifrado **por defecto** de cada bucket.
- Cada archivo subido se cifra con una clave única; Amazon gestiona la creación, almacenamiento y
  rotación de esas claves.
- Al acceder a los datos, AWS usa automáticamente la clave adecuada para descifrarlos.
- No requiere ninguna gestión por parte del usuario.

#### SSE-KMS — claves gestionadas con AWS KMS

- En lugar de usar claves gestionadas por Amazon, se integra con **KMS** para crear y gestionar las
  propias claves de cifrado.
- Da control sobre las claves: **rotarlas, desactivarlas y borrarlas** cuando sea necesario.
- Permite definir **políticas** sobre quién puede usar cada clave y cómo se gestiona — útil para
  requisitos de cumplimiento (compliance) o auditoría.

#### Cifrado de doble capa del lado del servidor (DSSE-KMS)

- Los datos se cifran **dos veces**, cada vez con una clave KMS distinta.
- Primera capa: se aplica en cuanto los datos llegan a S3.
- Segunda capa: se aplica con una clave KMS separada de la primera.
- Garantiza que, si una de las capas se ve comprometida, la segunda sigue protegiendo el dato.
- Necesario en algunos casos que requieren un nivel de seguridad adicional.

#### SSE-C — claves proporcionadas por el cliente

- A diferencia de los métodos anteriores, aquí el usuario debe **proporcionar su propia clave** para
  cada objeto subido a S3.
- El usuario es totalmente responsable de **generar, almacenar y gestionar** las claves.
- Al subir un archivo, la clave de cifrado debe enviarse también, a través de una **conexión segura
  (HTTPS)**.
- AWS **nunca almacena** la clave, lo que reduce el riesgo de acceso no autorizado — útil en sectores
  muy regulados.

> ⚠️ Con SSE-C toda la responsabilidad recae en el usuario: asegurar las claves en tránsito y en
> reposo, rotarlas periódicamente y usar algoritmos criptográficos estándar del sector para
> generarlas. Es el método con mayor nivel de control, pero también de responsabilidad.
