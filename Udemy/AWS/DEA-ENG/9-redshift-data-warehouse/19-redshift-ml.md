# Redshift ML

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Redshift ML** permite a los usuarios **crear, entrenar y aplicar** modelos de machine learning
usando **solo SQL**, entrenados con los datos ya almacenados en Redshift.

## Cómo funciona

- Se entrena un modelo con un único comando SQL: **`CREATE MODEL`**.
- El modelo entrenado se puede usar para generar **predicciones (inferencia)** directamente desde
  SQL, dentro del propio entorno de Redshift.
- Como las predicciones se hacen **dentro del clúster**, no es necesario mover los datos fuera de
  Redshift — esto agiliza el proceso y simplifica la arquitectura.
- Es especialmente útil para usuarios que no tienen experiencia en machine learning pero sí están
  familiarizados con SQL y con Redshift.

## Algoritmos soportados

Redshift ML soporta algoritmos comunes de ML, incluyendo:

- **Clasificación binaria**.
- **Clasificación multiclase**.
- **Regresión** (distintos tipos).

## Por debajo: Amazon SageMaker

- Redshift ML usa **Amazon SageMaker Autopilot** para encontrar automáticamente el **mejor
  modelo**, entrenando y ajustando modelos en función de los datos disponibles — sin que el
  usuario tenga que elegirlo manualmente.
- Una vez entrenado, **SageMaker Neo** compila el modelo entrenado y lo hace disponible para
  hacer predicciones directamente en el clúster de Redshift.

## Inferencia

- Al usar el modelo entrenado para hacer predicciones, se ejecuta una **consulta de inferencia de
  ML**.
- Esta consulta puede aprovechar tanto el **procesamiento paralelo masivo (MPP)** de Redshift
  como las **predicciones basadas en ML**, todo dentro de la misma consulta.

> ⚠️ La ventaja clave de Redshift ML es que todo el ciclo — entrenamiento e inferencia — ocurre
> **dentro del entorno de Redshift**, sin necesidad de mover los datos a un servicio de ML aparte.
