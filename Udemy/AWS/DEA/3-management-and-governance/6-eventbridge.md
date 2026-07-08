# Amazon EventBridge

## ¿Qué es?

EventBridge facilita la **conexión de aplicaciones con datos** que provienen de diversas fuentes: servicios de AWS, aplicaciones SaaS (software como servicio) y aplicaciones externas.

Como usuarios, lo que hacemos es **definir y enviar eventos** a través de **buses de eventos** de EventBridge. Esto permite crear aplicaciones **reactivas y altamente personalizadas**, basadas en eventos específicos del negocio, reaccionando en tiempo real.

> 💡 Dato histórico: este servicio antes se llamaba **CloudWatch Events**. Dentro de la consola de CloudWatch, en la sección de Eventos, ahora redirige directamente a Amazon EventBridge.

## Tipos de buses de eventos

| Tipo de bus                      | Descripción                                                                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bus predeterminado (default)** | Generado automáticamente; recibe eventos de servicios de AWS. Viene creado por defecto al crear la cuenta.                                                           |
| **Bus de socios (partner)**      | Proviene de plataformas externas: Zendesk, Datadog, Segment, Auth0, Salesforce, y muchas más (actualmente hay decenas de socios disponibles, la lista va creciendo). |
| **Bus personalizado**            | Creado por el usuario para sus propias aplicaciones.                                                                                                                 |

## Registro de esquemas (Schema Registry)

- EventBridge puede **analizar los eventos** del bus e **inferir su esquema** automáticamente.
- Un **esquema** define la forma y el formato de los eventos.
- Con el registro de esquemas se puede **generar código** para la aplicación, sabiendo de antemano cómo se estructuran los datos.
- Los esquemas pueden **versionarse** (mantener varias versiones del mismo esquema).

## Políticas basadas en recursos

Permiten **gestionar permisos sobre un bus de eventos**, por ejemplo:

- Permitir o denegar eventos provenientes de **otra cuenta de AWS** o de **otra región**.
- Caso de uso típico: una organización grande que centraliza todos los eventos de varias cuentas en **una única cuenta dedicada a eventos**.

### Ejemplo de arquitectura multi-cuenta

```text
Cuenta A (EC2) ─┐
Cuenta B (EC2) ─┤
Cuenta C (EC2) ─┼──► Bus de eventos con política de recursos ──► Cuenta central de eventos ──► Acciones
Cuenta D (EC2) ─┘
```

Ejemplo: una regla detecta cuando **cambia el estado de una instancia EC2** en cualquiera de las cuentas, y todos esos eventos se centralizan en la cuenta principal para procesarlos.

## Caso práctico: monitoreo de salud en tiempo real

Empresa de tecnología con infraestructura en AWS que necesita **monitorear la salud de sus servicios** en tiempo real:

1. **Detección de incidentes:** servicios como EC2 o RDS envían automáticamente alertas de estado a EventBridge (ej. sobrecarga de CPU, fallos de conexión a la base de datos).
2. **Automatización de respuestas:** EventBridge recibe la alerta y dispara **funciones Lambda** preconfiguradas para escalar recursos o reiniciar instancias.
3. **Notificación a equipos:** EventBridge envía notificaciones a **Slack** o **Microsoft Teams** para informar al equipo técnico del incidente.

---

## Práctica: creación de un bus de eventos y una regla

### 1. Ubicación en la consola

En la consola de CloudWatch, la sección de **Eventos** ahora redirige a **Amazon EventBridge**.

### 2. Buses de eventos

- Existe un **bus por defecto**, creado automáticamente con la cuenta.
- Se pueden crear **buses adicionales** (ej. "mi bus de eventos").
- Opciones al crear un bus personalizado:
  - **Archivar eventos:** de forma indefinida o durante un periodo definido, para no perderlos.
  - **Detección de esquemas:** habilitable para que EventBridge infiera automáticamente el esquema de los eventos entrantes.
  - **Política basada en recursos:** se puede cargar una plantilla o importar una propia para permitir que otras cuentas/servicios envíen eventos al bus.

### 3. Orígenes de eventos de socios (partners)

- En la sección de **Integración → Orígenes de eventos de socios**.
- Actualmente hay decenas de socios disponibles (ej. **Auth0**, **Salesforce**, y muchos más, la lista cambia con el tiempo).
- Configurar un socio como origen de eventos es un proceso guiado y sencillo.

### 4. Creación de una regla (Rule)

Pasos principales al crear una regla (ej. `demo-regla-eventbridge`):

1. **Nombre y descripción** de la regla.
2. **Selección del bus de eventos** (por defecto, de socio, o personalizado).
3. **Tipo de regla:**
   - **Programada:** se ejecuta según una programación definida (cron/rate).
   - **Con patrón de eventos:** se ejecuta cuando un evento coincide con un patrón específico (ej. una instancia EC2 cambia de estado).
4. **Origen del evento:** eventos de AWS, o eventos de socios de EventBridge (Auth0, Salesforce, etc.).
5. **Evento de muestra (opcional pero recomendado):** permite probar que el patrón de eventos definido funciona correctamente antes de desplegarlo.
6. **Método de creación del patrón:**
   - Usar un **esquema** de EventBridge para generar el patrón.
   - Usar un **formulario** con plantilla proporcionada por EventBridge (opción usada en el ejemplo).
   - Definir un **patrón personalizado**.

### Ejemplo práctico: detectar cambio de estado en EC2

- Servicio: **EC2**
- Tipo de evento: **EC2 Instance State-change Notification**
- Se pueden especificar los estados concretos a notificar (ej. `stopped`, `terminated`).

**Prueba con evento de muestra:**

- Se selecciona un evento de muestra de EC2 (`EC2 Instance State-change Notification`).
- Se pueden simular distintos estados: `pending`, `running`, `stopping`, `stopped`, `terminated`, etc.
- Es importante verificar el estado **exacto** definido en el patrón (ej. `stopped` ≠ `stopping`); si no coincide, el test de coincidencia del patrón fallará.
- Al ajustar correctamente el estado (ej. `stopped`), el test confirma que el patrón **sí coincide**.

### 5. Destino del evento (Target)

Una vez la regla coincide con un evento, se envía a un **destino**, por ejemplo:

- Un **servicio de AWS** (ej. un tema de **Amazon SNS** para enviar notificaciones por email o SMS a un suscriptor).
- Otro **bus de eventos** (destino de la propia API de EventBridge).
- Otros destinos como **Amazon S3**, entre muchos más.

## Idea clave

EventBridge permite construir arquitecturas **reactivas basadas en eventos**: conecta fuentes de datos (AWS, socios o aplicaciones propias) con reglas que detectan patrones específicos, y desencadena acciones automáticas (Lambda, notificaciones, escalado) sobre destinos configurables — todo esto sin necesidad de sondear (polling) constantemente el estado de los recursos.
