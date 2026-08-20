# Redshift: Workload Management (WLM)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Workload Management (WLM)** es una función que ayuda a gestionar el rendimiento de las
consultas en función de sus **prioridades**.

## El problema

A menudo hay distintas consultas **compitiendo entre sí** y ejecutándose de forma simultánea —
por ejemplo, consultas de corta duración que no queremos que se queden **atascadas** esperando
detrás de consultas largas.

Con WLM podemos gestionar cómo se asignan los recursos a las distintas consultas según su
**complejidad** y **prioridad**, obteniendo un rendimiento más **predecible**.

## Colas de consulta (query queues)

La unidad básica que se gestiona y configura en WLM es la **cola de consulta (query queue)**.

- Se pueden crear hasta **8 colas** distintas.
- Las consultas se **enrutan** a una cola u otra en función de reglas — por ejemplo, según el
  **grupo de usuarios** o el **grupo de consulta** al que pertenecen.
- Cada cola se configura con sus propios **recursos asignados** (ej. una cola de alta prioridad
  con más recursos dedicados).

Hay dos modos de gestionar estas colas: **automático** y **manual**.

## Gestión automática de la carga de trabajo

- Redshift determina **automáticamente**:
  - Cuántas consultas se ejecutan **simultáneamente** en una cola (concurrencia).
  - Cuánta **memoria** se asigna a cada una.
- La concurrencia se ajusta según la complejidad de la consulta:
  - Consultas complejas (ej. **hash joins** entre tablas grandes) → **menor concurrencia**.
  - Consultas simples (ej. inserciones sencillas) → **mayor concurrencia**.

A nivel de cola sí se pueden configurar algunas propiedades:

- **Grupos de usuarios (user groups)**: se asignan colas específicas según el grupo de usuarios
  que envía la consulta.
- **Grupos de consulta (query groups)**: permiten categorizar consultas o usuarios, para
  enrutarlos a colas dedicadas configuradas de forma específica.
- **Prioridad**: no todas las consultas tienen la misma importancia — por ejemplo, un job **ETL**
  de alta prioridad puede necesitar priorizarse sobre cargas de trabajo analíticas de menor
  prioridad.

## Gestión manual de la carga de trabajo

- Ofrece **más opciones de configuración** y control a nivel más detallado — por ejemplo,
  especificar exactamente cuánta **memoria** se asigna a cada cola.
- Útil cuando se conoce bien la carga de trabajo y se quiere un control fino sobre la asignación
  de recursos.

> ⚠️ El modo **automático** suele ser una buena opción por defecto y con frecuencia logra **mejor
> rendimiento** que una configuración manual, ya que Redshift ajusta dinámicamente la concurrencia
> y la memoria según la carga real.

## Concurrency scaling

- Modo disponible tanto en la gestión **automática** como en la **manual** de WLM.
- Cuando está habilitado, añade **automáticamente capacidad adicional al clúster** cuando es
  necesario — por ejemplo, ante un aumento de lecturas o escrituras concurrentes.

## Short Query Acceleration (SQA)

**SQA** es una función adicional de WLM, **activada por defecto**, que **prioriza las consultas
de corta duración** frente a las de larga duración, para que no tengan que esperar a que
terminen estas últimas.

- Redshift usa **algoritmos de machine learning** para predecir el **tiempo de ejecución previsto**
  de una consulta, y así identificar cuáles son de corta duración.
- Las consultas identificadas como cortas se ejecutan de inmediato en un **espacio dedicado**, sin
  esperar a que terminen las consultas largas.
- Mejora tanto el **rendimiento** como la **experiencia del usuario**.

> ⚠️ SQA solo aplica a sentencias **`CREATE TABLE ... AS`** y a **consultas de solo lectura** (ej.
> `SELECT`) — son las que más se benefician de esta ejecución acelerada.
