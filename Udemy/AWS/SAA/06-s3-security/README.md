# Seguridad en S3

## 🔐 Seguridad en S3: Cifrado

Amazon S3 ofrece múltiples opciones para proteger los datos **en reposo** y **en tránsito**. El cifrado protege los datos frente a accesos no autorizados si se compromete el almacenamiento físico o las credenciales de acceso.

---

### 🧊 Cifrado en reposo (Server-Side Encryption - SSE)

Este cifrado ocurre **después** de que S3 recibe los datos y **antes** de almacenarlos en disco.

---

### 1. 🔐 **SSE-S3** (Server-Side Encryption con claves de Amazon S3)

- 🔑 **Claves gestionadas por Amazon S3**
- 🔒 Utiliza **AES-256**
- ✅ Amazon se encarga del ciclo de vida de las claves
- 📌 Cabecera HTTP requerida:

  ```plaintext
  x-amz-server-side-encryption: AES256
  ```

**Ventajas:**

- Simple de usar
- Sin costos adicionales

---

### 2. 🔐 **SSE-KMS** (Server-Side Encryption con AWS KMS)

- 🔑 **Claves gestionadas por el servicio AWS Key Management Service (KMS)**
- 🧾 Requiere políticas de permisos KMS + IAM
- 📋 Registra auditoría de accesos en **AWS CloudTrail**
- 📌 Cabecera HTTP requerida:

  ```plaintext
  x-amz-server-side-encryption: aws:kms
  ```

**Ventajas:**

- Auditoría de accesos (CloudTrail)
- Control de permisos más granular

**Limitantes:**

- Cada operación de subida → `GenerateDataKey`
- Cada descarga → `Decrypt`
- 👉 Estas operaciones cuentan para la **cuota de KMS por segundo** (ej. 1000 req/s por defecto en `us-east-1`)

---

### 3. 🔐 **SSE-C** (Server-Side Encryption con claves proporcionadas por el cliente)

- 🗝️ Tú proporcionas la clave directamente
- 🛑 **S3 no almacena la clave**, ni siquiera temporalmente
- 📌 La clave debe ser enviada en cada petición usando HTTPS
- 🔄 S3 cifra y descifra en el servidor usando tu clave

**Cabeceras típicas:**

```http
x-amz-server-side-encryption-customer-algorithm: AES256
x-amz-server-side-encryption-customer-key: <Base64-encoded-key>
x-amz-server-side-encryption-customer-key-MD5: <Base64-encoded-MD5>
```

**Requisitos:**

- ✅ HTTPS es obligatorio
- 🚫 No se puede usar con SDKs o herramientas que no soporten SSE-C directamente

---

### 4. 🧠 **Cifrado del lado del cliente (Client-Side Encryption)**

- 🔐 El cliente **cifra los datos antes** de enviarlos a S3
- 🔑 El cliente gestiona el almacenamiento de claves
- 🔁 El cliente también debe descifrar al recuperar los datos

**Ejemplos de uso:**

- SDKs de AWS con soporte para Client-Side Encryption
- Integraciones con herramientas como `aws-encryption-sdk`, `Cryptography SDK`, `KMS`

**Ventajas:**

- Máximo las claves
- Protección incluso antes de llegar a AWS

**Desventajas:**

- Mayor complejidad
- Mayor responsabilidad del cliente

---

### 🌐 Cifrado en tránsito

| Tema                  | Detalles                                                |
| --------------------- | ------------------------------------------------------- |
| Protocolo recomendado | **HTTPS (TLS)**                                         |
| S3 soporta            | HTTP y HTTPS                                            |
| SSE-C requiere        | **Obligatoriamente HTTPS**                              |
| Cliente usa           | TLS 1.2 o superior recomendado                          |
| ¿Qué protege?         | La comunicación cliente ↔️ S3 (previene sniffing, MITM) |

---

## 🔄 Comparativa rápida de tipos de cifrado

| Tipo            | Claves  | Gestión                 | Auditable (CloudTrail) | HTTPS requerido |
| --------------- | ------- | ----------------------- | ---------------------- | --------------- |
| **SSE-S3**      | Amazon  | Totalmente gestionado   | ❌                     | Opcional        |
| **SSE-KMS**     | KMS     | Parcialmente gestionado | ✅                     | Recomendado     |
| **SSE-C**       | Cliente | Cliente                 | ❌                     | ✅ Obligatorio  |
| **Client-side** | Cliente | Cliente                 | ❌                     | ✅              |

