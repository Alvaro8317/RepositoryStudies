# Lifecycle Rules de S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son?

Las **Lifecycle Rules** permiten aplicar un conjunto de reglas sobre los objetos de un bucket S3 para
**automatizar** acciones en función de la antigüedad de los datos.

Esto conecta directamente con las distintas [[3-storage-classes|clases de almacenamiento]]: al
principio del ciclo de vida de un dato se suele necesitar acceso frecuente (ej. S3 Standard), pero con
el tiempo el patrón de acceso cambia y conviene moverlo a una clase más rentable — las Lifecycle Rules
son el mecanismo para automatizar esa transición, en vez de moverlo manualmente.

## Tipos de acción

Una Lifecycle Rule define una de estas dos acciones sobre los objetos:

### Transición (transition)

Mueve los objetos a una **clase de almacenamiento distinta** después de un tiempo determinado.

- Ejemplo: transicionar los objetos a una clase más barata después de **30 días**.
- Se puede configurar de distintas formas, definiendo cuándo debe producirse cada transición concreta
  en función de la antigüedad de los datos (por ejemplo, encadenando varias transiciones: Standard →
  Standard-IA → Glacier, cada una a partir de un número de días distinto).

### Expiración (expiration)

Marca los objetos para su **eliminación** una vez alcanzada cierta antigüedad. Los objetos caducados
son borrados automáticamente por AWS en nombre del usuario, sin intervención manual.
