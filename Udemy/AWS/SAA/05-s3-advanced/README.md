# S3 avanzado

---

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

### 🧠 Ejemplo típico

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

### 📘 Sintaxis común en consola

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

## 📋 Resumen de s3 analytics

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
| **Cuándo usarlo**            | - Compartir grandes datasets (logs, imágenes satelitales, genomics…) sin cargar al dueño.- Repositorios públicos de investigación donde cada equipo cubre su propio ancho de banda.                                             |
| **Requisitos**               | 🔐 El solicitante **debe autenticarse** con una cuenta AWS (no funciona para acceso anónimo).🔑 La **política**/ACL debe autorizar la acción solicitada.🌐 Aplica tanto a Internet como a VPC Endpoints.                        |
| **Quién paga qué**           | Propietario ⇒ _GB-mes de almacenamiento_.Solicitante ⇒ _Requests_, **Data Transfer OUT**, **Data Transfer IN** (si aplica).                                                                                                     |
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
