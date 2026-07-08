# Alarmas de CloudWatch

## ¿Qué son y para qué sirven?

Las alarmas de CloudWatch permiten **detectar anomalías** en el comportamiento de los recursos de AWS y **actuar con una respuesta rápida** ante ellas (como si fueran "los bomberos" del sistema).

Permiten **automatizar respuestas**, por ejemplo:

- Resolver problemas automáticamente.
- **Escalar recursos** de AWS, tanto **incrementando** como **decrementando** (levantar o tumbar instancias EC2, por ejemplo).

## Umbrales sobre métricas

Las alarmas se basan en **límites/umbrales definidos sobre una métrica específica**.

### Ejemplo práctico

- Escenario: 10 instancias EC2 activas ejecutando un e-commerce durante un **Black Friday**.
- Se define un umbral: si el **uso de CPU supera el 70%**, se dispara una acción de **escalado**.
- El mismo principio aplica a cualquier otra métrica, no solo CPU.

### Otro ejemplo

- Se puede establecer una **alarma de facturación mensual**, desencadenando acciones según el gasto acumulado.

## Estados de una alarma

Una alarma de CloudWatch puede estar en uno de tres estados:

| Estado                                      | Significado                                              |
| ------------------------------------------- | -------------------------------------------------------- |
| **OK**                                      | Todo funciona dentro de los parámetros esperados         |
| **INSUFFICIENT_DATA** (datos insuficientes) | Faltan datos para evaluar la métrica                     |
| **ALARM**                                   | Se ha superado el umbral definido; la alarma está activa |

## Acciones que pueden desencadenar las alarmas

### 1. Sobre instancias EC2

- **Detener** (stop)
- **Terminar** (terminate)
- **Reiniciar** (reboot)
- **Recuperar** una instancia que haya caído (recover)

### 2. Auto Scaling

- **Incrementar** el número de instancias en un grupo de Auto Scaling.
- **Decrementar** el número de instancias.

### 3. Notificaciones vía Amazon SNS

- Envío de **correos electrónicos** o **mensajes SMS** al equipo técnico/ingenieros.
- Permite notificar al equipo responsable en cuanto se activa una alarma.

## Diagrama conceptual

```text
CloudWatch Alarm
      │
      ├──► Amazon SNS (email / SMS al equipo técnico)
      │
      ├──► AWS Lambda (ejecución de código/acción personalizada)
      │
      ├──► Instancias EC2 (stop / terminate / reboot / recover)
      │
      └──► Grupo de Auto Scaling (incrementar / decrementar instancias)
```

## Integración con CloudWatch Logs

Las alarmas de CloudWatch también se pueden integrar con **CloudWatch Logs**: a partir de la información contenida en los logs (mediante filtros de métrica), se pueden desencadenar acciones posteriores a través de una alarma.

## Idea clave

Las alarmas de CloudWatch conectan **métricas → umbrales → acciones automatizadas**, permitiendo reaccionar de forma proactiva ante problemas, picos de demanda o costes, sin necesidad de intervención manual constante.
