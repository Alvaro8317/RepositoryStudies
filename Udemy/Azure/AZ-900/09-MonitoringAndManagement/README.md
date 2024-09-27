# Monitorización y gestión

## Gobernanza

Se refiere al conjunto de procesos, directrices y prácticas mediante los cuales los recursos y servicios de Azure se administran y supervisan.

- Políticas de azure
- Blueprints de azure
- RBAC (Control de acceso basado en roles)
- Locks de recursos
- Monitoreo y auditoria

## Azure Policy

Políticas, permiten aplicar los estándares de la organización y evaluar el cumplimiento a escala. Es lo que permite aplicar políticas en los recursos.

## Control de acceso basado en roles de Azure (RBAC)

Son herramientas para administrar quién tiene acceso a los recursos de Azure, qué pueden hacer con esos recursos y qué areas pueden hacer.

Para controlar el acceso a los recursos que usan RBAC hay que utilizar asignaciones de roles, una asignación de rol está compuesta por::

1. Entidad de seguridad
2. Definición de rol
3. Ámbito

### Entidad de seguridad

Es un objeto que representa un usuario, un grupo, una entidad de servicio o una entidad administrada, se le puede asignar un rol a estas entidades.

### Definición de rol

Una definición de qué puede hacer y que no hacer (Las políticas en AWS)

### Ámbito

Es el conjunto de recursos al que se aplica el acceso, cuando se asigna un rol, solo funcionará para un ambito especifico, se puede especificar a nivel de grupo de administración, suscripción, grupo de recursos o recursos (Las relaciones de confianza en AWS)

## Locks

Son elementos que protegen los recursos evitando su eliminación accidental o modificación, hay de tipos read-only (bloquea modificaciones) y delete (bloquea eliminaciones).

Se pueden asignar a nivel de recurso, grupo de recursos o suscripción manejando una jerarquia de aplicación. Si un grupo de recursos tiene un lock y se intenta eliminar, la operación será bloqueada.

## Blueprints

Estos permiten la orquestación de soluciones repetibles con un conjunto predefinido de recursos, cuenta con:

- Plantillas
- Políticas y roles
- Versionado

### Azure Resource Manager vs Blueprints

ARM permite desplegar recursos individuales en Azure usando plantillas

Blueprints combina plantillas ARM, políticas de Azure y otras configuraciones en un diseño cohesivo para deplegar soluciones completas y repetibles

## Azure Cloud Adoption Framework

Es una guía probada para crear e implementar las estrategias empresariales y tecnológicas necesarias para que todo vaya bien en la nube. Proporciona procedimientos recomendados, documentación, etc. Estos procedimientos permiten a las organizaciones alinear mejor sus estrategias empresariales para asegurar un resultado satisfactorio.

1. Se define la estrategia
2. Se define el planteamiento
3. Se está listo preparando el entorno en la nube
4. Se realiza migración

Luego se requerirá

- Seguridad
- Administración
- Gobernanza

Es una guía para tener las mejores prácticas en la nube de azure

## Azure Monitor

Herramienta para supervisar aplicaciones, infraestructura y recursos, sirve con nube e instalaciones locales.

- Cuenta con una integración completa con registros y métricas detalladas
- Provee análisis avanzado
- Cuenta con alertas proactivas a problemas potenciales
- Permite visualización de datos
- Automatiza respuestas basadas en condiciones

Útil para observabilidad reactiva y proactiva

Este servicio cuenta con algunas caracteristicas fundamentales como:

- Telemetría continua
- Centralización y gestión automatizada
- Lenguaje de consulta avanzado, tiene una herramienta de consulta interactiva para analizar los datos de telemetría
- Inteligencia predictiva, utiliza machine learning para identificar y prevenir problemas proactivamente

## Herramientas de monitorización

Estas herramientas permiten supervisar y registrar el rendimiento o el estado de recursos como hardware, redes o software

### Log analytics

Recolecta y analiza datos de telemetría de recursos azure, identifica patrones y ayuda en la soluciónn de problemas.

