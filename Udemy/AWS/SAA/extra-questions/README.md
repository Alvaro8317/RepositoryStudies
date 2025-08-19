# Preguntas refuerzo nacidas de simuladores

## **AWS Global Accelerator**

* **Qué es**: Servicio de red global que optimiza el enrutamiento hacia tus aplicaciones usando la **red troncal de AWS** en lugar de depender del internet público.
* **Cómo funciona**:

  * Asigna **dos direcciones IP estáticas** (anycast) que actúan como puntos de entrada globales.
  * Cuando un usuario envía tráfico, este entra al **punto de presencia más cercano** (edge location) y viaja por la red privada de AWS hasta tu aplicación.
  * Reduce latencia y mejora disponibilidad.
* **Cuándo usarlo**:

  * Aplicaciones distribuidas globalmente que requieren **baja latencia constante**.
  * Casos típicos: APIs, juegos online, apps financieras.
  * Se usa con ALB, NLB, EC2, Elastic IP, etc.
* **Ventaja clave frente a DNS**: DNS resuelve una vez, pero Global Accelerator ajusta rutas dinámicamente según la salud y cercanía.

---

## **S3 Transfer Acceleration**

* **Qué es**: Característica de S3 que acelera las cargas y descargas usando **edge locations de CloudFront** como puntos de entrada.
* **Cómo funciona**:

  * El cliente sube el archivo a la edge location más cercana.
  * De ahí, el archivo viaja por la **red interna optimizada de AWS** hasta el bucket S3 en su región de destino.
* **Cuándo usarlo**:

  * Cargas de **archivos grandes** a S3 desde ubicaciones geográficamente lejanas a la región del bucket.
  * Casos típicos: vídeos, backups, datasets.
* **Cómo habilitarlo**:

  * En el bucket S3 → Propiedades → Activar **Transfer Acceleration**.
  * Se accede al bucket con la URL especial:

    ```
    https://<bucketname>.s3-accelerate.amazonaws.com
    ```
* **Costo**: Tiene tarifa adicional por GB transferido.
* **Nota**: No acelera transferencias dentro de la misma región; está pensado para distancias largas.

---

Sí, en **Kinesis Data Streams (KDS)** existe algo llamado **Enhanced Fan-Out** (fanout mejorado).

---

## **Qué es Enhanced Fan-Out**

* Es una característica que **aumenta la velocidad de entrega de datos** desde Kinesis Data Streams a los consumidores.
* En el fan-out estándar, **todos los consumidores comparten un mismo throughput de 2 MB/s por shard** y deben hacer *polling* (GetRecords) continuamente.
* Con Enhanced Fan-Out, **cada consumidor obtiene su propio flujo dedicado** de hasta **2 MB/s por shard** **de manera independiente**, usando *push* en vez de *polling*.

---

## **Ventajas**

* **Baja latencia**: suele estar en el rango de 70 ms desde que los datos llegan al stream hasta que se entregan al consumidor.
* **Throughput independiente**: un consumidor no afecta el rendimiento de otro.
* **Menos sobrecarga de polling**: los datos se envían automáticamente usando HTTP/2.

---

## **Costos**

* Se cobra por cada **unidad de throughput de fanout** (2 MB/s por shard por consumidor) y por el volumen de datos entregados.
* Es adicional al costo del stream.

---

## **Cuándo usarlo**

* Cuando tienes **múltiples consumidores** y cada uno necesita leer todos los datos a alta velocidad.
* Procesamiento en **tiempo casi real** (trading, telemetría, streaming de vídeo, etc.).
* Reemplazar arquitecturas complejas que intentan optimizar el polling manual.

---

📌 **Ejemplo**:
Si tienes 3 consumidores leyendo de un shard:

* **Normal**: comparten 2 MB/s → si uno lee mucho, los demás se ralentizan.
* **Enhanced Fan-Out**: cada uno tiene 2 MB/s → total 6 MB/s posibles desde el mismo shard.

---

Aquí tienes la comparación clara para tus apuntes:

---

## **S3 Standard-IA vs S3 One Zone-IA**

