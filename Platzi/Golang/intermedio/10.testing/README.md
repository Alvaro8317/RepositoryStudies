## Testing
Los archivos deben de tener el sufijo _test, para usar el testing, se tiene que estar dentro de un modulo

Un código entre más tests tenga en el code coverage, dá más confianza

Para obtener que parte del código se ha testeado y cuál no, se puede hacer uso de:
```bash
go test -coverprofile=coverage.out
```
Esto generará un archivo coverage.out y para obtener las métricas, se usa go tool, para este caso, se usará el tool cover, ejemplo:
```bash
go tool cover -func=coverage.out
```
Este generará una salida con las funciones ya probadas y qué hace falta

## Profiling
¿Cómo optimizar un programa? El profiling es una herramienta que colabora para solucionar este problema, para generar el informe (similar al coverage) se debe de usar el siguiente comando
```bash
go test -cpuprofile=cou.out
```
Esto generará el archivo cou.out mientras que corre los tests y ya generado, se usa el siguiente:
```bash
go tool pprof cou.out
```
Esto ejecutará una CLI pprof y aquí aplican los siguientes comandos:
- top -> Como se ha comportado los programas que ejecutó el test
- list FunctionToProfile -> Muestra un detalle de en qué punto se generó la demora
- web -> Muestra un diagrama de flujo en HTML
- pdf -> Genera el diagrama de flujo en PDF

## Mock
Los mocks se utilizan cuando se requiere un test unitario y que un método hace una consulta a una base de datos, los mock service simulan la base de datos