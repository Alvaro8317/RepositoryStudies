# Discusiones de arquitecturas serverless

## Arquitectura serverless para una aplicación móvil con autenticación, S3 y DynamoDB

Esta arquitectura está diseñada para aplicaciones móviles que requieren autenticación, acceso seguro a objetos S3 por usuario, almacenamiento de datos (como to-dos), y rendimiento de lectura alto.

---

### Componentes de la arquitectura

#### 1. **Cliente móvil**

- Aplicación nativa (iOS/Android) o React Native
- Interactúa vía **HTTPS** con una **API REST** expuesta por **Amazon API Gateway**
- Se autentica con **Amazon Cognito**

---

#### 2. **Amazon Cognito**

- Servicio gestionado de autenticación de usuarios
- Proporciona:

  - **User Pools**: manejo de usuarios (registro, login, MFA, etc.)
  - **Identity Pools**: otorga **credenciales temporales IAM** para acceder a servicios como S3 o DynamoDB

**Ventajas**:

- Escalabilidad automática
- No es necesario implementar login en backend
- Compatible con OAuth2, OpenID Connect, SAML

---

#### 3. **Amazon API Gateway**

- Expone la API REST a los clientes móviles
- Protegido con autenticación vía Cognito (JWT desde el User Pool)
- **Opcional**: usa **caché en API Gateway** para respuestas GET frecuentes

**Ejemplo de endpoint**:

```http
GET /todos             → lectura de todos los ítems
POST /todos            → agregar un ítem
PUT /todos/{id}        → actualizar un ítem
```

---

#### 4. **AWS Lambda**

- Procesa la lógica de negocio (validación, escritura/lectura en DynamoDB)
- Backend completamente serverless
- Solo se invoca si no hay una respuesta caché en API Gateway

---

#### 5. **Amazon DynamoDB**

- Base de datos NoSQL completamente gestionada
- Ideal para el patrón to-do (clave-partición por usuario)
- **Escala automáticamente** (on-demand o provisioned)
- **Alto rendimiento de lectura y escritura**

---

#### 6. **Amazon DAX (DynamoDB Accelerator)**

- Caché en memoria para DynamoDB
- Mejora latencia de lectura hasta microsegundos
- Ideal cuando:

  - La app realiza muchas **lecturas repetidas**
  - Se requiere **respuesta inmediata** (como en listas de to-dos)

---

#### 7. **Amazon S3 (con carpetas por usuario)**

