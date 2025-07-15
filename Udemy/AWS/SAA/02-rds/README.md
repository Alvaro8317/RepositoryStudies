# RDS

## ⚙️ **Amazon RDS Custom**

---

### ✅ ¿Qué es RDS Custom?

**Amazon RDS Custom** es una variante de Amazon RDS que te permite ejecutar una base de datos **gestionada por AWS**, pero con acceso completo al sistema operativo y al entorno de la base de datos.

> 🔧 **Piensa en ello como una mezcla entre RDS y EC2**:

- Tienes gestión de backups, snapshots y escalabilidad como en RDS.
- Pero puedes acceder al SO, modificar parámetros de bajo nivel y usar agentes externos como si fuera EC2.

---

## 🧠 ¿Por qué usarlo?

### Casos donde RDS estándar no sirve

| Necesitas...                                   | Porque...                                                  |
| ---------------------------------------------- | ---------------------------------------------------------- |
| Acceso al SO                                   | Para instalar software adicional o hacer tuning bajo nivel |
| Parches manuales o agentes externos            | Por requisitos de auditoría, cumplimiento o software       |
| Customización de parámetros del motor          | Que no están permitidos en RDS estándar                    |
| Soporte a apps legacy o certificadas (ej: SAP) | Que requieren configuraciones avanzadas del DBMS o SO      |

---

## 🔐 Motores soportados

| Motor          | Versiones compatibles                   |
| -------------- | --------------------------------------- |
| **Oracle**     | Oracle Database Enterprise Edition (EE) |
| **SQL Server** | SQL Server Enterprise Edition           |

🔸 No disponible para MySQL, PostgreSQL, Aurora, MariaDB.

---

## 🧩 ¿Qué lo diferencia de RDS estándar?

| Característica              | RDS estándar             | RDS Custom                 |
| --------------------------- | ------------------------ | -------------------------- |
| Acceso al sistema operativo | ❌ No                    | ✅ Sí (SSH habilitado)     |
| Instalación de software     | ❌ No                    | ✅ Sí                      |
| Parcheo automatizado        | ✅ Sí                    | ⚠️ Manual                  |
| Uso con apps certificadas   | ⚠️ Limitado              | ✅ Total                   |
| Cambios profundos en DB     | ❌ Limitado              | ✅ Total                   |
| Modelo de responsabilidad   | AWS administra casi todo | Tienes más responsabilidad |

---

## 🚨 Consideraciones importantes

- **Tú eres responsable** de muchas tareas que AWS hace en RDS estándar:

  - Parches
  - Antimalware
  - Configuración del SO
  - Seguridad

- AWS ofrece **una capa de automatización**, pero se **interrumpe si haces cambios no permitidos**.
- **Puede invalidarse el soporte** si modificas configuraciones críticas sin seguir las guías.

---

## 🧱 ¿Cuándo _no_ usar RDS Custom?

| Si...                                       | Entonces...                                |
| ------------------------------------------- | ------------------------------------------ |
| Quieres administración 100% automática      | Usa RDS estándar                           |
| No necesitas modificar el sistema operativo | RDS estándar basta                         |
| Tu carga es compatible con Aurora           | Aurora puede ser más escalable y económico |

---

## 🧪 Ejemplo práctico

> Una empresa necesita migrar una base de datos Oracle con un software de respaldo certificado por SAP que requiere instalación de un agente en el SO.
> ✅ Usan **RDS Custom for Oracle**, instalan el agente, pero aún conservan backups y snapshots automáticos.

---

## 🧠 Tips para el examen

- ❓ _¿Necesitas acceso SSH al sistema operativo para configurar agentes propios?_ → ✅ **RDS Custom**
- ❓ _¿Quieres que AWS maneje parches, seguridad y escalado por ti?_ → ✅ **RDS estándar**
- ❓ _¿Tu carga requiere configuraciones no permitidas en RDS normal?_ → ✅ **RDS Custom**

---

## 🧠 **Aurora – Resumen general**

