# ELASTICACHE

## ⚡️ **Amazon ElastiCache – Seguridad**

---

Amazon ElastiCache ofrece dos motores:

- **Redis**
- **Memcached**

Ambos son soluciones de **caché en memoria** de alto rendimiento, pero tienen diferencias clave en **seguridad**.

---

## 🔐 **Seguridad general en ElastiCache**

| Nivel                                       | ¿Soportado? | Descripción                                                                                   |
| ------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------- |
| 🔐 IAM **para conexión a la caché**         | ❌ No       | IAM **NO** controla el acceso al nodo de caché                                                |
| 🔐 IAM **para gestionar ElastiCache (API)** | ✅ Sí       | Controla quién puede crear, modificar o eliminar clústeres, pero **no regula acceso a datos** |
| 🔒 **Acceso controlado por VPC**            | ✅ Sí       | Solo accesible desde instancias dentro de la VPC y grupos de seguridad asignados              |

---

## 🔑 **Autenticación en ElastiCache**

### 🔹 Para Redis

| Mecanismo             | Soportado  | Detalles                                                                                          |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| `AUTH`                | ✅ Sí      | Permite establecer una **contraseña única** para acceso                                           |
| IAM                   | ❌ No      | No puedes usar tokens de IAM para acceder a Redis                                                 |
| SSL/TLS (en tránsito) | ✅ Sí      | Puedes cifrar la comunicación cliente ↔ Redis                                                     |
| Redis 6.x ACLs        | ✅ Parcial | Puedes configurar múltiples usuarios ACL con distintas reglas (en modo Redis Cluster o Redis 6/7) |

📌 Redis + TLS + AUTH = **acceso seguro con cifrado y autenticación básica**

---

### 🔹 Para Memcached

| Mecanismo | Soportado         | Detalles                                                                                               |
| --------- | ----------------- | ------------------------------------------------------------------------------------------------------ |
| `SASL`    | ✅ Sí             | Soporta **autenticación avanzada basada en usuario y contraseña**, más sofisticado que `AUTH` de Redis |
| SSL/TLS   | ❌ No nativamente | Memcached no cifra datos en tránsito en ElastiCache                                                    |
| IAM       | ❌ No             | Igual que Redis, no aplica para conexiones                                                             |

📌 Para seguridad con Memcached debes controlar el acceso por **red/VPC/grupo de seguridad** y usar **SASL** si necesitas autenticación.

---

## 🛡️ Acceso por red: fundamental

| Mecanismo                           | Descripción                                                            |
| ----------------------------------- | ---------------------------------------------------------------------- |
| **VPC/Subredes privadas**           | El clúster ElastiCache se lanza dentro de una VPC privada              |
| **Grupos de seguridad**             | Solo permite tráfico desde direcciones IP, instancias o SG específicos |
| **Sin acceso público (por diseño)** | No puedes asignarle una IP pública a ElastiCache                       |

---

## 🚫 ¿Qué no puedes hacer?

| Acción                                            | ¿Permitida?                                                   |
| ------------------------------------------------- | ------------------------------------------------------------- |
| Conectar con ElastiCache desde fuera de la VPC    | ❌ No                                                         |
| Usar SSH al nodo de ElastiCache                   | ❌ No (es servicio administrado)                              |
| Usar políticas IAM para restringir acceso a datos | ❌ No, solo gestionan llamadas API a ElastiCache              |
| Configurar firewall dentro del nodo               | ❌ No, debes usar **grupos de seguridad** y VPC para aislarlo |

---

## 🔐 Resumen comparativo Redis vs Memcached en seguridad

| Función                             | Redis             | Memcached |
| ----------------------------------- | ----------------- | --------- |
| Autenticación básica (`AUTH`)       | ✅ Sí             | ❌ No     |
| Autenticación avanzada (ACL / SASL) | ✅ Redis 6+ (ACL) | ✅ SASL   |
| SSL / TLS en tránsito               | ✅ Sí             | ❌ No     |
| Acceso IAM directo                  | ❌ No             | ❌ No     |
| Gestión por IAM (API)               | ✅ Sí             | ✅ Sí     |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Puedes usar IAM para autenticarte con Redis o Memcached?_
  ❌ No. IAM solo protege llamadas a la **API de ElastiCache**, **no conexiones de datos**.