- Cada usuario puede leer/escribir objetos en su propio directorio (`/user-id/archivo.jpg`)
- Se utiliza **Cognito Identity Pool** para otorgar **credenciales temporales IAM**
- Acceso granular con políticas por usuario:

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::mi-bucket/${cognito-identity.amazonaws.com:sub}/*"
}
```

---

### Flujo de interacción

1. Usuario se registra o inicia sesión vía **Cognito User Pool**
2. Recibe un **JWT** (para API Gateway) y **credenciales temporales IAM** (vía Identity Pool)
3. Puede:

   - Invocar la API (API Gateway → Lambda → DynamoDB)
   - Leer directamente desde caché de **API Gateway** o **DAX**
   - Subir o leer archivos desde su carpeta en S3 (mediante SDK directamente)

---

### Ventajas de esta arquitectura

| Necesidad                          | Solución                                    |
| ---------------------------------- | ------------------------------------------- |
| Escalado automático                | Lambda, API Gateway, DynamoDB, Cognito, S3  |
| Autenticación y autorización       | Cognito User Pool + Identity Pool           |
| Acceso controlado a S3 por usuario | IAM + políticas dinámicas con `cognito:sub` |
| Bajo mantenimiento                 | 100% serverless                             |
| Rendimiento en lectura             | API Gateway caching + DynamoDB + DAX        |

---

### Representación general

```
[Mobile App]
   │
   ├── Auth (Cognito)
   │     ├─ User Pool (login/signup → JWT)
   │     └─ Identity Pool (→ IAM temp credentials)
   │
   ├── API Call (→ API Gateway)
   │     ├─ Cache (GET /todos) [opcional]
   │     └─ Lambda → DynamoDB (DAX para lecturas rápidas)
   │
   └── S3 SDK Call
         └─ S3 Bucket (con acceso restringido por usuario)
```

---

Esta arquitectura es altamente escalable, segura y optimizada para aplicaciones móviles modernas que requieren acceso autenticado, rendimiento rápido y manejo de archivos por usuario.

## Arquitectura de microservicios distribuida en AWS con patrones mixtos

Esta arquitectura representa una aplicación basada en **microservicios desacoplados**, donde cada servicio puede usar diferentes tecnologías según sus necesidades de cómputo, almacenamiento, caché o escalado.

---

### Visión general de la arquitectura

```text
      [Usuarios]
          │
       [Route 53]
          │
     ┌────┼──────┬────────┐
     │    │      │        │
     ▼    ▼      ▼        ▼
 [ALB] [ALB]   [API GW]  [ALB]
   │     │        │        │
[ECS] [ECS]    [Lambda]  [ECS]
  │     │         │        │
[DDB] [RDS]   [ElastiCache]│
                ▲          │
               └───────────┘
                Comunicación entre servicios
```

---

### Microservicio 1: ECS + ALB + DynamoDB

- **Route 53** proporciona el DNS para direccionar hacia el **ALB**
- **ALB (Application Load Balancer)** enruta peticiones al servicio desplegado en **ECS (Fargate o EC2)**
- Utiliza **DynamoDB** como base de datos NoSQL (escalado automático, baja latencia)
- Comunicación con otros micros mediante HTTP interno (o VPC PrivateLink)

**Patrón predominante**: **síncrono** (API REST)

---

### Microservicio 2: API Gateway + Lambda + ElastiCache

- API pública expuesta con **API Gateway**
- Procesamiento backend con **Lambda**, totalmente serverless
- Utiliza **Amazon ElastiCache (Redis o Memcached)** como caché para mejorar latencia en datos consultados frecuentemente
- Ideal para datos efímeros, sesiones, autenticación rápida, etc.

**Patrón predominante**: **serverless + síncrono**

---

### Microservicio 3: ECS + ALB + Auto Scaling Group + RDS

- Desplegado en **ECS con EC2** dentro de un **Auto Scaling Group (ASG)**
- Escalado controlado por métrica o demanda
- Base de datos relacional en **Amazon RDS** (MySQL, PostgreSQL, Aurora)
- ALB enruta el tráfico, permite observabilidad y control del tráfico por path

**Patrón predominante**: tradicional/estado transaccional con **RDBMS**

---

### Comunicación entre microservicios

- **VPC privada compartida** o peering entre subredes internas
- Se pueden comunicar vía:

  - HTTP interno sobre **ALB**
  - **API Gateway con autenticación**
  - **Mensajería asincrónica** con **SNS, SQS o Kinesis**
  - **EventBridge** para desacoplar eventos

---

## Patrones de diseño en microservicios

| Patrón                         | Descripción                                                             |
| ------------------------------ | ----------------------------------------------------------------------- |
| **Síncrono**                   | Comunicación directa vía HTTP/API REST (ALB o API Gateway)              |
| **Asíncrono**                  | Uso de colas, streams, pub/sub (SQS, SNS, Kinesis, S3 Triggers, Lambda) |
| **Command Query Split (CQRS)** | Lecturas por caché/stream, escrituras por API                           |
| **Event-Driven**               | Servicios reaccionan a eventos de otros (via SNS/SQS/EventBridge)       |

---

## Desafíos comunes en arquitecturas de microservicios

| Desafío                                        | Descripción                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| **Sobrecarga de infraestructura**              | Repetir plantillas de despliegue, balanceo, monitoreo, permisos, etc.      |
| **Densidad ineficiente en servidores ECS EC2** | Bajo aprovechamiento de recursos por contenedor                            |
| **Gestión de múltiples versiones**             | Complicado coordinar APIs v1, v2... sin romper compatibilidad              |
| **Cliente acoplado a muchos endpoints**        | SDKs de cliente pesados, múltiples dominios y control de errores dispersos |

---

### Cómo mitigar estos desafíos

- **API Gateway + Lambda**:

  - Escalado automático y pago por uso
  - Reduce infraestructura duplicada

- **Clonación fácil de APIs**:

  - Se pueden versionar y reproducir entornos rápidamente
  - Integración con Swagger/OpenAPI permite generar SDKs automáticamente para iOS, Android, JavaScript, etc.

- **Uso de Step Functions o EventBridge**:

  - Orquestación sin código para flujos complejos

- **Fargate**:

  - Evita problemas de densidad subutilizada en instancias EC2

- **Centralización de logs con CloudWatch Logs y X-Ray**

---

## Conclusión

Esta arquitectura permite combinar diferentes tecnologías según las necesidades de cada microservicio:

| Microservicio   | Computo         | Base de datos | Escalado         | Patrón   |
| --------------- | --------------- | ------------- | ---------------- | -------- |
| Microservicio 1 | ECS + ALB       | DynamoDB      | Fargate/EC2      | Síncrono |
| Microservicio 2 | API GW + Lambda | ElastiCache   | Serverless       | Síncrono |
| Microservicio 3 | ECS + ALB + ASG | RDS           | Auto Scaling EC2 | Síncrono |

Al usar una combinación de patrones síncronos y asíncronos, con opciones serverless cuando sea conveniente, se logra una arquitectura **resiliente, escalable y modular**.

## Optimización de descargas masivas de actualizaciones de software con Amazon CloudFront

Cuando tienes una aplicación que distribuye archivos de actualización desde instancias **EC2** y, al publicarse una nueva versión, se generan **picos masivos de tráfico**, el costo de transferencia de datos y el uso de CPU pueden aumentar drásticamente.

---

### Escenario actual

- Las actualizaciones se sirven desde **instancias EC2**
- El tráfico es bajo la mayor parte del tiempo, pero **se dispara en lanzamientos**
- La arquitectura ya tiene un **Application Load Balancer (ALB)** que enruta a las EC2
- No se desea **modificar la aplicación** existente
- El objetivo es **optimizar costos de red y CPU** sin cambiar la lógica de backend

---

### Solución recomendada: usar **Amazon CloudFront**

**CloudFront** es una red de distribución de contenido (CDN) que **cachéa contenido estático** en ubicaciones cercanas al usuario (Edge Locations), reduciendo:

- Latencia para descargas
- Carga sobre las instancias EC2
- Costos de transferencia de datos salientes

---

### Ventajas de esta solución

| Beneficio                        | Descripción                                                                |
| -------------------------------- | -------------------------------------------------------------------------- |
| **Sin cambios en la app**        | CloudFront actúa como proxy entre el cliente y el ALB                      |
| **Caché de contenido estático**  | Los archivos de actualización (ZIP, EXE, etc.) se cachean por distribución |
| **Menor uso de CPU en EC2**      | La mayoría de las solicitudes nunca llegan a la instancia                  |
| **Reducción de costos**          | CloudFront tiene tarifas más bajas por GB transferido que EC2/ALB directo  |
| **Mejor experiencia de usuario** | Descargas más rápidas, geográficamente optimizadas                         |

---

### Implementación mínima

1. **Crear una distribución CloudFront**

   - **Origin**: el **ALB** ya existente
   - Habilitar **caché** para rutas como `/updates/*` o `/downloads/*`

2. **Configurar caché por encabezado (opcional)**

   - Si los archivos tienen versión en la URL (ej. `/v1.2.3/setup.exe`), es ideal
   - Si no, puedes usar encabezados o query strings como claves de caché

3. **Actualizar el cliente para que descargue desde CloudFront**

   - Ejemplo: `https://d123abcxyz.cloudfront.net/updates/v1.2.3.zip`

4. **Controlar TTL (time-to-live)**

   - Puedes configurar la duración del caché para actualizaciones antiguas y recientes

---

### Consideraciones

| Punto                                  | Detalle                                                              |
| -------------------------------------- | -------------------------------------------------------------------- |
| **No se necesita Lambda**              | La aplicación no cambia; solo se optimiza la entrega                 |
| **No es necesario escalar más EC2**    | La mayoría de peticiones no llegan al backend                        |
| **ASG puede mantenerse pequeño**       | Ahorra costos en instancias sin perder rendimiento                   |
| **Almacenamiento puede seguir en EC2** | Aunque migrarlo a S3 + CloudFront sería aún más eficiente (a futuro) |

---

### Alternativa futura: migrar los archivos a S3

Aunque no es necesario para esta solución, si en el futuro puedes mover los archivos a **Amazon S3**, el flujo se simplifica aún más:

```text
[Client] → [CloudFront] → [S3 bucket with static files]
```

Esto elimina el uso de ALB y EC2 para archivos estáticos, y reduce aún más los costos operativos.

---

### Resumen

| Elemento               | Antes (solo EC2 + ALB)        | Después (EC2 + ALB + CloudFront)        |
| ---------------------- | ----------------------------- | --------------------------------------- |
| Latencia de descarga   | Alta en regiones alejadas     | Baja, distribuida por Edge Locations    |
| Costo de transferencia | Alto (desde EC2 directamente) | Reducido (CloudFront más barato por GB) |
| Uso de CPU en EC2      | Alto en picos                 | Bajo, gracias a caché                   |
| Escalado requerido     | Manual o limitado             | Mucho menor necesidad de escalar        |
| Cambios en la app      | Ninguno                       | Ninguno                                 |
