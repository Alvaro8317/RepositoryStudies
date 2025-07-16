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

## 🧊 Movimiento entre clases de almacenamiento en S3

Amazon S3 ofrece **varias clases de almacenamiento**, diseñadas para diferentes patrones de acceso y requisitos de costo. Puedes mover objetos entre ellas **automáticamente** mediante reglas de **ciclo de vida (Lifecycle rules)**.

---

### 📦 Principales clases de almacenamiento

| Clase                       | Descripción                                                     | Uso ideal                         |
| --------------------------- | --------------------------------------------------------------- | --------------------------------- |
| **S3 Standard**             | Alta disponibilidad, baja latencia                              | Archivos accedidos frecuentemente |
| **S3 Standard-IA**          | Infrequent Access: bajo costo, pero con tarifa por recuperación | Archivos accedidos ocasionalmente |
| **S3 One Zone-IA**          | Similar a Standard-IA, pero solo en 1 AZ                        | Backups no críticos               |
| **S3 Glacier**              | Archivo con acceso en minutos u horas                           | Archivado de datos a largo plazo  |
| **S3 Glacier Deep Archive** | Acceso en 12-48h, más económico                                 | Archivado casi histórico          |
| **S3 Intelligent-Tiering**  | Mueve objetos automáticamente según patrones de acceso          | Datos con accesos impredecibles   |

---

## 🔁 Transiciones de clase (Lifecycle Transitions)

Puedes configurar reglas que **transicionen objetos de una clase a otra** después de un número de días.

### 🧠 Ejemplo típico:

1. **Día 0:** Objeto guardado en **S3 Standard**
2. **Día 60:** Mover a **S3 Standard-IA**
3. **Día 180:** Mover a **S3 Glacier**
4. **Día 365:** Eliminar el objeto (opcional)

---

## 🔄 Reglas del ciclo de vida (Lifecycle Rules)

### 📌 ¿Qué pueden hacer?

- **Transicionar objetos entre clases** según edad.
- **Eliminar objetos automáticamente** (expiración).
- **Aplicarse a todo el bucket o a subconjuntos** por:

  - **Prefijo** (por ejemplo: `logs/`)
  - **Etiquetas (tags)** (por ejemplo: `{"archivado": "sí"}`)

### 📘 Sintaxis común en consola:

```plaintext
Transición:
- Si objeto tiene más de 60 días → IA
- Si objeto tiene más de 180 días → Glacier

Expiración:
- Si objeto tiene más de 365 días → eliminar
```

---

## 🧪 Casos de uso comunes

| Caso                           | Clase de destino     |
| ------------------------------ | -------------------- |
| Logs que se consultan poco     | IA o Glacier         |
| Archivos de cumplimiento legal | Glacier Deep Archive |
| Cachés estáticas               | S3 Standard          |
| Backups diarios                | IA o One Zone-IA     |

---

## 💡 Recomendaciones

- Usa **tags** para tener reglas específicas sin afectar todo el bucket.
- Glacier y Deep Archive no son instantáneos: ten presente los **tiempos de recuperación**.
- S3 Intelligent-Tiering puede ayudarte si **no sabes con certeza** cómo se accederán los datos.

---

## 📋 Resumen

| Elemento                 | Detalle                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| Clases de almacenamiento | 6 principales, cada una con casos de uso                          |
| Movimiento entre clases  | Se hace con **acciones de transición** en reglas de ciclo de vida |
| Eliminación automática   | Se hace con **acciones de expiración**                            |
| Aplicación de reglas     | Por **prefijo**, **tag** o global                                 |
| Costo eficiente          | Reduce costos al mover archivos inactivos a clases más baratas    |
| Automatizable            | ✅ 100% con lifecycle rules y sin necesidad de scripts externos   |

## 📊 Amazon S3 Storage Class Analysis (Analytics)

### 🎯 ¿Para qué sirve?

**S3 Analytics** te ayuda a analizar los patrones de acceso a los objetos almacenados en un bucket para decidir **cuándo moverlos automáticamente a una clase de almacenamiento más económica**, como **S3 Standard-IA**.

> Es útil especialmente cuando **no estás seguro de la frecuencia de acceso a tus datos**.

---

## ✅ Casos de uso ideal

- Buckets con objetos en **S3 Standard** que podrían beneficiarse del cambio a **S3 Standard-IA**.
- Análisis previo antes de configurar reglas de ciclo de vida.
- Proyectos con gran volumen de datos y comportamiento variable.