---

## 🧠 Casos de uso

| Caso                              | Cifrado recomendado    |
| --------------------------------- | ---------------------- |
| Sencillo y seguro                 | SSE-S3                 |
| Cumplimiento y auditoría          | SSE-KMS                |
| Requisitos externos de clave      | SSE-C                  |
| Encriptación total por el cliente | Client-side encryption |

## 🌐 CORS (Cross-Origin Resource Sharing) en Amazon S3

\| ¿Qué es? | Política JSON en el bucket que indica a los navegadores qué orígenes externos (`Origin`) pueden pedir recursos S3 mediante **XHR / fetch / <img> / video**, qué métodos se permiten y qué cabeceras se exponen. |
\| Casos de uso típicos | • SPA o sitio React alojado en **CloudFront/S3** que consume imágenes desde otro bucket. • Aplicación móvil que carga audio en un dominio distinto al de la API. • Web pública que permite descargas de objetos alojados en un bucket privado. |
\| Ejemplo mínimo | `json { "CORSRules":[{ "AllowedOrigins":["https://www.ejemplo.com"], "AllowedMethods":["GET"], "MaxAgeSeconds":3000 }]} ` |
\| Buenas prácticas | 1️⃣ Mantén la lista de **AllowedOrigins** lo más corta posible. 2️⃣ Limita **AllowedMethods** a lo necesario (`GET`, `PUT`, etc.). 3️⃣ Activa **HTTPS** para evitar mixed-content. |

---

## 📑 S3 **Server Access Logs**

\| Qué registran | Cada solicitud (_REST, SDK, CLI, pre-signed URLs_) con IP, hora, usuario/role, latencia, bytes transferidos, error code, user-agent. |
\| Activación | En “Properties → Server access logging” del bucket origen, indicas **bucket destino** (debe estar **en la misma región**). |
\| Precaución del “bucket loop” | **No** guardes los logs en el mismo bucket que registras: si activas logging en `my-data` y apuntas a `my-data` → cada log genera otra entrada → crecimiento exponencial. Usa un bucket dedicado (`my-data-logs`) o al menos otro prefijo. |
\| Análisis posterior | Athena, S3 Select, Redshift Spectrum, herramientas SIEM. |
\| Seguridad | Otorga al bucket origen permiso `WRITE` y `READ_AC el bucket destino con un bucket policy mínima. |

---

## 🔑 Pre-signed URLs (URL pre-firmadas)

\| Qué son | URLs temporales que incluyen la firma de AWS SigV4. Permiten **GET, PUT, DELETE** (u operaciones resumidas POST) a objetos sin exponer credenciales. |
\| Quién firma | Un **usuario IAM, rol (por ej. Lambda) o federated identity** con permisos en el objeto. |
\| Permisos heredados | El receptor **hereda exactamente** las acciones permitidas al firmante. Si el firmante solo tenía `s3:GetObject`, la URL solo funcionará para descarga (`GET`). |
\| Expiración | De segundos a 7 días (SDK v2) o a 12 h con SigV4-presign‐URL en CLI. Tras vencer → 403 Forbidden. |
\| Casos de uso | • Descargar vídeo premium / factura PDF.• Permitir carga directa a una carpeta precisa (signed PUT) desde un navegador o móvil, evitando pasar por el backend.• Compartir documento grande a un partner sin dar accesos permanentes. |
\| Ejemplo (CLI) | `aws s3 presign s3://my-bucket/video.mov --expires-in 600` → URL válida 10 min. |
\| Seguridad extra | • Usar HTTPS al transmitir la URL.• Generar con duración mínima necesaria.• Si es PUT, valida later que el objeto cumple tamaño/MIME. |

---

### 📋 Resumen rápido

| Función            | Punto clave                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| **CORS**           | Controla qué orígenes web pueden llamar a tu bucket desde el navegador. |
| **Access Logs**    | Guarda cada acceso para auditoría; usa bucket destino distinto.         |
| **Pre-signed URL** | Firma temporal que delega permisos GET/PUT; expira automáticamente.     |