- ❓ _¿Qué mecanismo permite autenticar el acceso a Redis?_
  ✅ `AUTH` o **ACLs** (Redis 6+)

- ❓ _¿Cómo puedes asegurar Redis contra accesos no deseados?_
  ✅ Usar VPC privada, grupos de seguridad, AUTH y TLS.

- ❓ _¿Memcached en ElastiCache soporta cifrado en tránsito?_
  ❌ No.

¡Excelente! Aquí tienes una guía clara y precisa sobre los **patrones de uso de Amazon ElastiCache**, especialmente **Redis**, que suelen preguntarse en **certificaciones como AWS SAA-C03** y también se aplican en arquitecturas modernas para mejorar el rendimiento y reducir carga en bases de datos.

---

## 📦 **Patrones comunes de uso en ElastiCache (Redis/Memcached)**

---

### 🐢 **1. Lazy Loading (Carga lenta)**

---

### ✅ ¿Qué es?

- Se consulta primero la **caché**.
- Si no hay datos (**cache miss**), se obtiene de la **fuente de datos (ej. RDS)**, se **almacena en caché**, y se devuelve el resultado.

### 🔄 Flujo:

```
App → Redis (cache)
   → si no hay dato → consulta BD → guarda en cache → retorna
```

### 🧠 Ventajas:

- Simple de implementar.
- Se cachea solo lo que realmente se usa.

### ⚠️ Desventajas:

- El primer acceso **es lento**.
- Si el dato se elimina del cache y se vuelve a consultar, se **repite el acceso a la base de datos**.
- Si muchas claves expiran a la vez (**cache stampede**), la BD puede recibir picos de tráfico.

---

### 🖋️ **2. Write-Through / Write-Behind**

---

### 🔹 **Write-Through**

#### ✅ ¿Qué es?

- Los **escritos van primero a la caché**.
- El sistema luego **escribe en la base de datos inmediatamente**.

### 🔄 Flujo:

```
App → escribe en Redis → escribe en BD (sincrónicamente)
```

### 🧠 Ventajas:

- La caché siempre está actualizada.
- Ideal para sistemas que **leen más de lo que escriben**.

### ⚠️ Desventajas:

- Puede ser más lento en escritura (doble paso).
- Mayor latencia en operaciones de escritura.

---

### 🔹 **Write-Behind (Write-Back)**

#### ✅ ¿Qué es?

- Se escribe primero en la **caché**.
- La escritura a la base de datos ocurre de forma **asíncrona** (diferida).

### 🔄 Flujo:

```
App → escribe en Redis (rápido) → Redis actualiza BD después
```

### 🧠 Ventajas:

- Escritura muy rápida desde el punto de vista del usuario.
- Reduce carga en la base de datos.

### ⚠️ Desventajas:

- Riesgo de **pérdida de datos** si Redis falla antes de escribir en la BD.
- Debe manejarse con mucha precaución y consistencia.

📌 **Redis Streams** o colas externas pueden ayudar a gestionar el buffer intermedio para write-behind.

---

### 🧑‍💻 **3. Almacenamiento de sesión (Session Store)**

---

### ✅ ¿Qué es?

Usar ElastiCache como **almacenamiento rápido y compartido de sesiones de usuario**, especialmente útil en arquitecturas **sin estado (stateless)** como microservicios o aplicaciones distribuidas.

### 📦 ¿Qué se guarda?

- ID de sesión
- Token JWT o credenciales temporales
- Configuraciones de usuario
- Historiales temporales

### 🧠 Ventajas:

- Lecturas/escrituras muy rápidas.
- Las sesiones pueden compartirse entre instancias (ej. en ECS, Lambda, EC2).
- Escalable horizontalmente.

### 🧱 Buenas prácticas:

- Definir **TTL (Time-To-Live)** para que las sesiones expiren automáticamente.
- Usar claves como `session:{user_id}` para organización.
- Encriptar datos sensibles si es necesario.

---

## 🧠 Comparativa rápida

| Patrón            | Lectura                          | Escritura             | Persistencia requerida | Riesgo           |
| ----------------- | -------------------------------- | --------------------- | ---------------------- | ---------------- |
| **Lazy loading**  | Solo desde BD si es necesario    | No cachea al escribir | ❌                     | Cache miss lento |
| **Write-through** | Cache + escritura inmediata a BD | ✅                    | ✅ Alta                | + latencia       |
| **Write-behind**  | Cache primero, BD después        | ✅ diferido           | ❗ Debe diseñarse bien | Pérdida si falla |
| **Session store** | Rápido y temporal                | ✅                    | No necesaria en disco  | Expiración       |