---

## 🧠 Cómo funciona

1. **Activas Analytics** en un bucket o prefijo.
2. AWS comienza a recopilar datos de acceso.
3. Después de **24 a 48 horas**, empiezas a recibir reportes.
4. Se actualiza **diariamente** y muestra:

   - Bytes almacenados
   - Número de objetos
   - Frecuencia de acceso
   - Porcentaje de acceso reciente vs histórico

5. Tú decides si mover esos objetos a IA o no.

---

## 📁 Aplicabilidad

- Puedes aplicar el análisis a **todo el bucket**, a **un prefijo específico** o a **objetos con ciertas etiquetas (tags)**.
- Esto te da granularidad: puedes analizar solo los objetos que te interesan.

---

## 📉 Ejemplo de análisis

Supongamos que tienes un bucket con 100 GB de datos. S3 Analytics puede mostrarte:

| Prefijo      | Tamaño | % Accedido últimos 30 días | ¿Conviene IA? |
| ------------ | ------ | -------------------------- | ------------- |
| `/logs/`     | 30 GB  | 2%                         | ✅            |
| `/images/`   | 50 GB  | 85%                        | ❌            |
| `/archivos/` | 20 GB  | 5%                         | ✅            |

---

## 🧩 Integración con reglas de ciclo de vida

Una vez identificados los datos que no se acceden frecuentemente, puedes:

- Crear reglas de **transición** a **IA o Glacier**
- Crear reglas de **expiración**
- Aplicar reglas a los prefijos analizados

> 📌 **S3 Analytics no realiza la transición automáticamente**, pero **es un primer paso crucial**.

---

## 🛑 Limitaciones

| Limitación        | Detalle                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Tiempo inicial    | Tarda **24-48h** en generar los primeros informes                                              |
| Clases soportadas | Solo compara entre **S3 Standard** y **S3 Standard-IA**                                        |
| Costo             | **Gratuito** dentro del servicio de S3, pero hay cargos normales por almacenamiento y requests |
| No analiza        | Glacier, Deep Archive, Intelligent-Tiering, etc.                                               |

---

## 📋 Resumen

| Tema                   | Detalle                                          |
| ---------------------- | ------------------------------------------------ |
| Qué es                 | Herramienta para analizar el acceso a objetos    |
| Objetivo               | Ayudar a decidir si conviene mover a Standard-IA |
| Frecuencia de análisis | Diario                                           |
| Tiempo inicial         | Primer informe: 24-48 horas                      |
| Aplicable por          | Bucket, prefijo, o etiqueta                      |
| Ideal para             | Crear reglas de ciclo de vida informadas         |
| Automatización         | No realiza cambios, solo analiza                 |

## 💰 S3 “**Requester Pays**” buckets

| Concepto                     | Detalle                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **¿Qué resuelve?**           | El **propietario** de un bucket paga siempre el **almacenamiento**. Con _Requester Pays_ el **coste de las peticiones y de la transferencia de datos** (GET, LIST, PUT, egress) lo asume **quien descarga o sube los objetos**. |
| **Cuándo usarlo**            | - Compartir grandes datasets (logs, imágenes satelitales, genomics…) sin cargar al dueño.<br>- Repositorios públicos de investigación donde cada equipo cubre su propio ancho de banda.                                         |
| **Requisitos**               | 🔐 El solicitante **debe autenticarse** con una cuenta AWS (no funciona para acceso anónimo).<br>🔑 La **política**/ACL debe autorizar la acción solicitada.<br>🌐 Aplica tanto a Internet como a VPC Endpoints.                |
| **Quién paga qué**           | Propietario ⇒ _GB-mes de almacenamiento_.<br>Solicitante ⇒ _Requests_, **Data Transfer OUT**, **Data Transfer IN** (si aplica).                                                                                                 |
| **Clases de almacenamiento** | Funciona con todas; los recargos (ej. Glacier retrieval) también los paga el solicitante.                                                                                                                                       |

---

### 🔧 Cómo activarlo

```bash
aws s3api put-bucket-request-payment \
  --bucket my-dataset-bucket \
  --request-payment-configuration Payer=Requester
```

_Para comprobar:_

```bash
aws s3api get-bucket-request-payment --bucket my-dataset-bucket
```

---

