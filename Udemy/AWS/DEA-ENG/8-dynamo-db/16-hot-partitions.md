# Rendimiento y optimización de costes: Hot Partitions

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es una hot partition?

Una **hot partition** (partición caliente) es una partición que recibe un volumen
desproporcionadamente alto de solicitudes de lectura o escritura en comparación con las demás
particiones de la tabla.

- Suele deberse a un **diseño deficiente de la clave de partición** — la clave de partición es la
  encargada de distribuir los datos entre particiones — o a **patrones de acceso desiguales**, donde
  algunos datos se consultan con mucha más frecuencia que otros.
- El resultado es una distribución de datos/tráfico desigual entre particiones, lo que provoca
  **throttling**.

## Throttling

Ocurre cuando el número de solicitudes supera el rendimiento provisionado para una tabla o índice.

- DynamoDB deniega temporalmente las solicitudes adicionales — no se procesan.
- Provoca **aumento de latencia** y **solicitudes fallidas**, afectando directamente a la aplicación.

> ⚠️ El throttling no ocurre solo por particiones calientes — cualquier tabla o índice que reciba más
> tráfico del que tiene provisionado sufre throttling. Las hot partitions son una causa habitual, pero
> no la única.

## Cómo mitigarlo

- **Diseñar bien las claves de partición** para que los datos se distribuyan de forma uniforme, y
  ajustar los patrones de acceso para que el tráfico se reparta de manera pareja entre particiones —
  evitando así puntos calientes.
- **Backoff exponencial**: lógica de reintento para manejar solicitudes estranguladas de forma más
  eficiente. Tras cada solicitud denegada se espera un poco más antes de reintentar (el tiempo de
  espera crece exponencialmente con cada reintento fallido).
- **Monitorización con CloudWatch**: vigilar las métricas y ajustar el rendimiento provisionado según
  haga falta.
- **[[11-dax|DAX]]** para aplicaciones con carga de lectura intensiva: cachea los datos accedidos con
  más frecuencia, reduciendo las lecturas directas sobre la tabla.

## Burst Capacity

Mecanismo de DynamoDB que permite a las tablas absorber picos cortos de capacidad de lectura o
escritura **sin throttling**, independiente de las hot partitions en concreto — ataja el problema de
la estrangulación en general.

- La capacidad **no utilizada** se acumula durante un máximo de **5 minutos**.
- Esa capacidad acumulada se puede consumir en ráfagas cortas por encima del rendimiento
  provisionado.

> ⚠️ La capacidad acumulada no se conserva indefinidamente — solo se puede "ahorrar" hasta 5 minutos,
> no acumular durante días para absorber picos enormes más adelante.

## Adaptive Capacity

Mecanismo que redistribuye automáticamente el rendimiento provisionado de una tabla entre sus
particiones para adaptarse a patrones de acceso desiguales.

- Cuando existen hot partitions, Adaptive Capacity redistribuye la capacidad entre las distintas
  particiones para ayudar a mantener el rendimiento.
- Actúa como red de seguridad en condiciones de tráfico donde los patrones de acceso no son uniformes,
  pero no sustituye a un buen diseño de claves de partición y buenas prácticas.
