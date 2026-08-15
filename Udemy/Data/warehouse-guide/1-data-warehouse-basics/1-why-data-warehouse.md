# ¿Por qué necesitamos un Data Warehouse?

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Los dos propósitos del uso de datos en una empresa

Para entender por qué una empresa necesita un **Data Warehouse**, primero hay que distinguir los dos
propósitos distintos con los que se usan los datos:

1. **Fines operativos**: usar los datos para que la empresa funcione día a día — recibir y tramitar
   pedidos, gestionar reclamaciones, reponer existencias, etc. Es "mantener la rueda girando".
2. **Fines analíticos**: usar los datos para tomar mejores decisiones de cara al futuro y entender
   mejor el negocio. Aquí se busca responder preguntas como:
   - ¿Cuál es la mejor categoría en la que estamos vendiendo productos?
   - ¿Cuál es el número de ventas de este mes comparado con el mes pasado?
   - ¿Qué podemos hacer para mejorar las cosas en la empresa?

Mientras que los datos operativos sirven para que "la rueda siga girando", el tratamiento analítico
sirve para **observar cómo gira esa rueda** y decidir qué mejorar.

## OLTP vs. OLAP

Estos dos propósitos le dan nombre a dos formas distintas de procesar datos:

| | **OLTP** (Online Transaction Processing) | **OLAP** (Online Analytical Processing) |
|---|---|---|
| Propósito | Mantenimiento de datos operativos | Procesamiento analítico de datos |
| Unidad de trabajo | Un registro a la vez (insertar/editar) | Miles o millones de registros a la vez |
| Foco temporal | Solo datos actuales (poco histórico) | Datos a lo largo del tiempo (se necesita historial) |
| Objetivo de rendimiento | Procesar transacciones rápido | Rendimiento de consulta rápido sobre grandes volúmenes |
| Ejemplo de uso | Registrar un pedido nuevo | Promedio de ventas de los últimos 6 meses |

> ⚠️ OLTP y OLAP tienen requisitos tan distintos (una fila vs. millones de filas, poco histórico vs.
> mucho histórico, escritura frecuente vs. lectura analítica) que tiene sentido mantenerlos como
> **sistemas separados** en vez de forzar un único sistema a cubrir ambos casos de uso.

## Señales de que falta un Data Warehouse

La ausencia de un Data Warehouse en una empresa suele notarse en afirmaciones como:

- "Tenemos muchos datos, pero no los usamos realmente" porque acceder a ellos es complicado.
- "Es muy difícil analizarlos" porque están repartidos en diferentes sistemas de la empresa.
- "Solo quiero ver lo que es relevante" y tenerlo accesible de forma rápida y sencilla.
- "Queremos tomar decisiones basadas en hechos" y dejar de discutir sobre los números.

## Definición de Data Warehouse

Un **Data Warehouse** existe precisamente para atender las necesidades analíticas (OLAP) de una
empresa, separadas del sistema operativo (OLTP).

> Un Data Warehouse es una ubicación de datos que se utiliza para la presentación de informes
> (reporting) y el análisis de datos.
