# Route 53

---

## 🌍 ¿Qué es DNS?

**DNS (Domain Name System)** es el sistema que traduce **nombres de dominio legibles para humanos** (como `ejemplo.com`) en **direcciones IP** (como `192.0.2.1` o `2001:db8::1`) que entienden las computadoras.

> 🔁 DNS actúa como la "guía telefónica" de Internet.

---

## 🔄 Flujo básico de resolución DNS

1. Tu navegador pide `https://www.ejemplo.com`.
2. Consulta al **resolver DNS** (normalmente del proveedor de Internet o de Cloudflare, Google, etc.).
3. El resolver busca en **caché**.
4. Si no está en caché, sigue una **búsqueda recursiva**:

   - Pregunta a los **root servers** → dan los **TLD servers**.
   - Pregunta a los **servidores del TLD** (como `.com`) → dan el **servidor de nombres** del dominio (`ejemplo.com`).
   - Finalmente pregunta al **servidor autoritativo**, que responde con la IP.

---

## 🧱 Estructura jerárquica del DNS

```
.         ← raíz (root)
└── com             ← TLD (Top-Level Domain)
    └── ejemplo     ← SLD (Second-Level Domain)
        └── www     ← subdominio
```

> El dominio completo sería: `www.ejemplo.com.` (la raíz está implícita)

---

## 🧠 Terminología clave

### 📌 **Nombre de dominio completo (FQDN)**

- Ejemplo: `https://api.blog.ejemplo.com`
- Componentes:

  - **Protocolo:** `https://`
  - **Subdominio:** `api.blog`
  - **SLD (Second-Level Domain):** `ejemplo`
  - **TLD (Top-Level Domain):** `.com`

---

### 🌐 **Registrador de dominios (Domain Registrar)**

Empresa autorizada para **vender y registrar nombres de dominio**.

#### Ejemplos de registradores:

| Registrador                                   | Características                                                |
| --------------------------------------------- | -------------------------------------------------------------- |
| **Namecheap**                                 | Barato, interfaz sencilla                                      |
| **GoDaddy**                                   | Popular, pero a veces más caro                                 |
| **Google Domains** (ya migrado a Squarespace) | Integración con G Suite                                        |
| **Cloudflare Registrar**                      | Ofrece dominios **a precio de costo** (muy barato, sin margen) |
| **AWS Route 53**                              | Más caro, pero integrado con AWS y automatización              |

---

### 📄 **Registros DNS (DNS Records)**

Indican cómo debe manejarse el dominio o subdominio.

| Tipo      | Uso                                               |
| --------- | ------------------------------------------------- |
| **A**     | Apunta a una dirección IPv4                       |
| **AAAA**  | Apunta a una dirección IPv6                       |
| **CNAME** | Alias de otro dominio                             |
| **MX**    | Registros para correos electrónicos               |
| **TXT**   | Texto arbitrario (DKIM, verificación, etc.)       |
| **NS**    | Indica qué servidores de nombre son autoritativos |
| **SOA**   | Información sobre la zona DNS (TTL, contacto)     |

---

### 📁 **Archivo de zona (Zone file)**

Es un archivo plano que contiene **todos los registros DNS** de un dominio. Es mantenido por el **servidor de nombres autoritativo**.

---

### 🖥️ **Servidor de nombres (Name Server)**

- Es el **servidor que responde consultas DNS** para un dominio específico.
- **Autoritativo**: responde con datos verificados.
- Se define en los registros `NS`.

---

### 🧩 **Subdominio**

Es una parte extendida del dominio principal.

- Dominio: `ejemplo.com`
- Subdominio: `blog.ejemplo.com`, `api.ejemplo.com`

---

### 🧪 Ejemplo completo

**Nombre de dominio completo con protocolo:**

```
https://dashboard.api.ejemplo.org
```

- Protocolo: `https`
- Subdominios: `dashboard.api`
- SLD: `ejemplo`
- TLD: `org`

---

## 🧠 Tips para el examen (y la vida real)

- ❓ _¿Cuál es la función del DNS?_
  ✅ Convertir nombres de dominio en direcciones IP.

- ❓ _¿Cuál es el nombre de dominio en `https://app.misitio.com`?_
  ✅ `misitio.com` (SLD + TLD), `app` es subdominio.

- ❓ _¿Qué es un TLD?_
  ✅ `.com`, `.org`, `.io`, etc.

- ❓ _¿Qué registro se usa para apuntar un dominio a una IP?_
  ✅ `A` o `AAAA`.

---

## 🧠 ¿Qué es **Amazon Route 53**?

---

### 🌐 Servicio de DNS de AWS

**Amazon Route 53** es un servicio de **DNS escalable, altamente disponible, totalmente gestionado y autoritativo**, diseñado para:

| Capacidad                   | Descripción                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------ |
| 🌍 Alta disponibilidad      | Diseñado para ser resiliente a fallos regionales, con múltiples ubicaciones globales |
| ⚖️ Escalabilidad automática | Soporta desde proyectos personales hasta empresas globales                           |
| ⚙️ Totalmente gestionado    | AWS opera los servidores DNS por ti                                                  |
| 🛡️ Autoritativo             | Responde con autoridad por los nombres de dominio que administra                     |

---

## 🔄 ¿Qué puedes hacer con Route 53?

| Función                             | Detalle                                               |
| ----------------------------------- | ----------------------------------------------------- |
| 📦 Registrar dominios               | Comprar dominios directamente desde AWS               |
| 🌐 Gestionar registros DNS          | A, AAAA, MX, TXT, CNAME, NS, etc.                     |
| ⚖️ Balanceo de carga DNS            | Con políticas de enrutamiento avanzadas               |
| ✅ Verificar estado de endpoints    | Health checks para DNS inteligente                    |
| 🌍 Soporte a múltiples regiones     | Puedes enrutar tráfico por latencia o geolocalización |
| 🔐 Integración con IAM y CloudTrail | Para control de acceso y auditoría                    |

---

## 🧾 Registro de dominios

Route 53 te permite **registrar y renovar dominios** para cientos de TLDs como `.com`, `.org`, `.io`, etc.

### 🧠 Nota:

- **No es el registrador más barato**, pero ofrece **automatización e integración perfecta** con otros servicios de AWS.
- Puedes importar dominios registrados en otros servicios.

---

## 🧱 Tipos de registros DNS que puedes gestionar

| Tipo         | Uso                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------- |
| **A / AAAA** | IP (IPv4 / IPv6)                                                                               |
| **CNAME**    | Alias de otro dominio                                                                          |
| **MX**       | Servidores de correo                                                                           |
| **TXT**      | Verificaciones, SPF, DKIM, etc.                                                                |
| **NS**       | Servidores de nombres para delegación                                                          |
| **Alias**    | Similar a CNAME pero soporta recursos de AWS (como ELB, S3) y **no rompe el apex/root domain** |

---

## 🔀 Políticas de enrutamiento (routing policies)

Route 53 puede tomar decisiones inteligentes sobre a qué IP enrutar al cliente:

| Tipo                  | Descripción                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| **Simple**            | Una sola respuesta (registro A/CNAME fijo)                                  |
| **Weighted**          | Balanceo por peso, ej. 70%-30% entre dos endpoints                          |
| **Latency-based**     | Redirige al endpoint más rápido según latencia regional                     |
| **Failover**          | Redirige a una copia secundaria si el primario falla                        |
| **Geolocation**       | Enruta según la ubicación del usuario (por país o continente)               |
| **Geoproximity**      | Similar a geolocation pero con más control (requiere Route 53 Traffic Flow) |
| **Multivalue answer** | Devuelve múltiples registros con salud evaluada                             |

---

## 🛠️ Administración

Puedes administrar Route 53 desde:

- La **Consola AWS**
- La **CLI**
- APIs o SDKs
- Herramientas como **Terraform**, **CloudFormation**, **CDK**

---

## 💵 **Costos de Amazon Route 53** (a 2025, aproximados)

