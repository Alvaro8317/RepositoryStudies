# Curso de Fundamentos de Ingeniería de Datos

La ingeniería de datos no se trata únicamente de modelos y ciencias de datos. Implica formular preguntas importantes, realizar un modelado adecuado, identificar las características y naturaleza de los datos, y combinar estos conocimientos con prácticas de ingeniería de software. Esto permite crear soluciones que no solo sean factibles, sino también escalables y sostenibles. Además, es esencial diseñar una arquitectura e infraestructura robusta que pueda implementarse en una nube como AWS.

El campo de juego para un ingeniero de datos es amplio. Startups son un excelente entorno para aprender, ya que suelen crecer de forma acelerada y requieren soluciones dinámicas. Por otro lado, empresas grandes como Airbnb o Facebook ofrecen especialización en temas específicos, ya que los equipos suelen dividirse en áreas concretas de trabajo.

---

## Tareas que implican ser Data Engineer

El rol de un ingeniero de datos abarca la implementación de **DataOps**, una filosofía que parte de:

1. **Entender el negocio**: Colaborar con científicos de datos para comprender las necesidades y objetivos empresariales.
2. **Preparar y modelar datos**: Procesar, transformar y optimizar datos para ser utilizados en proyectos.
3. **Diseñar proyectos**: Crear código y estructuras de datos (tablas, esquemas, flujos).
4. **Migración y prueba de modelos**: Ajustar modelos entre lenguajes y realizar pruebas exhaustivas.
5. **Automatización**: Implementar scheduling y tareas recurrentes.
6. **Monitoreo**: Crear sistemas de monitoreo de características clave.
7. **Despliegue continuo**: Usar CI/CD para integrar y entregar soluciones dinámicamente.

Esto se traduce en un ciclo de desarrollo que genera entregables incrementales, normalmente organizados en **sprints de producto**.

### Filosofías de DataOps

1. **Agile**:  
   Busca entregar valor de forma continua mediante iteraciones cortas. Los proyectos se dividen en fases como: analizar, planear, diseñar, construir, testear, revisar y lanzar. Es opuesto al modelo Waterfall (cascada), ya que se adapta al cambio constantemente.

2. **Lean**:  
   Complementa a Agile al enfocarse en eliminar desperdicios y optimizar procesos. Los principios clave incluyen: identificar valor, mapear la corriente de valor, crear flujo, establecer pull (basado en demanda) y mejorar continuamente.

3. **DevOps**:  
   Se centra en integrar el desarrollo y las operaciones para garantizar que el código esté disponible, implementado y funcionando de manera eficiente.

**Resumen**: DataOps toma elementos de estas filosofías para orquestar procesos con grandes volúmenes de datos, integrándolos con herramientas y prácticas que aseguren gobernanza y calidad.

Un equipo de DataOps típicamente incluye:

- Ingeniero de datos (Data Engineer)  
- Científico de datos (Data Scientist)  
- Analista BI (Business Intelligence Analyst)  
- Especialista en gobernanza de datos (Data Governance)

---

## Agile en Ingeniería de Datos

La agilidad se implementa mediante dos metodologías clave:

1. **Scrum**:  
   Organiza el trabajo en **sprints**, ciclos de trabajo cortos y planificados. Incluye ceremonias como:  
   - **Daily Standups**: Reuniones diarias para revisar avances.  
   - **Sprint Planning**: Definición de objetivos del sprint.  
   - **Sprint Review**: Evaluación de los resultados obtenidos.  

2. **Kanban**:  
   Usa un tablero visual que divide las tareas en: "Por hacer", "En progreso" y "Finalizado". Es ideal para flujos continuos donde los cambios deben ser rápidos.

---

## Lenguajes de Programación e Ingeniería de Software

Es fundamental diferenciar entre "escribir código" y desarrollar software robusto. Los lenguajes más importantes para ingeniería de datos son:

- **Python**:  
  Popular por su simplicidad y bibliotecas científicas como Pandas, NumPy y PySpark. Ideal para ETL y análisis.  

- **R**:  
  Enfocado en estadística y visualización. Muy utilizado por analistas y estadísticos.

- **Scala**:  
  Construido sobre Java, optimizado para Spark y programación funcional. Ideal para procesamientos distribuidos.  

