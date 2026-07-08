# AWS CloudTrail

## Caso de uso motivador

Escenario: un día se entra a la consola y **todas las instancias EC2 han desaparecido**. ¿Qué ha pasado?

Posibles causas:

- Un fallo del propio sistema de AWS (poco probable, pero posible).
- Otro servicio que las haya terminado.
- **Una persona del equipo** que las eliminó.

Para responder a la pregunta **"¿qué ha pasado y quién lo hizo?"** existe **AWS CloudTrail**.

> No es un servicio de uso diario para la mayoría de perfiles, pero es fundamental conocerlo para situaciones críticas puntuales.

## ¿Qué ofrece CloudTrail?

- **Gobernanza, cumplimiento normativo y auditoría** para la cuenta de AWS.
- **Activado por defecto**: no es necesario activarlo manualmente.
- Proporciona un **historial de eventos**: llamadas a la API y consultas realizadas en la cuenta.
- Registra acciones realizadas desde:
  - La **consola**
  - El **SDK**
  - La **CLI**
  - **Servicios de AWS**

## Alcance y almacenamiento

- Los **trails (rastros)** se aplican a **todas las regiones por defecto** de la cuenta.
- Cualquier acción, en cualquier región, queda registrada en este historial.
- Los datos se pueden enviar a:
  - **CloudWatch Logs**
  - Un **bucket de Amazon S3**

## Inmutabilidad del historial

🔒 El historial de CloudTrail es **inmutable**. Si alguien elimina un recurso intentando ocultarlo, **no podrá borrar el registro** de esa acción en CloudTrail — siempre se podrá saber qué pasó y quién lo hizo.

## Fuentes que generan eventos

- SDK
- Consola
- Usuarios
- Roles

Todas estas fuentes, al ejecutar acciones, quedan registradas y disponibles para auditoría en CloudTrail.

## Retención de eventos

- Los eventos se almacenan en CloudTrail durante **90 días**.
- Para conservarlos **más allá de ese periodo**, se recomienda enviarlos a un **bucket S3**.
- Para **consultar** esos datos históricos guardados en S3, se puede usar **Amazon Athena**.

```text
Fuentes (SDK, consola, usuarios, roles)
        │
        ▼
   CloudTrail (retención: 90 días)
        │
        ├──► CloudWatch Logs
        │
        └──► Bucket S3 (retención indefinida) ──► Amazon Athena (consultas)
```

---

## Comparativa final: CloudTrail vs CloudWatch vs X-Ray

| Servicio       | Uso principal                                                                                                                                                               | Frecuencia de uso típica                        |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **CloudTrail** | Auditoría de llamadas a la API (usuarios, roles, servicios, consola). Detecta llamadas no autorizadas o la causa raíz de cambios.                                           | Puntual / crítico                               |
| **CloudWatch** | Métricas y monitorización general. Incluye **CloudWatch Logs** (almacenamiento de logs de aplicaciones) y **CloudWatch Alarms** (notificaciones ante métricas inesperadas). | Uso diario                                      |
| **X-Ray**      | Análisis de trazas automatizado, mapas de servicios, análisis de latencia y errores. Ideal para sistemas distribuidos/microservicios.                                       | Según arquitectura (muy útil en microservicios) |

## Idea clave

- **CloudTrail** responde a "¿quién hizo qué, cuándo y por qué?" — auditoría y gobernanza.
- **CloudWatch** responde a "¿cómo está funcionando mi sistema ahora mismo?" — métricas, logs y alarmas del día a día.
- **X-Ray** responde a "¿dónde está el problema dentro de mi arquitectura distribuida?" — trazabilidad de peticiones.

Los tres servicios son complementarios y cubren distintas necesidades dentro de la observabilidad y gobernanza en AWS.