**Amazon Aurora** es una base de datos relacional **compatible con MySQL y PostgreSQL**, **administrada y optimizada por AWS**, con mejoras en rendimiento, disponibilidad y escalabilidad.

- Hasta 5 veces más rápida que MySQL.
- Alta disponibilidad nativa.
- Separación de **writer** y **readers**.
- Diseñada para cargas modernas y exigentes.

---

## ⚡️ Aurora Serverless

| Versión                  | Detalles                                                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aurora Serverless v1** | Escala automáticamente entre 0 y N unidades (ACUs), pero con **latencia al escalar** y poco control fino.                                             |
| **Aurora Serverless v2** | Escala en **tiempo casi real** (subsegundos), más granular y con mejor integración con autoscaling, IAM, VPC, etc. Recomendado para nuevos proyectos. |

### 🧪 Casos de uso:

- Cargas intermitentes o impredecibles.
- Apps con usuarios variables.
- Ambientes dev/test.

---

## 📈 Escalado automático

Aurora puede escalar automáticamente de dos formas:

| Tipo de escalado                   | Detalle                                                                |
| ---------------------------------- | ---------------------------------------------------------------------- |
| **Escalado horizontal**            | Añadir hasta **15 réplicas de lectura** distribuidas en múltiples AZs. |
| **Escalado vertical (serverless)** | Aumentar o reducir CPU y RAM (ACUs) automáticamente en función de uso. |

---

## 🌐 Endpoints en Aurora

### 1. **Writer Endpoint**

- Se conecta al **nodo principal (writer)**.
- Solo permite operaciones de lectura y escritura.
- **Ejemplo**: `mydb.cluster-ABCDEFGHIJKL.us-east-1.rds.amazonaws.com`

---

### 2. **Reader Endpoint**

- Se conecta a un pool de **réplicas de lectura** automáticamente balanceadas.
- Solo acepta **lectura**. Si haces un `INSERT`, falla.
- **Ejemplo**: `mydb.cluster-ro-ABCDEFGHIJKL.us-east-1.rds.amazonaws.com`

🧠 **Importante**:

- AWS balancea automáticamente entre las réplicas disponibles.
- ¡No garantiza que siempre envíe tráfico a la misma réplica!

---

### 3. **Custom Endpoints**

- Puedes **crear un endpoint personalizado** con un subconjunto de réplicas.
- Útil si quieres controlar qué instancias manejan ciertas cargas.
- Ejemplo: un endpoint para un dashboard pesado que va solo a 1 réplica específica.

🛑 **Problema**: muchos devs dejan de usar el **reader endpoint automático** después de usar custom endpoints, porque pierden el beneficio de **balanceo automático**.

---

### 4. **Endpoint extendido (Cluster endpoint o RDS Proxy)**

- Permite gestionar de forma **más inteligente** conexiones y failover.
- Ejemplo: usar un **proxy endpoint** para gestionar múltiples conexiones persistentes y multiplexarlas.

---

## 🧩 Flota de proxies

### 🔐 ¿Qué es RDS Proxy?

- Servicio administrado que actúa como **intermediario entre tu app y Aurora/RDS**.
- Reutiliza conexiones (pooling), maneja failover, reduce la sobrecarga de conexiones abiertas.

### 🎯 Ventajas:

| Beneficio              | Explicación                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| 🔄 Failover más rápido | Sin necesidad de reabrir conexiones                                |
| 🔌 Pool de conexiones  | Reduce número de conexiones activas al clúster                     |
| 🔒 Seguridad           | Soporte nativo para IAM y Secrets Manager                          |
| 💸 Eficiencia          | Apps con muchas conexiones concurrentes consumen menos recursos DB |

---

## ⚔️ Aurora Multi-Master

### ✅ ¿Qué es?

- Variante de Aurora que **permite múltiples nodos writer activos al mismo tiempo**, todos **aceptan escrituras**.
- Disponible solo para **Aurora MySQL** (a partir de ciertas versiones).
- Útil para **alta disponibilidad y tolerancia a fallos sin pérdida de escrituras**.

