# Arquitecturas clásicas

## 🕐 Caso: Arquitectura de **WhatIsTheTime.com**

Aplicación web sin estado que permite a los usuarios saber la hora actual. No requiere base de datos.

---

### 🧪 **Etapa 1: Prueba de concepto (POC)**

- Se despliega en una sola **instancia EC2 t2.micro**.
- La instancia devuelve la hora del sistema.
- Se asigna una **Elastic IP** para acceso público.

❌ **Problemas:**

- Monolítica.
- Si cae la instancia, el servicio se interrumpe.
- Escalar verticalmente a una `m5.large` implica **tiempo de inactividad**.

---

### 📈 **Etapa 2: Escalamiento horizontal**

- En vez de escalar verticalmente, se despliega una **segunda instancia EC2**.
- Se elimina la **Elastic IP**: ya no tiene sentido una IP fija si hay múltiples instancias.
- Se configura **Route 53** con un **registro A (api.whatisthetime.com)** con **TTL de 1 hora**.

❌ **Problemas:**

- Si una instancia se cae, y el TTL es alto, los usuarios seguirán consultando la IP incorrecta.

---

### ⚖️ **Etapa 3: Alta disponibilidad con balanceador**

- Se introduce un **ELB (Elastic Load Balancer)**:

  - Expone una única IP pública.
  - Se encarga del **routing del tráfico a instancias sanas**.
  - Realiza **health checks** automáticamente.

- Se reemplaza el **registro A** en Route 53 por un **registro Alias** apuntando al DNS del ELB.

✅ **Beneficios:**

- Soporte para múltiples instancias sin manejar IPs manualmente.
- Soporte para escalamiento dinámico.
- Conmutación automática si una instancia falla.

---

### 📉 **Etapa 4: Auto Scaling & optimización de costes**

- Se configura un **ASG (Auto Scaling Group)**:

  - Capacidad mínima: 2 instancias.
  - Capacidad deseada: ajustada según tráfico.
  - Capacidad máxima: para picos de carga.

- Instancias en **múltiples AZ (Multi-AZ)** para alta disponibilidad.

> 💡 Si una AZ falla (ej. terremoto), las instancias en otras zonas mantienen el servicio activo.

---

### 💰 Optimización de costos

- Las instancias son **bajo demanda** inicialmente.
- Se puede usar **Capacity Reservation** o **Savings Plans / RI** para reservar capacidad con descuentos a largo plazo.

---

## 🧩 Conceptos usados

| Componente                     | Detalles                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **Elastic IP**                 | Fija para una instancia única, eliminada cuando se escala horizontalmente       |
| **Route 53**                   | Registro A (IP directa) → Alias (apunta al ELB)                                 |
| **TTL**                        | Bajo TTL recomendado si se usan IPs variables (30s–60s)                         |
| **ELB**                        | Balanceo, health checks, integración con ASG                                    |
| **ASG**                        | Escalado automático según demanda, mínimo 2 instancias para alta disponibilidad |
| **Instancias EC2**             | Sin estado, distribuidas en múltiples zonas                                     |
| **Grupos de seguridad**        | Definen el tráfico permitido hacia EC2 y ELB                                    |
| **Multi-AZ**                   | Mejora la resiliencia ante fallas en una AZ                                     |
| **Health Checks**              | ELB detecta instancias no saludables                                            |
| **Capacity Reservation / RIs** | Reserva capacidad con descuento para mínimo 2 instancias                        |

---

## 🏗️ Pilares del Well-Architected Framework aplicados

| Pilar                     | Aplicación en la arquitectura                         |
| ------------------------- | ----------------------------------------------------- |
| 🛡️ Seguridad              | Grupos de seguridad, sin acceso directo a EC2         |
| 🔁 Fiabilidad             | Multi-AZ, ELB con health checks, ASG                  |
| 📈 Rendimiento            | Escalado automático según tráfico                     |
| 💰 Optimización de costos | Escalado dinámico, RIs o Savings Plans                |
| 🧰 Excelencia operativa   | Despliegue sencillo, sin estado, cambios sin downtime |

