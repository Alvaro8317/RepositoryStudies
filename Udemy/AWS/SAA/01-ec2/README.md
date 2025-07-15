# EC2

## 🧠 **Resumen clave: EC2 Spot Instances para el examen AWS SAA-C03**

### 🔹 ¿Qué son las Instancias Spot?

- Te permiten ahorrar **hasta 90%** respecto al precio bajo demanda.
- Pagas mientras el **precio spot actual** sea menor que tu **precio máximo definido**.
- Si el precio sube por encima de tu límite, AWS puede **detener o terminar** la instancia con **2 minutos de aviso**.

### 🔹 Bloqueo de Spot (Spot Block)

- Garantiza que la instancia no se interrumpa por **1 a 6 horas**.
- Ideal para **trabajos temporales tolerantes a fallos**, como:

  - Procesamiento por lotes
  - Análisis de datos
  - Renderizado

Cada AZ puede tener un costo distinto para las instancias spot.

- **No es recomendable** para sistemas críticos o bases de datos.
- **NOTA**: Este bloqueo dejó de estar disponibles desde finales del 2022

### 🔹 Finalización de Spot Instances

- Para terminar correctamente:

  1. **Cancelar la solicitud Spot**
  2. Luego **terminar la instancia**

- Cancelar una solicitud NO termina la instancia automáticamente.

### 🔹 Flotas Spot (Spot Fleets)

- Combina **instancias Spot** con (opcionalmente) **instancias bajo demanda** para cumplir una capacidad deseada.
- Define múltiples **pools de lanzamiento** (tipo de instancia, zona, SO).
- La flota detiene el aprovisionamiento al alcanzar el **límite de capacidad o presupuesto**.
- Estrategias de asignación:

  - **Lowest price**: costo mínimo (ideal para tareas cortas)
  - **Diversified**: mayor disponibilidad, tolerancia a fallos
  - **Capacity optimized**: asegura capacidad suficiente (ideal para cargas grandes o persistentes)

---

## 🎯 Pregunta de práctica estilo examen AWS

**Pregunta:**

Una empresa de análisis de datos quiere ejecutar trabajos de procesamiento por lotes de bajo costo que pueden interrumpirse ocasionalmente. ¿Cuál es la opción más adecuada en términos de costo y tolerancia a fallos?

A. Instancias bajo demanda con Auto Scaling
B. Instancias reservadas
C. Instancias Spot con estrategia de asignación "lowest price"
D. Instancias Spot bloqueadas durante 6 horas

**Respuesta correcta:** ✅ **C. Instancias Spot con estrategia de asignación "lowest price"**

**Justificación:** Los trabajos por lotes tolerantes a fallos se ajustan perfectamente a instancias Spot con optimización de costo. El "Spot Block" sería mejor si no toleran interrupciones, pero no es necesario en este caso.

---

## 🧠 **Apuntes de AWS – Spot Fleet Request**

### 🧾 ¿Qué es una Spot Fleet?

Una **Spot Fleet** es un conjunto de instancias EC2 que se ejecutan con capacidad Spot (instancias con descuento) y, opcionalmente, On-Demand, gestionadas de forma automática para cumplir una **capacidad objetivo** (por número de instancias o vCPUs).

---

## 🛠️ **Parámetros de lanzamiento**

### 📦 AMI (Amazon Machine Image)

- Plantilla que contiene el sistema operativo, aplicaciones y configuración.
- Puede ser:

  - Proporcionada por AWS.
  - De la comunidad.
  - De AWS Marketplace.
  - Personalizada (propia del usuario).

### 🔐 Key Pair

- Conjunto de clave pública (guardada en AWS) y clave privada (guardada localmente).
- **Linux**: SSH con clave privada.
- **Windows**: La clave privada se usa para descifrar la contraseña del administrador.

### 📁 Almacenamiento

- **EBS-Optimized**: Mejor rendimiento entre EC2 y volúmenes EBS.
- **Instance Store**: Almacenamiento efímero (se pierde al detener la instancia).
- **EBS Volumes**: Persistente, configurable (Snapshot, tamaño, tipo, IOPS, encriptación, auto-delete, etc.).

---

## 📊 **Monitoreo y Seguridad**

### 📈 Monitoring

- **Básico** (por defecto): métricas cada 5 minutos.
- **Detallado** (opcional): métricas cada 1 minuto (con costo).

### 🏠 Tenancy

- **Shared hardware**: por defecto, instancia en hardware compartido.
- **Dedicated**: hardware dedicado (más costoso, por requerimientos especiales).

### 🔐 Security Groups

- Reglas de firewall asociadas a la instancia.
- Para VPCs, deben crearse dentro de la misma.

---

## 🌐 Red y Accesibilidad

### 🌍 IP Pública

- Se puede asignar una IPv4 pública automáticamente.

### 🆔 IAM Instance Profile

- Permite a la instancia asumir un rol IAM y acceder a servicios de AWS.

### 🧾 User Data

- Script que se ejecuta al lanzar la instancia (como `cloud-init` para instalar paquetes o configurar servicios).

---

## 🏷️ Tags

- Claves/valores para organizar recursos.
- Se pueden asignar por instancia o por fleet.

---

## 🎯 Detalles de la Fleet Request

### 🧾 IAM Fleet Role