### 🧱 Limitaciones y advertencias:

| Punto               | Detalle                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| 🔄 Replicación      | Internamente Aurora sincroniza los writers para evitar conflictos                                |
| 🧠 Complejidad      | Tu aplicación debe estar preparada para manejar **conflictos de escritura**                      |
| 🛑 No es para todos | Aurora Multi-Master solo se recomienda si **realmente necesitas HA sin downtime para escritura** |
| 📦 Uso común        | Sistemas críticos financieros o de manufactura que **no pueden permitirse downtime al escribir** |

---

## 🧠 Tips de examen (SAA-C03)

- ❓ _¿Necesitas una base de datos que escale automáticamente con carga variable?_ → ✅ **Aurora Serverless v2**
- ❓ _¿Quieres separar tráfico de escritura y lectura?_ → ✅ Usa **writer y reader endpoints**
- ❓ _¿Tu app abre miles de conexiones que la DB no puede manejar?_ → ✅ Usa **RDS Proxy**
- ❓ _¿Buscas una DB que siga operando incluso si un writer falla?_ → ✅ Considera **Aurora Multi-Master** (si puedes gestionar la complejidad)

¡Perfecto! Aquí tienes apuntes enfocados en:

1. 🌍 **Amazon Aurora Global Databases**
2. 🤖 **Aurora Machine Learning (ML Integration)**

## 🌍 **Aurora Global Database**

---

### ✅ ¿Qué es?

Una **Aurora Global Database** permite replicar una base de datos Aurora entre **múltiples regiones de AWS**, para lograr:

- **Alta disponibilidad global**
- **Recuperación ante desastres (DR)**
- **Lecturas de baja latencia** desde distintas partes del mundo

---

### 🏗️ Arquitectura básica

| Rol                      | Región                           | Descripción                                            |
| ------------------------ | -------------------------------- | ------------------------------------------------------ |
| **Región primaria**      | `us-east-1` (por ejemplo)        | Región donde se hacen las **escrituras**               |
| **Regiones secundarias** | `eu-west-1`, `ap-southeast-1`... | Solo permiten **lecturas** desde réplicas asincrónicas |

- Cada región secundaria puede tener **hasta 16 réplicas de lectura**.
- Las réplicas están **fuertemente desacopladas** → replicación **asíncrona**, pero muy rápida (\~<1 segundo).

---

### ⚠️ Latencia e impacto

| Acción    | Región primaria        | Región secundaria                                                                                 |
| --------- | ---------------------- | ------------------------------------------------------------------------------------------------- |
| Escritura | ✅ Sí                  | ❌ No (excepto en failover manual)                                                                |
| Lectura   | ✅ Baja latencia local | ✅ Baja latencia local, pero los datos pueden tener **ligera latencia (\~1s)** respecto al writer |
| Failover  | ❌ No automático       | ✅ Puedes promover una región secundaria a **primaria** manualmente                               |

---

### 🧠 Casos de uso:

- Apps globales con usuarios en múltiples continentes.
- Requerimientos de recuperación ante desastres (DR) geográficamente distante.
- Latencia optimizada para lectura desde Europa/Asia/Latam.

---

### 🚨 Recomendaciones

- No usar para cargas con requerimientos de consistencia estricta entre regiones.
- Escribes **solo en la región primaria**.
- En caso de desastre, puedes **promover una región secundaria** a primaria con un solo clic (o API/CLI).

---

## 🧠 **Aurora ML Integration**

---

### ✅ ¿Qué es Aurora ML?

Aurora permite **integrar directamente modelos de Machine Learning** desde **Amazon SageMaker** y **Amazon Comprehend**, sin salir de SQL.

> Es decir, ¡puedes ejecutar inferencias desde una consulta SQL dentro de Aurora!

---

### 🎯 ¿Qué servicios se integran?