---

## 👗 Caso: Arquitectura de **MyClothes.com**

Aplicación web de e-commerce con estado (carrito de compras, datos del usuario) que:

- Tiene cientos de usuarios simultáneamente.
- Requiere **escalabilidad horizontal**.
- Debe mantener la aplicación **lo más sin estado posible** para ser escalable y resiliente.
- Debe mantener **persistencia del carrito y datos del usuario**.

---

## 🧠 Desafío: ¿Cómo mantener el estado del **carrito de compras**?

### 1️⃣ **Sticky sessions del ELB** (no recomendado para HA)

- Las **sticky sessions** permiten que un usuario se mantenga con la **misma instancia EC2** durante su sesión.
- Usan una cookie llamada `AWSELB`.

> ❌ Problema: si la instancia falla o hay un rebalanceo, **el estado se pierde**.

---

### 2️⃣ **Almacenar estado en cookies del cliente**

- El **carrito se serializa como JSON** en una cookie.
- Las instancias siguen siendo **sin estado**.
- El frontend maneja la carga del estado.

> ⚠️ Riesgos:

- Las cookies deben ser **< 4 KB**.
- Pueden ser manipuladas (riesgo de seguridad).
- Se debe implementar **validación (firma, HMAC)**.
- Las peticiones HTTP serán más pesadas.

---

### 3️⃣ **Solución ideal: almacenar sesiones en un backend compartido**

✅ Mejor enfoque: usar un **backend compartido para sesiones** con un identificador único (`session_id`) en la cookie.

#### Alternativas

| Opción                         | Ventajas                                                                                | Consideraciones                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Amazon ElastiCache (Redis)** | Millisegundos de latencia, soporte a expiración de sesiones, estructuras como hash/zset | Se debe usar **Multi-AZ** y grupos de seguridad                     |
| **Amazon DynamoDB**            | Sin servidor, escalado automático, TTL para expiración de sesiones                      | Latencia mayor, pero buena para aplicaciones distribuidas o móviles |

💡 Patrón clásico:

1. Cliente envía `session_id` (cookie segura).
2. EC2 o Lambda lee sesión desde **Redis o DynamoDB**.
3. Devuelve respuesta con estado persistido.

---

## 🧾 Almacenamiento de datos del usuario

- Se usa **Amazon RDS** (ej: MySQL/PostgreSQL) para datos como nombre, dirección, historial de pedidos.
- Se puede aplicar **modelo maestro-esclavo**:

### 🔁 Replicación

- **Instancia principal** → solo escritura.
- **Réplica(s) de lectura** → para balancear cargas de consultas.

💡 Alternativa avanzada:

- **Elasticache como capa de caché delante de RDS**:

  - Si hay **hit**: responde desde caché.
  - Si hay **miss**: consulta RDS y cachea el resultado.

---

## 🌍 Alta disponibilidad

- **Instancias EC2 y bases de datos distribuidas en varias AZ** (Multi-AZ).
- Si una AZ falla, los recursos siguen funcionando desde otra.
- **ElastiCache también debe configurarse en modo Multi-AZ (con Redis cluster y réplica)**.

---

## 🔒 Seguridad

| Recurso            | Medida                                                                    |
| ------------------ | ------------------------------------------------------------------------- |
| EC2 ↔ ElastiCache  | Grupos de seguridad deben permitir solo el tráfico necesario              |
| EC2 ↔ RDS          | Acceso restringido por grupo de seguridad                                 |
| Base de datos      | Usuarios con mínimos privilegios, sin acceso público                      |
| Cookies de sesión  | Deben estar firmadas o encriptadas si contienen datos sensibles           |
| Redis (AUTH) o SSL | Activar si aplica, especialmente con ElastiCache público (no recomendado) |

---

## 📋 Resumen general de decisiones

