## Testing con golang
¿Por qué es importante testear?
Por la calidad, que se sabe que se le puede enviar algo mal a la aplicación y no se va a dañar la app

Los archivos de test se llaman casi igual que los archivos pero finalizan con un _test

Para ejecutar los tests de la ruta actual o correr los test en general, se usa:
```bash
go test
```
Para ejecutar todos los tests dentro de un directorio, se usa este comando:
```bash
go test ./util
```
Para añadirle "verbosidad" al comando, usar la bandera -v, ejemplo
```bash
go test ./util -v
```
Para correr un solo test, se puede especificar el nombre del test de la siguiente manera:
```bash
go test ./util -run=TestParserPokemonSuccess -v
```
## Excepciones
Las excepciones en go NO EXISTEN, pero existe panic, aunque este corta la ejecución de todo, se recomienda evitar su uso, aunque el acceder a índices de array que no existe, podría generar un panic

Con go, se tiene un paquete de errors que permite personalizarlas

## Mocks
Un mock es una simulación de un objeto o una función real, es perfecto para unit testing y así aíslar múltiples comportamientos, así se puede testear lo que está a mi alcance. ¿Cuándo hacer mocks?
- Llamadas a API externas
- Interacciones con la BD
- Simular errores de paquetes externos
- **Siempre que se necesite simular un comportamiento**