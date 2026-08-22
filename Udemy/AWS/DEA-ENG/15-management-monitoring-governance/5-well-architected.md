# AWS Well-Architected Framework y Well-Architected Tool

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

El **AWS Well-Architected Framework** es una guía desarrollada por AWS para ayudar a construir
infraestructuras **eficientes**: seguras, de alto rendimiento y resilientes. Ofrece un enfoque
**coherente** para evaluar la arquitectura e implementar diseños que funcionen y escalen bien con
el tiempo, basado en **seis pilares**.

## Los seis pilares

| Pilar | Enfoque | Prácticas clave |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Excelencia operativa** | Que todo funcione correcta y eficazmente; automatizar operaciones y monitorizar para detectar/solucionar problemas antes de que afecten al cliente. | Usar herramientas de automatización, configurar dashboards de monitorización, y actualizar continuamente los procedimientos operativos según lo aprendido. |
| **Seguridad** | Sistemas y datos seguros; solo las personas adecuadas acceden a ellos. | Buena gestión de identidades (ej. MFA), cifrado de datos sensibles, y herramientas de monitorización para detectar/alertar actividad sospechosa. |
| **Fiabilidad** (*reliability*) | La aplicación siempre disponible y capaz de recuperarse rápido ante fallos. | Gestionar cambios en la demanda (más carga de trabajo) y recuperarse de interrupciones **sin intervención manual**. |
| **Eficiencia de rendimiento** | Usar los recursos con prudencia para que los sistemas funcionen rápido y eficazmente, adaptándose a necesidades cambiantes sin sobregastar. | Elegir el tipo/tamaño adecuado de recurso (ej. tipo de instancia EC2), aprovechar tecnologías modernas (serverless, contenedores), y monitorizar el rendimiento para ajustar recursos. |
| **Optimización de costes** | Pagar solo por lo necesario y usar los recursos de forma eficiente. | Desactivar recursos no utilizados, elegir el modelo de precios adecuado (instancias reservadas, Spot), y revisar periódicamente costes y uso con herramientas de gestión de costes. |
| **Sostenibilidad** | Diseñar y operar sistemas que minimicen el impacto ambiental, reduciendo emisiones de carbono. | Elegir tamaño/tipo de recurso ajustado a la necesidad real, código eficiente para reducir carga computacional, y desplegar en regiones con energías renovables cuando sea posible. Mejora continua. |

> El framework funciona como una **checklist** para diseñar sistemas seguros, eficientes y
> resilientes, y para evaluar periódicamente la arquitectura frente a estos seis pilares.

## AWS Well-Architected Tool

Herramienta que permite **revisar cargas de trabajo** frente al framework, guiando al usuario a
través de una serie de **preguntas** relacionadas con cada uno de los seis pilares.

### Componentes clave

| Componente | Descripción |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Workload** (carga de trabajo) | La unidad que se evalúa: una colección de componentes que aportan valor de negocio — por ejemplo, una aplicación orientada al cliente o un proceso interno. |
| **Milestones** (hitos) | Puntos de control para hacer seguimiento del progreso de las revisiones de una workload a lo largo del tiempo, documentando cambios y mejoras de la arquitectura. |
| **Lenses** (lentes) | Conjuntos de preguntas usados durante la revisión; se seleccionan según lo que se quiere evaluar y se combinan con las preguntas estándar del framework. |

### Tipos de lens

| Tipo | Descripción |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Catálogo de lenses de AWS** | Creadas y mantenidas por AWS; disponibles para cualquiera, sin instalación adicional, y su uso es **gratuito**. |
| **Lenses personalizadas** | Creadas por el propio usuario/organización, con preguntas y mejores prácticas propias, para evaluar workloads según un marco definido internamente. |

> ⚠️ Límites: hasta **5 lenses a la vez** por workload, y un máximo de **20 lenses** en total
> añadidas a las workloads.

### Resultado de la revisión

Al finalizar la revisión, la herramienta genera un informe con los problemas detectados,
clasificados por nivel de riesgo:

| Nivel de riesgo | Descripción |
| --------------------------- | -------------------------------------------------------------------------------- |
| **High risk** (alto riesgo) | Opciones que pueden tener un impacto realmente **negativo** en el negocio. |
| **Medium risk** (riesgo medio) | Opciones con un impacto menor que las de alto riesgo. |

### Flujo de uso

1. Definir la **workload** a evaluar.
2. Revisarla respondiendo las preguntas de los pilares (y de las lenses seleccionadas).
3. Obtener un informe con la lista de problemas y un **plan de mejora** sugerido.
4. Aplicar las mejoras y, con el tiempo, usar **milestones** para trazar la evolución.

> Este proceso habilita una **gobernanza coherente** y una mejora continua de la arquitectura.
