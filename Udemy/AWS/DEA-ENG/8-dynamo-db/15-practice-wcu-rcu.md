# Práctica: calculadora de capacidad y pricing (WCU/RCU)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada en la consola sobre las [[14-wcu-rcu|unidades de capacidad]] en el modo
**Provisioned**: la calculadora de capacidad al crear una tabla, la comparativa de precios frente a
**On-Demand**, y cómo se refleja el consumo real de RCU al operar sobre una tabla.

## Calculadora de capacidad al crear una tabla

Las unidades de capacidad (WCU/RCU) solo aplican al modo **Provisioned** — en **On-Demand** no hace
falta especificarlas.

- Al crear una tabla, con **Customize settings** y modo **Provisioned**, la consola ofrece una
  **calculadora de capacidad** que muestra cuántas WCU/RCU se necesitarían para un rendimiento dado.
- Recomendable jugar con los valores e intentar calcular el resultado a mano antes de verlo, para
  asegurarse de dominar la fórmula de cara al examen (ver [[14-wcu-rcu|cálculos de ejemplo]]).
- Ejemplo: con un tamaño de elemento de **5 KB** y lectura **fuertemente consistente**, la calculadora
  muestra **2 RCU** — 5 KB no cabe en un bloque de 4 KB, así que se redondea a 2 bloques.
- Al aumentar el valor de entrada, el número de unidades de capacidad requeridas aumenta en
  consecuencia, siguiendo la misma lógica de redondeo.

## Provisioned vs. On-Demand: precios

En la página de precios de DynamoDB:

- **Provisioned** — se paga por unidad de capacidad **aprovisionada por hora**, se use o no. Las
  unidades se definen tal como ya se vio: por segundo, hasta 1 KB (WCU) o hasta 4 KB (RCU).
- **On-Demand** — se paga **por solicitud** realizada, no por capacidad reservada. Aquí la unidad se
  define **por solicitud** (no por segundo): cada solicitud de escritura de hasta 1 KB, y el precio se
  cobra por millón de solicitudes.

> ⚠️ No hace falta memorizar los precios exactos para el examen, pero sí tener una idea aproximada de
> la diferencia de coste entre ambos modos.

Con un rendimiento **constante y predecible**, Provisioned puede salir aproximadamente **7-8 veces
más barato** que On-Demand — el escenario ideal para el modo Provisioned. Pero esto depende del caso
de uso: si la carga de trabajo tiene picos repentinos o es muy inestable, On-Demand puede seguir
siendo la opción más rentable pese a su precio unitario más alto.

## Consumo real de capacidad en la consola

Al explorar los elementos de una tabla (por ejemplo, con la acción **Scan**), la consola muestra
cuánta capacidad se ha consumido realmente en esa operación.

- Un Scan puede consumir, por ejemplo, **0.5 RCU** — el valor exacto depende de la acción concreta
  realizada y de los datos leídos.
- Repetir la misma operación puede dar un resultado de consumo distinto, útil para comprobar en vivo
  cómo se traduce una acción en unidades de capacidad consumidas.

## Próxima clase

Con la calculadora de capacidad y el pricing ya vistos en la práctica, la siguiente clase profundiza
en las mejores prácticas y mecanismos para mejorar el rendimiento y evitar el throttling.