| Concepto                             | Costo                                                   |
| ------------------------------------ | ------------------------------------------------------- |
| Registro de dominio                  | \~\$12 USD/año para `.com`, varía por TLD               |
| Hosted Zone (zona hospedada pública) | **\$0.50 USD/mes** por zona                             |
| Consultas DNS                        | \~\$0.40 por millón de consultas (primeros 1B)          |
| Health checks                        | \~\$0.50/mes por check (sin alarmas)                    |
| Enrutamiento avanzado (Traffic Flow) | Costos adicionales si usas geoproximity y visual editor |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué tipo de servicio DNS es Route 53?_
  ✅ **Autoritativo y gestionado**

- ❓ _¿Puedes usar IAM para restringir acceso a modificar zonas DNS?_
  ✅ Sí, con políticas IAM

- ❓ _¿Qué registro DNS permite enrutar a un ELB sin usar CNAME?_
  ✅ **Alias**

- ❓ _¿Cómo logras failover automático si un sitio cae?_
  ✅ Usando **routing policy de failover** con **health checks**

- ❓ _¿Route 53 resuelve nombres de dominio internos dentro de una VPC?_
  ✅ Solo si usas **zonas hospedadas privadas**

## ✅ 1. **Health Check en Route 53**

---

### 🧠 ¿Qué es?

Un **health check** en Route 53 permite monitorear la **salud de un recurso** (como una instancia EC2, un Load Balancer o una app en otro proveedor) y **redireccionar el tráfico** automáticamente si el recurso falla.

---

### 🩺 ¿Qué puede monitorear?

- Endpoints HTTP o HTTPS (`http://miapp.com/health`)
- TCP (verifica que un puerto esté abierto)
- Integración con **CloudWatch Alarm** (basado en métricas personalizadas)
- Comprobaciones **recursivas**: puedes verificar la salud de otro health check

---

### 🔄 ¿Cómo se usa?

Se asocia a un **registro DNS**, y Route 53 lo usa para:

| Acción                 | Resultado                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| ✅ El recurso responde | El registro se mantiene activo                                                                           |
| ❌ El recurso falla    | Route 53 **redirecciona el tráfico** a otro registro sano (si configuraste failover o multivalue answer) |

---

### 🧾 Parámetros clave

| Parámetro          | Descripción                                                                             |
| ------------------ | --------------------------------------------------------------------------------------- |
| Intervalo          | Cada 30 o 10 segundos                                                                   |
| Umbral de fallos   | Cuántas veces debe fallar para marcarlo como "no saludable"                             |
| Tiempo de espera   | Cuánto esperar antes de marcar como fallido                                             |
| Monitoreo regional | Health check se ejecuta desde **varias regiones globales** para evitar falsos positivos |

---

## 📈 2. **SLA de disponibilidad de Route 53**

---

### 📊 Garantía de disponibilidad

- **SLA: 100% de disponibilidad para el servicio de resolución DNS**
- Amazon se compromete a una disponibilidad **sin interrupciones** del servicio de DNS para dominios correctamente configurados.

### 💰 Créditos por SLA

Si AWS falla en cumplir el SLA, puedes solicitar **Service Credits**, pero debes reportarlo tú (no se da automáticamente).

---

## 📦 3. **Registros DNS en Route 53 y enrutamiento del tráfico**

---

### 🎯 ¿Cómo decides a dónde dirigir el tráfico de un dominio?

Usas los **registros DNS en una zona hospedada** para decirle a Route 53 qué responder cuando alguien consulta por `www.tudominio.com`.

---

### 🧱 Registros comunes

| Tipo    | Función                                                                          | Ejemplo                        |
| ------- | -------------------------------------------------------------------------------- | ------------------------------ |
| `A`     | Apunta a una IPv4                                                                | `A www → 192.0.2.10`           |
| `AAAA`  | Apunta a una IPv6                                                                | `AAAA www → 2001:db8::1`       |
| `CNAME` | Alias de otro nombre DNS                                                         | `CNAME www → app.ejemplo.com`  |
| `Alias` | Como un CNAME, pero para recursos de AWS (ELB, S3, CloudFront) y en root domains | `Alias www → ELB`              |
| `MX`    | Mail Exchange (email)                                                            | `MX @ → mail.tudominio.com`    |
| `TXT`   | Verificación, SPF, DKIM                                                          | `TXT @ → "v=spf1 include:..."` |

---

### 🧭 ¿Cómo se dirige el tráfico?

Route 53 usa **Routing Policies** según tus necesidades:

| Tipo de routing       | ¿Qué hace?                                           | Cuándo usarlo                           |
| --------------------- | ---------------------------------------------------- | --------------------------------------- |
| **Simple**            | Devuelve una sola respuesta                          | Casos básicos, un solo recurso          |
| **Weighted**          | Divide el tráfico en porcentajes                     | Pruebas A/B, despliegues graduales      |
| **Latency-based**     | Redirige al recurso con menor latencia               | Mejor experiencia global                |
| **Failover**          | Redirige al recurso de respaldo si el primario falla | Alta disponibilidad                     |
| **Geolocation**       | Según ubicación del cliente                          | Contenido localizado                    |
| **Multivalue answer** | Devuelve múltiples IPs y excluye las fallidas        | Simple balanceo con tolerancia a fallos |

---

### 🧪 Ejemplo: Alta disponibilidad con health check

1. Tienes dos instancias en diferentes regiones:

   - `A` en Virginia (`primary`)
   - `A` en Oregón (`secondary`)

2. Configuras **failover routing**:

   - El registro de Virginia tiene un **health check activo**
   - Si falla, Route 53 redirige al segundo A record en Oregón

3. Resultado: el tráfico se mantiene operativo sin intervención manual

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Route 53 garantiza el 100% de disponibilidad para el servicio de resolución DNS?_
  ✅ Sí (según su SLA)

- ❓ _¿Cómo hacer failover automático si tu app cae?_
  ✅ Routing policy de **failover** + **health check**

- ❓ _¿Qué tipo de registro usas para apuntar a un ELB en el root domain (`ejemplo.com`)?_
  ✅ **Alias record**

- ❓ _¿Puedes verificar la salud de un endpoint externo a AWS?_
  ✅ Sí, con un health check HTTP o TCP

## 📦 **¿Qué es una zona de alojamiento (Hosted Zone) en Route 53?**

Una **zona de alojamiento** es el contenedor en Route 53 donde se **almacenan los registros DNS de un dominio** (como `ejemplo.com`).
Es equivalente a un **archivo de zona** en un servidor DNS tradicional.

> 📌 Cada hosted zone representa **una autoridad sobre un dominio o subdominio**.

---

## 🔸 Tipos de zonas de alojamiento en Route 53

| Tipo                              | Descripción                                                               | ¿Visible desde Internet? |
| --------------------------------- | ------------------------------------------------------------------------- | ------------------------ |
| **Pública (Public Hosted Zone)**  | Maneja registros DNS que deben ser **resueltos públicamente en Internet** | ✅ Sí                    |
| **Privada (Private Hosted Zone)** | Maneja nombres DNS **solo accesibles desde una VPC de AWS**               | ❌ No                    |

---

### ✅ 1. **Zona pública**

- Se usa para dominios registrados en la web (como `midominio.com`).
- Route 53 responde solicitudes DNS públicas por ti.
- Puedes configurar registros como `A`, `CNAME`, `MX`, `TXT`, `Alias`, etc.

#### Ejemplo:

```plaintext
Dominio: ejemplo.com
Zona hospedada pública:
- A → www.ejemplo.com → 192.0.2.123
- MX → mail.ejemplo.com
```

---

### 🔐 2. **Zona privada**

- Asociada a una o más **VPCs**.
- Sirve para manejar **nombres internos** como `db.interno.local` o `api.app.local`.
- Route 53 solo responde si la consulta viene **desde recursos dentro de esas VPCs**.

#### Ejemplo:

```plaintext
Dominio: app.local
Zona hospedada privada:
- A → db.app.local → 10.0.0.25
```

---

## 🧾 ¿Cómo se crea una zona hospedada?

Puedes crearla desde:

- La consola de AWS
- CLI:

