# Amazon Neptune

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**Amazon Neptune** es una base de datos de **grafos** totalmente gestionada, muy especializada,
diseñada para almacenar y gestionar relaciones de datos complejas mediante distintos modelos de
grafo — no es una base de datos de propósito general, sino una pensada específicamente para casos de
uso donde las **relaciones entre datos** son el elemento central.

## Casos de uso

- **Grafos de conocimiento** (ej. la red de enlaces entre artículos de Wikipedia).
- **Detección de fraude**.
- **Motores de recomendación**.
- **Redes sociales**.

## Modelos de datos

| Modelo | Descripción |
| --------------------- | ------------------------------------------------------------------------------ |
| **Property Graph** | Los datos se organizan en **vértices** (nodos) y **aristas** (*edges*), que representan las relaciones entre ellos. |
| **RDF** (*Resource Description Framework*) | Modelo de datos basado en **triples**. |

## Características

- Servicio **totalmente gestionado**: AWS gestiona aprovisionamiento, parches, backups, recuperación
  y escalado.
- **Alta disponibilidad**: replicación en **3 Availability Zones** con failover automático.
- **Cifrado** en reposo y en tránsito (TLS).
- Soporte de **VPC** para aislamiento de red.
- **Read replicas** para escalar automáticamente las consultas de lectura.
- Almacenamiento escalable automáticamente hasta **64 TB**.
- Alto rendimiento: capaz de almacenar miles de millones de relaciones con latencia de milisegundos.
- Integración con el ecosistema de AWS: **Lambda** (para disparar funciones), **S3** (importar/exportar
  datos), **SageMaker** (casos de uso de machine learning).
- Compatible con estándares abiertos de tecnología de grafos: **Gremlin** y **SPARQL**.
- Rendimiento optimizado tanto en lectura como en escritura, usando técnicas avanzadas de
  optimización de consultas y estrategias de indexación, con soporte para alta concurrencia.

## Precios

Modelo de pago por uso, basado en:

- **Tamaño de la instancia** y **región** de despliegue.
- **Horas de uso**.
- Características opcionales adicionales: **almacenamiento**, **I/O** y **transferencia de datos**.

> ⚠️ Neptune es una base de datos muy especializada — requiere conocimiento específico de modelado de
> grafos y solo tiene sentido cuando el caso de uso gira realmente en torno a relaciones complejas
> entre datos, no como sustituto de una base de datos de propósito general.