| Componente                     | Función                                        |
| ------------------------------ | ---------------------------------------------- |
| **Sticky session (ELB)**       | ❌ Solo útil si hay una única instancia        |
| **Cookies de usuario**         | ✅ Posible, pero limitada y riesgosa           |
| **ElastiCache (Redis)**        | ✅ Ideal para sesiones rápidas, TTL, multi-AZ  |
| **DynamoDB**                   | ✅ Alternativa serverless, buena escalabilidad |
| **RDS maestro + réplicas**     | ✅ Almacén duradero para datos de usuario      |
| **Multi-AZ EC2 / Redis / RDS** | ✅ Alta disponibilidad y tolerancia a fallos   |
| **Grupos de seguridad**        | ✅ Control granular del tráfico                |

---

## 🧠 Pilares del AWS Well-Architected Framework

| Pilar                     | Aplicación                                                      |
| ------------------------- | --------------------------------------------------------------- |
| 💰 Cost Optimization      | Cacheo de lecturas, instancias por demanda con ASG              |
| ⚙️ Operational Excellence | Sin estado, sesiones desacopladas, escalado automático          |
| 🔁 Reliability            | Multi-AZ en todos los componentes críticos                      |
| 🔐 Security               | Cookies seguras, tráfico interno controlado, usuarios limitados |
| 📈 Performance Efficiency | Redis para sesiones, réplicas para lecturas, TTLs               |

## 📝 Caso: Arquitectura de **myWordpress.com**

Sitio web basado en WordPress que:

- Muestra contenido dinámico (posts, usuarios, sesiones).
- Sube imágenes desde el frontend.
- Usa una base de datos MySQL.
- Requiere **alta disponibilidad**, **persistencia de datos** y **escalabilidad horizontal**.

---

## 🧱 Arquitectura inicial

| Componente                    | Uso                                                            |
| ----------------------------- | -------------------------------------------------------------- |
| **Amazon Route 53**           | DNS para `www.mywordpress.com`                                 |
| **ELB (ALB/NLB)**             | Balanceador para distribuir tráfico entre instancias           |
| **Auto Scaling Group (ASG)**  | Escala horizontalmente las EC2                                 |
| **Amazon EC2 (m5.large)**     | Servidor de WordPress                                          |
| **Amazon RDS MySQL Multi-AZ** | Base de datos relacional para posts, usuarios, configuraciones |
| **EBS (Elastic Block Store)** | Disco persistente para cada instancia                          |

---

### ❌ Problema con EBS

- EBS está **acoplado a una sola instancia EC2**.
- Si el usuario sube una imagen a `instancia-1`, y en su siguiente solicitud va a `instancia-2`, esa imagen **no estará disponible**.

---

## ✅ Solución: almacenamiento compartido

| Recurso                                  | Solución                                                          |
| ---------------------------------------- | ----------------------------------------------------------------- |
| 📷 Subida de imágenes                    | Usar **EFS** (Elastic File System) para almacenamiento compartido |
| 💾 Datos estructurados (posts, usuarios) | Usar **Aurora MySQL** (escalable y resiliente)                    |

---

### 🗃️ Amazon EFS

| Característica  | Detalle                                                        |
| --------------- | -------------------------------------------------------------- |
| Tipo            | File System compartido y elástico                              |
| Acceso          | Todas las instancias EC2 pueden montarlo por NFS               |
| Multi-AZ        | ✅ Alta disponibilidad por diseño                              |
| Montaje         | A través de **ENI (Elastic Network Interface)** en cada AZ     |
| Escenario ideal | Compartir recursos como imágenes, archivos de usuario, plugins |

> ⚠️ EFS no es ideal para objetos grandes y fríos → ahí entra S3.

---

## 🧠 ¿Por qué no usar S3 directamente para WordPress?

| S3 es excelente para...                                            | Pero...                                                              |
| ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Sitios estáticos, archivos JS/CSS, backups, multimedia distribuida | WordPress espera un **sistema de archivos** tradicional para uploads |
| Plugins como WP Offload Media permiten mover los uploads a S3      | Requiere ajustes extra, **no plug-and-play**                         |

---

## 💾 Aurora MySQL para WordPress