```bash
aws route53 create-hosted-zone \
  --name ejemplo.com \
  --caller-reference $(date +%s) \
  --hosted-zone-config Comment="Mi zona pública"
```

---

## 🧩 Relación con dominios

- Si registras un dominio con Route 53, se crea automáticamente una **zona pública**.
- Si registras el dominio con otro proveedor, puedes:

  - Crear la zona en Route 53
  - Apuntar los **servidores de nombres (NS)** en el registrador externo hacia los de AWS

---

## 📄 ¿Qué contiene una zona de alojamiento?

1. **Registros DNS** como `A`, `CNAME`, `MX`, `TXT`, `Alias`, etc.
2. **Registro SOA** (Start of Authority)
3. **Registros NS** (Name Server), necesarios para que el dominio apunte a Route 53

---

## 💵 Costos aproximados (2025)

| Recurso          | Costo mensual                                               |
| ---------------- | ----------------------------------------------------------- |
| **Zona pública** | \$0.50 USD/mes por zona                                     |
| **Zona privada** | \$0.50 USD/mes por zona + \$0.50 por VPC adicional asociada |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué tipo de zona hospedada debes usar para manejar nombres accesibles solo desde dentro de una VPC?_
  ✅ **Zona privada**

- ❓ _¿Qué contiene una zona hospedada?_
  ✅ Registros DNS como A, CNAME, MX, NS, SOA

- ❓ _¿Puedo tener una zona privada y pública para el mismo dominio?_
  ✅ Sí (split-horizon DNS), pero debes tener cuidado con los registros duplicados.

- ❓ _¿Puedo usar Route 53 para dominios registrados en otro proveedor?_
  ✅ Sí, apuntando los servidores NS a los de Route 53

## 🕓 ¿Qué es TTL en Route 53?

---

### ✅ **TTL** (Time To Live)

Es el **tiempo en segundos** que un registro DNS puede ser **almacenado en caché** por resolvers DNS, navegadores y sistemas operativos antes de volver a consultar a Route 53.

> 🎯 En Route 53, puedes establecer el TTL **en la mayoría de los registros DNS**, como `A`, `CNAME`, `MX`, `TXT`, etc.

---

## 🔄 ¿Qué pasa con TTL?

- **TTL alto** → Menos consultas a Route 53 → Más rendimiento, menos costo
- **TTL bajo** → Más control sobre cambios → Más tráfico DNS, más costo

---

## 📈 Ejemplo práctico

```plaintext
TTL = 86400  → 24 horas
TTL = 60     → 1 minuto
```

- Si cambias la IP de un registro A y su TTL es 24h, los usuarios podrían seguir yendo a la IP antigua durante **hasta 24h**.
- Si el TTL es 60, **el cambio se propaga en 1 minuto**.

---

## 📌 ¿Cuándo usar TTL **alto**?

| Cuándo                                             | Por qué                           |
| -------------------------------------------------- | --------------------------------- |
| Sitio web o API **estable y poco cambiante**       | Reduces la carga de consultas DNS |
| Aplicaciones con **poco tráfico global**           | Reduces costos en Route 53        |
| Registros que rara vez se actualizan (ej. MX, SPF) | La caché es tu aliada             |

🧠 Beneficio: Menos tráfico, menos facturación por consultas DNS

⚠️ Riesgo: Si haces un cambio inesperado (por error o migración urgente), puede tardar **horas en propagarse**.

---

## ⚠️ ¿Cuándo usar TTL **bajo**?

| Cuándo                                                                     | Por qué                                                |
| -------------------------------------------------------------------------- | ------------------------------------------------------ |
| Vas a cambiar la IP de un servidor (ej. migración)                         | El cambio se propaga más rápido                        |
| Balanceo entre entornos (ej. Blue/Green deployment)                        | Rediriges tráfico fácilmente                           |
| Tienes tráfico alto con cambios dinámicos                                  | Necesitas **agilidad y control**                       |
| Estás usando **routing policies avanzadas** (latencia, failover, weighted) | La resolución depende de salud y decisiones frecuentes |

🧠 Beneficio: Flexibilidad total

⚠️ Riesgo: Más tráfico de consultas → puede incrementar tu factura en Route 53

---

## ❗ **Excepción: Registros Alias**

En Route 53, los **Alias records** (para ELB, S3 static sites, CloudFront, etc.) **no requieren TTL explícito**.
AWS lo gestiona internamente y optimiza el TTL de forma automática.

| Atributo                      | Alias Record | Registro A normal |
| ----------------------------- | ------------ | ----------------- |
| TTL configurable              | ❌ No        | ✅ Sí             |
| Usa recursos AWS directamente | ✅ Sí        | ❌ No             |

---

## 📋 Resumen

| TTL alto (ej. 3600 o más)     | TTL bajo (ej. 60–300)                      |
| ----------------------------- | ------------------------------------------ |
| Estático y predecible         | Dinámico y cambiante                       |
| Menor costo                   | Mayor control                              |
| Cambios lentos                | Cambios rápidos                            |
| Riesgo de registros obsoletos | Más tráfico DNS                            |
| Ideal para producción estable | Ideal para entornos de prueba, migraciones |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué pasa si cambias un registro con TTL alto?_
  ❗ El cambio puede tardar en reflejarse debido al **cacheo**.

- ❓ _¿Qué registros no requieren TTL en Route 53?_
  ✅ Los **Alias records**

- ❓ _¿Cuándo debes usar TTL bajo?_
  ✅ Cuando necesitas **flexibilidad y cambios rápidos**

- ❓ _¿Cuándo debes usar TTL alto?_
  ✅ Cuando el dominio es **estable y quieres minimizar tráfico DNS y costos**

## 🧩 ¿Qué es un registro CNAME?

---

### ✅ **CNAME** (Canonical Name)

Un registro CNAME **asocia un nombre de dominio con otro nombre de dominio**, en lugar de apuntar a una IP.

> 📌 _Es un "alias" a otro nombre DNS, no a una IP._

---

### 🧪 Ejemplo:

```plaintext
www.ejemplo.com → CNAME → ejemplo.net
```

Cuando alguien accede a `www.ejemplo.com`, su navegador resuelve primero `ejemplo.net`, y luego ese nombre es resuelto a su IP real.

---

### ⚠️ Restricción importante:

> ❌ **NO se puede usar CNAME en el apex/root domain**, como `ejemplo.com`
> Solo se permite en subdominios (`www.ejemplo.com`, `api.ejemplo.com`, etc.)

---

## 🧩 ¿Qué es un registro ALIAS?

---

### ✅ **ALIAS** (Route 53-specific feature)

Un registro **propietario de Route 53** que funciona como CNAME, pero con **diferencias clave**:

| ALIAS puede apuntar a...                              |
| ----------------------------------------------------- |
| Recursos de AWS (ELB, CloudFront, S3, API Gateway) ✅ |
| Apex domain (`ejemplo.com`) ✅                        |
| Otro nombre DNS ✅                                    |

---

### 🧪 Ejemplo:

```plaintext
ejemplo.com → ALIAS → d123.cloudfront.net
```

---

### 💡 Beneficios clave del ALIAS:

| Característica                                    | CNAME | ALIAS                     |
| ------------------------------------------------- | ----- | ------------------------- |
| Apunta a nombre DNS                               | ✅    | ✅                        |
| Apunta a IP directamente                          | ❌    | ❌                        |
| Puede usarse en apex domain (`ejemplo.com`)       | ❌    | ✅                        |
| Integra con recursos de AWS (ELB, S3, CloudFront) | ❌    | ✅                        |
| TTL configurable                                  | ✅    | ❌ (lo gestiona AWS)      |
| Visible en consultas DNS estándar (`dig`)         | ✅    | ❌ (parece un registro A) |

---

## 🧠 Cuándo usar cada uno