- Rol IAM necesario para que la Fleet gestione las instancias por ti.

### ⏳ Duración y Terminación

- Puedes definir una duración (ej. 1 año) y si las instancias deben terminar al expirar.

### 🔢 Target Capacity

- Capacidad total deseada.
- Puede incluir:

  - **On-Demand base capacity**
  - **Spot capacity restante**

### 🔁 Maintain Capacity

- AWS reemplazará automáticamente instancias Spot interrumpidas.

### 💰 Precio Máximo

- Puedes definir cuánto estás dispuesto a pagar por hora como máximo.

---

## 🗺️ Red y Zona de Disponibilidad

### 🌐 VPC

- Debes lanzar las instancias dentro de una VPC.

### 📍 Availability Zones

- Puedes lanzar instancias en varias AZs para alta disponibilidad.

---

## 📐 Requisitos de instancia

### ✅ Selección de Instancias

- **Atributos definidos**: vCPU, RAM, etc. AWS selecciona instancias que cumplan.
- **Manual**: seleccionas tipos específicos de instancia.

### 💡 Atributos opcionales

- Arquitectura, generación, almacenamiento, tipo de red, etc.

---

## 🎛️ Estrategia de asignación

### 📊 Spot Allocation Strategy

- **Price capacity optimized (recomendada)**: mejor equilibrio entre precio y disponibilidad.
- **Capacity optimized**: menor riesgo de interrupción.
- **Diversified**: distribuye la carga entre varios pools de instancia (no compatible con selección por atributos).

---

## 📌 Resumen final

- **Capacidad objetivo**: 1 instancia
- **Estrategia basada en atributos**
- **566 tipos de instancia disponibles**
- **6 zonas de disponibilidad posibles**
- **Precio estimado**: \~\$0.741/hora
- **Ahorro estimado**: 87% frente a instancias On-Demand

## 🧠 **Apuntes de AWS – EC2 Instances & Modelos de Compra**

---

### 🖥️ **Instances**

Una **instancia EC2** es una máquina virtual que se ejecuta en la infraestructura de AWS. Puedes elegir su tipo, sistema operativo, almacenamiento, red, entre otros.

---

### 📦 **Instance Types**

Tipos de instancia diseñados para distintos casos de uso:

- **t3/t4g (burstable)**: cargas variables
- **m5/m6i (general purpose)**: balance entre CPU/RAM
- **c5/c6g (compute optimized)**: cargas con alto uso de CPU
- **r5/r6g (memory optimized)**: bases de datos, analytics
- **g4/g5 (GPU)**: ML, gráficos

---

### 🚀 **Launch Templates**

- Plantillas predefinidas con parámetros para lanzar instancias: AMI, tipo, clave SSH, redes, volúmenes, etc.
- Reutilizables.
- Usadas por Spot Fleets, Auto Scaling Groups, etc.
- Reemplazan y mejoran los antiguos **Launch Configurations**.

---

### 🔁 **Spot Requests**

- Solicitudes para usar **instancias Spot**, que son capacidad sobrante de EC2 con descuentos de hasta 90%.
- Pueden ser interrumpidas por AWS con 2 minutos de aviso.
- Ideales para cargas tolerantes a fallos: procesamiento por lotes, CI/CD, entrenamiento ML, etc.

---

### 💸 **Savings Plans**

Compromisos de uso de **una cantidad de USD por hora** (ej: \$50/hora durante 1 o 3 años) a cambio de **descuentos automáticos**:

- **Compute Savings Plans**: descuento para cualquier servicio que use EC2 (Lambda, Fargate), sin importar región o familia.
- **EC2 Instance Savings Plans**: más restrictivos, pero con mayor descuento si usas una familia, región y sistema operativo específicos.

---

### 📅 **Reserved Instances (RIs)**

- Reservas de instancias específicas por **1 o 3 años**.
- A cambio, tienes descuentos hasta del **72%** vs On-Demand.
- Se aplican automáticamente cuando lanzas instancias que coinciden con los parámetros reservados (tipo, AZ, OS, etc.).
- Tipos:

  - **Standard RIs**: más descuento, menos flexibilidad.
  - **Convertible RIs**: puedes cambiar tipo de instancia, pero con menos descuento.

---

### 🧱 **Dedicated Hosts**

- Hardware físico reservado completamente para ti.
- Control total sobre la asignación de instancias (cumple regulaciones de licenciamiento como Windows Server/SQL Server BYOL).
- Costoso, pero útil para cumplimiento o aplicaciones con licencias específicas.

---

## 🏠 **Capacity Reservations (¡explicación en profundidad!)**

### ❓ ¿Qué son?

Son **reservas de capacidad de EC2** en una zona de disponibilidad específica dentro de tu cuenta, pero **sin comprometer un modelo de precios**.

👉 **Reservas capacidad ≠ descuento automático**

---

### 📌 Características clave

| Característica               | Explicación                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| 🔒 Capacidad garantizada     | Aseguras que, cuando necesites lanzar instancias específicas, habrá capacidad disponible.    |
| ⚠️ No implican descuento     | Se cobra al precio **On-Demand** a menos que también tengas RIs o Savings Plans compatibles. |
| 🧩 Compatibles con RIs       | Si lanzas instancias que coincidan con una **Reserved Instance**, se usa el descuento.       |
| 🔄 Flexible                  | Puedes modificarla o cancelarla sin costo adicional.                                         |
| 🕐 Temporal o permanente     | Puedes dejar la reserva "hasta que la canceles", o definir un rango de fechas.               |
| ✅ Requiere detalles exactos | Debes especificar tipo de instancia, AZ, plataforma, tenancy, etc.                           |

