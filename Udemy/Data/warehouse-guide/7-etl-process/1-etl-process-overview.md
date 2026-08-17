# Visión general del proceso ETL

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Ahora que ya se sabe cómo modelar los datos dimensionalmente, se está listo para ver cómo llevar ese
modelo a la práctica usando el proceso `ETL`: traer los datos de las fuentes, transformarlos según el
modelo dimensional diseñado, y cargarlos en el `Data Warehouse`.

## Repaso: fuentes de datos y capas

Como ya se ha visto en secciones anteriores, los datos del `Data Warehouse` pueden venir de fuentes
muy distintas, y hay que integrarlas, limpiarlas y transformarlas. Todo esto se hace con una
herramienta `ETL`, que estructura el proceso en tres pasos:

1. **`Extract`** — extraer los datos de las fuentes de datos.
2. **`Transform`** — transformar los datos.
3. **`Load`** — cargar los datos transformados en la ubicación centralizada final (el `Data
   Warehouse`).

Este proceso se apoya en las distintas capas del `Data Warehouse`:

- De las fuentes de datos se extrae primero hacia la **`Staging Area`** — aquí los datos ya están en
  tablas, puede que con alguna limpieza básica, con toda la información pertinente ya extraída.
- Durante la carga de `Staging` a `Core` es donde se aplica el **modelado dimensional**: se toman los
  datos de `staging`, se transforman, y esos datos transformados se cargan en el `Core`.
- Desde el `Core`, los datos se pueden usar con distintas aplicaciones, y en la mayoría de los casos
  tiene sentido tener un **`Data Mart`** adaptado a un caso de uso específico — esto mejora tanto la
  usabilidad como el rendimiento, y por tanto el valor del `Data Warehouse`.

## Herramientas ETL

En la práctica, el `ETL` se implementa con **herramientas ETL** (hay muchas disponibles en el
mercado — se profundizará en algunas más adelante). Estas herramientas son, básicamente, un conjunto
de utilidades integradas para:

- **Conectarse a distintas fuentes de datos** y extraer los datos (`Extract`).
- **Transformar los datos**: cambiar tipos de datos, añadir columnas adicionales, limpiar los datos,
  y remodelarlos — esta suele ser la parte principal del proceso `ETL`.
- **Escribir los datos de nuevo** en distintos formatos y destinos — en este curso, interesa
  particularmente escribirlos de vuelta en bases de datos (el `Data Warehouse`).

> ⚠️ Las herramientas ETL suelen ofrecer miles de funcionalidades distintas, pero normalmente solo se
> usa un subconjunto muy pequeño de ellas — en este caso, el necesario para construir el `Data
> Warehouse`.

## Workflows y jobs

Con una herramienta `ETL` se suelen configurar **workflows** (flujos de trabajo) separados para cada
capa/fase del proceso — por ejemplo, un workflow para `Staging`, otro para `Core`, y normalmente
también uno para el `Data Mart`. Esto no es una regla fija, sino una estrategia habitual por defecto.

Un workflow típico se arma con componentes de arrastrar y soltar: se configuran credenciales y
detalles de conexión para extraer datos específicos, se aplican las transformaciones necesarias, y al
final se escriben los resultados de vuelta en las tablas correspondientes.

De forma correspondiente a estos workflows separados por capa, la base de datos del `Data Warehouse`
suele tener un **esquema distinto por capa** (`staging`, `core`, `data mart`) — aunque también sería
posible usar una base de datos separada por capa.

Una vez configurados los workflows, se programan mediante **`jobs`**: estos `jobs` ejecutan los
workflows según reglas definidas — es decir, en momentos concretos y con frecuencias específicas —
para realizar la extracción, limpieza y transformación de los datos.

## Próximas clases

Profundizar en los distintos pasos y procesos concretos que forman el proceso `ETL`.
