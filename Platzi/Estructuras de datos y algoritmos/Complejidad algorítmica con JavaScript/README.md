# Complejidad Algorítmica con JavaScript

## Temas a tratar en el curso

- **Comprender el concepto de complejidad algorítmica**.
- **Evaluar la eficiencia de los algoritmos** en términos de tiempo y espacio.
- **Aprender a seleccionar algoritmos óptimos** según el consumo de recursos y el contexto de uso.

## ¿Por qué aprender análisis de algoritmos?

- Permite desarrollar **software más eficiente** al seleccionar algoritmos que optimicen el uso de recursos.
- Es una **habilidad clave en entrevistas técnicas de trabajo**, ya que muchas empresas evalúan la capacidad de resolución de problemas mediante algoritmos.

## Estructura de un algoritmo

### ¿Qué es un algoritmo?

Un algoritmo es una **secuencia de instrucciones ordenadas** para resolver un problema, que generalmente incluye:

1. **Entrada**: Datos necesarios para el proceso.
2. **Proceso**: Serie de pasos o instrucciones.
3. **Salida (opcional)**: Resultado del proceso aplicado a la entrada.

El análisis de algoritmos se centra en aquellos que tienen al menos una entrada (input), ya que esta afecta directamente la eficiencia y el uso de recursos.

## Cómo elegir un buen algoritmo

Para resolver un problema, pueden existir múltiples algoritmos. Elegir el adecuado depende de factores como el tiempo de ejecución, el espacio en memoria y las limitaciones del entorno. Ejemplos:

- **Aplicaciones ligeras** priorizan el uso reducido de espacio.
- **Dispositivos embebidos** requieren una memoria eficiente.
- **Aplicaciones web con JavaScript** optimizan el tiempo de ejecución para mejorar la experiencia del usuario.

### Tiempo de un algoritmo

Evalúa cuánto tiempo tarda en procesar una entrada dada. Se mide generalmente con **complejidad temporal** (Big O), observando cómo crece el tiempo de ejecución con el tamaño de la entrada.

### Espacio de un algoritmo

Indica cuánta memoria en RAM utiliza un algoritmo. Incluye tanto el espacio para los datos de entrada como el **espacio auxiliar** adicional que necesita el algoritmo.

## Complejidad Algorítmica

### Introducción

La **complejidad algorítmica** mide el crecimiento del uso de recursos (como tiempo y espacio) en función del tamaño de la entrada. Este análisis permite optimizar el rendimiento en escenarios de gran escala y se basa en la **teoría de la complejidad**, que estudia el consumo de recursos a medida que aumenta el tamaño de los datos.

### Teoría de la Complejidad

Esta teoría analiza el uso de recursos, como tiempo y memoria, y evalúa la **escalabilidad** de los algoritmos. Más allá de los valores numéricos, se enfoca en el "big picture" o comportamiento del algoritmo ante el aumento de datos de entrada.

## Complejidad Espacial

La **complejidad espacial** mide la cantidad de memoria que un algoritmo utiliza al ejecutarse. Es clave cuando se procesan grandes volúmenes de datos o en entornos con limitaciones de memoria.

### Espacio Auxiliar

La complejidad espacial incluye el **espacio auxiliar**, espacio adicional que el algoritmo necesita más allá de los datos de entrada. Este espacio es importante en algoritmos que dependen de estructuras temporales como pilas o matrices.

## Complejidad Temporal

Es el tiempo que un algoritmo tarda en ejecutarse, evaluando cómo este tiempo crece en relación al tamaño de los datos de entrada. La **complejidad temporal** se mide en función de cómo aumenta el tiempo en lugar de segundos exactos.

## Medir la Complejidad Temporal en JavaScript

JavaScript ofrece herramientas como `performance.now()` para medir el tiempo entre líneas de código en milisegundos, una opción más precisa que `console.time`.

## El Estado de la Complejidad

La complejidad algorítmica mide no solo tiempo y espacio, sino también aspectos como accesos a memoria y comparaciones. La **notación Big O** simplifica la complejidad al centrarse en el término de crecimiento más significativo, proporcionando una visión clara de la escalabilidad del algoritmo.

## Análisis Asintótico

El **análisis asintótico** es un método utilizado para describir el comportamiento de una función a medida que su entrada crece hacia un límite (por lo general, cuando tiende al infinito). Este enfoque permite analizar cómo escalan los algoritmos en términos de tiempo o espacio cuando los datos de entrada aumentan.

## Notación Big-O

La **Notación Big-O** es una forma estándar de medir la eficiencia de un algoritmo, similar a la notación científica en matemáticas, diseñada para simplificar y expresar de forma clara la complejidad de un algoritmo. Big-O nos ayuda a identificar y comunicar el comportamiento de un algoritmo en términos de los "peores casos" posibles, es decir, aquellos en los que el consumo de recursos es más alto.

### ¿Por qué se necesita una notación?

La notación Big-O permite:

- **Simplificar explicaciones**: Proporciona una forma compacta de describir el crecimiento de recursos necesarios para un algoritmo.
- **Identificar la eficiencia en casos extremos**: Big-O se centra en el rendimiento en el peor de los casos, siendo útil para evaluar la estabilidad y eficiencia de un algoritmo bajo cargas elevadas.

### Clases de Big-O

Big-O se clasifica en varias categorías según cómo escala el tiempo o el espacio de un algoritmo en función del tamaño de los datos de entrada. Algunas de las más comunes son:

- **Constante**: \( O(1) \)
- **Logarítmica**: \( O(\log n) \)
- **Lineal**: \( O(n) \)
- **Cuadrática**: \( O(n^2) \)
- **Exponencial**: \( O(2^n) \)