| Característica              | **S3 Standard-IA**                                                                                                 | **S3 One Zone-IA**                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Disponibilidad**          | 99.9%                                                                                                              | 99.5%                                                                                                 |
| **Durabilidad**             | 99.999999999% (11 nueves)                                                                                          | 99.999999999% (11 nueves)                                                                             |
| **Ubicación de datos**      | Replicados en **mínimo 3 AZ** dentro de la región                                                                  | **Solo en 1 AZ**                                                                                      |
| **Costo de almacenamiento** | Más caro que One Zone-IA                                                                                           | Más barato que Standard-IA                                                                            |
| **Costo de recuperación**   | Igual en ambos: se paga por GB recuperado y por solicitud                                                          | Igual                                                                                                 |
| **Casos de uso**            | Datos a los que se accede pocas veces pero **críticos** y que requieren alta disponibilidad en caso de fallo de AZ | Datos poco críticos o que se pueden volver a generar fácilmente, **no requieren alta disponibilidad** |
| **Riesgo**                  | Baja probabilidad de pérdida, incluso si una AZ falla                                                              | Si la AZ falla, los datos se pierden                                                                  |
| **Ejemplos de uso**         | Copias de seguridad a largo plazo que igual deben sobrevivir a fallos de AZ                                        | Datos temporales, cachés, copias secundarias que se pueden regenerar                                  |

---

📌 **Resumen rápido**:

* **Standard-IA** = baja frecuencia de acceso + redundancia en múltiples AZ.
* **One Zone-IA** = baja frecuencia de acceso + almacenamiento más barato, pero solo en **una** AZ, con más riesgo.

Sí ✅, **AWS Global Accelerator** soporta **UDP** además de TCP.

---

### 📌 Detalles clave

* **Protocolos soportados:**

  * **TCP**
  * **UDP**
  * También puedes tener aceleradores que soporten **ambos** en listeners distintos o combinados.

* **Cómo funciona con UDP:**
  Global Accelerator crea **endpoints** en las regiones que definas (por ejemplo, NLBs o EC2) y enruta el tráfico UDP desde la ubicación más cercana al usuario hasta tu backend a través de la red global de AWS.
  Esto reduce la latencia y evita problemas de pérdida de paquetes en Internet público.

* **Casos de uso típicos de UDP:**

  * Juegos en tiempo real
  * Streaming en vivo
  * Comunicaciones VoIP
  * DNS personalizado
  * Protocolos como QUIC

---

💡 **En el examen SAA**, si ves algo sobre *"entregar tráfico global de baja latencia usando TCP o UDP"*, la respuesta suele ser **AWS Global Accelerator**, **no CloudFront** (que solo maneja HTTP/HTTPS sobre TCP).

## Apuntes adicionales

Existe AWS Storage Gateway, pero de varios tipos:
- File gateway, buckets s3 como si fueran compartidos como NFS o SMB locales
- Volume Gateway, discos iSCSI locales respaldados en NFS o S3
- Tape Gateway, cintas virtuales que se almacenan en S3

La diferencia entre AWS DataSync y AWS Storage es que DataSync es para migrar y/o sincronizar datos, es decir, movimiento puntual o recurrente, en cambio storage gateway es para exponer almacenamiento AWS en on-premises (Integración continua)

---

En RDS Aurora existen algunos endpoints como cluster endpoints, reader endpoints y custom endpoints, donde cluster son letura y escritura, apuntan al cluster principal, reader endpoints son como un NLB para replicas de lectura y custom endpoints son opcionales, se usan como para instancias más poderosas

---

Amazon firehose soporta como destino S3, OpenSearch, Splunk, Redshift, etc.

---

Se puede usar cfn-signal con una instancia EC2 para indicarle a cloudformation que prosiga con la creación de una pila

---

Los volumenes de Instance store son efímeros, si se quisiera tener persistencia, se requeriría un EBS o algo similar, Instance store es super rapido pero al detener una instancia, se borran los datos, en caso que se reinicie la instancia y se mantenga en el mismo host, se mantendrán los datos.