| Servicio              | ¿Qué aporta?                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Amazon SageMaker**  | Ejecuta **modelos ML personalizados** creados por ti (ej. regresión, clasificación, etc.)                                  |
| **Amazon Comprehend** | Proporciona capacidades **NLP preentrenadas**, como detección de idioma, análisis de sentimientos, extracción de entidades |

---

### 🔧 ¿Cómo se usa?

Usas funciones SQL integradas:

```sql
-- Con SageMaker
SELECT id,
       product_name,
       aws_sagemaker_infer_sql(input_column, 'endpoint-name') as prediction
FROM sales_data;

-- Con Comprehend
SELECT review,
       aws_comprehend_detect_sentiment(review, 'en') as sentiment
FROM customer_reviews;
```

---

### 🧠 Beneficios

- **No necesitas ETL** ni extraer datos de Aurora.
- Baja latencia → inferencias en tiempo real desde tu base.
- Permite enriquecer dashboards, validaciones, scoring, etc.

---

### ⚠️ Consideraciones

- Solo disponible en **Aurora PostgreSQL y MySQL** en versiones recientes.
- **No entrena modelos**, solo **consume endpoints existentes**.
- Requiere IAM y permisos configurados correctamente.
- Puede generar costos de inferencia por uso de SageMaker o Comprehend.

---

### 🧪 Casos de uso:

| Caso                           | Descripción                                                          |
| ------------------------------ | -------------------------------------------------------------------- |
| Clasificación de transacciones | Enviar valores a SageMaker y obtener predicción de fraude            |
| Análisis de sentimiento        | Usar Comprehend para analizar comentarios de clientes en tiempo real |
| Enriquecimiento de datos       | Enriquecer consultas con predicciones o entidades nombradas          |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Quieres una base de datos Aurora replicada entre regiones para DR y lecturas locales?_
  ✅ **Aurora Global Database**

- ❓ _¿Necesitas consultar un modelo ML directamente desde Aurora sin extraer los datos?_
  ✅ **Aurora ML Integration con SageMaker o Comprehend**

## 🧠 **Copias de seguridad en Amazon RDS**

---

### 🔄 **Backups automáticos**

- **Habilitados por defecto** al lanzar una instancia RDS (puedes desactivarlos, pero no es recomendable).
- Se realiza una copia diaria del volumen y transacciones continuas para restaurar en un punto en el tiempo (**PITR: Point In Time Recovery**).
- Guarda las transacciones cada 5 minutos
- Puedes definir un **período de retención** de backups: **1 a 35 días**.

📌 Importante:

- Necesitas backups automáticos habilitados para poder **restaurar en un punto en el tiempo**.
- **No puedes restaurar sobre la misma instancia**, siempre crea una nueva.

---

### 📸 **Snapshots manuales**

- Son copias **completas del estado de la base de datos en un momento puntual**.
- Se crean de forma explícita por el usuario (CLI, consola o API).
- **No se borran automáticamente** (persisten hasta que los elimines).

🔹 Ideal para:

- Tareas de mantenimiento o migración.
- Guardar estados estables antes de actualizaciones.
- Reducción de costos: puedes **eliminar la instancia y conservar solo el snapshot**.

---

## 💸 **Optimización de costos con snapshots**

> Aunque detengas una instancia RDS, **sigues pagando por el almacenamiento** de los volúmenes EBS y backups.

💡 Estrategia recomendada:

1. Crear un **snapshot manual**.
2. Eliminar la instancia RDS.
3. Restaurar la base de datos **solo cuando se necesite**, usando el snapshot.

```bash
aws rds create-db-snapshot \
  --db-instance-identifier mydb \
  --db-snapshot-identifier mydb-snapshot

# Luego puedes restaurar
aws rds restore-db-instance-from-db-snapshot \
  --db-snapshot-identifier mydb-snapshot \
  --db-instance-identifier restored-db
```

---

## 🌊 **Copias de seguridad en Aurora**

Aurora maneja los backups de forma **ligeramente diferente**, porque su arquitectura es distribuida:

