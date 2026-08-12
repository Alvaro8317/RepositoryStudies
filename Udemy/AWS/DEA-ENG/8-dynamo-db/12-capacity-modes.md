# Modos de capacidad de DynamoDB

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

DynamoDB se puede configurar con dos **modos de capacidad** distintos, que determinan tanto el
**coste** como el **rendimiento** y se adaptan a diferentes tipos de carga de trabajo: **On-Demand** y
**Provisioned**.

## On-Demand

- El rendimiento de lectura/escritura se factura **por solicitud** — no hace falta especificar la
  capacidad de antemano.
- Ideal cuando **no se conoce la carga de trabajo**, o cuando el tráfico es **esporádico/variable**
  con picos difíciles de predecir.
- Ofrece un rendimiento **consistente y de baja latencia** a cualquier escala, y las solicitudes
  **nunca sufren throttling** — el rendimiento siempre está asegurado.
- No requiere gestión ni planificación de capacidad: todo lo gestiona AWS automáticamente.

> ⚠️ Esta flexibilidad tiene un coste: On-Demand es **más caro** que Provisioned. Para cargas de
> trabajo predecibles, sale más rentable usar el modo Provisioned.

## Provisioned

- Pensado para cargas de trabajo **predecibles**: hay que especificar explícitamente el rendimiento
  de lectura y escritura por segundo, mediante **RCU** (*Read Capacity Units*) y **WCU** (*Write
  Capacity Units*).

  > Qué son exactamente RCU y WCU se cubre en detalle en la siguiente clase.

- Es el modo **más económico**, ya que solo se paga por la capacidad especificada.
- Existe una función de **auto-escalado** que ajusta la capacidad automáticamente en función del
  tráfico real (ver más abajo).
- Riesgo: si el rendimiento real supera la capacidad provisionada, las solicitudes adicionales sufren
  **throttling**. Requiere planificación de capacidad más cuidadosa y monitorización continua para
  evitar problemas de rendimiento — más carga operativa que On-Demand.

### Capacidad reservada (Reserved Capacity)

Opción de facturación disponible para el modo Provisioned: permite comprometerse a una cantidad
específica de capacidad (RCU/WCU) durante un periodo de **1 o 3 años**, a cambio de un **descuento**
frente al precio estándar de Provisioned (o de On-Demand).

- Requiere pago por adelantado y un compromiso a largo plazo.
- Adecuado para aplicaciones **muy estables**, con tráfico predecible de forma fiable a largo plazo.

### Auto Scaling

Mecanismo que se usa junto con el modo Provisioned para ajustar dinámicamente la capacidad de lectura
y escritura de una tabla, en función de las tasas de uso reales — ayuda a optimizar el coste.

- Requiere configurar valores **mínimo**, **máximo** y **objetivo** de capacidad.
- No es tan flexible ni inmediato como On-Demand: puede haber un **ligero desfase** en la respuesta a
  cambios de tráfico (se ajusta con base en el histórico), lo que puede provocar throttling puntual
  mientras se escala.

## Resumen

| Modo            | Cuándo usarlo                               | Coste                               | Gestión requerida                                            |
| --------------- | ------------------------------------------- | ----------------------------------- | ------------------------------------------------------------ |
| **On-Demand**   | Carga de trabajo desconocida o muy variable | Más caro (por solicitud)            | Ninguna — gestionado por AWS                                 |
| **Provisioned** | Carga de trabajo predecible                 | Más barato (capacidad fija/RCU-WCU) | Planificación de capacidad + monitorización (o Auto Scaling) |