| Funcionalidad       | Detalle                                              |
| ------------------- | ---------------------------------------------------- |
| Motor               | Aurora compatible con MySQL                          |
| Modo Multi-AZ       | Alta disponibilidad automática                       |
| Réplicas de lectura | Para escalar consultas pesadas sin afectar escritura |
| Escenario ideal     | Wordpress con mucho tráfico, lecturas constantes     |

---

## 🔐 Seguridad

| Recurso        | Medidas recomendadas                                               |
| -------------- | ------------------------------------------------------------------ |
| RDS/Aurora     | Solo accesible desde SG de EC2                                     |
| EFS            | Solo montable desde instancias en la misma VPC y con SG autorizado |
| EC2            | SG con acceso solo desde el ELB                                    |
| EFS Encryption | Activar cifrado en reposo y en tránsito                            |

---

## 📋 Resumen técnico

| Componente   | Función                      | Tipo                         |
| ------------ | ---------------------------- | ---------------------------- |
| Route 53     | DNS de `www.mywordpress.com` | Alta disponibilidad          |
| ELB          | Balancea tráfico entre EC2   | Escalabilidad                |
| ASG          | Escala horizontal EC2        | Performance y disponibilidad |
| EC2 (m5)     | Servidor WordPress           | Stateless (con EFS)          |
| EBS          | Temporal / Sistema base      | Por instancia                |
| EFS          | Imágenes / Uploads           | Compartido, Multi-AZ         |
| Aurora MySQL | Base de datos de WordPress   | Multi-AZ, escalable          |
| ENI          | Permite conexión a EFS       | Por zona                     |

---

## 🧠 Diferencia entre EBS, EFS y S3

| Recurso | Tipo     | ¿Compartido? | Persistencia | Acceso                                    |
| ------- | -------- | ------------ | ------------ | ----------------------------------------- |
| **EBS** | Bloques  | ❌ No        | ✅ Sí        | Solo 1 instancia                          |
| **EFS** | Archivos | ✅ Sí        | ✅ Sí        | Varias instancias vía NFS                 |
| **S3**  | Objetos  | ✅ Sí        | ✅ Sí        | Acceso HTTP (no como sistema de archivos) |

---

## ✅ Pilares del Well-Architected Framework aplicados

| Pilar                     | Aplicación                                             |
| ------------------------- | ------------------------------------------------------ |
| 🔁 Fiabilidad             | Aurora Multi-AZ + Réplicas, EC2 Multi-AZ, EFS Multi-AZ |
| 💰 Cost Optimization      | ASG para escalar según demanda, lectura en Aurora      |
| 🔐 Seguridad              | Grupos de seguridad estrictos, cifrado EFS/RDS         |
| 📈 Performance Efficiency | Réplicas de lectura, EFS para múltiples EC2            |
| ⚙️ Operational Excellence | Separación de capas, despliegues sin acoplamiento      |

## 🧱 Arquitectura web clásica de 3 niveles en AWS

Esta arquitectura suele componerse de:

| Capa                   | Componentes típicos                                  |
| ---------------------- | ---------------------------------------------------- |
| 🔓 **Subred pública**  | ELB (ALB o NLB), NAT Gateway                         |
| 🖥️ **Subred privada**  | EC2 (web/app servers), Auto Scaling Group            |
| 🗃️ **Subred de datos** | RDS, ElastiCache, a veces S3 para recursos estáticos |

---

## ⚠️ Problemas comunes para desarrolladores

Aunque esta arquitectura es sólida y escalable, puede generar **fricción** para equipos de desarrollo:

| Área                                   | Dificultad                                                                |
| -------------------------------------- | ------------------------------------------------------------------------- |
| 🔧 **Gestión de infraestructura**      | Hay que definir y mantener VPCs, subredes, grupos de seguridad, ELB, etc. |
| 🚀 **Despliegue del código**           | Hay que coordinar pipelines, instalación de dependencias, configuraciones |
| ⚙️ **Configuración de bases de datos** | Usuarios, backups, subredes privadas, endpoints, etc.                     |
| 📈 **Escalado horizontal/vertical**    | Requiere configurar ASG, políticas de escalado, métricas                  |
| 💰 **Costos y optimización**           | Ajustar tipos de instancia, escalado y tiempos de vida                    |