---

### 🔄 Backups automáticos

- Se realizan **de forma continua** a nivel de clúster (no por instancia).
- Están almacenados en **Amazon S3 automáticamente** y **no afectan el rendimiento**.
- Puedes recuperar el clúster Aurora en cualquier punto dentro del período de retención (hasta 35 días).

📌 Nota: **No ocupan espacio en el almacenamiento del clúster Aurora.**

---

### 📸 Snapshots manuales en Aurora

- Igual que en RDS, puedes tomar snapshots manuales del **clúster completo**.
- Puedes restaurar a partir de ellos creando un nuevo clúster Aurora.

```bash
aws rds create-db-cluster-snapshot \
  --db-cluster-identifier my-aurora-cluster \
  --db-cluster-snapshot-identifier my-snapshot

# Restaurar el clúster
aws rds restore-db-cluster-from-snapshot \
  --db-cluster-snapshot-identifier my-snapshot \
  --db-cluster-identifier restored-cluster
```

---

## 🚀 Diferencias clave RDS vs Aurora en backups

| Característica               | **RDS**                                     | **Aurora**                        |
| ---------------------------- | ------------------------------------------- | --------------------------------- |
| Backups automáticos          | Diarios + logs para PITR                    | Continuos y sin impacto           |
| Snapshots manuales           | Por instancia                               | Por clúster                       |
| Almacenamiento de backups    | En S3 (pero ligado al volumen de instancia) | En S3, fuera del volumen          |
| Restauración                 | Crea nueva instancia                        | Crea nuevo clúster                |
| Cobro por instancia detenida | ✅ Sí (almacenamiento)                      | ✅ Sí (volumen clúster + backups) |
| Optimización con snapshot    | ✅ Elimina instancia y conserva snapshot    | ✅ Igual                          |

---

## 🧠 Tips para el examen

- ❓ _¿Puedes restaurar una base de datos RDS directamente sobre la misma instancia?_
  ❌ No. Siempre crea una nueva instancia.

- ❓ _¿Los snapshots manuales se borran con la instancia?_
  ❌ No. Debes eliminarlos explícitamente.

- ❓ _¿Qué pasa si detienes una instancia RDS sin eliminarla?_
  ➕ Dejas de pagar por CPU, pero **sigues pagando por almacenamiento** y backups.

- ❓ _¿Puedes restaurar un clúster Aurora desde snapshot?_
  ✅ Sí, pero crea uno nuevo.

## 🔁 **Restauración en Amazon RDS y Aurora**

---

### ✅ Opciones generales de restauración

| Tipo                                         | RDS                                         | Aurora                                                         |
| -------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------- |
| **Restauración a punto en el tiempo (PITR)** | ✅ Sí (dentro de la retención, máx 35 días) | ✅ Sí (continuo, sin impacto)                                  |
| **Snapshot manual**                          | ✅ Sí (por instancia)                       | ✅ Sí (por clúster)                                            |
| **Snapshot automático**                      | ✅ Sí (diario)                              | ✅ Interno a Aurora (invisible)                                |
| **Exportar snapshot a S3**                   | ✅ Sí (JSON, Parquet)                       | ✅ Sí                                                          |
| **Clonación rápida**                         | ❌ No                                       | ✅ Sí, ver más abajo                                           |
| **Restore desde backup externo**             | Limitado                                    | Soportado con herramientas como Percona (solo en Aurora MySQL) |

---

## 🧰 **Restauración desde Percona XtraBackup**

**Percona XtraBackup** es una herramienta popular en MySQL para realizar **backups consistentes en caliente** sin bloquear escrituras.

### 💡 ¿Qué soporte tiene en AWS?

| Plataforma       | ¿Soporta restauración desde XtraBackup?        | Cómo funciona                                                                                                                    |
| ---------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **RDS**          | ❌ No soportado directamente                   | No tienes acceso al sistema operativo ni a archivos de datos                                                                     |
| **Aurora MySQL** | ✅ **Sí, soportado** desde versiones recientes | Puedes restaurar una base externa con Percona hacia un clúster Aurora usando **MySQL native replication** y archivos restaurados |