Azure Monitor genera grandes cantidades de registros y datos, pero log analytics permite almacenar y consultar estos datos, permitiendo a los usuarios obtener información valiosa de ellos. Las consultas en log analytics de azure se utiliza Kusto Query Language

### Application insights

Herramienta enfocada en aplicaciones web compatible con app service, azure vms y recursos externos. Con VM se requiere un agente necesario y diagnostica cuellos de botella en rendimiento, además, analiza interacciones de usuario en el sitio.

### Alertas de Azure Monitor

En Azure monitor se puede tener notificaciones ante eventos inesperados con alertas como que una VM no responde, uso excesivo, etc. Cuando algo no funciona como se espera, las alertas de Azure Monitor informan al grupo adecuado para que haga algo al respecto, un grupo de acción se puede notificar por medio de email / SMS o flujos de trabajo automatizados integrable con Logic Apps, Azure Functions, etc.

## Azure Service Health

Servicio que indica si hay problemas con algún servicio o si hay mantenimientos programados en Azure. Cuenta con:

- Dashboard personalizable para visualizar los impactos de los recursos sobre la infraestructura de uno
- Alertas configurables y personalizables para estar informado de interrumpciones
- Monitorización en directo que permite vigilar las laertas y dificultades en tiempo real con informes de las incidencias ya solucionadas
- Totalmente gratuito disponible sin coste adicional

## Azure Arc

Permite aplicar políticas de gobernanza de Azure y gestionar recursos que no son de Azure, pueden estar en servidores locales o incluso otras nubes.

- Cuenta con gestión unificada
- Cuenta con aplicación consistente de políticas
- Permite extender los servicios de Azure a cualquier infraestructura

**Para extender y gestionar recursos que no son de Azure, Azure Arc es la solución**.

## Resumen

- Gobernanza - Un sistema de regulaciones, prácticas, políticas y procedimientos para dirigir y administrar una entidad o recurso
- Azure Policy - Permite establecer y aplicar reglas específicas en los recursos de Azure
- Control de acceso basado en rol de Azure (RBAC) - Sistema de permisos que asigna roles específicos a usuarios
- Locks - Mecanismo de Azure que previene la modificación o eliminación
- Azure Blueprints - Permite definir conjuntos repetibles de recursos Azure
- Azure monitor - Diseñado para recopilar, analizar y actuar sobre datos telemétricos
- Microsoft Cloud Adoption framework - Conjunto de prácticas, guías y herramientas proporcionadas por Microsoft
- Herramientas de monitorización
  - Log analytics
  - Application insights
  - Alertas de azure monitor
- Azure Service Health - Proporciona información sobre la salud
- Azure Arc - Permite administrar infraestructuras de cualquier lugar

Azure Policy permite establecer y aplicar reglas específicas en los recursos de Azure para asegurar el cumplimiento de normativas y estándares corporativos

Azure Locks proporciona un mecanismo para bloquear los recursos y prevenir su modificación o eliminación accidental

Azure RBAC (Control de acceso basado en rol) permite asignar roles específicos a usuarios y grupos, determinando lo que pueden y no pueden hacer con los recursos

Microsoft Cloud Adoption Framework proporciona un conjunto de prácticas, guías y herramientas para ayudar a las organizaciones en su transición a la nube

Azure Blueprints permite definir conjuntos repetibles de recursos de Azure, facilitando la implementación y el cumplimiento de estándares organizacionales

Azure Monitor está diseñado para recopilar, analizar y actuar sobre los datos telemétricos de aplicaciones y recursos en la nube

Log Analytics es una herramienta que permite recopilar y analizar datos telemétricos y registros de recursos en la nube

Application Insights monitoriza el rendimiento y uso de las aplicaciones, proporcionando análisis y visualizaciones en tiempo real

Las Alertas de Azure Monitor permiten configurar notificaciones que se activan basadas en condiciones específicas, alertando sobre cambios o problemas en los recursos

Azure Service Health proporciona información en tiempo real sobre la salud y el estado de los servicios de Azure, incluyendo alertas sobre interrupciones y mantenimientos.

Azure Arc extiende las capacidades de administración y servicios de Azure a cualquier infraestructura, permitiendo una gestión unificada de recursos.
