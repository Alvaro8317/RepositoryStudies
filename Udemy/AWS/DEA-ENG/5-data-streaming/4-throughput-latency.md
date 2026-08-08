# Rendimiento y Latencia en flujos de datos

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Dos medidas muy importantes a la hora de diseñar y dimensionar un flujo de datos (data stream).

## Rendimiento (Throughput)

- Es el **volumen de datos** que se ingiere o se recupera del flujo de datos.
- Se mide normalmente en **megabytes o registros por segundo** (una unidad por intervalo de tiempo).
- Es una medición del **mundo real**: la tasa real de datos procesados, teniendo en cuenta todos los
  factores que influyen en el sistema.
- En AWS Kinesis se escala mediante el **número de shards**: cada shard aporta una capacidad
  específica al stream, por lo que el rendimiento total es **directamente proporcional** al número de
  shards.
  - Si se necesita procesar más volumen de datos en el mismo tiempo, se puede **aumentar el número de
    shards**.

> ⚠️ El rendimiento no debe confundirse con el **ancho de banda**: el ancho de banda es un **límite
> máximo teórico**, mientras que el rendimiento es la tasa real conseguida, que puede verse afectada
> por otros factores.

## Latencia (Latency)

- Es el **tiempo transcurrido** entre el inicio de un proceso y la disponibilidad de su resultado.
- En Kinesis, el concepto específico es el **retardo de propagación (propagation delay)**: la latencia
  de extremo a extremo desde que un registro se **escribe** en el stream hasta que es **leído** por la
  aplicación consumidora.
- El factor que más influye en la latencia es el **intervalo de sondeo (polling interval)**: la
  frecuencia con la que la aplicación consumidora consulta el stream en busca de nuevos registros.
  - AWS recomienda comprobar cada shard **una vez por segundo** por consumidor.
  - La **Kinesis Client Library (KCL)** usa este valor (1 segundo) como intervalo de sondeo por
    defecto, lo que mantiene el retardo de propagación medio **por debajo de 1 segundo**.
- Si una aplicación necesita un retraso mínimo, se puede **aumentar la frecuencia de sondeo** (sondear
  más de una vez por segundo) para reducir el retardo de propagación y procesar los datos más rápido.

> ⚠️ Aumentar la frecuencia de sondeo es un caso especial: hay que gestionar bien esta configuración
> para no alcanzar los **límites de tarifa (rate limits)** del shard.
