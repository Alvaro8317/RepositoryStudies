# Grafana desde cero a avanzado

## ¿Qué es un dashboard?

Un dashboard es un componente gráfico de tipo interactivo que se utiliza para visualizar datos de una o varias fuentes de información, compuestos por paneles que permiten ver de forma independiente distintos tipos de datos. Cada panel permite mostrar un tipo diferente de datos y ser representado en barras, series, tablas, mapas y texto.

Antes de hacer un dashboard, se debe de tener la fuente de datos para extraer la información. Una fuente de datos puede ser una conexión a una base de datos, un servicio de almacenamiento en la nube o un sistema de monitorización. Una vez que se tenga la fuente de datos, se pueden crear los paneles.

## Proceso interno de construcción del dashboard

La construcción de un dashboard pasa por una serie de pasos:

1. Fuente de datos, los origenes donde se extraerá la información, pueden ser de muy distinto tipo como CSV, Loki, Prometheus, bases de datos, etc.
2. Plugin, son componentes que extienden las capacidades de grafana, permiten acceder a las fuentes de datos, cada fuente de dato tiene su tipo de dato distinto, oracle no implementa la información como con un csv, entonces un plugin convierte los datos en base a la fuente a **data frames**, estos data frames permiten ser utilizados por grafana.
3. Query, las consultas permiten extraer un dataset, un subconjunto de datos que se quiere mostrar en el dashboard, se pueden encadenar querys o consultas para visualizar los datos que uno necesita. Se puede tener agregaciones y cada plugin debe de tener su propio lenguaje de consulta.
4. Transformación, permiten cambiar y tranformar los datos devueltos por una consulta, por ejemplo, unir campos o cambiar el tipo de datos, permite encadenar transformaciones pero **GRAFANA NO ES UNA ETL**, si se requiere una transformación compleja, se recomienda mejor usar una ETL como fuente
