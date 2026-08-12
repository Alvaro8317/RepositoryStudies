# Buenas prácticas de RDS

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Buenas prácticas para optimizar una instancia de [[1-rds|RDS]]: monitorización, copias de seguridad,
conexión de clientes, rendimiento, y recomendaciones específicas por motor de base de datos.

## Monitorización y logging

- Usar **CloudWatch** para vigilar métricas como **CPU**, **almacenamiento** y **replica lag**
  (retardo de réplica) — permite entender y mantener el rendimiento, la disponibilidad y la salud de
  los recursos.
- Si las métricas muestran que nos acercamos a un límite de capacidad (por ejemplo, de
  almacenamiento), es el momento de escalar la instancia.
- Dejar un **buffer** de almacenamiento y memoria para poder absorber aumentos inesperados de carga
  sin degradar el rendimiento.

## Copias de seguridad automáticas

- Elegir el horario de backups automáticos basándose en las métricas, no adivinando: el momento
  adecuado es cuando las **write IOPS** son bajas — así el backup es lo menos disruptivo posible para
  la base de datos.
- Si la base de datos necesita más I/O del que tiene provisionado, la recuperación tras un failover
  puede volverse lenta. Aprovisionar la capacidad de I/O adecuada evita este problema.

## Conexión de clientes: DNS TTL

Las aplicaciones cliente usan DNS para resolver la dirección IP de la base de datos.

> ⚠️ Si el resultado de la resolución DNS se cachea durante demasiado tiempo, y la IP de la base de
> datos cambia (por ejemplo, tras un failover), la aplicación puede seguir intentando conectarse a la
> IP antigua. Configurar el **TTL de caché DNS a un valor por debajo de 30 segundos** ayuda a que la
> aplicación siempre use la IP actual, reduciendo el riesgo de fallos de conexión.

## Probar el failover

Probar la conmutación por error de la base de datos **regularmente** para entender cuánto tarda el
proceso en cada escenario concreto — el tiempo de failover varía según el caso, y solo probándolo se
conoce el comportamiento real.

## Rendimiento

### Working set en memoria

Una de las prácticas más importantes: asignar suficiente RAM para que el **working set** (los datos e
índices de uso frecuente) resida casi por completo en memoria.

- El working set crece cuanto más se usa la instancia.
- Para comprobar si el working set está mayormente en memoria, revisar las **read IOPS** en
  CloudWatch mientras la instancia está bajo carga — un valor de read IOPS **bajo y estable**
  indica que el working set cabe en memoria.

### Enhanced Monitoring

Proporciona información en tiempo real más detallada sobre el rendimiento y la salud de la base de
datos que la monitorización estándar: utilización de CPU, uso de memoria, actividad de disco y
actividad de red, a un nivel más granular.

### RDS Performance Insights

Disponible tanto para **RDS** como para **Aurora**. Simplifica la monitorización de rendimiento y el
tuning de la base de datos, con un dashboard fácil de usar que visualiza la carga de la base de datos
e identifica cuellos de botella — accesible incluso sin ser experto en el motor de base de datos.

Casos de uso:

- **Detectar y resolver problemas de rendimiento** en producción a medida que ocurren.
- **Desarrollo y testing**: evaluar el impacto de consultas SQL específicas y optimizarlas antes de
  llevarlas a producción.
- **Migraciones a la nube**: evaluar y ajustar el rendimiento durante la transición.

## Buenas prácticas por motor de base de datos

| Motor          | Recomendación                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MySQL**      | Evitar que las tablas crezcan demasiado (restringir su tamaño) y particionarlas cuando corresponda — mejora el rendimiento y el tiempo de recuperación. |
| **Oracle**     | Usar **FlashGrid** para tener control total de la base de datos, incluyendo acceso a nivel de sistema operativo.                                          |
| **PostgreSQL** | Mantener activo **Autovacuum**, que automatiza los comandos `VACUUM` y `ANALYZE` — gestiona el almacenamiento, mejora el rendimiento de consultas y evita el "bloat" de la base de datos. Viene habilitado por defecto en todas las instancias nuevas de RDS para PostgreSQL. |

## IOPS suficientes

En todos los casos, aprovisionar **IOPS suficientes** para la carga de trabajo — unos IOPS
inadecuados pueden alargar los tiempos de failover, ya que la recuperación de la base de datos
requiere suficiente I/O disponible.