---

## 🧠 Tips para el examen (SAA-C03)

- ❓ _¿Qué patrón cachea solo cuando es necesario y puede causar un "cache miss"?_
  ✅ **Lazy loading**

- ❓ _¿Qué patrón mejora la escritura, pero tiene riesgo de pérdida si el sistema falla antes de persistir?_
  ✅ **Write-behind**

- ❓ _¿Qué patrón es ideal para compartir información temporal de usuarios en apps web?_
  ✅ **Session store**

## 🕹️ **Caso de uso: Tablas de clasificación (leaderboards) en juegos con ElastiCache (Redis)**

---

### 🎯 **Escenario**

Una aplicación de videojuegos en línea necesita mostrar una **tabla de clasificación en tiempo real** con los mejores jugadores ordenados por puntuación. Este ranking:

- Se actualiza constantemente.
- Debe ser **rápido y en tiempo real**.
- Debe mantener **unicidad por jugador** y **orden por puntuación**.
- Debe permitir consultas como:

  - Top 10 jugadores.
  - La posición de un jugador específico.
  - Qué jugadores están justo encima o debajo del usuario.

---

## 🧱 Solución con Redis – Sorted Sets (`ZSET`)

---

### ✅ ¿Qué son los sorted sets?

- Son estructuras de datos en Redis que **almacenan elementos únicos con una puntuación**.
- Redis los mantiene **ordenados automáticamente por esa puntuación**.
- Permiten consultas eficientes por rango, puntuación o posición.

---

### 🧪 Ejemplo real:

```bash
ZADD leaderboard 1500 "player1"
ZADD leaderboard 2000 "player2"
ZADD leaderboard 1700 "player3"
```

Redis guarda los jugadores en orden: `player1 (1500)`, `player3 (1700)`, `player2 (2000)`

---

### 📥 Para obtener el top 3 jugadores:

```bash
ZREVRANGE leaderboard 0 2 WITHSCORES
```

### 🔍 Para obtener la posición de un jugador:

```bash
ZREVRANK leaderboard "player1"
```

---

## 🧠 Ventajas de Redis para este caso

| Ventaja             | Explicación                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
| ⚡ Ultra rápido     | Opera todo **en memoria**, ideal para cargas intensas                        |
| 🔄 Orden automático | No necesitas ordenar manualmente los datos                                   |
| 📶 Escalable        | Redis en ElastiCache escala horizontalmente (sharding) y verticalmente       |
| 🔐 Seguro           | Acceso controlado por VPC, Redis AUTH y TLS                                  |
| ⏱️ TTL opcional     | Puedes hacer que la clasificación se reinicie cada semana (ranking temporal) |

---

## 🧠 Comparación con otros enfoques

| Enfoque                                      | Problemas                                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Base de datos relacional** (ej: RDS MySQL) | Ordenar rankings con `ORDER BY` y `LIMIT` en tablas grandes es **costoso en CPU y lento** |
| **DynamoDB con índices secundarios**         | Puede servir, pero requiere diseño cuidadoso y aún tiene latencia más alta que Redis      |
| **Redis (sorted sets)**                      | Solución ideal para este patrón, **tanto para lectura como escritura en tiempo real**     |

---

## 🧠 Tips para el examen

- ❓ _¿Qué estructura de datos en Redis permite almacenar elementos únicos ordenados por puntuación?_
  ✅ **Sorted Set (ZSET)**

- ❓ _¿Qué servicio de AWS usarías para una tabla de clasificación de alta velocidad con miles de jugadores actualizando scores?_
  ✅ **Amazon ElastiCache (Redis)**

## Puertos importantes

FTP: 21

SSH: 22

SFTP: 22 (igual que SSH)

HTTP: 80

HTTPS: 443

vs Puertos de las bases de datos RDS:

PostgreSQL: 5432

MySQL: 3306

Oracle RDS: 1521

Servidor MSSQL: 1433

MariaDB: 3306 (igual que MySQL)

Aurora: 5432 (si es compatible con PostgreSQL) o 3306 (si es compatible con MySQL)

## Datos importantes

- RDS soporta hasta 5 replicas de lectura
- Aurora soporta hasta 15 replicas de lectura