| Situación                                                                    | Usa...    | Por qué                         |
| ---------------------------------------------------------------------------- | --------- | ------------------------------- |
| Tienes un subdominio (`www.ejemplo.com`) y apuntas a otro dominio            | **CNAME** | Simple alias entre nombres      |
| Quieres apuntar el **apex domain** (`ejemplo.com`) a un **ELB o CloudFront** | **ALIAS** | No puedes usar CNAME en el root |
| Quieres integrar con **recursos de AWS** directamente (sin IP fija)          | **ALIAS** | AWS gestiona las IPs            |
| Necesitas TTL controlable                                                    | **CNAME** | Puedes ajustarlo libremente     |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Puedes usar CNAME en `ejemplo.com`?_
  ❌ **No**, solo subdominios

- ❓ _¿Qué registro usarías para apuntar `ejemplo.com` a un ELB sin usar IP?_
  ✅ **ALIAS**

- ❓ _¿Cuál se ve como un A record en el resultado de `dig` o `nslookup`?_
  ✅ **ALIAS**

- ❓ _¿Cuál puedes usar fuera de AWS?_
  ✅ **CNAME** (ALIAS es exclusivo de Route 53)

---

## 🧪 Ejemplo visual

```plaintext
ejemplo.com        → ALIAS → my-loadbalancer-123.elb.amazonaws.com
www.ejemplo.com    → CNAME → ejemplo.com
api.ejemplo.com    → CNAME → api.myapp.io
```

## 🚦 ¿Qué es el “enrutamiento” en DNS?

---

### ❗ **DNS NO enruta tráfico** (como lo haría un router o balanceador de carga)

El **DNS solo resuelve nombres** a direcciones IP.
**No transporta paquetes ni enruta datos**.

---

## 🧠 Entonces, ¿qué es una “política de enrutamiento” en Route 53?

---

En Amazon Route 53, una **política de enrutamiento** determina **cómo responde Route 53 a una consulta DNS**.
Por ejemplo: ¿cuál IP devuelve Route 53 cuando alguien consulta `www.ejemplo.com`?

---

## 🎯 Objetivo: **Controlar dinámicamente la respuesta DNS**

---

Ahora vamos con la **primera y más simple política:**

---

## 🔵 1. Política de enrutamiento **Simple** (Simple Routing Policy)

---

### ✅ ¿Qué hace?

- Devuelve **una o varias respuestas fijas** cuando se consulta un dominio.
- Es la política por defecto.
- Si configuras **varios valores** (ej. varias IPs), Route 53 **devuelve todas**, y **el cliente (navegador, SO, resolver)** elige **una al azar** para usarla.

---

### 🧪 Ejemplo 1: una sola IP

```plaintext
www.ejemplo.com → A → 192.0.2.10
```

Cuando un usuario consulta `www.ejemplo.com`, Route 53 siempre devuelve `192.0.2.10`.

---

### 🧪 Ejemplo 2: múltiples valores

```plaintext
www.ejemplo.com → A → 192.0.2.10
www.ejemplo.com → A → 192.0.2.11
```

Route 53 devuelve ambas IPs, el **cliente selecciona una aleatoriamente**.

> 🧠 No hay balanceo activo de parte de Route 53. El cliente decide.

---

### 🚫 Limitaciones

- No admite **routing inteligente** (como latencia o geografía).
- No permite **health checks** si usas **Alias record**.

  - Si usas un **registro A normal**, puedes asociarlo a un health check.
  - Pero si es un **Alias**, **no puedes asociar health check** en esta política.

---

### 📌 Alias en política simple

Cuando usas un **Alias** en esta política:

```plaintext
ejemplo.com → Alias → my-elb.amazonaws.com
```

Route 53 simplemente **resuelve la IP del recurso AWS** (como ELB), pero no puedes asociarle health check.

Esto es porque el ELB ya tiene su propio mecanismo interno de salud.

---

## 📋 Resumen de la política simple

| Característica      | Valor                                    |
| ------------------- | ---------------------------------------- |
| Balanceo de carga   | ❌ No                                    |
| Health check        | ✅ Solo con registros A/CNAME (no Alias) |
| TTL configurable    | ✅ Sí                                    |
| Varias IPs posibles | ✅ Sí, cliente elige                     |
| Alias compatible    | ✅ Sí, pero sin health check             |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué política de enrutamiento usarías si solo necesitas apuntar un dominio a una IP fija?_
  ✅ Simple

- ❓ _¿El DNS enruta tráfico?_
  ❌ No. Solo resuelve nombres a direcciones IP

- ❓ _¿Qué pasa si se usan varios registros A en una política simple?_
  ✅ Route 53 devuelve todos y el **cliente escoge uno**

- ❓ _¿Puedo usar health checks con registros Alias en política simple?_
  ❌ No

## ⚖️ ¿Qué es la política ponderada en Route 53?

---

La **Weighted Routing Policy** permite a Route 53 **controlar qué porcentaje del tráfico DNS** (consultas DNS) debe dirigirse a **cada uno de varios recursos** asociados al mismo dominio.

> 📌 Esto **no es balanceo de carga como en un ELB**, sino **balanceo a nivel de resolución DNS**.

---

## 🧠 ¿Qué controla realmente Route 53?

- Route 53 **no enruta paquetes**, solo responde con direcciones IP.
- En esta política, **Route 53 controla con qué probabilidad** entrega cada respuesta.

---

## 🎯 Requisitos para usar esta política

- Todos los **registros DNS** deben:

  - Tener el **mismo nombre** (ej. `www.ejemplo.com`)
  - Tener el **mismo tipo** (`A`, `CNAME`, etc.)

---

## 🔢 ¿Cómo funciona el peso?

- A cada registro se le asigna un **peso (número entero positivo o 0)**.
- Route 53 calcula la **proporción relativa** con base en los pesos.

---

### 🧪 Ejemplo: balanceo 70/30

```plaintext
www.ejemplo.com
→ A → 192.0.2.10  (peso: 70)
→ A → 192.0.2.20  (peso: 30)
```

- Route 53 devolverá `192.0.2.10` en aprox. el **70% de las consultas DNS**
- Y `192.0.2.20` en el **30% restante**

> 📌 ¡Esto ocurre **a nivel DNS**, antes de que el cliente se conecte!

---

## 🔄 ¿Qué pasa si le asignas peso 0 a un registro?

- El registro **sigue existiendo**, pero **Route 53 nunca lo devolverá** **a menos que todos los demás estén inactivos** por fallos de salud.
- Útil para mantener configuraciones listas pero **fuera de rotación**.

---

### 🧠 Nota: Puedes asociar **Health Checks** a registros en esta política

- Si un recurso falla, **Route 53 lo deja de devolver**, incluso si tenía peso alto.
- Se comporta similar a un "failover automático".

---

## 🔁 Diferencia con un ELB

| Característica         | Route 53 ponderado                              | ELB                                                 |
| ---------------------- | ----------------------------------------------- | --------------------------------------------------- |
| Balanceo de tráfico    | A nivel de **resolución DNS**                   | A nivel de **conexiones y paquetes**                |
| Conocimiento de estado | Sólo a través de **health checks DNS**          | Verifica estado de instancias en tiempo real        |
| Persistencia de sesión | ❌ No                                           | ✅ Soporta sticky sessions                          |
| Uso recomendado        | Balanceo entre regiones, blue/green deployments | Balanceo dentro de una región, entre instancias EC2 |
| Control porcentual     | ✅ Basado en **respuestas DNS**                 | ❌ No configurable directamente así                 |

---

## 🧠 Casos de uso comunes

| Caso                      | Descripción                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| **Blue/Green Deployment** | Dirige 90% del tráfico a producción y 10% a nueva versión         |
| **Migración gradual**     | Mueve tráfico progresivamente de un recurso a otro                |
| **Test A/B**              | Comparar rendimiento de dos versiones                             |
| **Backups configurables** | Mantener una IP con peso 0 lista para usarse solo si otras fallan |

---

## 📋 Resumen de la política ponderada

