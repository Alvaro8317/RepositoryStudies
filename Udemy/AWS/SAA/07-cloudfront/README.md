# Cloudfront

## 🌍 Clases de precio de CloudFront (Price Classes)

| Clase de precio     | Regiones incluidas                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Price Class All** | Todas las ubicaciones de borde (edge locations) disponibles mundialmente ([Amazon Web Services, Inc.][1])                      |
| **Price Class 200** | Incluye Price Class 100 **más**: Sudáfrica, Kenia, Medio Oriente, Japón, Singapur, Corea del Sur, Taiwán, Hong Kong, Filipinas |
| **Price Class 100** | Solo EEUU, Canadá, Europa e Israel                                                                                             |

---

## 💸 Precios promedio estimados por región (Edge Data Transfer + HTTPS requests)

Basado en las tarifas de CloudFront actualizadas:

| Región                        | Transferencia ∼\$/GB | HTTPS Requests ∼\$/10 k                                                    |
| ----------------------------- | -------------------- | -------------------------------------------------------------------------- |
| **EE. UU., Canadá**           | \$0.085              | \$0.010                                                                    |
| **Europa, Israel**            | \$0.085              | \$0.012                                                                    |
| **Asia Pacífico (ej. Japón)** | \$0.114              | \$0.012                                                                    |
| **Sudamérica**                | \$0.110              | \$0.022                                                                    |
| **Oriente Medio/África**      | \$0.110              | \$0.009–0.022 según país ([Amazon Web Services, Inc.][1], [Simple AWS][2]) |

---

## 🛠️ Estrategias de optimización

- Selecciona la **Price Class** según la ubicación principal de tus usuarios:

  - Si solo atiendes a **América del Norte y Europa**, usa **Class 100** para reducir costos tan bajos como \$0.085/GB.
  - Si también necesitas llegar a **Asia o Sudáfrica**, elige **Class 200**.
  - Para **audiencia global completa**, elige **Class All** para máxima cobertura a mayor costo.

- Reducir **número de edge locations** puede disminuir costos, pero puede aumentar la latencia para usuarios fuera de las regiones activas.

---

### 🧠 Resumen

- **Price Class 100**: EEUU, Canadá, Europa, Israel.
- **Price Class 200**: ● Class 100 + Japón, Singapur, Corea, Hong Kong, Taiwán, Medio Oriente, África.
- **Price Class All**: todas las edge locations.
- Los precios por GB suben desde \$0.085 (regiones baratas) hasta \$0.114–\$0.110 en regiones como Japón o Sudáfrica.
- Las requests HTTPS varían entre \$0.01 y \$0.022 por 10 000.
- Elegir correctamente tu Price Class permite un buen balance entre **coste** y **rendimiento global**.

---

[1]: https://aws.amazon.com/cloudfront/pricing/ "Amazon CloudFront CDN - Plans & Pricing - Try For Free - AWS"
[2]: https://newsletter.simpleaws.dev/p/amazon-cloudfront-optimizing-content-delivery "Amazon CloudFront: Optimizing Content Delivery - Simple AWS"

## 🔄 **Invalidaciones de caché en CloudFront**

---

### 🧠 ¿Por qué hacer una invalidación?

CloudFront **almacena en caché el contenido del origen (backend)** por un tiempo definido por el **TTL (Time To Live)**.
Si el contenido del origen cambia, CloudFront **no lo actualizará inmediatamente**.

➡️ El contenido seguirá sirviéndose **desde la caché** hasta que expire el TTL.

---

### 💥 ¿Qué es una invalidación?

Una **invalidation** es un proceso para **eliminar objetos específicos o todos** de la caché de CloudFront **antes** de que expire su TTL.

Una vez invalidado:

- CloudFront eliminará ese archivo de la caché.
- En la próxima solicitud, irá al origen para obtener el nuevo contenido.

---

### 🛠️ Opciones de invalidación

| Tipo de invalidación                       | Descripción                                            |
| ------------------------------------------ | ------------------------------------------------------ |
| 🔄 **Total (`/*`)**                        | Invalida todos los objetos almacenados en caché        |
| 📂 **Parcial (`/css/*`, `/img/logo.png`)** | Invalida solo una ruta específica o patrón de archivos |

---

### 📘 Ejemplo práctico

Supón que actualizas tu archivo de estilos CSS en el origen, ubicado en `/styles/app.css`.

#### ✅ Opción 1: Invalidez solo el archivo

```bash
aws cloudfront create-invalidation \
  --distribution-id EXXXXXX123 \
  --paths "/styles/app.css"
```

#### ✅ Opción 2: Invalidez todo (⚠️ más costosa)

```bash
aws cloudfront create-invalidation \
  --distribution-id EXXXXXX123 \
  --paths "/*"
```

---

### 💲 Costos

| Detalle                                  | Costo                                    |
| ---------------------------------------- | ---------------------------------------- |
| Primeras **1,000 invalidaciones** al mes | ✅ **Gratis**                            |
| A partir de la **1001**                  | **\$0.005 por cada solicitud adicional** |

---

### ✅ Buenas prácticas

| Práctica                                | Descripción                                                                                   |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| 🏷️ Versionar archivos                   | Ej: `/app.v2.css` en vez de `/app.css` → evita tener que invalidar                            |
| ⏱️ Usar TTL bajo para archivos críticos | Solo si cambian frecuentemente                                                                |
| 🎯 Invalidar solo lo necesario          | Invalida rutas específicas en vez de usar `/*` siempre                                        |
| ⚙️ Automatizar                          | Puedes hacer invalidaciones automáticas desde CI/CD (ej: GitHub Actions) al desplegar cambios |

