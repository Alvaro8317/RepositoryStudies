# AWS Step Functions

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**AWS Step Functions** es un servicio que permite crear **flujos de trabajo** complejos y de
varios pasos para **coordinar** la ejecución de funciones **Lambda** y otros servicios de AWS.

- Se integra con muchos servicios y permite crear flujos de trabajo **visuales** (editor
  drag-and-drop) que orquestan, por ejemplo, canalizaciones de datos.

## Casos de uso

- **Orquestación de aplicaciones**: automatiza flujos de trabajo que coordinan tareas entre
  distintas aplicaciones y servicios, garantizando una ejecución fiable y escalable.
- **Procesamiento de datos**: flujos de trabajo complejos con varios pasos (recopilar datos,
  transformarlos, controles de calidad) que a menudo requieren **lógica de ramificación**.
- **Coordinación y gestión de microservicios**: garantiza que los servicios interactúen de forma
  fluida, con manejo de errores y reintentos incorporados.
- **Automatización de modelos de Machine Learning**: preprocesamiento de datos, entrenamiento y
  despliegue como parte de un mismo flujo de trabajo.

> En resumen: siempre que haya que orquestar/integrar varios servicios (por ejemplo, una función
> Lambda que después debe actualizar una tabla de DynamoDB), Step Functions es la herramienta
> adecuada.

## Máquinas de estado (State Machines)

Un flujo de trabajo en Step Functions se basa en una **máquina de estados** (*state machine*):

- La **máquina de estados** es, en esencia, el flujo de trabajo completo.
- Cada paso individual del flujo se llama **estado** (*state*).
- Una **tarea** (*task*) representa una unidad de trabajo dentro de un estado — por ejemplo,
  ejecutar una función Lambda. Un estado de tarea puede llamar a cualquier servicio o API de AWS.

### Tipos de estado

| Tipo de estado | Función                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Task**       | Ejecuta una única unidad de trabajo (ej. una función Lambda o una llamada a un servicio/API). Es el más utilizado. |
| **Choice**     | Añade lógica de ramificación: evalúa condiciones y encamina la ejecución a un estado distinto según el resultado. |
| **Wait**       | Pausa la máquina de estados durante una duración especificada, un intervalo fijo o hasta una marca de tiempo.      |
| **Succeed**    | Representa el final exitoso de la ejecución y la detiene.                                                        |
| **Fail**       | Representa una ejecución fallida y la termina, marcándola como fallida.                                          |
| **Parallel**   | Ejecuta múltiples ramas de la máquina de estados **simultáneamente** y recoge los resultados en un array.         |
| **Map**        | Procesa múltiples elementos de forma dinámica, iterando sobre una lista y procesando cada elemento con un subflujo. Muy útil para flujos de trabajo a gran escala sobre grandes conjuntos de datos — el más relevante para procesamiento de datos. |
| **Pass**       | Pasa la entrada a la salida, opcionalmente aplicando transformaciones a los datos.                                |

> ⚠️ El estado **Map** es especialmente importante para procesamiento de datos: está pensado para
> iterar y procesar grandes conjuntos de datos elemento a elemento.

Las máquinas de estado se definen en **ASL** (**Amazon States Language**), un lenguaje basado en
**JSON**. No es necesario saber leer ASL en detalle — basta con recordar que es el lenguaje en el
que se definen las máquinas de estado internamente.

## Integraciones con otros servicios

Step Functions ofrece dos formas de integrarse con el resto de servicios de AWS:

| Tipo de integración | Descripción |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Integraciones SDK de AWS** | Permiten llamar directamente a cualquiera de los +200 servicios de AWS (más de 9000 acciones de API) desde la máquina de estados. Muy flexibles y con alto nivel de control, pero más complejas de configurar. |
| **Integraciones optimizadas** | Personalizadas y preconfiguradas para servicios populares (Lambda, S3, DynamoDB, etc.), pensadas para simplificar el uso. Más sencillas de configurar y ejecutar. |

## Permisos IAM

Es fundamental que la máquina de estados tenga los **permisos IAM** suficientes para ejecutar
código y acceder a otros recursos (por ejemplo, invocar una función Lambda).

- Se debe conceder acceso mediante un **rol IAM** asociado a la máquina de estados.
- La política IAM debe incluir todos los permisos necesarios para las acciones del flujo — por
  ejemplo, si una función Lambda invocada necesita leer/escribir en una tabla de DynamoDB, esa
  Lambda también necesita sus propios permisos correspondientes.

> ⚠️ Sin los permisos IAM correctos en el rol de la máquina de estados (y en los recursos que esta
> invoca), el flujo de trabajo fallará al intentar ejecutar sus tareas.

## Tipos de flujo de trabajo

| Tipo | Duración | Rendimiento | Registro/auditoría | Coste |
| ---------------------------- | ---------------------------------- | ------------------------------------------------------ | ---------------------------------------------- | --------------------- |
| **Standard** (estándar) | Procesos complejos y de larga duración, hasta **1 año** | Menor rendimiento | Registro detallado de cada paso — ideal para pistas de auditoría/cumplimiento | Más caro |
| **Express** (exprés) | Corta duración, normalmente hasta ~5 minutos | Alto rendimiento: hasta **100 000 tareas/segundo**, tasa de transacciones casi ilimitada | Registro menos detallado, integración más limitada con servicios externos | Más económico |

> ⚠️ Elegir **Standard** cuando se necesita trazabilidad completa de cada paso (cumplimiento,
> auditoría) o ejecuciones muy largas. Elegir **Express** cuando prioriza el coste y la
> escalabilidad para tareas de gran volumen y corta duración.