| Atributo                                | Valor                                                 |
| --------------------------------------- | ----------------------------------------------------- |
| Controla % del tráfico                  | ✅ Sí, a nivel DNS                                    |
| Health checks permitidos                | ✅ Sí                                                 |
| Registros deben tener mismo nombre/tipo | ✅ Sí                                                 |
| TTL configurable                        | ✅ Sí                                                 |
| Soporta Alias                           | ✅ Sí (pero sin health check)                         |
| Peso 0                                  | Registro se ignora a menos que todos los demás fallen |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Puedes hacer una migración gradual entre dos recursos con Route 53?_
  ✅ Sí, con **Weighted Routing**

- ❓ _¿Qué pasa si asignas peso 0 a un registro?_
  ✅ Se excluye de respuestas salvo que **todos los demás estén inactivos**

- ❓ _¿Route 53 realiza balanceo de carga como un ELB?_
  ❌ No. Solo **responde consultas DNS**, no enruta tráfico de red

- ❓ _¿Puedes usar health checks con política ponderada?_
  ✅ Sí, excepto si es un **Alias record**

---

## ⚡ Política de enrutamiento por **latencia** (Latency-based routing)

---

### 🧠 ¿Qué hace?

La política de **latencia** permite que Route 53 responda a las consultas DNS con la **IP del recurso que ofrece la menor latencia al usuario**, basada en:

- 🌍 **Región de AWS** donde vive el recurso (por ejemplo, us-east-1, eu-west-1, etc.)
- 📍 **Ubicación del usuario** que hace la solicitud

> 📌 No mide latencia en tiempo real. Se basa en un **mapa global de latencias mantenido por AWS**.

---

## 🧪 Ejemplo

Tienes una app desplegada en dos regiones:

```plaintext
api.ejemplo.com
→ A → EC2 en us-east-1 (nombre: US-East, latencia: 20 ms)
→ A → EC2 en eu-west-1 (nombre: EU-West, latencia: 90 ms)
```

- Un usuario de **Colombia** recibe la IP de `us-east-1`.
- Un usuario de **España** recibe la IP de `eu-west-1`.

---

## 🎯 ¿Cuándo usar esta política?

| Caso                                                               | ¿Por qué usarla?                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------- |
| Aplicaciones sensibles al tiempo (ej. gaming, finanzas, streaming) | Para reducir **lag** o latencia                         |
| Infraestructura replicada en múltiples regiones                    | Para dirigir usuarios al recurso **más cercano** en red |
| Experiencia de usuario global                                      | Cada usuario accede al punto de menor latencia          |

---

## ❤️‍🩹 Integración con **health checks**

Puedes asociar **health checks** a cada recurso:

- Si un recurso está inactivo, Route 53 lo elimina de las posibles respuestas.
- Así puedes tener **conmutación por error (failover) implícito**.

---

## 🔁 ¿En qué se diferencia de un CDN (como CloudFront)?

| Aspecto                 | Latency-based routing                     | CloudFront (CDN)                           |
| ----------------------- | ----------------------------------------- | ------------------------------------------ |
| Nivel                   | DNS (resolución)                          | Red de distribución (HTTP, TLS, caché)     |
| Decide en base a        | Latencia entre usuario y región AWS       | Latencia al **edge location** más cercano  |
| Usa servidores de caché | ❌ No                                     | ✅ Sí                                      |
| Ideal para              | APIs, microservicios, backends replicados | Contenido estático, multimedia, assets     |
| Reducción de latencia   | ✅ Por elegir IP más cercana              | ✅ Por traer contenido desde caché cercana |
| Protección DDoS         | ❌ No directamente                        | ✅ Sí (por medio de WAF + caché)           |

> 📌 ¡Pueden complementarse!
> Usas **latency-based routing** para dirigir a la **región** correcta y **CloudFront** para servir desde un **edge cercano**.

---

## 📋 Requisitos clave

| Requisito            | Detalle                                              |
| -------------------- | ---------------------------------------------------- |
| Nombre y tipo        | Los registros deben tener el **mismo nombre y tipo** |
| Región AWS           | Debes especificar la **región AWS** del recurso      |
| Health checks        | ✅ Se pueden usar (excepto con Alias)                |
| TTL                  | ✅ Puedes configurarlo                               |
| Usabilidad con Alias | ✅ Sí, pero sin health checks                        |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Cuándo usarías enrutamiento basado en latencia?_
  ✅ Cuando quieres **dirigir usuarios al recurso más cercano** en términos de latencia

- ❓ _¿Route 53 mide la latencia en tiempo real?_
  ❌ No. Usa un **mapa de latencias geográficas mantenido por AWS**

- ❓ _¿Puedes usar health checks con esta política?_
  ✅ Sí (excepto si es un **Alias record**)

- ❓ _¿Latency-based routing reemplaza a CloudFront?_
  ❌ No. **CloudFront es un CDN** que sirve contenido estático desde ubicaciones cacheadas

---

## 🎯 Resumen

| Característica                                | Valor                                                              |
| --------------------------------------------- | ------------------------------------------------------------------ |
| Basado en latencia entre usuario y región AWS | ✅                                                                 |
| Requiere múltiples regiones                   | ✅                                                                 |
| Se puede combinar con health checks           | ✅                                                                 |
| TTL configurable                              | ✅                                                                 |
| Alias compatible (sin health check)           | ✅                                                                 |
| Mide latencia en tiempo real                  | ❌ No                                                              |
| Nivel de decisión                             | DNS                                                                |
| Diferencia con ELB                            | ELB balancea dentro de una región, esto lo hace **entre regiones** |

## ❤️‍🩹 ¿Qué son los **controles de salud (health checks)** en Route 53?

Los **health checks** permiten que Route 53 **verifique automáticamente si un recurso está disponible**.
Se utilizan para tomar decisiones **dinámicas de enrutamiento DNS**, como enrutamiento por latencia, failover o ponderado.

---

## 🎯 ¿Por qué se aplican solo a recursos **públicos**?

- Route 53 **es un servicio DNS público**.
- Sus **health checkers** (servidores distribuidos globalmente) **deben poder alcanzar el recurso directamente por Internet**.
- Por eso, solo puedes hacer health checks a:

  - IPs públicas
  - Endpoints accesibles por Internet (ej: `www.miapi.com`)
  - Ciertos recursos de AWS públicos (ELB, EC2 con IP pública)

> ⚠️ Si necesitas monitorear algo **privado en una VPC**, puedes usar **CloudWatch** + una Lambda o alarmas internas, pero no los health checks nativos de Route 53.

---

## 🔁 Relación con conmutación por error (Failover DNS)

- Los **health checks** son el mecanismo que permite a Route 53 **activar el failover automático**.
- Si el recurso **primario** falla, Route 53 puede **responder con el recurso secundario**.

> 🧠 Esto es especialmente útil con la **política de enrutamiento Failover**.

---

## 🧪 ¿Qué pueden comprobar?

Route 53 puede comprobar la salud de:

| Tipo                  | Ejemplo                                                        |
| --------------------- | -------------------------------------------------------------- |
| Aplicaciones web      | `https://api.misitio.com/health`                               |
| Servidores            | IP pública con puerto TCP                                      |
| Otros recursos de AWS | Como una **instancia EC2 con IP pública** o un **ELB público** |

---

## 🔁 Controles de salud que controlan **otros controles de salud**

- Puedes crear **health checks dependientes**: un health check principal que se basa en el estado de **otros health checks**.

> Ejemplo: Considerar “saludable” un sitio **solo si al menos 2 de 3 endpoints** están saludables.

---

## 📊 Integración con CloudWatch

- Cada health check puede generar **métricas personalizadas en CloudWatch**:

  - `HealthCheckStatus = 1` → saludable
  - `HealthCheckStatus = 0` → no saludable

- Puedes crear **alarmas** en base a esas métricas para activar notificaciones o acciones automáticas.

---

## ⏱️ Intervalo de verificación configurable

Puedes configurar cada control para que se ejecute cada:

| Intervalo | Valor                         |
| --------- | ----------------------------- |
| Corto     | **10 segundos**               |
| Largo     | **30 segundos** (menos costo) |

Y también puedes configurar:

- **Número de fallos consecutivos** antes de marcar como "unhealthy"
- **Número de éxitos consecutivos** para volver a "healthy"

---

## 🌐 Protocolos soportados

