# Enhanced Fan-Out

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Fan-Out vs. Fan-In

Antes de ver la funcionalidad de Kinesis, dos conceptos generales:

- **Fan-Out**: una **fuente única** (en nuestro caso, un data stream) distribuye sus datos hacia
  **múltiples destinos** (varios consumidores/aplicaciones que necesitan consumir esos datos).
- **Fan-In**: lo contrario — **múltiples fuentes** se agregan/combinan en un **único destino**. Por
  ejemplo, varios sensores de temperatura en distintas habitaciones que envían sus datos a un mismo
  destino para consolidarlos.

## El problema del consumidor estándar

Con el modelo de consumo **estándar**, todos los consumidores de un shard comparten el mismo
rendimiento de lectura (recordar: **2 MB/s de salida por shard**). Al añadir más consumidores, ese
rendimiento se reparte entre todos ellos, creando un **cuello de botella**: el modelo no escala bien
cuando hay muchos consumidores concurrentes.

## Enhanced Fan-Out (EFO)

**Enhanced Fan-Out** es la funcionalidad que resuelve este problema: se configura en el stream para
que los datos se **empujen (push)** a cada consumidor vía **HTTP/2**, en lugar del modelo estándar de
sondeo (pull) con rendimiento compartido.

### Ventajas

| Aspecto | Consumidor estándar | Enhanced Fan-Out |
| ------- | -------------------- | ----------------- |
| Rendimiento de lectura | **Compartido** entre todos los consumidores (2 MB/s por shard en total) | **Dedicado**: cada consumidor obtiene hasta 2 MB/s por shard, independientemente del número de consumidores |
| Escalabilidad | Limitada — más consumidores = cuello de botella | Alta — hasta **20 consumidores** por stream, cada uno con su propio rendimiento |
| Latencia | ~200 ms | ~70 ms |
| Modelo de entrega | Pull (sondeo) | Push vía HTTP/2 |

- Con rendimiento **dedicado**, 10 consumidores usando Enhanced Fan-Out obtendrían en total **20 MB/s**
  (2 MB/s cada uno), frente a los 2 MB/s totales que se compartirían con el consumidor estándar.
- También **simplifica el desarrollo**: la gestión de la distribución a múltiples consumidores queda a
  cargo del propio servicio, en vez de tener que gestionarla manualmente.

> ⚠️ Enhanced Fan-Out tiene un **coste más elevado** que el modelo estándar.

## Cuándo usarlo

- Cuando hay un **número elevado de consumidores concurrentes** (ej. 5+) y se necesita alto
  rendimiento sin que unos consumidores afecten a otros.
- Cuando se necesita **reducir la latencia** de extremo a extremo.
- En general, cuando el beneficio de escalabilidad/latencia compensa el coste adicional.