---

## 🌱 ¿Qué es Elastic Beanstalk?

**Elastic Beanstalk** es un servicio **gestionado** que permite a los desarrolladores **desplegar y escalar rápidamente aplicaciones web y servicios** sin gestionar la infraestructura subyacente.

### 💡 Principio clave

> _"Tú subes el código, Beanstalk hace el resto."_

---

## ✅ Beneficios clave de Beanstalk

| Ventaja           | Explicación                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| ⚙️ Automatización | Maneja aprovisionamiento, escalado, monitoreo y despliegue                       |
| 🧠 Abstracción    | Oculta detalles complejos como VPC, ELB, ASG, etc.                               |
| 🪟 Visibilidad    | Aún puedes ver y modificar los recursos creados                                  |
| 🎯 Integración    | Compatible con CloudFormation, CloudWatch, IAM, RDS, etc.                        |
| 💸 Costo          | El servicio **no tiene costo adicional**, solo pagas por los recursos utilizados |

---

## 🧩 Componentes de Elastic Beanstalk

| Componente                   | Descripción                                                                 |
| ---------------------------- | --------------------------------------------------------------------------- |
| **Aplicación**               | Contenedor lógico del proyecto (puede tener múltiples versiones y entornos) |
| **Versión de la aplicación** | Código + configuración específica que puede ser desplegada                  |
| **Entorno**                  | Colección de recursos donde corre una versión específica de la aplicación   |

---

## 🎛️ Tipos de entornos en Beanstalk

### 🌐 Entorno web (web server environment)

- Contiene:

  - ELB
  - ASG
  - Instancias EC2

- Maneja peticiones HTTP/HTTPS
- Ideal para sitios web, APIs, frontends

### ⚙️ Entorno de trabajo (worker environment)

- Contiene:

  - SQS (cola de tareas)
  - EC2 (workers)

- Las peticiones se encolan y los workers las procesan de forma asíncrona
- Ideal para procesamiento en segundo plano (envío de emails, procesamiento de imágenes, tareas pesadas)

💬 **Los entornos pueden comunicarse entre sí**, por ejemplo:

- El **frontend web** encola tareas en SQS
- El **entorno worker** las consume y ejecuta

---

## 🧠 Plataformas soportadas por Beanstalk

| Lenguaje / Plataforma            | ¿Soportado? |
| -------------------------------- | ----------- |
| Go                               | ✅          |
| Java SE, Tomcat                  | ✅          |
| .NET (Core y Framework)          | ✅          |
| PHP                              | ✅          |
| Node.js                          | ✅          |
| Python                           | ✅          |
| Ruby                             | ✅          |
| Docker                           | ✅          |
| Custom platform (Packer Builder) | ✅          |

> Puedes traer tu propio contenedor o construir una plataforma personalizada con Packer si necesitas más control.

---

## 🧭 Flujo típico de uso

1. Desarrollador hace push del código (`zip`, `git`, `eb deploy`, etc.)
2. Elastic Beanstalk crea o actualiza el entorno con:

   - ELB
   - EC2 + ASG
   - RDS opcional

3. Se monitorea desde CloudWatch
4. Si falla el entorno, puedes hacer rollback con otra versión

---

## 📋 Resumen final

| Tema                 | Detalle                                                             |
| -------------------- | ------------------------------------------------------------------- |
| Arquitectura clásica | 3 capas: pública, privada, datos                                    |
| Problema             | Mucho manejo de infraestructura                                     |
| Solución             | Elastic Beanstalk abstrae la complejidad                            |
| Control              | Puedes personalizar recursos si lo necesitas                        |
| Costos               | Solo por lo que usas (Beanstalk en sí es gratuito)                  |
| Ideal para           | Desarrolladores que quieren enfocarse en código, no infraestructura |