Route 53 soporta los siguientes protocolos para comprobar la salud:

| Protocolo | Uso                                                               |
| --------- | ----------------------------------------------------------------- |
| **HTTP**  | Verifica respuestas desde endpoints HTTP (`/health`, por ejemplo) |
| **HTTPS** | Igual que HTTP, pero usando TLS                                   |
| **TCP**   | Verifica que el puerto esté abierto y acepte conexiones           |

> ⚠️ En TCP no se hace solicitud HTTP, solo se establece conexión.

---

## 📦 Configuración avanzada – **Bytes mínimos**

- Puedes configurar el health check para que **la respuesta contenga al menos 5120 bytes** (5 KB).
- Esto es útil cuando:

  - Quieres verificar que una página **realmente cargó el contenido**
  - O que la aplicación está devolviendo más que solo un código 200 vacío

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Los health checks de Route 53 pueden monitorear recursos privados dentro de una VPC?_
  ❌ No. Solo **recursos accesibles públicamente**

- ❓ _¿Puedes usar health checks para activar failover automático en DNS?_
  ✅ Sí

- ❓ _¿Puedes monitorear múltiples endpoints con un solo control de salud?_
  ✅ Sí, usando **health checks que supervisan otros**

- ❓ _¿Se puede usar TCP en controles de salud?_
  ✅ Sí

- ❓ _¿Puedes generar métricas de health checks en CloudWatch?_
  ✅ Sí

---

## 📋 Resumen general

| Atributo                                               | Valor               |
| ------------------------------------------------------ | ------------------- |
| Aplican solo a recursos públicos                       | ✅                  |
| Integran con políticas de enrutamiento                 | ✅                  |
| Activan failover automático                            | ✅                  |
| Protocolos soportados                                  | HTTP, HTTPS, TCP    |
| Intervalo configurable                                 | 10s o 30s           |
| Verificación mínima de bytes                           | ✅ Hasta 5120 bytes |
| Health check dependiente de otros                      | ✅                  |
| Genera métricas en CloudWatch                          | ✅                  |
| No disponible para registros Alias en muchas políticas | ⚠️                  |

## ✅ ¿Qué es un **control de salud calculado** en Route 53?

---

Un **calculated health check** permite **combinar los resultados de varios controles de salud (health checks)** en **uno solo**, usando **operadores lógicos** como:

- `AND`
- `OR`
- `NOT`

> 🧠 Es útil para tener una **visión consolidada** de la salud de varios recursos.

---

### 🔁 ¿Cómo funciona?

Creas un **chequeo de salud lógico** (calculado) que **no verifica directamente** un endpoint, sino que **depende del estado de otros controles de salud existentes**.

---

### 🧪 Ejemplo 1: `AND` lógico

```plaintext
Control de salud calculado: "Healthy" si los 3 siguientes están saludables:
- check_API_EC2
- check_ELB
- check_Auth_Service
```

---

### 🧪 Ejemplo 2: `OR` lógico

```plaintext
Control de salud calculado: "Healthy" si al menos uno está saludable:
- check_East_Region
- check_West_Region
```

---

### 🧪 Ejemplo 3: `NOT`

```plaintext
Control de salud calculado: "Unhealthy" si check_Malicious_API está healthy
```

> ⚠️ Casos útiles en **detección inversa o comportamiento inesperado**

---

### ⚙️ Configuración

- Puedes definir:

  - Número mínimo de checks saludables requeridos (`minHealthy`)
  - Lista de health checks incluidos
  - Operador lógico implícito (`AND`, `OR`, etc.)

---

## 🔒 ¿Por qué los health checks de Route 53 **no funcionan en zonas privadas**?

---

Los **controles de salud de Route 53** son ejecutados por **servidores distribuidos globalmente por AWS**, **fuera de tu VPC**.

Por eso, **no pueden acceder a recursos privados** (por ejemplo, un servicio en una **subred privada**, o en una **zona de alojamiento privada de Route 53**).

> 🧠 Route 53 no puede hacer requests internos a IPs privadas o nombres internos (como `api.internal.local`).

---

## ✅ ¿Cómo monitorear recursos **privados**?

### 🔄 Solución alternativa: **CloudWatch + health check "basado en métricas"**

Puedes crear un **health check personalizado en Route 53** que **use una métrica de CloudWatch** como fuente de verdad.

---

### 🧪 Ejemplo práctico

1. Configuras una métrica en CloudWatch (`api_availability = 1` si está vivo).
2. Crea una **alarma de CloudWatch** sobre esa métrica.
3. En Route 53, creas un **health check basado en esa alarma**.

> ✅ ¡Funciona incluso para recursos **dentro de una VPC** o sin IP pública!

---

## 📋 Resumen

| Atributo                        | Valor                                                    |
| ------------------------------- | -------------------------------------------------------- |
| Calculated health check         | ✅ Combina otros health checks con lógica (AND, OR, NOT) |
| Aplica sobre otros checks       | ✅ No revisa directamente recursos                       |
| Health checks en zona privada   | ❌ No se puede directamente                              |
| Solución para VPC privada       | ✅ Usar métricas de CloudWatch                           |
| CloudWatch como fuente de salud | ✅ Válido para recursos internos, Lambdas, etc.          |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Puede un control de salud calculado verificar un endpoint?_
  ❌ No, solo combina resultados de otros health checks

- ❓ _¿Route 53 puede hacer health checks en subredes privadas?_
  ❌ No. Sus servidores están fuera de la VPC

- ❓ _¿Puedes monitorear un recurso privado con Route 53?_
  ✅ Sí, usando **CloudWatch + health check basado en métricas**

- ❓ _¿Puedes usar lógica personalizada como OR, AND, NOT en controles de salud?_
  ✅ Sí, con **calculated health checks**

## ⚠️ ¿Qué es la **política de conmutación por error (Failover)**?

Es una política de enrutamiento que permite que **Route 53 redirija el tráfico automáticamente** a un recurso **secundario (pasivo)** si el **recurso primario (activo)** falla.

> ✅ Útil para construir soluciones de **alta disponibilidad** y **disaster recovery**.

---

## 🧠 ¿Cómo funciona?

1. Configuras **dos registros DNS** (con el mismo nombre y tipo):

   - Uno como **primario (Primary)**
   - Otro como **secundario (Secondary)**

2. El registro **primario tiene un health check** asociado.

3. Si el health check del primario falla, Route 53:

   - ❌ Deja de responder con el recurso primario.
   - ✅ Responde con el recurso **secundario**.

---

## 🏗️ Topología típica (Activo - Pasivo)

```plaintext
www.ejemplo.com (Failover Routing Policy)
├── A → IP del recurso primario (activo) [con health check]
└── A → IP del recurso secundario (pasivo) [sin health check]
```

- Mientras el **primario esté saludable**, Route 53 **solo responde con él**.
- Si el **primario falla**, Route 53 cambia automáticamente al **pasivo**.

---

## 🧪 Caso de uso clásico: Recuperación ante desastres (Disaster Recovery)

- Tienes tu sitio principal en **us-east-1**.
- Tienes una réplica lista en **us-west-2** (pero no sirve tráfico mientras todo esté bien).
- Si el recurso de us-east-1 cae, Route 53 hace failover a us-west-2.

---

## ❤️‍🩹 Health Check requerido

- **Solo el primario necesita un health check.**
- Si el primario está marcado como "unhealthy", el secundario entra a operar.
- Si el primario se recupera, Route 53 lo vuelve a usar.

---

## 🧠 Notas importantes

| Atributo                      | Valor                                                    |
| ----------------------------- | -------------------------------------------------------- |
| Misma región                  | ✅ O diferentes regiones (recomendado para DR)           |
| Health check obligatorio      | ✅ En el recurso primario                                |
| Health check en el secundario | ❌ No requerido                                          |
| TTL bajo recomendado          | ✅ Para conmutar rápidamente                             |
| Aliases compatibles           | ✅ Sí, pero no puedes asociar health check si usas Alias |
| Failover automático           | ✅ Basado en estado del health check                     |
| Failback automático           | ✅ Si el primario se recupera, Route 53 vuelve a él      |