### 🛂 Política mínima de acceso (ejemplo)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOnlyRequesterPays",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::my-dataset-bucket/*"
    }
  ]
}
```

> Aunque la política permita `*`, cada requester **debe** usar `--request-payer requester` (CLI/SDK) para que la operación prospere y se le facture.

---

### 🧪 Uso desde CLI por parte del solicitante

```bash
aws s3 cp s3://my-dataset-bucket/bigfile.csv ./ \
  --request-payer requester
```

Sin el flag, la llamada devuelve **403 Access Denied**.

---

### ⚠️ Consideraciones

- **Costes inesperados**: el propietario sigue pagando el almacenamiento diario.
- **Logging**: habilita Server Access Logs o CloudTrail para auditoría.
- **Cross-Account**: combina _Requester Pays_ con **Bucket Policy** o **Access Points** para precisar permisos.
- **No caching de CloudFront gratuito**: si pones el bucket detrás de CloudFront, el dueño del CloudFront paga el egress desde la edge, no el requester.

---

### 📝 Resumen rápido

1. _Requester Pays_ = el **requester** paga **requests + transferencia**.
2. Propietario **siempre** paga **almacenamiento**.
3. Requiere **autenticación AWS** y `--request-payer requester`.
4. Perfecto para compartir datasets voluminosos sin facturas sorpresa.

## 📣 Notificaciones de eventos de Amazon S3

### 🎯 ¿Qué son?

Permiten a S3 **notificar automáticamente** cuando ocurren ciertos eventos sobre los objetos en un bucket, como:

- Subida (`s3:ObjectCreated:*`)
- Eliminación (`s3:ObjectRemoved:*`)
- Restauración desde Glacier
- Fallos de replicación
- Cambios en el ciclo de vida

---

## 📍 Destinos compatibles

| Destino         | ¿Para qué sirve?                                                       | Características                                                   |
| --------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **SNS**         | Publicar notificaciones a múltiples suscriptores (email, SMS, HTTP...) | Envío masivo y fan-out                                            |
| **SQS**         | Encolar eventos para procesamiento posterior por consumidores          | Asegura el orden, desacopla procesamiento                         |
| **Lambda**      | Ejecutar lógica directamente sobre un evento                           | Serverless, reactivo, código en tiempo real                       |
| **EventBridge** | Motor de eventos con reglas avanzadas, múltiples destinos y fiabilidad | Filtros JSON, redirección de eventos, almacenamiento y repetición |

---

## 🔁 Flujo típico

1. Se sube un archivo al bucket (ej. `PUT`).
2. S3 detecta el evento `ObjectCreated:Put`.
3. Envía notificación al destino configurado (ej. SQS, Lambda, etc).
4. El destino reacciona (procesa, transforma, almacena…).

---

## 🔧 Configuración básica (SQS, SNS, Lambda)

Se puede hacer por:

- **Consola**
- **AWS CLI**
- **S3 API** (vía `NotificationConfiguration`)

```json
{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:region:account:function:processImage",
      "Events": ["s3:ObjectCreated:*"],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "suffix",
              "Value": ".jpg"
            }
          ]
        }
      }
    }
  ]
}
```

> También puedes usar prefijos (`prefix`) para limitar eventos a carpetas específicas.

---

## 🔥 Ventajas de usar EventBridge con S3

| Ventaja                           | Detalle                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 🎯 **Filtros potentes en JSON**   | Puedes hacer filtros por prefijo, sufijo, bucket name, región, o campos personalizados                 |
| 🚦 **Ruteo avanzado**             | Puedes dirigir eventos a múltiples destinos: Lambda, Step Functions, Kinesis, SNS, SQS, otros EventBus |
| 🕒 **Reintento y entrega fiable** | Reintentos automáticos y Dead Letter Queues                                                            |
| 🔄 **Repetición de eventos**      | Puedes volver a emitir eventos pasados almacenados en EventBridge                                      |
| 🧩 **Integración con SaaS**       | Puedes capturar eventos de servicios SaaS como Datadog, Auth0, MongoDB Atlas                           |
| 🗂️ **Archivado de eventos**       | Puedes conservar eventos históricos por tiempo definido                                                |

---

## 🧠 Cuándo usar qué

| Escenario                                        | Mejor opción |
| ------------------------------------------------ | ------------ |
| Reacción simple al subir archivo                 | Lambda       |
| Procesamiento en cola por lotes                  | SQS          |
| Publicación a múltiples sistemas                 | SNS          |
| Necesitas filtros complejos o múltiples destinos | EventBridge  |

---

## 🧪 Ejemplo de caso real

> Se sube un archivo `.csv` al bucket `data-ingest`, y se debe:

- Validar el archivo con Lambda
- Enviar notificación al equipo vía SNS
- Registrar el evento en una base de eventos

📌 Solución:

- S3 envía eventos a **EventBridge**
- EventBridge enruta a:

  - Lambda para validación
  - SNS para alerta
  - Firehose o DynamoDB vía Lambda para almacenar eventos

---

## 🧾 Resumen

| Tema                 | Detalle                                                                      |
| -------------------- | ---------------------------------------------------------------------------- |
| ¿Qué son?            | Eventos automáticos que lanza S3 ante acciones sobre objetos                 |
| Destinos directos    | SNS, SQS, Lambda                                                             |
| Destino avanzado     | EventBridge                                                                  |
| EventBridge ventajas | Filtros JSON, múltiples destinos, repetición, archivado, DLQ                 |
| Configuración        | Por consola, CLI o `NotificationConfiguration`                               |
| Casos comunes        | Subida de imágenes, workflows de ingesta, validaciones, eventos distribuidos |

## 🚀 Rendimiento en Amazon S3

Amazon S3 está diseñado para **escalar automáticamente** para soportar cargas de trabajo con alta demanda de lectura y escritura, sin necesidad de que tú administres el escalado.

---

### 📈 Límites de rendimiento por **prefijo**

| Operación                      | Límite por segundo **por prefijo** |
| ------------------------------ | ---------------------------------- |
| **PUT / COPY / POST / DELETE** | 3,500 requests/segundo             |
| **GET / HEAD**                 | 5,500 requests/segundo             |

📌 **No hay límite en la cantidad de prefijos** que puede tener un bucket, por lo tanto puedes escalar horizontalmente tu carga de trabajo creando más prefijos (por ejemplo: `img/2025/07/`, `img/2025/08/`…).

#### 💡 Recomendación

> Distribuye objetos entre **múltiples prefijos** si esperas un volumen muy alto de solicitudes concurrentes.

---

### 🧩 Carga de varias partes (Multipart Upload)

| Característica  | Detalle                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Qué hace?      | Divide un archivo grande en partes independientes que se suben en paralelo                                                                               |
| ¿Cuándo usarlo? | Recomendado: archivos > 100 MB<br>Obligatorio: archivos > 5 GB                                                                                           |
| ¿Ventajas?      | - Mejora el rendimiento<br>- Recuperación ante errores<br>- Posibilidad de reintento de partes fallidas<br>- Compatible con aceleración de transferencia |
| ¿Cómo funciona? | 1. Inicia carga<br>2. Sube partes<br>3. Finaliza la carga                                                                                                |

> Se puede hacer desde AWS CLI, SDK o S3 Console (archivos grandes).

---

### 🌍 Aceleración de transferencia en S3 (Transfer Acceleration)

| Característica | Detalle                                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Qué hace?     | Usa **Amazon CloudFront** (edge locations) para acelerar la subida y descarga de archivos a S3                                                       |
| ¿Beneficios?   | - Reducción de latencia en cargas y descargas<br>- Ideal para cargas de archivos desde ubicaciones globales<br>- Compatible con **multipart upload** |
| ¿Cómo usarla?  | Habilita la opción en tu bucket y usa la URL `bucketname.s3-accelerate.amazonaws.com`                                                                |

> Ejemplo: para apps móviles o clientes globales que cargan imágenes o documentos a un bucket centralizado.

---

### 📦 Recuperación de rango de bytes (Range GET)

| Característica   | Detalle                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Qué hace?       | Permite recuperar **solo una parte de un objeto** especificando el **rango de bytes**                                                         |
| ¿Para qué sirve? | - **Descarga paralela** de un archivo grande<br>- **Reanudar descargas** incompletas<br>- **Procesamiento parcial** sin bajar todo el archivo |
| ¿Ejemplo?        | Descargar bytes 0–999 de un archivo:                                                                                                          |

```http
Range: bytes=0-999
```

📌 Ideal para descargas por partes en clientes como video streaming, grandes backups o descargas multi-threaded.

---

## 🧠 Casos de uso combinados

| Requisito                              | Técnica recomendada                  |
| -------------------------------------- | ------------------------------------ |
| Subida de archivos de 10 GB            | Multipart upload                     |
| Subida rápida desde Asia               | Transfer Acceleration                |
| Muchas descargas simultáneas           | Distribuir prefijos y usar Range GET |
| Acceso concurrente de objetos          | Más prefijos = más rendimiento       |
| Reanudar descargas sin repetir todo    | Range GET                            |
| Mejorar resiliencia en uploads grandes | Multipart upload con reintentos      |

---

## 📋 Resumen final

| Tema                   | Detalle                                         |
| ---------------------- | ----------------------------------------------- |
| Límites de rendimiento | 3.5K escritura / 5.5K lectura por prefijo       |
| Escalado               | Usa múltiples prefijos para mayor rendimiento   |
| Multipart Upload       | Paraleliza subidas, mejora tolerancia a fallos  |
| Transfer Acceleration  | Usa edge locations para mejorar latencia        |
| Range GET              | Descarga parcial o paralela de archivos grandes |

## 🧠 ¿Qué es S3 Select?

**S3 Select** te permite ejecutar **consultas SQL directamente sobre objetos almacenados en S3**, sin necesidad de descargar el objeto completo a tu aplicación o servidor.

---

### 🎯 ¿Qué resuelve?

✅ **Filtrado de datos del lado del servidor**, antes de enviarlos por red.
✅ **Reducción del volumen de datos transferidos**, y del uso de **CPU en el cliente**.
✅ Ideal para leer **solo columnas o filas específicas** de archivos grandes como CSV, JSON o Apache Parquet.

---

### 📊 ¿Cómo funciona?

1. El objeto (CSV, JSON, Parquet) está almacenado en S3.
2. Ejecutas una consulta SQL como:

   ```sql
   SELECT s.name, s.age FROM S3Object s WHERE s.age > 25
   ```

3. S3 procesa el archivo **dentro del servicio**.
4. Devuelve **solo las filas y columnas que cumplen la condición**.

> 🔸 Esto permite ahorro de ancho de banda, menos espera y menor uso de recursos cliente.

---

### 📁 Formatos soportados por S3 Select

| Formato        | Soportado |
| -------------- | --------- |
| CSV            | ✅        |
| JSON           | ✅        |
| Apache Parquet | ✅        |

📌 Comprimidos en GZIP o BZIP2: sí, siempre y cuando no estén divididos en múltiples bloques internos.

---

## 🧊 Glacier Select

Funciona de forma muy similar a S3 Select, pero sobre **archivos archivados en S3 Glacier** o **Glacier Deep Archive**.

- Permite ejecutar consultas SQL para recuperar **solo una parte del archivo archivado**.
- Reduce el **costo y tiempo de recuperación**, ya que no necesitas restaurar todo el archivo.

🔁 Los pasos son similares: lanzas una consulta SQL, y Glacier devuelve solo el subconjunto filtrado.

> 💡 Es especialmente útil cuando tienes grandes volúmenes de logs, datos históricos o archivos que necesitas analizar esporádicamente.

---

### 🧾 Resumen comparativo

| Característica                | S3 Select                                    | Glacier Select                                |
| ----------------------------- | -------------------------------------------- | --------------------------------------------- |
| Coste                         | Bajo                                         | Más bajo que restauración completa            |
| Latencia                      | Milisegundos a segundos                      | Minutos a horas (según clase de recuperación) |
| Casos ideales                 | Análisis en tiempo real de datos almacenados | Consultas puntuales sobre archivos históricos |
| Formatos soportados           | CSV, JSON, Parquet                           | CSV, JSON                                     |
| Reduce transferencia de datos | ✅                                           | ✅                                            |
| Reduce uso de CPU en cliente  | ✅                                           | ✅                                            |

---

### 🧪 Ejemplo de uso en CLI (S3 Select)

```bash
aws s3api select-object-content \
  --bucket my-data-bucket \
  --key large-file.csv \
  --expression "SELECT s._1, s._2 FROM S3Object s WHERE s._3 > 100" \
  --expression-type SQL \
  --input-serialization '{"CSV": {"FileHeaderInfo": "USE"}}' \
  --output-serialization '{"CSV": {}}' \
  output.json
