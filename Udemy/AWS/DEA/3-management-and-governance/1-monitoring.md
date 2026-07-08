# Monitorización en AWS

## ¿Por qué monitorizar?

A los usuarios/clientes finales no les importa **cómo** se ha desplegado una aplicación, sino que **funcione correctamente**. Por eso es fundamental monitorizar en todo momento para garantizar que el sistema se comporta como se espera.

Preguntas clave que la monitorización ayuda a responder:

- ¿Cuál es la **latencia** de la aplicación? ¿Aumenta con el tiempo?
- ¿Se notifica correctamente cuando hay una **caída** de la aplicación? (Puede pasarle a cualquiera, incluso a AWS).
- ¿Estamos evitando que los **usuarios se quejen** o contacten a soporte por problemas detectables antes?

## Beneficios de monitorizar

1. **Prevenir problemas antes de que ocurran**
   Mediante métricas se puede anticipar el estado del sistema y actuar antes de que se convierta en un incidente.

2. **Performance y coste**
   Ejemplo: si una aplicación debe responder en menos de 10 segundos, hay que monitorizar que se cumpla ese SLA y detectar cuándo se supera, además del coste económico asociado a las llamadas.

3. **Tendencias y patrones de escalado**
   Permite identificar patrones de uso (ej. más llamadas entre semana que en fin de semana) para ajustar el escalado de forma proactiva (añadir o quitar instancias según el patrón detectado).

4. **Aprendizaje y mejora continua**
   Las métricas recolectadas permiten aprender del sistema y mejorarlo de forma incremental.

## Herramientas principales de monitorización en AWS

### 1. Amazon CloudWatch

El servicio más destacado y ampliamente usado. Ofrece:

- **Métricas:** recopilación y seguimiento de métricas clave del sistema.
- **Logs:** recopilación, análisis y almacenamiento de registros (logs).
- **Eventos:** notificaciones generadas ante cambios de estado de recursos (ej. un recurso se cae o se crea uno nuevo), que pueden desencadenar otras acciones.
- **Alarmas:** reaccionan automáticamente ante una métrica o condición definida.
  - Ejemplo: una alarma basada en el nivel de CPU de una instancia que dispara el lanzamiento de una nueva instancia.

### 2. AWS X-Ray

- Enfocado en **monitorizar el rendimiento (performance)** y **notificar errores** de la aplicación.
- Permite el **rastreo distribuido (distributed tracing)** de microservicios.
- Especialmente útil en arquitecturas de microservicios, donde ayuda a seguir el flujo de una petición a través de múltiples servicios.

### 3. AWS CloudTrail

- Monitoriza de forma interna **todas las llamadas a la API de AWS** realizadas en la cuenta.
- Mantiene un **historial inmutable** de las acciones realizadas.
- Caso de uso típico: auditoría — por ejemplo, saber **quién eliminó una instancia, cuándo y por qué**, especialmente útil cuando varias personas de una empresa usan la misma cuenta de AWS.

## Resumen comparativo

| Herramienta | Enfoque principal | Caso de uso típico |
|---|---|---|
| **CloudWatch** | Métricas, logs, eventos y alarmas | Monitorización general del sistema y automatización de respuestas (ej. auto scaling por CPU) |
| **X-Ray** | Rendimiento y trazabilidad | Rastreo distribuido en arquitecturas de microservicios |
| **CloudTrail** | Auditoría de llamadas a la API | Saber quién hizo qué acción, cuándo y por qué en la cuenta de AWS |

> Estos tres servicios (CloudWatch, X-Ray y CloudTrail) son la base de la monitorización en AWS y se profundizarán con más detalle en las siguientes clases.