---

## 📋 Resumen de Failover Routing Policy

| Característica                       | Valor               |
| ------------------------------------ | ------------------- |
| Enrutamiento activo-pasivo           | ✅                  |
| Basado en salud del recurso primario | ✅                  |
| Health checks requeridos             | Solo en el primario |
| Conmutación automática ante fallo    | ✅                  |
| Ideal para DR (Disaster Recovery)    | ✅                  |
| TTL recomendado                      | Bajo (ej. 30s)      |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué política de enrutamiento usarías para recuperación ante desastres?_
  ✅ Failover Routing Policy

- ❓ _¿Se necesita un health check en el recurso secundario?_
  ❌ No

- ❓ _¿Route 53 puede hacer failback automático al recurso primario?_
  ✅ Sí, cuando se recupera

- ❓ _¿Puedes usar Alias con failover?_
  ✅ Sí, pero sin health checks

## 🌎 ¿Qué es la **política de geolocalización**?

La **Geolocation Routing Policy** permite que **Route 53 responda una IP distinta según la ubicación geográfica del usuario** que hace la consulta DNS.

> 📌 Esta política **NO mide latencia**, sino que usa la **ubicación geográfica del resolver DNS** para tomar decisiones.

---

## 📍 ¿Qué se puede identificar?

Route 53 puede identificar la ubicación del usuario según:

- Continente (`North America`, `Europe`, etc.)
- País (`Colombia`, `Germany`, `USA`, etc.)
- Estado/Región (solo para **Estados Unidos**)

---

## 🧪 Ejemplo práctico

```plaintext
www.ejemplo.com
→ Usuarios en Colombia → IP: 35.180.1.1
→ Usuarios en USA → IP: 13.58.2.2
→ Usuarios en Europa → IP: 18.202.3.3
→ Otros (por defecto) → IP: 3.3.3.3
```

---

## 🧠 ¿Qué pasa si un usuario **no encaja** en ninguna regla?

Debes definir un **registro por defecto (default)**, que Route 53 usará cuando no pueda determinar la ubicación o no haya coincidencias específicas.

> ⚠️ Si **no configuras un registro por defecto**, Route 53 **no responderá** para ese usuario.

---

## 📊 Geolocation vs Latency-based

| Aspecto               | Geolocation Routing                                 | Latency-based Routing                      |
| --------------------- | --------------------------------------------------- | ------------------------------------------ |
| Basado en             | Ubicación geográfica del cliente                    | Latencia medida entre cliente y región AWS |
| Usa mapa de latencias | ❌ No                                               | ✅ Sí (AWS lo mantiene)                    |
| Precisión             | País / continente / región (USA)                    | IP pública + topología de red              |
| Casos comunes         | Regulaciones locales, idioma, contenidos regionales | Optimización de rendimiento, juegos, video |
| Failover disponible   | ✅ Con health checks                                | ✅ Con health checks                       |
| TTL configurable      | ✅                                                  | ✅                                         |

---

## 🎯 Casos de uso comunes

| Caso                                          | Por qué es útil                                 |
| --------------------------------------------- | ----------------------------------------------- |
| Mostrar contenido en diferentes idiomas       | Determinas el país y sirves idioma correcto     |
| Reglas de cumplimiento local                  | Por ejemplo, leyes de datos distintas en Europa |
| Experiencia personalizada por región          | Menús, servicios o branding localizados         |
| Redirección a instancias en diferentes países | Para APIs o microservicios regionalizados       |

---

## 📋 Resumen de Geolocation Routing Policy

| Atributo                        | Valor                                  |
| ------------------------------- | -------------------------------------- |
| Basado en ubicación del cliente | ✅                                     |
| Latencia medida                 | ❌ No                                  |
| Soporta health checks           | ✅ Sí                                  |
| Registro por defecto necesario  | ✅ Muy recomendable                    |
| Alias soportado                 | ✅ Sí (sin health check)               |
| Granularidad                    | Continente, país, subregión (solo USA) |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué política usarías para servir contenido diferente según el país del cliente?_
  ✅ Geolocation Routing

- ❓ _¿Route 53 puede identificar el estado de un usuario en USA?_
  ✅ Sí (solo con Geolocation Routing)

- ❓ _¿Qué pasa si no hay una coincidencia de ubicación y no configuras un registro por defecto?_
  ❌ Route 53 **no responderá** la consulta

- ❓ _¿La geolocalización en Route 53 mide latencia?_
  ❌ No. Solo ubicación geográfica

## 🌐 ¿Qué es **Geoproximity Routing Policy**?

Esta política permite **redirigir tráfico a los recursos más cercanos** geográficamente al cliente, pero con la posibilidad de **ajustar el alcance efectivo** de cada recurso mediante un **bias o sesgo**.

> 📌 A diferencia de **geolocalización**, esta no se basa en países sino en **distancia geográfica** y **área de influencia controlable**.

---

## 📍 ¿Cómo determina Route 53 la "proximidad"?

- Usa las **coordenadas geográficas** (latitud/longitud) asociadas a:

  - Una **región de AWS** (si es recurso de AWS)
  - Una **ubicación personalizada** (si es recurso externo a AWS)

---

## ⚙️ ¿Qué puedes enrutar?

- ✅ **Recursos de AWS** como:

  - Instancias EC2
  - ALBs / NLBs
  - CloudFront

- ✅ **Recursos externos a AWS** usando una lat/lon personalizada

> 🧠 Esto permite distribuir tráfico a tu datacenter **fuera de AWS**, por ejemplo, en Latinoamérica o Europa.

---

## 📦 ¿Qué es el **bias**?

El **bias** permite **manipular el área de influencia** de un recurso.
Se mide en porcentaje y puede ser:

- 🔼 **Bias positivo (+%)**: **Aumenta** el área de influencia
- 🔽 **Bias negativo (-%)**: **Reduce** el área de influencia

---

### 🧪 Ejemplo:

```plaintext
• Región us-east-1 → 0% bias
• Región eu-central-1 → +50% bias
```

➡️ Más tráfico de Europa del Este podría ser direccionado a **eu-central-1**
➡️ Incluso si **us-east-1** está técnicamente más cerca, el sesgo inclina la decisión

---

## 🛠️ ¿Cómo se configura?

- Esta política **solo se puede configurar usando Route 53 Traffic Flow** (consola visual o API).
- Cada ubicación debe tener:

  - Coordenadas geográficas (lat/lon)
  - Opcionalmente un **bias**
  - Health check si aplica

---

## 📉 Casos de uso comunes

| Caso                                                   | Descripción                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| Balanceo de tráfico multi-región con sesgos            | Controlar cuánto tráfico recibe cada región manualmente                     |
| Servir usuarios desde una ubicación **no AWS** cercana | Definir un recurso externo con lat/lon personalizada                        |
| Migraciones progresivas                                | Ir moviendo tráfico entre centros gradualmente usando el bias               |
| Optimizar costos                                       | Dirigir más tráfico a regiones más baratas (aunque estén un poco más lejos) |

---

## 🎯 Comparativa con otras políticas

| Característica                  | Geolocation              | Geoproximity                 |
| ------------------------------- | ------------------------ | ---------------------------- |
| Basado en país/región           | ✅ Sí                    | ❌ No                        |
| Basado en distancia geográfica  | ❌ No                    | ✅ Sí                        |
| Ajuste manual (bias)            | ❌ No                    | ✅ Sí                        |
| Soporta recursos fuera de AWS   | ✅ Sí (con limitaciones) | ✅ Sí (con lat/lon)          |
| Configurable vía consola simple | ✅                       | ❌ Solo con **Traffic Flow** |

---

## 📋 Resumen de Geoproximity Routing

| Atributo                           | Valor               |
| ---------------------------------- | ------------------- |
| Basado en proximidad física        | ✅                  |
| Permite usar recursos fuera de AWS | ✅ (con lat/lon)    |
| Bias para manipular tráfico        | ✅                  |
| Requiere Traffic Flow              | ✅ Obligatoriamente |
| TTL configurable                   | ✅                  |
| Soporta health checks              | ✅                  |
| Alias compatible                   | ✅                  |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué política usarías para enrutar tráfico a centros de datos más cercanos geográficamente, pero dando preferencia a uno?_
  ✅ **Geoproximity Routing** con bias positivo