---

### 🔄 Flujo general con Aurora + Percona:

1. Tomas un backup con `xtrabackup` en tu entorno local (on-premises o EC2).
2. Restauras los archivos en una instancia EC2 de MySQL.
3. Creas un clúster Aurora vacío.
4. Usas **replicación binlog** o **importación física** para traer los datos a Aurora.

> ⚠️ Requiere **conocimientos avanzados de MySQL**, IAM y VPC bien configurados.

---

## 🧬 **Clonación de bases de datos Aurora**

---

### ✅ ¿Qué es la clonación?

- Aurora permite **clonar un clúster completo**, incluyendo datos, configuraciones y esquemas.
- Utiliza una técnica llamada **copy-on-write**, lo que significa que **no copia físicamente los datos al inicio**.
- Solo se copian los bloques modificados después del clonado.

📌 **Resultado: la clonación es mucho más rápida que restaurar desde un snapshot**, especialmente con grandes volúmenes.

---

### 🔄 Diferencia entre Snapshot y Clon

| Característica | Snapshot + Restore                 | Clonación Aurora                                |
| -------------- | ---------------------------------- | ----------------------------------------------- |
| Tiempo         | Lento (copia total)                | Rápido (instante inicial)                       |
| Costos         | Cobra por almacenamiento duplicado | Solo se cobra cuando se escriben datos          |
| Uso típico     | Backup, retención a largo plazo    | Testing, staging, análisis                      |
| Tipo           | Persistente                        | Temporal/experimental (puedes eliminar después) |

---

### 🧪 Casos de uso

| Caso                                                              | Solución                           |
| ----------------------------------------------------------------- | ---------------------------------- |
| Necesito crear un ambiente de pruebas con datos reales en minutos | ✅ Usa **Aurora clone**            |
| Quiero conservar un punto estable por meses                       | ✅ Usa **snapshot**                |
| Necesito restaurar datos de una BD externa con backup físico      | ✅ Aurora + **Percona XtraBackup** |

---

### 🛠️ Comando de clonación (CLI)

```bash
aws rds clone-db-cluster \
  --source-db-cluster-identifier my-source-cluster \
  --target-db-cluster-identifier my-clone-cluster \
  --region us-east-1
```

---

## 🧠 Tips para el examen

- ❓ _¿Cuál es la forma más rápida de crear una copia de Aurora para pruebas sin duplicar el almacenamiento?_
  ✅ **Clonación**

- ❓ _¿Puedes restaurar una base MySQL en Aurora usando un backup físico (Percona)?_
  ✅ **Sí, pero solo con Aurora MySQL**, requiere trabajo técnico adicional.

- ❓ _¿Puedes restaurar desde Percona en RDS estándar?_
  ❌ **No** (no tienes acceso al sistema operativo).

## 🔐 **Seguridad en RDS y Aurora**

---

### 🧊 **1. Cifrado en reposo con AWS KMS**

#### ✅ ¿Qué es?

El cifrado **en reposo** protege los datos almacenados en:

- Volúmenes de base de datos (EBS)
- Backups automáticos
- Snapshots manuales
- Réplicas

#### 🗝️ Se usa **AWS KMS**:

- Puedes usar **claves administradas por AWS (aws/rds)** o **claves personalizadas (CMK)**.
- Los datos son cifrados con AES-256 automáticamente.

#### 📌 Consideraciones importantes:

| Pregunta                                                        | Respuesta                                                             |
| --------------------------------------------------------------- | --------------------------------------------------------------------- |
| ¿Se puede cifrar una base ya creada sin cifrado?                | ❌ No directamente                                                    |
| ¿Cómo se cifra una base no cifrada?                             | ✅ Crear un snapshot, **copiarlo con cifrado**, y restaurar desde ahí |
| ¿Las réplicas pueden ser cifradas si la base original no lo es? | ❌ No, **la base maestra debe estar cifrada**                         |

