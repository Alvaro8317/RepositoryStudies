# Pruebas unitarias y de integración

## Pruebas unitarias

Están enfocadas a pequeñas piezas a probar, ejemplo, probar una llanta de un vehículo

## Pruebas de integración

Están enfocadas a probar múltiples piezas que funcionan entre sí, ejemplo, probar como funciona la llanta con el resto del vehículo

## Características de las pruebas

Deben de ser:

- Fáciles de escribir
- Fáciles de leer
- Confiables
- Rápidas
- Principalmente unitarias

Estos pasos se les conoce como AAA:

- Arrange -> Se prepara el estado inicial, se inicializan variables, se realizan las importaciones necesarias, etc
- Act -> Se realizan las acciones o estímulos al sujeto de pruebas, como llamar métodos, simular clicks, realizar acciones sobre el paso anterior
- Assert -> Observa el comportamiento resultante, valida si los resultados son los esperados.

Algunos mitos son que las pruebas hacen que la aplicaciones no tenga errores, que las pruebas no pueden fallar (como faltos positivos o falsos negativos), que hacen más lenta la aplicación, que es una pérdida de tiempo (En parte puede ser verdad si se prueban cosas que ya fueron probadas como una dependencia externa), que hay que probar todo (se puede probar el critical path) y todo esto es falso.
