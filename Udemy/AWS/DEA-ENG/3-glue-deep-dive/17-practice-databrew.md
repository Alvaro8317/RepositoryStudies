# Práctica: AWS Glue DataBrew

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

En esta práctica se crea un proyecto de ejemplo en **DataBrew** para limpiar y normalizar datos de
forma **interactiva**, aplicar una receta de transformaciones y, finalmente, crear un **Job** que
ejecute esa receta con una salida programada.

## Precios

- **Sesiones interactivas**: se facturan por **sesión**, con un coste aproximado de **1 $ por
  sesión**. Las primeras **40 sesiones son gratuitas** para usuarios nuevos de DataBrew. Cada sesión
  dura **30 minutos**.
- **DataBrew Jobs** (uso en producción, por ejemplo programados con una ubicación de salida
  específica): se facturan por **nodo/hora**, según el número de nodos configurado (se puede definir
  un número máximo de nodos). La facturación se desglosa realmente por **minuto** dentro de esa hora.

## Crear el proyecto

1. En **DataBrew**, crear un nuevo proyecto de ejemplo.
2. Elegir uno de los **datasets de muestra** disponibles (en la demo se usa un dataset de movimientos
   de ajedrez).
3. Elegir un **rol IAM**: se puede reutilizar uno existente o crear uno nuevo sobre la marcha,
   indicando un prefijo para el nombre (ej. `prueba2`).
4. Crear el proyecto. Esto inicia la **sesión interactiva**: se aprovisionan automáticamente los
   recursos de cómputo y el dataset (tarda aproximadamente **1 minuto**).

## Trabajar con la receta de forma interactiva

En el panel central se ve la **vista previa** de los datos, reflejando el efecto de los pasos ya
aplicados en la receta.

### Inspeccionar y transformar una columna

- Se puede ver el **tipo de dato** de cada columna (ej. `string`) y, si tuviera sentido, convertirlo
  a otro tipo (ej. a fecha).
- Al seleccionar una columna se pueden aplicar transformaciones desde el menú contextual, por ejemplo:
  - **Filtrar valores faltantes**.
  - Aplicar una **función de texto**, como convertir el valor a **mayúsculas**.
- Al seleccionar una columna también se muestran sus **detalles / perfil**: estadísticas sobre la
  calidad de los datos.
- En la pestaña **Schema** se puede ver información adicional sobre calidad de datos, valores no
  válidos, distribución, etc. También existe la opción de ejecutar un **Data profile** completo sobre
  el dataset (no se ejecuta en esta demo).

### Aplicar pasos a la receta

- **Eliminar una columna**: seleccionar la columna a eliminar (ej. `CreatedAt`, considerada
  innecesaria/confusa), previsualizar el efecto del cambio y, si es el resultado esperado, **aplicar**
  el paso. El paso queda registrado en el panel de la **receta** (ej. "delete column" como primer
  paso).
- **Aplicar una función matemática**: por ejemplo, la función **Add** sobre una columna numérica,
  sumando un valor específico (ej. `2`), previsualizando el resultado antes de aplicarlo.
- Cada paso aplicado se añade a la lista de pasos visible en el panel de la receta, y se pueden editar
  o eliminar posteriormente.
- Las recetas se pueden **publicar** para reutilizarlas en otros datasets/proyectos (no se hace en
  esta demo).

## Crear un Job a partir de la receta

1. Crear un nuevo **DataBrew Job** (ej. nombrado `ml-drop-one`).
2. Configurar la **salida**:
   - Un bucket **S3** de destino.
   - **Formato de archivo** (ej. CSV, con su delimitador correspondiente).
   - Opciones de **compresión**.
3. Configurar la **capacidad**: número de nodos a usar (se puede reducir para ahorrar costes).
4. Asociar un **schedule** (horario) al job:
   - Se puede crear uno nuevo sobre la marcha, dándole un nombre (ej. `diario`).
   - Configurar días específicos (ej. solo martes y miércoles).
   - Configurar una recurrencia en horas (ej. cada 8 horas) y ver las ocurrencias resultantes.
5. Seleccionar el **rol IAM** a usar (se reutiliza el creado al inicio de la práctica).
6. **Create and run job** para crear y ejecutar el job.

## Limpieza

> ⚠️ Al finalizar, se eliminan todos los **proyectos** creados (seleccionándolos y usando **Delete**)
> para evitar incurrir en costes innecesarios.