---

### 📥 **2. Cifrado en tránsito (en vuelo)**

#### ✅ ¿Qué es?

El cifrado en tránsito asegura la comunicación entre el cliente y RDS/Aurora usando **TLS/SSL**.

#### 🌐 ¿Cómo se habilita?

- Se conecta con TLS usando certificados proporcionados por AWS.
- Las conexiones deben usar el puerto adecuado y especificar el uso de SSL en el driver o cliente.

```bash
mysql --host=mydb.123456789012.us-east-1.rds.amazonaws.com \
      --ssl-ca=AmazonRootCA1.pem \
      --ssl-mode=REQUIRED
```

---

## 🔑 **3. Autenticación con IAM**

#### ✅ ¿Qué es?

Puedes autenticar usuarios de RDS (MySQL, PostgreSQL y Aurora) usando **tokens de IAM**, en vez de nombre de usuario y contraseña.

> Así, no almacenas passwords en tu aplicación.

#### 🔧 ¿Cómo funciona?

- El usuario de IAM recibe un token con duración limitada (15 minutos).
- Se usa ese token como "contraseña" al conectarse a RDS.

```bash
aws rds generate-db-auth-token \
  --hostname mydb.123456789012.us-east-1.rds.amazonaws.com \
  --port 3306 \
  --region us-east-1 \
  --username dbuser
```

#### 🧠 Beneficios:

- Acceso temporal → menos riesgo de filtraciones.
- Integración con políticas IAM → control centralizado.
- Útil para entornos sin secretos persistentes (como Lambda, Fargate).

---

## 🔥 **4. Grupos de seguridad (RDS)**

| Característica                                                | Detalle                                                               |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| RDS usa **grupos de seguridad VPC**                           | Para permitir tráfico entrante por puerto de la base (ej. 3306 MySQL) |
| No hay acceso por **SSH**                                     | No puedes ingresar a la instancia, es gestionada por AWS              |
| Solo puedes controlar acceso por **IP, rango CIDR, otros SG** | Usa esto para definir quién puede conectarse                          |

---

### 🚫 No puedes hacer:

- `ssh` a la instancia
- Instalar software en ella
- Acceder al sistema de archivos (excepto en **RDS Custom**)

---

## 📝 **5. Auditoría y logs**

#### ✅ ¿Cómo hacer auditoría en RDS y Aurora?

Puedes enviar varios tipos de logs a **Amazon CloudWatch Logs**:

| Tipo de log                                                   | ¿Qué incluye?                                       |
| ------------------------------------------------------------- | --------------------------------------------------- |
| **Error logs**                                                | Problemas del motor de base                         |
| **Slow query logs**                                           | Consultas lentas                                    |
| **General logs**                                              | Conexiones y comandos SQL (solo en algunos motores) |
| **Audit logs** (ej: PostgreSQL `pg_audit`, MySQL `audit_log`) | Actividades de usuarios, cambios, acceso a datos    |

#### 🧠 Beneficios:

- Centraliza logs en CloudWatch.
- Permite crear **alarmas, dashboards y consultas de seguridad**.
- Mejora el cumplimiento de normas como **PCI-DSS, HIPAA, etc.**

---

## 🧠 Tips para el examen (y producción)

| Situación                           | Solución                                                              |
| ----------------------------------- | --------------------------------------------------------------------- |
| Cifrar una base RDS no cifrada      | ❌ No se puede directamente → ✅ Snapshot + copia cifrada + restaurar |
| Proteger comunicación con la base   | ✅ TLS/SSL (en tránsito)                                              |
| Controlar acceso sin credenciales   | ✅ Autenticación IAM                                                  |
| Ver actividad sospechosa en base    | ✅ Activar logs y enviarlos a CloudWatch                              |
| Restringir acceso a IPs específicas | ✅ Usar grupos de seguridad de VPC                                    |
