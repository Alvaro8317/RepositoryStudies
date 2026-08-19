# Práctica: AWS Secrets Manager

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Objetivo

Explorar la consola de **Secrets Manager** y ver cómo se configura el almacenamiento de un nuevo
secreto, sin necesidad de guardarlo realmente.

> ⚠️ Secrets Manager tiene un **periodo de prueba gratuito**, pero después su coste es de
> **$0.40 por secreto al mes**. Si sigues la práctica y guardas un secreto de verdad, recuerda
> **borrarlo** después para evitar cargos.

## Pasos

1. Buscar **Secrets Manager** en la barra de búsqueda de la consola de AWS.
2. Elegir **Store a new secret** (almacenar un nuevo secreto).

### Tipos de secreto

En la pantalla de creación se ven los tipos de secreto disponibles, incluyendo las
**integraciones incorporadas** ya mencionadas en la teoría:

- **RDS**
- **DocumentDB**
- **Redshift** (data warehouse)

Al elegir uno de estos tipos:

- Solo hay que indicar un **nombre de usuario** y una **contraseña**.
- Se puede **seleccionar la base de datos** directamente desde una lista (si ya existen bases de
  datos creadas en la cuenta).
- El secreto queda **integrado directamente con esa base de datos**, lo que permite configurar la
  **rotación** de forma sencilla: todo el proceso de rotación queda gestionado por la integración,
  sin necesidad de lidiar con esa complejidad manualmente. El secreto se recupera fácilmente y no
  hace falta actualizar nada a mano.
- Para el cifrado se puede usar la **AWS managed key** (por defecto) o una **clave propia**
  (customer managed key).

### Secreto genérico (par clave-valor)

También es posible almacenar credenciales para otras bases de datos, o **cualquier tipo de
secreto** de forma más genérica, usando **pares clave-valor**:

- Ejemplo:
  - Clave `username` → valor `admin123`
  - Clave `password` → valor (una contraseña compleja)
- Igual que antes, se puede cifrar con la **AWS managed key** (por defecto) o con una clave propia.

### Configuración adicional del secreto

Tras definir los datos del secreto, se configuran:

- **Nombre del secreto** (ej. `prod-test-secret`) y **descripción**.
- **Etiquetas (tags)**.
- **Política de recursos (resource policy)**: aquí es donde se define en formato **JSON** el
  acceso desde **otras cuentas de AWS**, tal como se explicó en la teoría sobre secretos
  compartidos entre cuentas.
- **Réplicas de lectura (read replicas)**: se puede elegir una o varias **regiones adicionales**
  donde replicar el secreto, igual que se explicó en la teoría de replicación entre regiones.

### Configurar la rotación

En el siguiente paso se puede configurar la **rotación automática**:

- Se puede definir mediante una **expresión** (schedule expression) o con el **constructor visual**
  (elegir el intervalo en días, horas, etc.).
- La rotación requiere una **función Lambda**:
  - Si se usa uno de los tipos de secreto **preconfigurados** (RDS, DocumentDB, Redshift), la
    integración ya sabe cómo rotar el secreto.
  - Si se usa un secreto **genérico** (como el de par clave-valor de este ejemplo), hay que
    **elegir o crear la función Lambda** con la lógica de rotación uno mismo, ya que Secrets
    Manager no sabe automáticamente cómo rotarlo.

### Revisión final

- El último paso muestra un **resumen** de la configuración del secreto.
- También se incluye **código de ejemplo** en varios lenguajes de programación, mostrando cómo
  **recuperar el secreto** desde una aplicación.

> ⚠️ En esta práctica no se llegó a guardar el secreto — el objetivo era únicamente mostrar el
> flujo de configuración en la consola.
