# Tipos de hechos según su aditividad

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

## Por qué importa la aditividad

Los hechos suelen ser valores numéricos, y sumar valores numéricos es la operación más intuitiva
para análisis y reportes (ej. en `Power BI`). Pero no todos los hechos se pueden sumar de la misma
forma — a veces el total simplemente no tiene sentido de negocio. Por eso se distinguen **tres
tipos de hechos** según su aditividad.

## 1. Hecho completamente aditivo (`Fully Additive`)

El tipo **más común**. Se puede sumar a través de **todas** las dimensiones, y el total resultante
sigue siendo significativo. Es el tipo con **mayor valor analítico**, por su flexibilidad.

### Ejemplo: unidades vendidas

| Venta | Unidades vendidas |
| ----- | ----------------- |
| 1     | 3                 |
| 2     | 1                 |
| 3     | 2                 |
| 4     | 2                 |
| 5     | 2                 |

Sumar todas las filas da **10 unidades vendidas en total** — una cifra con sentido. Y esto se
cumple sin importar por qué dimensión se agrupe: por categoría, por nombre de producto, o por
fecha (sumando a través de todas las categorías y productos, se obtiene el total vendido por día).

## 2. Hecho semi-aditivo (`Semi-Additive`)

Solo se puede sumar a través de **algunas** dimensiones, no de todas. Es menos flexible que un
hecho completamente aditivo.

### Ejemplo típico: saldo de cuenta (`account balance`)

| Fecha | Tipo de cartera | Saldo |
| ----- | --------------- | ----- |
| Día 1 | Tipo 1          | $50   |
| Día 2 | Tipo 1          | $100  |
| Día 3 | Tipo 1          | $100  |
| Día 1 | Tipo 2          | $120  |
| Día 2 | Tipo 2          | $150  |

- **Sí tiene sentido** sumar el saldo **a través del tipo de cartera**, para un mismo día: por
  ejemplo, día 1 → $50 (tipo 1) + $120 (tipo 2) = $170 en total ese día.
- **No tiene sentido** sumar el saldo **a través de las fechas**: sumar $50 + $100 + $100 del tipo 1
  no da "$250 en la cuenta" — el saldo real al final es simplemente el último valor, $100. Sumar
  saldos de distintos días no representa nada real.

> ⚠️ La dimensión de **fecha** es el ejemplo típico donde un hecho semi-aditivo (como un saldo) no
> se puede sumar — el saldo es un "punto en el tiempo", no algo que se acumula sumando cada día.

Una alternativa común para analizar un hecho semi-aditivo a través de la dimensión problemática
(ej. fecha) es usar el **promedio** en vez de la suma (ej. saldo promedio diario), aunque hay que
tener cuidado de no sumarlo por error en dimensiones donde no corresponde.

## 3. Hecho completamente no aditivo (`Non-Additive`)

No se puede sumar **en ninguna dimensión**. Es el tipo con **menor valor analítico**, y requiere
más cuidado al usarlo.

### Ejemplo: precio unitario

Si se tiene `unidades vendidas` y `precio por unidad`, el **ingreso** (`unidades × precio`) sí es
completamente aditivo. Pero el `precio por unidad` en sí **no lo es**: sumar los precios de varios
productos y obtener "el precio total de una categoría" no tiene ningún sentido de negocio.

> ⚠️ Incluso el promedio es delicado con hechos no aditivos: para el precio, un promedio simple
> puede ser engañoso — hace falta un **promedio ponderado** por la cantidad de unidades vendidas
> para que el resultado sea correcto.

Otros ejemplos típicos de hechos no aditivos: **porcentajes** y **ratios** (ej. nivel de stock en
un almacén) — normalmente no tiene sentido sumarlos.

## Cómo manejar los hechos no aditivos

Dado su bajo valor analítico, hay quienes incluso recomiendan no incluirlos directamente en la
tabla de hechos. Un método mejor es **almacenar los valores subyacentes** en vez del ratio ya
calculado — por ejemplo, guardar el numerador y el denominador por separado, y calcular el ratio
final en la herramienta de BI (ej. `Power BI`).

> ⚠️ Guardar los valores subyacentes (en vez del resultado ya calculado) da el mayor valor
> analítico posible para un hecho no aditivo, ya que permite recalcularlo correctamente en
> cualquier combinación de dimensiones.

## Resumen

| Tipo                  | ¿Se puede sumar?            | Valor analítico | Ejemplo                        |
| --------------------- | --------------------------- | --------------- | ------------------------------ |
| Completamente aditivo | En todas las dimensiones    | Alto            | Unidades vendidas              |
| Semi-aditivo          | Solo en algunas dimensiones | Medio           | Saldo de cuenta (no por fecha) |
| No aditivo            | En ninguna dimensión        | Bajo            | Precio unitario, ratios, %     |
