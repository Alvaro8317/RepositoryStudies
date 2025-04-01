# Entorno de Trabajo para Ciencia de Datos con Jupyter Notebooks y Anaconda  

## Jupyter Notebooks vs Scripts  

Tanto los Jupyter Notebooks como los scripts tradicionales tienen un lugar en el flujo de trabajo de ciencia de datos.  

### **Jupyter Notebooks**  
- **Ventajas**:  
  - Interactividad: Permite probar código de manera incremental y visualizar resultados en tiempo real, ideal para exploración de datos y prototipos.  
  - Visualización integrada: Puede mostrar gráficos, tablas y texto enriquecido directamente en las celdas.  
  - Documentación: Permite combinar código con descripciones detalladas en Markdown, lo que lo hace ideal para reportes o tutoriales.  
  - Facilidad de uso: Su entorno es intuitivo y fácil de configurar con Anaconda.  

- **Desventajas**:  
  - Difícil mantenimiento: No es óptimo para proyectos grandes o colaborativos, ya que el código puede volverse desordenado.  
  - Escalabilidad limitada: No es ideal para manejar flujos complejos de datos o tareas críticas de producción.  

**Ejemplo práctico**: Explorar un dataset usando pandas y matplotlib, generar gráficos y escribir conclusiones en Markdown directamente en el notebook.  

### **Scripts tradicionales**  
- **Ventajas**:  
  - Modularidad: Fomenta un diseño estructurado y reutilizable del código, ideal para proyectos colaborativos y a largo plazo.  
  - Control de versiones: Más fáciles de gestionar con herramientas como Git.  
  - Integración: Adecuado para implementar soluciones en producción o integrarse con pipelines más grandes.  

- **Desventajas**:  
  - Menos interactivos: Requieren ejecutar todo el archivo para probar pequeños cambios, lo que puede ser menos eficiente en la exploración inicial.  
  - Visualización limitada: Necesitas herramientas externas para combinar resultados y documentación.  

**Ejemplo práctico**: Escribir un script Python para procesar un conjunto de datos de manera escalable y luego integrarlo con Airflow para su ejecución automatizada.  

### **¿Cuándo usar cada uno?**  
- **Notebooks**: Exploración inicial, prototipado rápido y análisis interactivo.  
- **Scripts**: Desarrollo de soluciones maduras, escalables y listas para producción.  

---

## Notebooks en la Nube vs Locales  

Tanto los notebooks en la nube como los locales tienen aplicaciones específicas según las necesidades del proyecto.  

### **Notebooks en la nube**  
- **Ventajas**:  
  - Escalabilidad: Aprovechan recursos como GPU/TPU para tareas intensivas, como entrenar modelos de machine learning.  
  - Accesibilidad: Se puede trabajar desde cualquier lugar sin necesidad de instalar entornos complejos localmente.  
  - Colaboración: Permiten que múltiples usuarios trabajen simultáneamente en el mismo notebook (ej. Google Colab, Databricks).  

- **Desventajas**:  
  - Dependencia de conexión: Requieren acceso constante a internet.  
  - Costos: Pueden implicar gastos adicionales si se usan recursos avanzados en servicios como AWS, Azure o GCP.  

**Ejemplo práctico**: Entrenar un modelo de deep learning en Google Colab utilizando una GPU gratuita.  

### **Notebooks locales**  
- **Ventajas**:  
  - Control total: Permiten personalizar el entorno y librerías según las necesidades del proyecto.  
  - Sin costo adicional: No hay gastos derivados de uso de infraestructura en la nube.  
  - Sincronización con herramientas locales: Facilidad para integrarse con archivos locales, bases de datos locales o servidores internos.  

- **Desventajas**:  
  - Limitación de recursos: Dependes del hardware de tu equipo local.  
  - Configuración: Requieren instalar y configurar entornos (por ejemplo, usando Anaconda).  

**Ejemplo práctico**: Limpieza y análisis inicial de un dataset usando pandas en un notebook configurado con Anaconda en tu máquina local.  

---

## Configuración de Entornos con Anaconda  

Anaconda es una herramienta clave para gestionar entornos de trabajo en ciencia de datos. Facilita la instalación y mantenimiento de librerías y dependencias en un entorno aislado.  

### **Ventajas de usar Anaconda**  
- **Gestión de entornos**: Crea entornos separados para diferentes proyectos, evitando conflictos de dependencias.  
- **Preinstalación de librerías**: Incluye librerías comunes como pandas, numpy, matplotlib, y Jupyter.  
- **Interfaz gráfica**: Su herramienta Anaconda Navigator simplifica la gestión de entornos y notebooks.  

**Comandos básicos**:
1. Crear un nuevo entorno:  
   ```bash  
   conda create -n mi_entorno python=3.9  
   ```  
2. Activar un entorno:  
   ```bash  
   conda activate mi_entorno  
   ```  
3. Instalar una librería:  
   ```bash  
   conda install pandas  
   ```  
4. Listar entornos:  
   ```bash  
   conda env list  
   ```  

**Ejemplo práctico**: Crear un entorno llamado "proyecto_ml" con Python 3.8 y librerías necesarias para machine learning:  
```bash  
conda create -n proyecto_ml python=3.8 scikit-learn matplotlib  
conda activate proyecto_ml  
jupyter notebook  
```  

## Qué es google colab

Es un servicio en la nube basado en jupyter notebooks, no requiere configuración y trabaja a nivel de archivo, el punto de entrada a un proyecto es un notebook, además que provee uso gratuito de GPUs y CPUs