- **Java**:  
  Lenguaje potente y escalable, común en sistemas críticos. Scala funciona sobre la JVM (Java Virtual Machine).  

- **JavaScript**:  
  Su versatilidad lo hace útil en visualización de datos interactiva (por ejemplo, con D3.js).  

- **C++ y derivados**:  
  Base de muchos sistemas de alto rendimiento. Aunque tiene una curva de aprendizaje elevada, es esencial para desarrollos de bajo nivel.  

---

## ¿Dónde y cómo escribir el código en Ingeniería de Datos?

Herramientas comunes:  
- **Jupyter Notebooks**: Para análisis exploratorio y prototipos rápidos.  
- **IDEs** (por ejemplo, PyCharm, IntelliJ): Para desarrollos robustos y colaborativos.  
- **VSCode**: Editor ligero y versátil.  
- **Terminal y Git**: Para control de versiones y gestión de proyectos.

---

## Automatización y Scripting

La automatización permite ahorrar tiempo y optimizar procesos repetitivos.  
**Python** es la elección ideal por su facilidad de uso, comunidad activa y compatibilidad multiplataforma.

Ejemplo de tareas automatizables:  
- Generación de reportes.  
- Procesamiento masivo de datos.  
- Migración de archivos entre sistemas.

---

## Fuentes de Datos

### Bases de datos relacionales (SQL)
Son fundamentales en ingeniería de datos, guiadas por el principio **ACID** (Atomicidad, Consistencia, Aislamiento, Durabilidad).

### Bases de datos NoSQL
Más flexibles para trabajar con datos no estructurados. Ejemplos:  
- MongoDB: Para documentos JSON.  
- Redis: Almacenamiento en memoria.  
- ElasticSearch: Búsqueda y análisis.

### APIs
Permiten consumir datos de terceros mediante solicitudes HTTP.

### Web Scraping
Herramientas como **Scrapy** permiten extraer información de páginas web. Siempre respeta el archivo `robots.txt` para verificar permisos.

---

## Procesamiento de Datos: Pipelines y Apache Spark

Los pipelines de datos suelen seguir un proceso **ETL** (Extract, Transform, Load). Un ejemplo es el stack de Netflix, que usa herramientas como Kafka, S3, Redshift y Tableau.

**Apache Spark**:  
Es una herramienta para procesamientos distribuidos, que destaca por:  
- Velocidad.  
- Procesamiento en caché.  
- Soporte para batch y streaming.  
- Escalabilidad en clústeres.  

---
Aquí tienes la sección complementada y mejorada con definiciones más completas y algunos ejemplos prácticos:

---

## Automatización de Pipelines con Airflow

Apache Airflow es una herramienta clave para la orquestación de pipelines de datos. Permite organizar y programar tareas mediante **DAGs** (Directed Acyclic Graphs o grafos acíclicos dirigidos). Los DAGs definen flujos de trabajo compuestos por tareas que dependen unas de otras, asegurando que se ejecuten en el orden correcto.

**Ventajas de Airflow**:
- **Escalabilidad**: Puede manejar flujos complejos de procesamiento de datos.  
- **Interfaz web**: Ofrece una interfaz visual para monitorear y gestionar las tareas.  
- **Flexibilidad**: Escribe las definiciones de pipelines en Python, lo que facilita su personalización.  
- **Reintentos automáticos**: Configura reintentos en caso de fallas.  

**Ejemplo de uso**:  
Un pipeline para procesar datos de ventas podría incluir tareas como:  
1. Extraer datos de una API de terceros.  
2. Transformarlos con PySpark.  
3. Cargar los datos procesados en una base de datos relacional como Redshift.  
4. Generar reportes automáticos en Tableau.

En Airflow, este flujo se definiría como un DAG con estas tareas conectadas, y cada una podría ejecutarse en horarios específicos o bajo ciertas condiciones.

---

## Manejo de Ambientes para Datos

En ingeniería de datos, el manejo de ambientes es esencial para mantener la calidad y estabilidad del sistema. Estos ambientes funcionan como las **ramas de Git**, cada una con un propósito específico:

1. **Local**:  
   - Ambiente de desarrollo personal donde los ingenieros prueban y validan cambios iniciales.  
   - Se utiliza para realizar pruebas sin afectar otros sistemas.  
   - Ejemplo: Pruebas iniciales de una nueva transformación ETL.  

2. **Beta (o Staging)**:  
   - Un ambiente intermedio que replica la configuración de producción.  
   - Aquí se validan integraciones y pruebas de sistemas completos.  
   - Ejemplo: Probar si un nuevo pipeline funciona correctamente con datos simulados.  

3. **Producción**:  
   - Ambiente final donde las soluciones están en uso por los usuarios o sistemas reales.  
   - Ejemplo: Procesamiento diario de datos reales de transacciones.

**Mejor práctica**: Automatiza la promoción entre ambientes usando herramientas de CI/CD para garantizar que las soluciones pasen pruebas antes de implementarse.

---

## Testing de Software y de Datos

El **testing** es fundamental para garantizar que el código y los datos cumplan con los requisitos.  

1. **Testing de software**:  
   - Valida la funcionalidad y rendimiento del código.  
   - Tipos:  
     - **Unit Tests**: Prueban funciones o módulos individuales.  
     - **Integration Tests**: Aseguran que los módulos funcionan correctamente juntos.  
     - **End-to-End Tests**: Simulan escenarios completos para validar el flujo total.  

2. **Testing de datos**:  
   - Valida la calidad y consistencia de los datos en pipelines.  
   - Ejemplo:  
     - **Tests de valores esperados**: ¿El valor promedio de una columna es el esperado?  
     - **Detección de anomalías**: Identificar valores fuera de rango o datos faltantes.  
     - **Validación de esquemas**: Verificar que las tablas cumplen con los formatos esperados (nombres de columnas, tipos de datos).  

**Herramientas comunes**:
- **Great Expectations**: Framework para pruebas de datos.  
- **dbt (data build tool)**: Automatiza transformaciones y pruebas en SQL.  

---

## DataOps vs DevOps

Aunque DataOps y DevOps comparten principios similares, están diseñados para resolver problemas en contextos diferentes:

### **DevOps**  
- **Enfoque**: Desarrollo y despliegue de software.  
- **Objetivo**: Automatizar y agilizar la creación, prueba e implementación de aplicaciones.  
- **Procesos clave**:  
  - CI/CD para código de aplicaciones.  
  - Gestión de infraestructura como código (IaC).  
  - Monitoreo de sistemas en producción.  
- **Herramientas comunes**: Jenkins, GitLab CI/CD, Docker, Kubernetes.

### **DataOps**  
- **Enfoque**: Gestión y orquestación de datos.  
- **Objetivo**: Asegurar la calidad, disponibilidad y gobernanza de datos.  
- **Procesos clave**:  
  - Diseño y ejecución de pipelines ETL/ELT.  
  - Pruebas de calidad de datos.  
  - Monitoreo y gestión de datos en producción.  
- **Herramientas comunes**: Apache Airflow, dbt, Great Expectations, Prefect.  

**Diferencias clave**:  
- DevOps trabaja en aplicaciones de software, mientras que DataOps se centra en la gestión de datos y los flujos asociados.  
- DataOps pone mayor énfasis en la gobernanza y la calidad de los datos como activos críticos.  

**Ejemplo práctico**:  
- **DevOps**: Configurar un pipeline CI/CD para desplegar una aplicación web.  
- **DataOps**: Configurar un pipeline ETL que extraiga datos de una API, los transforme y los cargue en un almacén de datos, validando su calidad en cada paso.

## Servidores y computación en la nube para data

Hay varias alternativas de nubes siendo AWS como la más común, conocida por sus servicios S3, Glue y EC2, también está Azure y GCP. 

## Reentrenamiento y control de salud de servicios

Los modelos a base que avanzan en el tiempo, los modelos quedan atrás en el tiempo porque las cosas van cambiando. Por ende, es buena práctica ir re entrenando los viejos modelos y generar nuevos modelos.

## Medición de indicadores y seguimientos a proyectos

En caso de no medir, uno se puede volver loco buscando un error, por ende, se debe de implementar un sistema de monitoreo teniendo una buena visibilidad como con dashboards y alertas. 