Cada una de estas clases ayuda a comparar y seleccionar algoritmos adecuados en función de la eficiencia que se necesita.

## Cálculo de la Notación Big-O

El cálculo de la notación Big-O varía según si se quiere medir la **complejidad temporal** o la **complejidad espacial** de un algoritmo.

### Complejidad Temporal - Cálculo

La **complejidad temporal** evalúa el número de ejecuciones que un algoritmo realiza para completar su tarea en función del tamaño de la entrada.

Ejemplos comunes de complejidad temporal:

```javascript
let bar = 'test'; // O(1) - constante, ya que la operación toma el mismo tiempo sin importar el tamaño de la entrada

if (condition) {
  // O(1) - también constante
  // código
}

for (let i = 0; i < n; i++) {
  // O(n) - lineal, la operación depende del tamaño de 'n'
  // código
}

while (i < n) {
  // O(n) - lineal, se ejecuta 'n' veces
  // código
}

for (let i = 0; i < n; i++) {
  // O(n^2) - cuadrática, doble bucle anidado
  for (let j = 0; j < n; j++) {
    // código
  }
}
```

### Complejidad Espacial - Cálculo

La **complejidad espacial** mide la cantidad de memoria que un algoritmo necesita para ejecutar. Esto incluye el espacio necesario para las variables, estructuras de datos temporales y otras estructuras auxiliares.

Ejemplos comunes de complejidad espacial:

```javascript
let bar = 'test';  // O(1) - constante, solo se declara una variable

if (condition) {   // O(1) - constante
  // código
}

for (let i = 0; i < n; i++) {   // O(1) - constante, aunque es un bucle, no requiere almacenamiento adicional significativo
  // código
}

let resultado = [1, 2, ..., n];   // O(n) - lineal, el tamaño del arreglo crece con 'n'

let dimensional = [[2, 4], [6, 8], [10, 12]];   // O(n^2) - cuadrática, el tamaño crece con n * n
```

Cuando se necesita almacenar datos en estructuras de dimensión **unidimensional**, el consumo de espacio es **O(n)**; mientras que en estructuras de dimensión **NxN** o **multidimensionales**, el consumo de espacio puede ser **O(n^2)** o más, dependiendo de las dimensiones.

### Simplificación de la Notación

La notación Big-O se centra en la eficiencia en los casos de gran escala y, por tanto, ignora las constantes y otros factores menores para concentrarse en los aspectos más relevantes del crecimiento de un algoritmo. Esto permite que la notación Big-O represente solo el comportamiento asintótico, es decir, el crecimiento de recursos a medida que la entrada aumenta.

La complejidad de un algoritmo nace de cuántos recursos utiliza el algoritmo al ejecutarse. La notación Big-O solo se enfoca en el crecimiento más no en datos absolutos ya que estos varían del entorno como el procesador.

## Recomendaciones para la Evaluación de Algoritmos

Al evaluar algoritmos, es crucial considerar varios factores más allá de la complejidad teórica. A continuación, se presentan algunas recomendaciones clave:

### ¿Es realmente importante que siempre sea constante?

No siempre es necesario que un algoritmo tenga complejidad **constante (O(1))** para ser eficiente. Aunque **O(1)** es ideal porque no depende del tamaño de la entrada, puede haber situaciones en las que un algoritmo constante sea lento por otras razones, como operaciones complejas o interacciones con hardware antiguo.

La teoría de la complejidad **trasciende el poder computacional**. Esto significa que el análisis teórico de la complejidad sigue siendo útil incluso con computadoras de diferentes capacidades, ya que el crecimiento relativo de los algoritmos en términos de recursos necesarios mantiene un comportamiento similar. Sin embargo, en una computadora antigua, los tiempos podrían ser más largos en términos absolutos, aunque el patrón de crecimiento sea igual al de una computadora actualizada.

### ¿El crecimiento siempre importa?

El crecimiento de un algoritmo se vuelve crítico cuando su **complejidad comienza a comprometer su eficiencia**, especialmente a medida que aumenta el tamaño de la entrada. Si un algoritmo tiene una complejidad exponencial (por ejemplo, O(2^n)), su tiempo de ejecución crecerá rápidamente con una entrada ligeramente más grande, volviéndolo impráctico.

Cuando la complejidad de un algoritmo se vuelve ineficiente, es un indicio de que se deben considerar **mejoras en el algoritmo** o en su implementación para alcanzar el objetivo de eficiencia. Optimizar la complejidad permite que el algoritmo sea más escalable y eficiente en diversos contextos.

### ¿Cómo usar correctamente el análisis asintótico?

El análisis asintótico se aplica adecuadamente cuando:

1. **Se busca simplificar y prever el comportamiento del algoritmo**: Permite evaluar cómo el algoritmo se comportará en grandes escalas de datos.

2. **Se comparan diferentes algoritmos para la misma tarea**: Si dos algoritmos resuelven el mismo problema, el análisis asintótico ayuda a identificar cuál es más eficiente para grandes entradas.

3. **Se considera el contexto y los recursos**: La eficiencia depende de la combinación entre el tipo de problema, los recursos disponibles y el tamaño de los datos de entrada. Por ejemplo, para una aplicación en un dispositivo de baja potencia, la complejidad espacial podría ser tan relevante como la temporal.

En resumen, el análisis asintótico es una herramienta valiosa para seleccionar y optimizar algoritmos, pero debe usarse junto con consideraciones prácticas y el contexto en que se ejecutará el algoritmo.
