# Application Auto Scaling

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es?

**Application Auto Scaling** permite escalar automáticamente los recursos escalables de distintos
servicios de AWS. Algunos de los servicios/recursos compatibles:

- **Amazon Aurora**
- **DynamoDB**
- **Amazon SageMaker**
- **Concurrencia aprovisionada (provisioned concurrency)** de funciones **Lambda**
- **Amazon Managed Streaming for Apache Kafka (MSK)**
- Clústeres de **Amazon Neptune**
- Clústeres de **Amazon EMR**

Ofrece dos enfoques de escalado: **políticas de seguimiento de objetivos (target tracking)** y
**escalado programado (scheduled scaling)**.

## Target tracking scaling policies (políticas de seguimiento de objetivos)

Se establece una política que ajusta automáticamente la capacidad de la aplicación en función de
una **métrica objetivo**, con el fin de garantizar el mejor rendimiento y optimizar los costes.

Funcionamiento:

1. Se elige una **métrica**, por ejemplo la utilización de CPU.
2. Se fija un **valor objetivo** que representa el nivel medio de utilización deseado, por ejemplo
   un 50% de utilización de CPU.
3. Application Auto Scaling crea y gestiona automáticamente las **alarmas de CloudWatch** que
   activan las acciones de escalado cuando la métrica se desvía del objetivo.

> ⚠️ Funciona como un termostato: intenta mantener la métrica en el valor objetivo, escalando hacia
> arriba o hacia abajo automáticamente, sin necesidad de definir manualmente cuándo escalar.

Tipos de métricas disponibles:

- **Métricas predefinidas**: proporcionadas por Application Auto Scaling (p. ej. utilización media
  de CPU).
- **Métricas personalizadas**: métricas propias publicadas en CloudWatch.

## Scheduled scaling (escalado programado)

Permite ajustar automáticamente la capacidad en función de **patrones de carga predecibles** (por
ejemplo, un día de la semana o una hora concreta en la que se esperan cargas más altas).

Se implementa mediante **acciones programadas (scheduled actions)**: se crea una acción que aumenta
o disminuye automáticamente la capacidad en momentos específicos definidos de antemano.

Es un enfoque **proactivo**, ideal cuando existen patrones de carga regulares y predecibles (por
ejemplo, picos de tráfico a mitad de semana que bajan hacia el fin de semana). Permite establecer un
calendario de aumento/disminución de capacidad según esos días concretos.

**Ventajas:**

- Optimización de costes: evita el sobreaprovisionamiento de recursos durante periodos de bajo
  tráfico.
- Garantía de rendimiento: asegura capacidad suficiente durante las horas de mayor tráfico.