- ❓ _¿Puedes usar recursos fuera de AWS con geoproximidad?_
  ✅ Sí, asignando coordenadas manuales

- ❓ _¿Qué herramienta debes usar para configurarla?_
  ❗ **Route 53 Traffic Flow**

- ❓ _¿Puedes controlar qué porcentaje del tráfico va a una región como con ponderado?_
  ❌ No directamente. Se hace ajustando el **bias**, pero **no se establece un % fijo**

## 🌐 ¿Qué es **Geoproximity Routing Policy**?

Esta política permite **redirigir tráfico a los recursos más cercanos** geográficamente al cliente, pero con la posibilidad de **ajustar el alcance efectivo** de cada recurso mediante un **bias o sesgo**.

> 📌 A diferencia de **geolocalización**, esta no se basa en países sino en **distancia geográfica** y **área de influencia controlable**.

---

## 📍 ¿Cómo determina Route 53 la "proximidad"?

- Usa las **coordenadas geográficas** (latitud/longitud) asociadas a:

  - Una **región de AWS** (si es recurso de AWS)
  - Una **ubicación personalizada** (si es recurso externo a AWS)

---

## ⚙️ ¿Qué puedes enrutar?

- ✅ **Recursos de AWS** como:

  - Instancias EC2
  - ALBs / NLBs
  - CloudFront

- ✅ **Recursos externos a AWS** usando una lat/lon personalizada

> 🧠 Esto permite distribuir tráfico a tu datacenter **fuera de AWS**, por ejemplo, en Latinoamérica o Europa.

---

## 📦 ¿Qué es el **bias**?

El **bias** permite **manipular el área de influencia** de un recurso.
Se mide en porcentaje y puede ser:

- 🔼 **Bias positivo (+%)**: **Aumenta** el área de influencia
- 🔽 **Bias negativo (-%)**: **Reduce** el área de influencia

---

### 🧪 Ejemplo:

```plaintext
• Región us-east-1 → 0% bias
• Región eu-central-1 → +50% bias
```

➡️ Más tráfico de Europa del Este podría ser direccionado a **eu-central-1**
➡️ Incluso si **us-east-1** está técnicamente más cerca, el sesgo inclina la decisión

---

## 🛠️ ¿Cómo se configura?

- Esta política **solo se puede configurar usando Route 53 Traffic Flow** (consola visual o API).
- Cada ubicación debe tener:

  - Coordenadas geográficas (lat/lon)
  - Opcionalmente un **bias**
  - Health check si aplica

---

## 📉 Casos de uso comunes

| Caso                                                   | Descripción                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| Balanceo de tráfico multi-región con sesgos            | Controlar cuánto tráfico recibe cada región manualmente                     |
| Servir usuarios desde una ubicación **no AWS** cercana | Definir un recurso externo con lat/lon personalizada                        |
| Migraciones progresivas                                | Ir moviendo tráfico entre centros gradualmente usando el bias               |
| Optimizar costos                                       | Dirigir más tráfico a regiones más baratas (aunque estén un poco más lejos) |

---

## 🎯 Comparativa con otras políticas

| Característica                  | Geolocation              | Geoproximity                 |
| ------------------------------- | ------------------------ | ---------------------------- |
| Basado en país/región           | ✅ Sí                    | ❌ No                        |
| Basado en distancia geográfica  | ❌ No                    | ✅ Sí                        |
| Ajuste manual (bias)            | ❌ No                    | ✅ Sí                        |
| Soporta recursos fuera de AWS   | ✅ Sí (con limitaciones) | ✅ Sí (con lat/lon)          |
| Configurable vía consola simple | ✅                       | ❌ Solo con **Traffic Flow** |

---

## 📋 Resumen de Geoproximity Routing

| Atributo                           | Valor               |
| ---------------------------------- | ------------------- |
| Basado en proximidad física        | ✅                  |
| Permite usar recursos fuera de AWS | ✅ (con lat/lon)    |
| Bias para manipular tráfico        | ✅                  |
| Requiere Traffic Flow              | ✅ Obligatoriamente |
| TTL configurable                   | ✅                  |
| Soporta health checks              | ✅                  |
| Alias compatible                   | ✅                  |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué política usarías para enrutar tráfico a centros de datos más cercanos geográficamente, pero dando preferencia a uno?_
  ✅ **Geoproximity Routing** con bias positivo

- ❓ _¿Puedes usar recursos fuera de AWS con geoproximidad?_
  ✅ Sí, asignando coordenadas manuales

- ❓ _¿Qué herramienta debes usar para configurarla?_
  ❗ **Route 53 Traffic Flow**

- ❓ _¿Puedes controlar qué porcentaje del tráfico va a una región como con ponderado?_
  ❌ No directamente. Se hace ajustando el **bias**, pero **no se establece un % fijo**

## 🔢 Política **Multivalue Answer** (Multi-Value) en Amazon Route 53

### 🚦 ¿Cómo funciona?

1. Creas **hasta 8 registros** (mismo nombre y tipo) en la zona:

   ```plaintext
   api.ejemplo.com  A  203.0.113.10   (HC-1)
   api.ejemplo.com  A  198.51.100.20  (HC-2)
   api.ejemplo.com  A  192.0.2.30     (HC-3)
   ```

2. (Opcional) Asocias un **health check** a cada registro.
3. Cuando un resolver consulta `api.ejemplo.com`, Route 53:

   - Filtra las entradas que están **unhealthy**.
   - Devuelve **hasta 8 valores** mezclados (orden aleatorio).

4. El **cliente** (navegador, sistema operativo) elige una de las IP para conectarse.

---

### 🛑 ¿Por qué **NO** sustituye a un ELB?

| Característica                           | Multivalue | Elastic Load Balancer                        |
| ---------------------------------------- | ---------- | -------------------------------------------- |
| Balanceo por conexión/paquete            | ❌ No      | ✅ Sí (Round-Robin, Least-Outstanding, etc.) |
| Detección de instancias lentas/saturadas | ❌ No      | ✅ Health checks cada pocos s + algoritmos   |
| Sticky sessions / TLS offload            | ❌ No      | ✅ Sí (ALB/NLB/CLB)                          |
| Autoscaling integrado                    | ❌ No      | ✅ Sí                                        |
| Nº de destinos                           | ≤ 8        | Hasta miles (por Target Group)               |

👉 \*\*Multivalue = “pseudobalanceo” de **DNS**, bueno para cargas ligeras o resiliencia básica; **ELB = balanceo L4/L7 real**, con mucha más inteligencia.

---

### ❤️‍🩹 Health checks con Multivalue

- **Recomendado** asociar un health check a cada registro.
- Si un check pasa a _unhealthy_, Route 53 **lo excluye** de la respuesta—el cliente ya no la recibe.
- Health checkers son públicos: asegúrate de que tu endpoint sea accesible desde Internet.

---

### ⚙️ Detalles rápidos

| Límite                         | Valor                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------- |
| Registros por nombre           | 8 (Route 53 ignora extras)                                                       |
| Tipos soportados               | A, AAAA, Alias                                                                   |
| TTL recomendado                | Bajo (30–60 s) para reacciones rápidas                                           |
| Se combina con otras políticas | ❌ No (exclusiva por nombre/tipo)                                                |
| Uso típico                     | Web/API de tamaño pequeño, split-horizon sencillo, migraciones graduales sin ELB |

---

### 🧠 Resumen de decisiones

- **Necesito balanceo inteligente, stickiness o TLS offload** ➡️ **Usa ELB**.
- **Solo quiero varias IP activas y excluir fallas a nivel DNS (≤ 8)** ➡️ **Multivalue Answer**.
- **Quiero dividir tráfico por % o ubicación** ➡️ Políticas _Weighted_, _Latency_, _Geolocation_, etc.