```

---

## 📌 Casos de uso comunes

- Analizar logs sin descargarlos completamente.
- Extraer solo las columnas necesarias para un dashboard.
- Validar datos de objetos comprimidos de forma eficiente.
- Consultas puntuales a archivos históricos en Glacier.

## ⚙️ S3 Batch Operations (Operaciones por lotes)

### 🎯 ¿Qué son?

Permiten ejecutar **acciones en masa sobre millones o miles de millones de objetos S3**, con una sola solicitud gestionada por AWS.

---

### ✅ ¿Qué operaciones se pueden hacer?

| Tipo de operación              | ¿Qué hace?                                                 |
| ------------------------------ | ---------------------------------------------------------- |
| ✅ **Modificar metadatos**     | Actualizar los metadatos como tipo MIME, fechas, etc.      |
| ✅ **Copiar objetos**          | Entre buckets, cuentas o incluso regiones                  |
| ✅ **Cifrar objetos**          | Aplicar cifrado a objetos no cifrados con SSE-S3 o SSE-KMS |
| ✅ **Actualizar ACLs**         | Cambiar permisos de acceso                                 |
| ✅ **Modificar etiquetas**     | Añadir, cambiar o eliminar tags                            |
| ✅ **Restaurar desde Glacier** | Restaurar objetos archivados                               |
| ✅ **Invocar Lambda**          | Ejecutar código personalizado sobre cada objeto            |
| ✅ **Eliminar objetos**        | Masivamente, incluso versiones                             |

---

## 📦 ¿Cómo se estructura un trabajo de batch?

Un **trabajo (job)** consiste en:

1. ✅ Una **lista de objetos** sobre los que aplicar la operación
2. ✅ La **acción** a ejecutar sobre cada objeto
3. ✅ **Parámetros adicionales** (como destino de copia, clave KMS, etc.)
4. ⏱️ Configuración de **notificaciones, seguimiento y reintentos**
5. 📝 Opción de generar un **informe final CSV** (por éxito/fallo)

---

### 🧾 ¿Cómo obtener la lista de objetos?

1. **S3 Inventory**

   - Genera archivos con el inventario de objetos de un bucket.
   - Incluye claves, tamaño, fecha, cifrado, tags, etc.
   - Útil como entrada para Batch Operations.

2. **S3 Select + S3 Inventory**

   - Usa **S3 Select** para **filtrar objetos relevantes** antes de pasar al lote.

---

### 🔄 Automatización con Lambda

- Puedes usar **AWS Lambda** para ejecutar lógica personalizada en cada objeto.

  - Validaciones
  - Redimensionar imágenes
  - Limpieza de datos
  - Generar thumbnails

> El resultado de cada invocación se monitorea automáticamente.

---

## 🧪 Ejemplo: Cifrar todos los objetos no cifrados en un bucket

1. Crear un inventario con los objetos del bucket.
2. Usar S3 Select para filtrar solo los no cifrados.
3. Crear un job de Batch Operations para aplicar **SSE-KMS** a cada objeto.
4. Activar notificaciones en SNS y generación de informe.
5. S3 gestiona el proceso, reintentos, paralelismo, y errores.

---

## 🔔 Ventajas

| Ventaja                   | Descripción                                 |
| ------------------------- | ------------------------------------------- |
| ⚙️ Automatización         | No requiere escribir código complejo        |
| 🔁 Reintentos automáticos | AWS maneja los errores por ti               |
| 📊 Seguimiento            | Puedes consultar progreso, historial y logs |
| ✉️ Notificaciones         | Compatible con SNS y CloudWatch Events      |
| 📄 Informes               | Detalle de éxito/fallo por objeto           |
| 🛡️ IAM integrado          | Control total sobre permisos y límites      |

---

## 💡 Casos de uso típicos

- Cifrado masivo de objetos antiguos sin cifrado.
- Aplicar nuevas ACLs a un bucket con millones de objetos.
- Copiar grandes volúmenes a otro bucket o región.
- Restaurar objetos desde Glacier en lote.
- Invocar una función Lambda para procesar contenido masivamente.

---

## 📌 Resumen

| Tema                | Detalle                                                       |
| ------------------- | ------------------------------------------------------------- |
| ¿Qué es?            | Procesamiento masivo de objetos S3 en paralelo                |
| Acciones soportadas | Copiar, cifrar, restaurar, invocar Lambda, borrar, modificar  |
| Entrada             | Lista de objetos (ej: S3 Inventory filtrado con S3 Select)    |
| Gestión             | AWS gestiona paralelismo, reintentos, monitoreo               |
| Casos ideales       | Operaciones a gran escala sin escribir scripts personalizados |
