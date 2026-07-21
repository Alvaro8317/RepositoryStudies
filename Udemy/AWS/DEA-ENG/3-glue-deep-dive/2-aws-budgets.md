# AWS Budgets

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son los AWS Budgets?

**AWS Budgets** es una funcionalidad de **Billing and Cost Management** que permite definir
presupuestos sobre la cuenta y configurar **alarmas** cuando se superan, notificando por
**correo electrónico**.

- Es útil para mantener el control del coste, especialmente al practicar en una cuenta real de AWS.
- Los umbrales se pueden basar en:
  - El **coste real** ya generado.
  - El **coste previsto** — permite ser notificado con antelación, antes de que se llegue a superar
    el presupuesto.

## Tipos de presupuesto

| Tipo                                   | Descripción                                                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Cost Budget**                        | El más común. Controla el coste en términos monetarios. Es el que se usa habitualmente para este curso.                      |
| **Usage Budget**                       | Disponible para algunos servicios. Controla el **uso** (no el coste directamente) como forma indirecta de contener el gasto. |
| **Savings Plans / Reservation Budget** | Para quienes usan **Savings Plans** o instancias reservadas — ayuda a entender qué tan eficientemente se están aprovechando. |

## Coste de AWS Budgets

- Los presupuestos normales son **totalmente gratuitos**.
- Los **Budget Actions** (presupuestos habilitados para ejecutar una acción automática, por ejemplo
  relacionada con IAM) tienen un límite de **2 gratuitos**; a partir del tercero se cobra
  **$0.10 por presupuesto al día**.
- Para este curso basta con el envío de **notificaciones**, que es gratuito.

> ⚠️ Un Cost Budget con notificación por correo (sin Budget Actions) es totalmente gratis — es la
> opción recomendada para practicar sin generar coste adicional por el propio presupuesto.