---

### 🎯 ¿Cuándo usar Capacity Reservations?

- Cuando necesitas asegurar capacidad para un evento crítico (ej: Black Friday).
- Para cargas importantes en regiones con **alta demanda o picos**.
- Para mantener cumplimiento en despliegues multi-región con instancias específicas.

---

### 🧠 Ejemplo real

> Tienes una app crítica que debe escalar a `c5.large` en `us-east-1a`. Haces una **Capacity Reservation** de 10 instancias `c5.large` ahí. Aunque no las uses aún, AWS garantiza que puedes lanzarlas cuando quieras. Si ya tienes RIs que aplican, el costo será menor. Si no, pagarás precio On-Demand aunque estén reservadas.

## 🌐 **IP Privada vs Pública vs Elástica en AWS**

---

### 🏠 **IP Privada (Private IP)**

#### ✅ Qué es IP privada

- IP asignada internamente dentro de una **VPC**.
- Solo accesible **dentro de la red privada de AWS** o mediante VPN/Direct Connect.
- **No se puede acceder desde Internet** directamente.

#### 🔒 Uso típico

- Comunicación entre instancias EC2.
- Acceso a bases de datos o servicios backend sin salir a Internet.

#### 📦 Ejemplo de IP privada

> Una instancia EC2 en una subred privada con IP `10.0.1.15`. Esta instancia puede acceder a una base de datos RDS en la misma VPC sin exponer nada al exterior.

---

### 🌍 **IP Pública (Public IP)**

#### ✅ Qué es IP publica

- IP asignada automáticamente **cuando lanzas una instancia EC2 en una subred pública** (si lo configuras así).
- Permite el acceso desde Internet **si también tienes una puerta de enlace NAT o Internet Gateway configurada**.

#### ⚠️ Consideraciones

- No es persistente: **si detienes la instancia y la vuelves a iniciar, cambiará**.
- Requiere una ruta al Internet Gateway y reglas de seguridad adecuadas.

#### 📦 Ejemplo de IP publica

> Lanzaste una instancia EC2 para un servidor web, se le asignó la IP pública `3.90.123.45`. Puedes acceder con `ssh ec2-user@3.90.123.45`.

---

### 📌 **Elastic IP (EIP)**

#### ✅ Qué es IP elastica

- IP pública **estática** que puedes asignar a cualquier instancia EC2.
- Se mantiene **aunque detengas y reinicies** la instancia.
- Puedes **desasociarla y reasociarla** entre instancias (ideal para failover).

#### 💰 Costo

- Gratuita **si está asociada a una instancia en uso**.
- **Cobran** si está sin asociar (para evitar mal uso de IPs escasas).

#### 📦 Ejemplo de IP elastica

> Tienes un servidor productivo con IP elástica `44.201.55.99`. Si debes reemplazar la instancia, reasocias el EIP a una nueva, y tus usuarios no notan el cambio.

---

## 🧠 Comparativa rápida

| Atributo       | IP Privada         | IP Pública             | Elastic IP (EIP)          |
| -------------- | ------------------ | ---------------------- | ------------------------- |
| Visibilidad    | Solo dentro de VPC | Internet (temporal)    | Internet (fija)           |
| Persistencia   | Fija               | Cambia al reiniciar    | Fija hasta que la liberes |
| Costo          | Incluida           | Incluida               | Gratis si está en uso     |
| Acceso externo | ❌ No              | ✅ Sí (con reglas)     | ✅ Sí (mejor control)     |
| Uso típico     | Backend, DB        | Dev, testing, web apps | Producción, failover      |

---

## 🧱 Ejemplo práctico completo

Imagina una arquitectura de 3 niveles:

- **Frontend EC2** en subred pública con Elastic IP (`44.55.66.77`)
- **Backend EC2** en subred privada con IP privada (`10.0.2.10`)
- **Base de datos RDS** en subred privada, solo accesible desde el backend

Solo el frontend tiene acceso a Internet. El backend y la base de datos **no necesitan ni deben tener IP pública**.

Una IP elastica no se recomienda usar en exceso ya que pueden significar una mala decisión de arquitectura, por eso se pueden tener máximo 5 IPs elasticas por cuenta, mejor usar un DNS o un balanceador de carga.
Si una instancia con IP publica se detiene y se vuelve a iniciar, la IP cambia a menos que sea elastica.

## 🧱 **Placement Groups en EC2 (Grupos de colocación)**

---

### ✅ ¿Qué son?

Son una característica de EC2 para **controlar la ubicación física** de las instancias dentro de una región o AZ (zona de disponibilidad), optimizando ya sea el rendimiento o la resiliencia.

---

## 📂 Tipos de Placement Groups

