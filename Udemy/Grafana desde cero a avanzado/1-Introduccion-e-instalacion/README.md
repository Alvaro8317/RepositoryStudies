# Grafana desde cero a avanzado

Grafana es la herramienta líder para visualizar datos, durante este curso se verá:

- Instalación de grafana
- Usar y gestionar fuentes de datos
- Crear dashboards
- Manejar visualizaciones
- Plugins
- Métricas
- Entre otros

## Contenido del curso

En detalle el contenido del curso es:

- Introducción a grafana
- Instalación y arranque
- Crear dashboards
- Series de tiempo, bases de datos de series temporales entre otros
- Prometheus para recolectar métricas
- Laboratorios prácticos
- Dashboards dinámicos
- Bases de datos, métricas
- Transformaciones para implementarlos correctamente
- Alertas
- InfluxDB
- Plugins
- Tags
- Snapshots
- Versiones
- Paneles de librería

## Introducción a la observabilidad

Es la capacidad que se tiene para observar los eventos, datos, logs que pueden entregar las aplicaciones. La observabilidad es el contexto de sistemas informáticos se refiere a la capacidad de un sistema para proporcionar información interna que pueda ser usada por productos externos. De esta forma los equipos dev y ops pueden entender el comportamiento de sus sistemas, especialmente en entornos de software distribuido y en la nube.

Se puede aplicar a:

- Diagnóstico de problemas y resolución de incidencias
- Mejora del rendimiento y la eficiencia
- Toma de decisiones basada en datos
- Mejor experiencia del usuario
- Adaptación a entornos dinámicos

### Pilares de la observabilidad

Son los componentes primarios

1. Métricas, datos cuantitativos que proporcionan una medida objetiva del comportamiento y el rendimiento. Son importantes para entender el estado y la salud
2. Registros, también conocidos como logs, son esenciales, son archivos o flujos de datos que registran eventos o acciones que ocurren dentro de una infraestructura, los registros son fundamentales para proporcionar información detallada sobre el comportamiento y el estado de los sistemas
3. Trazas, permiten entender la forma en que las solicitudes o transacciones fluyen a través de un sistema informático, especialmente en arquitecturas distribuidas como los microservicios. Proporcionan una visión detallada del camino que sigue una solicitud individual a través de diferentes servicios y componentes, permitiendo identificar dónde y por qué se producen cuellos de botella

## Introducción a grafana

Es una plataforma open source para visualizar y analizar datos de manera eficiente. Proporciona la capacidad de crear dashboards interactivos que transforman datos complejos en visualizaciones comprensibles para usuarios.

Se puede utilizar para visualizar datos de una amplia gama de fuentes, como bases de datos, servicios de almacenamiento en nube, etc.

Mejora la toma de decisiones a través de visualizaciones claras y es adaptable a una variedad de casos.

Ofrece una gran cantidad de funciones para crear paneles de control personalizados con gráficos, métricas, alertas y notificaciones, plugins, etc.

## Historia de grafana

Creada por Torkel Odegaard porque no le gustaba la herramienta que usaban (Grafite). La interfaz inicial de grafana estaba basada en la versión 3 de Kibana, un dashboard de visualización de datos de ElasticSearch.

En 2015 se volvió un proyecto independiente, 2016 lanzó versión 2 que introdujo una serie de nuevas característcias, en 2017 grafana se volvió un proyecto de la fundación apache, en 2018 se lanzó la versión 5 que introdujo graficos interactivos y mayor integración, en 2020 se lanzó la versión 7 de grafana que introdujo la capacidad de crear paneles de control y se suele sacar una versión anualmente.

Grafaba es una herramienta usada en todo el mundo usada por paypal, ebay, verizon, dapper, etc.

## Opciones para usar grafana

3 opciones:

1. Open source, gratuito y completo, libre para ser usado por cualquier empresa con todo lo necesario
2. Enterprise, pensada para empresas que necesiten trabajar con características críticas, plugins premium, autenticación y seguridad y soporte 24x7
3. Cloud, gestionado por grafana, permite no tener que preparar y mantener nuestra propia infraestructura, diseñada para ambientes enterprise, tiene una capa gratuita de igual manera.

## Grafana play

Es un playground para probar dashboards de grafana, tiene limitaciones pero sirve para tareas simples.

## Otros productos de grafana

Grafana dispone de productos adicionales compuesto por un stack llamado LGTM, que es loki para logs, grafana para visualización, tempo para trazas y mimir para métricas.

### Loki

Es un sistema de agregación de logs escalable horizontalmente, inspirado en prometheus, diseñado para almacenar y consultar registros de todas sus aplicaciones e infraestructura y tiene un lenguaje llamado LogQL, útil para análisis de registros, auditoría de seguridad, cumplimiento de normativas, entre otros.

### Tempo

Es un sistema de seguimiento distribuido de código abierto y fácil de usar, está diseñado para alomacenar y consultar datos de seguimiento de aplicaciones, se puede escalar fácilmente para manejar grandes cantidades de trazas y es compatible con una amplia gama de herramientas de seguimiento.

Almacena datos de seguimiento en un formato timestamp y así hace que sea eficiente para consultar trazas para períodos de tiempo.

### Mimir

Base de datos escalable para almacenar grandes cantidades de trazas y métricas. Compatible con diferentes entornos pero pensado para almacenar datos de Prometheus. Almacena datos de seguimiento y métricas en un formato timestamp

## Instalación de grafana

Hay instalación con instalador o standalone, en caso que sea con instalador se ejecutará todo en C:\Program Files\GrafanaLabs\grafana, con standalone se debe de correr el archivo grafana\bin\grafana-server, en grafana\conf NO SE DEBE de modificar los archivos directamente, hay 2, son defaults.ini y sample.ini, entonces se debe de copiar el sample.ini y crear en base a este el custom.ini, así grafana aplicará lo que tenga en custom.ini.

En linux en modo paquete se deben de hacer las modificaciones en /etc/grafana/grafana.ini
