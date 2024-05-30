# Mocks

Un mock es un objeto dummy, un objeto falso que devuelve lo que nosotros queremos o necesitamos para usar dentro del
test.

## Monkey patching

Es una técnica que permite modificar el pedazo de un código en tiempo de ejecución.

## Mocks para dummies

Un mock es un objeto que imita el comportamiento de otro objeto real de una manera controlada.

### Lazy methods y lazy attributes

Estos significan que un mock debe de crear estos atributos o métodos cuando los necesite.

### Side effect

Permiten ejecutar una función o excepción cuando corra un mock

### Magick Mock

Es una subclase o herencia de la clase Mock, pero tiene implementaciones
por defecto en casi todos mos métodos mágicos, es decir, sin tener que configurar
uno mismo los métodos mágicos. Es decir, sin hacer un mock desde cero.
Cuando se utilizan métodos mágicos, estos siguen generando Magick Mocks

## Documentación:

https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html