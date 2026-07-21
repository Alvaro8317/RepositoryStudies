# Práctica: Cost Explorer y AWS Budgets

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Cost Explorer

Dentro de **Billing and Cost Management**, el **Cost Explorer** permite revisar el coste y uso de
la cuenta:

- Vista previa del coste de todos los servicios, desglosada por **mes** y por **servicio**.
- También ofrece una vista tabular con más detalle.
- Se puede **filtrar** por distintas categorías: servicio (ej. solo Athena), región, y también por
  **Tags**.

> Etiquetar (Tag) los recursos al crearlos permite categorizar el coste de forma personalizada —
> por ejemplo, por departamento, unidad de negocio o proyecto — y así saber cuánto cuesta cada uno.
> Es una práctica muy habitual en cuentas reales.

## Crear un Budget

Los **Budgets** se configuran también dentro de Billing and Cost Management, en el apartado
**Budgets** del menú lateral. Al crear uno (botón **Create budget**) hay dos formas:

- **Usar una plantilla** (template) — más rápido y ya preconfigurado.
- **Personalizado** (custom) — igual de sencillo, en 4 pasos.

### Presupuesto de gasto cero (zero-spend budget)

- Se puede crear directamente con la plantilla de **Zero spend budget**.
- Alerta al superar **$0.01** de gasto.
- Solo hace falta darle un nombre y una dirección de correo electrónico para la notificación.
- Sirve para detectar en cuanto se supera la capa gratuita (Free Tier) o se empieza a usar algún
  servicio de pago (por ejemplo, **Glue**).

### Presupuesto de $5 (custom, paso a paso)

1. **Tipo de presupuesto**: elegir **Cost budget** (seguimiento del coste real, no solo uso).
2. **Configuración**:
   - Nombre (ej. `5 USD budget`).
   - Periodo: **mensual**, recurrente (se renueva cada mes, sin caducar).
   - Mes inicial: el mes en curso.
   - Método de presupuestación: **fijo** (no ajustar automáticamente).
   - Importe: **$5**.
   - Servicios incluidos: todos (valor por defecto, sin exclusiones).
3. **Alertas**: añadir un umbral de alerta, que puede definirse por:
   - **Porcentaje** del presupuesto (ej. 80%).
   - **Valor absoluto** en USD.
   - Se indica la dirección de correo electrónico a la que se enviará la notificación al superar el
     umbral.
4. **Acciones**: no se añade ninguna acción adicional → el presupuesto sigue siendo gratuito
   (sin Budget Actions).
5. Revisar y **crear el presupuesto**.

## Seguimiento del presupuesto

Una vez creados, cada Budget muestra en su resumen:

- **Coste actual** utilizado.
- **Coste previsto** (forecast).
- **Actual vs. presupuestado** (ej. "73% ya utilizado").

> ⚠️ Configurar el presupuesto de gasto cero **y** el de $5 antes de empezar la parte práctica de
> Glue ayuda a detectar cualquier coste inesperado a tiempo, en vez de descubrirlo en la factura.