---

## 📌 Resumen

- Las invalidaciones te permiten **refrescar la caché** de CloudFront antes de que expire.
- Se pueden hacer por ruta o de forma total.
- Las primeras 1,000 son gratis al mes.
- Ideal para cambios críticos como archivos JS/CSS, imágenes, landing pages, etc.
- Evita abusar de `/*` y mejor usa nombres versionados en archivos si puedes.

## 🌍 **AWS Global Accelerator (GA)** – Visión general

---

### 🚀 ¿Qué es?

Es un **servicio de red global** que mejora el rendimiento y disponibilidad de aplicaciones de usuario final accediendo a servicios AWS (como ALB, NLB, EC2, etc.) usando la red **privada global de AWS**.

---

## 🧠 **Conceptos clave**

| Concepto                     | Detalle                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Anycast IPs**              | Crea **2 direcciones IP estáticas** (anycast) que los usuarios finales usarán para conectarse           |
| **Rutas óptimas**            | El tráfico se enruta a través de la red troncal de AWS para alcanzar el destino más cercano y saludable |
| **Enrutamiento inteligente** | Detecta problemas de red y enruta al endpoint más disponible o más cercano                              |
| **Alta disponibilidad**      | Proporciona **failover automático y rápido** entre regiones o endpoints                                 |
| **Protocolo soportado**      | Funciona con **TCP o UDP**, a diferencia de CloudFront que es solo HTTP/HTTPS                           |
| **Integración**              | Compatible con ALB, NLB, EC2 (con Elastic IPs), IP estáticas, multi-region, etc.                        |

---

### 📍 Unicast vs Anycast

| Tipo de IP  | Significado                                                | Caso                                         |
| ----------- | ---------------------------------------------------------- | -------------------------------------------- |
| **Unicast** | Una IP ↔ un servidor                                       | Tradicional (1:1)                            |
| **Anycast** | Una IP ↔ múltiples servidores geográficamente distribuidos | Se enruta al servidor **más cercano** (1\:N) |

---

### 🔐 Seguridad

- Solo necesitas **permitir 2 direcciones IP** en tu firewall (las IPs anycast asignadas).
- Protección integrada con **AWS Shield** (básico y opcionalmente avanzado).
- **No es accesible públicamente como CloudFront**, requiere routing controlado.

---

## ⚙️ **Componentes de AWS Global Accelerator**

| Componente          | Descripción                                        |
| ------------------- | -------------------------------------------------- |
| **Accelerator**     | El recurso principal que contiene las 2 IP anycast |
| **Listeners**       | Controlan los puertos y protocolos (ej: TCP:443)   |
| **Endpoint groups** | Asociados a regiones específicas                   |
| **Endpoints**       | Targets concretos: ALB, NLB, EC2, EIP              |

---

## 📊 Diferencia clave: Global Accelerator vs CloudFront

| Característica               | Global Accelerator                                                                        | CloudFront                                      |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Protocolo**                | TCP/UDP                                                                                   | HTTP/HTTPS                                      |
| **Contenido**                | Dinámico y en tiempo real                                                                 | Estático y dinámico en caché                    |
| **Soporte no-HTTP**          | ✅ Sí (ej: juegos, VoIP, MQTT)                                                            | ❌ No                                           |
| **IP estáticas**             | ✅ Sí (Anycast)                                                                           | ❌ No (DNS)                                     |
| **Failover regional rápido** | ✅ Muy rápido (subsegundos)                                                               | ⚠️ Lento (basado en TTL DNS)                    |
| **Ubicación de borde**       | Proxy de paquetes en el borde + backhaul a AWS                                            | Cache en edge location                          |
| **Rendimiento**              | Ideal para tráfico sensible a latencia (e.g. multiplayer, financieros, streaming en vivo) | Ideal para sitios web, archivos, APIs cachables |

---

### 🧪 Ejemplo de uso real

> Imagina un juego online en tiempo real con servidores en Virginia y Tokio.
> Usuarios de Latinoamérica y Europa se conectan a una **IP estática**.
> Global Accelerator redirige automáticamente al servidor más cercano y con menor latencia usando la red interna de AWS, con recuperación automática si uno de los endpoints falla.

---

## ✅ Ventajas

| Ventaja                            | Explicación                                               |
| ---------------------------------- | --------------------------------------------------------- |
| ⚡ Bajísima latencia global        | Al usar la red troncal optimizada de AWS                  |
| 🛠️ Conmutación por error rápida    | Cambio automático de región o endpoint sin cambiar DNS    |
| 🌐 IPs estáticas globales          | Útil para clientes firewall-restringidos o listas blancas |
| 🔧 No requiere migrar arquitectura | Se puede agregar sobre infra existente                    |
| 🧪 Soporta UDP y TCP               | Ideal para más tipos de aplicación que CloudFront         |

---

## 🧠 Casos de uso comunes

- Juegos multijugador (UDP)
- Voz sobre IP (VoIP)
- Finanzas en tiempo real (baja latencia)
- APIs con IP fija (para firewalling)
- Alta disponibilidad multi-región con failover rápido
- Aplicaciones móviles con distribución global
