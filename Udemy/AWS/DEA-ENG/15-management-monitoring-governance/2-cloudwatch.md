# Amazon CloudWatch

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es CloudWatch?

**CloudWatch** es el servicio de **monitorización** de AWS: da visibilidad sobre el
**rendimiento** y la **salud operativa** de aplicaciones y recursos, **en tiempo real**.

- Permite reunir métricas y recopilarlas en **dashboards**: una colección de métricas centralizada
  en un mismo sitio.
- Es un servicio **global**: se pueden ver las métricas **independientemente de la región**, sin
  necesidad de cambiar de región para consultarlas.

## Métricas

Una **métrica** es un conjunto de **puntos de datos** — valores numéricos que se usan para medir
recursos y aplicaciones.

- Las métricas ayudan a entender **cuánto se está usando** un recurso y **qué tan saludable**
  está.
- Ejemplo típico: el **porcentaje de utilización de CPU** de una instancia EC2, para medir su
  salud, uso y rendimiento.
- Muchos servicios de AWS proporcionan métricas **por defecto** y **sin coste adicional**, para
  supervisar la salud, el rendimiento y la utilización de los recursos.

### Componentes de una métrica

| Componente | Descripción |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Namespace** | Contenedor que **agrupa métricas relacionadas**, para organizarlas y categorizarlas (por ejemplo, según su fuente/servicio o propósito). Convención habitual: `AWS/<servicio>` (ej. `AWS/EC2`), o algo propio como `mi-empresa/produccion`. |
| **Timestamp** | Momento en el que se tomó la medida. |
| **Dimensiones** | Pares **clave-valor** asociados a una métrica, que aportan **profundidad adicional**. Ej. para una instancia EC2: `InstanceId`, `InstanceType`, `ImageId`. Permiten ver los datos de una instancia específica o comparar varias instancias entre sí. |
| **Estadísticas** | Datos **agregados** de la métrica durante un periodo determinado (ej. la utilización **media** de CPU de una instancia EC2 en ese periodo). |
| **Periodo (Period)** | Intervalo de tiempo asociado a una estadística — determina con qué frecuencia se agregan/comprueban los datos. |
| **Resolución** | Nivel de detalle (granularidad) de los datos de la métrica. |

### Resolución: estándar vs. alta

- **Resolución estándar**: un punto de datos **cada minuto** (comportamiento por defecto).
- **Alta resolución**: registra métricas con granularidad de **hasta 1 segundo**.

> ⚠️ Las **métricas** son el concepto más fundamental de CloudWatch — namespace, dimensiones,
> estadísticas, periodo y resolución son los componentes clave a entender a nivel conceptual antes
> de ver funcionalidades más avanzadas como los **metric streams** (siguiente clase).