| Tipo          | Descripción                                                                          | Casos de uso                                                    | Requisitos                                                                                   |
| ------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Cluster**   | Agrupa instancias **muy cerca físicamente** dentro de una AZ.                        | HPC, big data, baja latencia, alto throughput entre instancias. | Instancias deben estar en la misma AZ y tipo compatible con redes mejoradas.                 |
| **Spread**    | Distribuye instancias entre **distintos racks físicos** para alta disponibilidad.    | Cargas críticas, quorum, bases de datos sensibles a fallos.     | Máximo **7 instancias por AZ** por grupo.                                                    |
| **Partition** | Agrupa instancias en **particiones lógicas separadas**, cada una en racks distintos. | Hadoop, Cassandra, HDFS: tolerancia a fallos por partición.     | Puedes definir hasta **7 particiones por AZ**, y hasta **100s de instancias por partición**. |

---

## 🎯 Comparativa visual rápida

| Atributo                | **Cluster**                       | **Spread**                     | **Partition**                |
| ----------------------- | --------------------------------- | ------------------------------ | ---------------------------- |
| 🎯 Objetivo             | Rendimiento                       | Alta disponibilidad            | Fallos aislados por grupo    |
| 📶 Red interna          | Muy rápida                        | Normal                         | Normal                       |
| 🧱 Misma AZ             | ✅ Sí                             | ✅ Sí                          | ✅ Sí                        |
| 🏗️ Mismo rack           | ✅ (posible)                      | ❌ (separados)                 | ❌ (separados por partición) |
| ⚠️ Límite de instancias | Sin límite fijo (depende de tipo) | 7 por AZ                       | Decenas o centenas           |
| 🔧 Uso ideal            | HPC, ML, renderizado              | Aplicaciones críticas pequeñas | Big data, bases distribuidas |

---

## 🔧 ¿Cómo se usan?

Puedes crear un placement group desde la consola, CLI o CloudFormation. Luego, al lanzar una instancia EC2, puedes especificar ese grupo.

```bash
aws ec2 create-placement-group \
  --group-name my-cluster \
  --strategy cluster

aws ec2 run-instances \
  --placement GroupName=my-cluster \
  ...
```

---

## 🧠 Tips para el examen

- **Cluster** = máximo rendimiento, mínimo retraso. Ideal para HPC.
- **Spread** = mínimo impacto si un rack falla. Ideal para **resiliencia**.
- **Partition** = separación lógica de fallos. Ideal para **sistemas distribuidos** como Hadoop o Cassandra.
- Si lanzas instancias en un grupo y alguna falla por falta de capacidad, **todas pueden fallar**. Para evitar esto, **verifica disponibilidad** antes.

---

## 📌 Ejemplo práctico

Tienes una base de datos NoSQL distribuida (como Cassandra). Para evitar que un fallo de hardware tumbe todo el clúster:

- Crea un **placement group tipo partition** con 3 particiones.
- Lanzas los nodos del clúster distribuidos en esas particiones.
- Si un rack falla, solo una partición se ve afectada, no el sistema completo.

¡Perfecto! Aquí tienes apuntes bien explicados sobre los **ENI (Elastic Network Interface)**, que también son preguntados en la certificación **AWS Certified Solutions Architect - Associate (SAA-C03)**, especialmente en temas de redes y alta disponibilidad.

---

## 🌐 **ENI – Elastic Network Interface**

---

### ✅ ¿Qué es un ENI?

Un **Elastic Network Interface (ENI)** es una **tarjeta de red virtual** que puedes adjuntar a una instancia EC2 dentro de una VPC.

---

### 🧱 ¿Qué incluye un ENI?

Cada ENI puede contener:

- 1 o más **IP privadas**
- 1 IP pública o **Elastic IP** (opcional)
- 1 MAC address (fijo)
- 1 o más **grupos de seguridad**
- Una **subred**
- Bandera para asignar IP pública automáticamente

---

## 🧠 ¿Para qué sirve un ENI?

| Uso                     | Explicación                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| 🕹️ Alta disponibilidad  | Puedes **mover un ENI** entre instancias en caso de fallo, como si movieras una tarjeta de red física.          |
| 🏗️ Arquitecturas de red | Tener múltiples ENIs permite **segmentar tráfico**: ejemplo, una ENI para tráfico web, otra para base de datos. |
| 🔐 Seguridad            | Puedes usar diferentes **grupos de seguridad** por ENI para separar reglas de entrada/salida.                   |
| 🔄 Reutilización        | Puedes asociar un ENI a otra instancia sin perder la IP privada (y EIP si aplica).                              |
| 🔍 Monitoreo avanzado   | Puedes controlar métricas por ENI y configurar flujos de tráfico con VPC Flow Logs.                             |

---

## 🔧 Tipos de ENI y uso

| Tipo de ENI                | Casos de uso                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------ |
| **Primario (default)**     | Siempre presente cuando lanzas una instancia EC2                                     |
| **Secundario (adicional)** | Se puede adjuntar manualmente a una instancia (hasta un límite)                      |
| **ENI independiente**      | Puedes crear un ENI sin asociarlo a una instancia y usarlo luego cuando lo necesites |

---

### 📌 Límite de ENIs por instancia

Depende del tipo de instancia. Ejemplo:

- `t3.micro` → hasta **2 ENIs**
- `m5.large` → hasta **3 ENIs**
- `c5.18xlarge` → hasta **15 ENIs**

---

## 💡 Ejemplo práctico

Supón que tienes una aplicación que necesita aislar el tráfico de usuarios del tráfico administrativo. Puedes:

- Crear una EC2 con **2 ENIs**:

  - ENI1: IP pública, grupo de seguridad web, puerto 80 y 443
  - ENI2: Solo IP privada, grupo de seguridad con puerto 22 (SSH) o admin tools

Así el tráfico se aísla, es más seguro y auditable.

---

## 🚨 Preguntas típicas en el examen

- ❓ _¿Qué puedes hacer si una instancia EC2 falla y necesitas mover su IP privada a otra instancia?_
  ✅ **Mover el ENI a otra instancia.**

- ❓ _¿Cuál es el método más simple para implementar failover de red entre dos instancias EC2?_
  ✅ **Desasociar un ENI de una instancia y asociarlo a otra.**

---

## 🛠️ CLI – Comandos útiles

```bash
# Crear un ENI
aws ec2 create-network-interface \
  --subnet-id subnet-12345 \
  --groups sg-12345

# Asociarlo a una instancia
aws ec2 attach-network-interface \
  --network-interface-id eni-12345 \
  --instance-id i-12345678 \
  --device-index 1
```

[Documentación de ENI](https://aws.amazon.com/blogs/aws/new-elastic-network-interfaces-in-the-virtual-private-cloud/)

## 💤 **Hibernación en EC2 (EC2 Hibernation)**

---

### ✅ ¿Qué es la hibernación?

La **hibernación** permite **detener una instancia EC2 y guardar su estado en disco**, de forma que cuando se reinicia:

- La RAM se restaura tal como estaba.
- Los procesos en memoria **retoman desde donde se dejaron**.
- El sistema operativo no se reinicia desde cero (a diferencia de un "stop").

---

### 🧠 ¿Cómo funciona?

1. Al hibernar, AWS:

   - Guarda el **contenido de la RAM** en el volumen raíz EBS.
   - **Detiene la instancia**.

2. Al reiniciar:

   - AWS **restaura la RAM** desde el volumen EBS.
   - Retoma desde el punto exacto donde se hibernó.

---

## 📋 Requisitos para usar hibernación

| Requisito            | Detalles                                                                        |
| -------------------- | ------------------------------------------------------------------------------- |
| ✅ Sistema Operativo | Solo soportado en: Amazon Linux 2, Ubuntu, RHEL, SUSE, Windows Server (algunos) |
| ✅ Tipo de instancia | Solo tipos específicos: `t3`, `t3a`, `m5`, `c5`, `r5`, etc. (con RAM ≤ 150 GB)  |
| ✅ Volumen raíz EBS  | Debe estar encriptado                                                           |
| ✅ AMI               | Debe ser **hibernation-enabled** (algunas AMIs de AWS lo están)                 |
| ✅ RAM               | Hasta **150 GB**                                                                |
| ✅ Solo EBS          | No funciona con instance store (almacenamiento efímero)                         |

---

## 🛠️ Cómo habilitarla

- Al lanzar una instancia, debes **habilitar la opción de hibernación al detener** (CLI, consola o API).
- La instancia debe cumplir con los requisitos anteriores.

```bash
aws ec2 run-instances \
  --image-id ami-xyz \
  --instance-type t3.medium \
  --hibernation-options Configured=true \
  ...
```

---

## 📌 Costos

- Mientras la instancia está hibernada:

  - **No se cobra uso de CPU o RAM.**
  - **Se siguen cobrando los volúmenes EBS.**
  - **La Elastic IP (si no está asociada) genera costo.**

---

## 🎯 Casos de uso ideales

| Caso                                  | Descripción                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| 🧪 Ambientes de desarrollo            | Guardas el estado de trabajo al final del día y retomas luego sin perder nada. |
| 🖥️ Escritorios virtuales persistentes | Usuarios reanudan sesiones sin reiniciar apps.                                 |
| 🧠 Cargas con estado complejo         | Modelos de ML o procesos largos que se pueden pausar.                          |

---

## ❌ Limitaciones

- No compatible con **Auto Scaling**.
- No se puede cambiar tipo de instancia mientras está hibernada.
- Algunas imágenes personalizadas o kernels no soportan la restauración.
- Mayor tiempo de detención/inicio que `stop/start` estándar (por el guardado/restauración de memoria).

---

## 🔄 Comparativa rápida

| Acción         | RAM guardada | Tiempo de arranque | Se cobra CPU |
| -------------- | ------------ | ------------------ | ------------ |
| **Stop/Start** | ❌ No        | Más lento          | ❌ No        |
| **Hibernar**   | ✅ Sí        | Más rápido         | ❌ No        |
| **Reboot**     | ❌ No        | Muy rápido         | ✅ Sí        |
| **Terminate**  | ❌ No        | N/A (se destruye)  | ❌ No        |

---

## 💽 **Amazon EBS (Elastic Block Store)**

---

### ✅ ¿Qué es EBS?

- **Servicio de almacenamiento en bloque** para instancias EC2.
- Los volúmenes EBS se comportan como **discos duros virtuales**.
- Son **persistentes**, es decir, los datos se conservan incluso si la instancia EC2 se detiene o termina (si se configura así).

---

### 📂 Tipos de volúmenes EBS

| Tipo          | Descripción                                          | Uso ideal                                               |
| ------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| **gp3**       | SSD de propósito general (nuevo por defecto)         | Boot volumes, bases de datos pequeñas, cargas generales |
| **gp2**       | SSD de propósito general (anteriormente por defecto) | Igual que gp3, pero menos eficiente                     |
| **io2 / io1** | SSD de alto rendimiento con IOPS provisionadas       | Bases de datos críticas, OLTP                           |
| **st1**       | HDD optimizado para throughput                       | Big Data, data lakes, logs                              |
| **sc1**       | HDD frío, de bajo costo                              | Archivos de poco acceso, backups                        |

---

### ⚙️ Características clave

| Característica           | Explicación                                         |
| ------------------------ | --------------------------------------------------- |
| 📌 Persistencia          | Los datos sobreviven reinicios de EC2               |
| 🔄 Snapshots             | Puedes hacer **copias puntuales** del volumen en S3 |
| 🚀 Performance escalable | `gp3` permite separar IOPS, throughput y tamaño     |
| 🔄 Resize dinámico       | Puedes cambiar tamaño/tipo sin detener la instancia |

---

## 🤝 **Multi-Attach en EBS**

---

### ✅ ¿Qué es?

- Permite **adjuntar un volumen EBS `io1` o `io2` a múltiples instancias EC2** en la misma **zona de disponibilidad (AZ)**.
- Solo compatible con instancias **Nitro** y volúmenes `io1/io2` con IOPS ≥ 500.

---

### 🔧 Consideraciones

| Atributo                               | Valor                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------ |
| Mismo volumen, múltiples instancias    | ✅ Sí                                                                          |
| Solo lectura o lectura/escritura       | ✅ Lectura/escritura **con coordinación** del lado del sistema operativo o app |
| Soporte nativo de sistemas compartidos | ❌ No (usa clústeres como Oracle RAC, Lustre, etc.)                            |
| Zona de disponibilidad                 | ❗ Todas las instancias deben estar en la **misma AZ**                         |

---

### ⚠️ Riesgos si no se sincroniza bien:

- Corrupción de datos si múltiples instancias escriben sin bloqueo.
- Requiere uso de **sistemas de archivos distribuidos o con locking**.

---

### 📦 Ejemplo:

> Volumen `vol-0123` con `io2`, montado en instancias `EC2-A` y `EC2-B` que corren Oracle RAC. Se usa Multi-Attach para alta disponibilidad y failover automático.

---

## 🔐 **Cifrado de EBS**

---

### ✅ ¿Qué es?

El cifrado de EBS garantiza que:

- **Datos en reposo, en tránsito y los snapshots** están cifrados automáticamente.
- Usa claves gestionadas por AWS (KMS) o personalizadas.

---

### 🔒 Tipos de claves

| Tipo                       | Descripción                                                  |
| -------------------------- | ------------------------------------------------------------ |
| **AWS-managed (default)**  | AWS maneja automáticamente la clave                          |
| **Customer-managed (CMK)** | Tú creas y controlas la clave KMS (rotación, permisos, logs) |

---

### 💡 ¿Qué se cifra?

- Datos en disco
- Snapshots
- Réplicas creadas desde snapshots
- Datos transferidos entre la instancia y EBS

---

### 📌 Reglas importantes

| Reglas                                                | Detalles                                                       |
| ----------------------------------------------------- | -------------------------------------------------------------- |
| Puedes lanzar instancias desde volúmenes cifrados     | ✅ Sí                                                          |
| Puedes copiar un snapshot y cifrarlo en el proceso    | ✅ Sí                                                          |
| Puedes **cambiar el cifrado** de un volumen existente | ✅ Solo **creando un snapshot** y volviendo a crear el volumen |
| Cifrado es transparente para el sistema operativo     | ✅ Sí                                                          |

---

## 🧠 Tips para el examen SAA-C03

- **gp3** permite separar rendimiento de tamaño → rentable para cargas exigentes.
- **Multi-Attach** solo con `io1/io2` y coordinación adecuada.
- **Cifrado de EBS no impacta el rendimiento**, y puedes usar tus propias CMKs.

¡Perfecto! Aquí tienes una guía completa sobre **Amazon EFS** y su comparativa con **Amazon EBS**, ideal tanto para el examen **AWS Certified Solutions Architect – Associate (SAA-C03)** como para diseñar arquitecturas efectivas en producción.

---

## 📁 **Amazon EFS (Elastic File System)**

---

### ✅ ¿Qué es?

**Amazon EFS** es un sistema de archivos compartido, totalmente administrado, que puede montarse **simultáneamente** en múltiples instancias EC2 (incluso en diferentes AZs). Ofrece almacenamiento **NFS (Network File System)** escalable y elástico.

---

### 🔧 Características principales

| Característica                    | Detalle                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------- |
| 📂 Sistema de archivos compartido | Múltiples instancias EC2 pueden montar el mismo sistema EFS al mismo tiempo.      |
| 📏 Escala automática              | El tamaño crece o se reduce automáticamente a medida que agregas/quitas archivos. |
| 📶 Protocolo                      | Usa NFSv4.1 o NFSv4.2                                                             |
| 🌍 Multi-AZ                       | Accesible desde múltiples Zonas de Disponibilidad por defecto.                    |
| 🔐 Cifrado                        | Soporta cifrado en reposo y en tránsito (TLS) con KMS                             |
| 🕒 Durabilidad                    | Alta durabilidad (replicado en múltiples AZs)                                     |
| 💸 Modelo de pago                 | Pago por GB utilizado al mes                                                      |
| 🚀 Performance                    | Dos modos: **Bursting (general)** y **Provisioned Throughput**                    |

---

## 🧠 Casos de uso típicos de EFS

- Aplicaciones web multi-AZ que requieren almacenamiento compartido.
- Contenedores (Fargate + EFS).
- Ambientes de desarrollo o home directories.
- Aplicaciones legacy que requieren NFS.

---

## 🔄 Comparativa: **EFS vs EBS**

| Característica         | **EBS (Elastic Block Store)**                            | **EFS (Elastic File System)**                             |
| ---------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| 🔗 Tipo                | Almacenamiento en bloque                                 | Almacenamiento en archivos                                |
| 🧍 Acceso              | Una sola instancia EC2 (excepto Multi-Attach)            | Múltiples instancias EC2 al mismo tiempo                  |
| 🌐 Multi-AZ            | ❌ No (solo dentro de la misma AZ)                       | ✅ Sí (diseñado para eso)                                 |
| 📏 Escalabilidad       | Debes modificar tamaño/tipo manualmente                  | Escala automáticamente                                    |
| 📂 Sistema de archivos | Lo decides tú (ext4, xfs, etc.)                          | NFS v4.1/v4.2                                             |
| 🔒 Cifrado             | En reposo (KMS), opcional                                | En reposo y en tránsito                                   |
| 💵 Cobro               | Por volumen aprovisionado (GB + IOPS)                    | Por uso real (GB utilizados)                              |
| 🧠 Casos de uso        | Bases de datos, boot volumes, apps de una sola instancia | Apps compartidas, microservicios, contenedores, home dirs |

---

### 📌 Reglas clave para el examen

- ❗ Si te preguntan por **almacenamiento compartido entre varias instancias**, la respuesta suele ser **EFS**.
- ❗ Si necesitas un sistema de archivos compartido entre **contenedores (Fargate, ECS)** → EFS.
- ❗ Si necesitas alto rendimiento de IOPS, discos persistentes, y almacenamiento por bloque → EBS (gp3, io2, etc.).

---

## 🔧 ¿Cómo se monta EFS?

Puedes montar un EFS desde una instancia EC2 (Linux) así:

```bash
sudo yum install -y amazon-efs-utils
sudo mkdir /mnt/efs
sudo mount -t efs fs-12345678:/ /mnt/efs
```

También puedes usarlo desde Fargate/ECS/EKS con configuraciones en YAML o tareas.

---

## 🧪 Bonus: Comparativa visual rápida

| Factor        | EBS                                  | EFS                                  |
| ------------- | ------------------------------------ | ------------------------------------ |
| Acceso        | 1 EC2 (o Multi-Attach limitado)      | Muchas EC2 (incluso en distintas AZ) |
| Escala        | Manual                               | Automático                           |
| Persistencia  | ✅                                   | ✅                                   |
| Tipo de datos | Bloques                              | Archivos (NFS)                       |
| Casos de uso  | Bases de datos, SO, apps monolíticas | Web apps compartidas, contenedores   |

¡Claro! Aquí tienes apuntes sobre las **clases de rendimiento y almacenamiento de Amazon EFS**, un tema frecuente en la certificación **AWS SAA-C03** y esencial para elegir la mejor configuración para tus cargas.

---

## ⚙️ **Clases de rendimiento y almacenamiento en Amazon EFS**

---

## 🧠 ¿Por qué importa?

Amazon EFS ofrece **opciones de rendimiento y almacenamiento** que puedes combinar para **optimizar costos o rendimiento**, según tu caso de uso.

---

## 🏃‍♂️ **Clases de rendimiento**

Estas definen **cómo se comporta** el sistema de archivos en cuanto a **latencia y throughput**.

### 1. **General Purpose (por defecto)**

| Característica | Valor                                                  |
| -------------- | ------------------------------------------------------ |
| Latencia       | Baja, en milisegundos                                  |
| Rendimiento    | Ideal para acceso frecuente                            |
| Casos de uso   | Web apps, microservicios, home directories, desarrollo |
| Notas          | Ideal para la mayoría de cargas                        |

---

### 2. **Max I/O**

| Característica | Valor                                                    |
| -------------- | -------------------------------------------------------- |
| Latencia       | Más alta y variable                                      |
| Rendimiento    | Escala a miles de instancias concurrentes                |
| Casos de uso   | Big data, machine learning, cargas de análisis intensivo |
| Notas          | Úsalo solo si General Purpose no es suficiente           |

📌 **Nota:** Solo puedes definir el modo de rendimiento al crear el sistema de archivos y **no se puede cambiar después**.

---

## 💾 **Clases de almacenamiento**

Estas definen **dónde y cómo** se almacenan físicamente los datos, afectando costo y disponibilidad.

### 1. **Standard (EFS Standard)**

| Característica | Valor                                            |
| -------------- | ------------------------------------------------ |
| Acceso         | Frecuente                                        |
| Redundancia    | Multi-AZ                                         |
| Durabilidad    | Alta                                             |
| Costo          | Más alto                                         |
| Casos de uso   | Datos activos, apps web, directorios compartidos |

---

### 2. **Infrequent Access (EFS-IA)**

| Característica | Valor                                       |
| -------------- | ------------------------------------------- |
| Acceso         | Poco frecuente                              |
| Redundancia    | Multi-AZ                                    |
| Durabilidad    | Alta                                        |
| Costo          | Más bajo (hasta 92% menos)                  |
| Casos de uso   | Backups, archivos antiguos, logs fríos      |
| Penalización   | Costo por acceso (lectura/escritura) por MB |

---

## 🔁 **Transición entre clases de almacenamiento**

Si habilitas **EFS Lifecycle Management**, los archivos que no se acceden por un tiempo (ej. 30 días) se **mueven automáticamente a EFS-IA**.

Puedes configurar los tiempos de transición: 7, 14, 30, 60, o 90 días.

---

## 📦 Combinaciones posibles

| Rendimiento                | Almacenamiento           | ¿Se puede combinar? |
| -------------------------- | ------------------------ | ------------------- |
| General Purpose + Standard | ✅ Sí (por defecto)      |                     |
| General Purpose + IA       | ✅ Sí con Lifecycle Mgmt |                     |
| Max I/O + Standard         | ✅ Sí                    |                     |
| Max I/O + IA               | ✅ Sí con Lifecycle Mgmt |                     |

---

## 🧪 Ejemplo práctico

> Tienes una aplicación de gestión documental con acceso frecuente al último año de archivos y acceso esporádico a archivos antiguos.
> ✅ Usa **EFS Standard** + **EFS-IA** con lifecycle de 30 días.

---

## 🧠 Resumen para el examen

| Clase           | Optimiza para            | Ideal para    | ¿Configuración?    |
| --------------- | ------------------------ | ------------- | ------------------ |
| General Purpose | Latencia baja            | Web apps      | Por defecto        |
| Max I/O         | Alta concurrencia        | Big Data / ML | Manual             |
| EFS Standard    | Acceso frecuente         | Apps activas  | Siempre disponible |
| EFS-IA          | Ahorro en archivos fríos | Backups, logs | Requiere lifecycle |

## 🧠 **Metadatos de Instancia EC2 en AWS**

---

### ✅ ¿Qué son?

Los **metadatos de instancia** son **información sobre la propia instancia EC2**, accesible desde **dentro** de la instancia, sin requerir credenciales o un rol IAM.

Permiten que la instancia “sepa cosas de sí misma”.

---

### 🌐 **URL del servicio de metadatos**

```bash
http://169.254.169.254/latest/meta-data/
```

Este **endpoint interno** solo está disponible **desde dentro de la instancia EC2**.

> ❗ No se puede acceder desde fuera, ni desde Internet.

---

## 📋 **Ejemplos de metadatos disponibles**

| Información                 | Ruta de metadatos                               |
| --------------------------- | ----------------------------------------------- |
| ID de instancia             | `/latest/meta-data/instance-id`                 |
| Tipo de instancia           | `/latest/meta-data/instance-type`               |
| Zona de disponibilidad      | `/latest/meta-data/placement/availability-zone` |
| Nombre del rol IAM asignado | `/latest/meta-data/iam/security-credentials/`   |
| Dirección IP privada        | `/latest/meta-data/local-ipv4`                  |
| Nombre AMI                  | `/latest/meta-data/ami-id`                      |
| Hostname                    | `/latest/meta-data/hostname`                    |

---

### 🛡️ ¿Se necesita IAM para acceder a metadatos?

❌ **No**. Acceder a metadatos **no requiere IAM**.
✅ Pero puedes **consultar el nombre del rol IAM asociado** a la instancia desde los metadatos.

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
# Devuelve el nombre del rol IAM
```

Y luego puedes hacer:

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/NombreDelRol
```

Para ver el **access key, secret key y token temporal**.

---

### 🔐 Riesgo de seguridad (¡clave en el examen!)

El acceso a metadatos puede representar un **riesgo si una app en la instancia es vulnerable** (ej. SSRF), ya que un atacante podría robar los **credenciales temporales del rol IAM**.

📌 Por eso AWS introdujo **IMDSv2 (Instance Metadata Service v2)**.

---

## 🛡️ IMDSv2 (versión segura)

- **Usa tokens** para acceder a los metadatos.
- Requiere que el cliente primero haga una solicitud `PUT` para obtener un token.

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

curl -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/instance-id
```

> 🎯 Puedes **forzar el uso de IMDSv2** cuando creas la instancia para mejorar la seguridad.

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Puede una instancia EC2 saber su propia zona de disponibilidad sin usar IAM?_
  ✅ Sí, usando metadatos.

- ❓ _¿Puedes conocer el nombre del rol IAM asignado a una instancia desde dentro de ella?_
  ✅ Sí, vía metadatos.

- ❓ _¿Por qué es importante IMDSv2?_
  ✅ Previene ataques como SSRF que intentan robar tokens IAM temporales.

---

## 🧪 Ejemplo práctico

Tu script de bootstrap puede usar metadatos para:

```bash
#!/bin/bash
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)

echo "Esta instancia $INSTANCE_ID está en $AZ"
```
