# AWS Application Migration Service (MGN)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué es?

Una vez planificada la migración (por ejemplo, con [[5-application-discovery-service|Application
Discovery Service]]), **AWS Application Migration Service (MGN)** se encarga de realizar la migración
real de los servidores.

- Automatiza gran parte del proceso manual de migración: realiza el **lift-and-shift** (rehosting) de la
  solución, permitiendo trasladar un gran número de servidores físicos o virtuales a la nube **sin
  problemas de compatibilidad ni interrupciones de rendimiento**.
- Permite crear **entornos de prueba** sin interrumpir las versiones en producción (live), de modo que se
  puede validar la migración antes del cambio final (cutover).
- Compatible con una amplia gama de entornos de origen: servidores **Windows** y **Linux**.

## Cómo funciona

1. **Instalar el AWS Replication Agent** en cada servidor de origen (compatible con Linux y Windows).
2. **Añadir el servidor de origen** a la consola de Application Migration Service.
3. **Configurar los launch settings** de cada servidor de origen — por ejemplo, el tipo de instancia
   adecuado. MGN permite lanzar una **instancia de prueba (test instance)** para encontrar el tipo de
   instancia que mejor se adapta a la configuración de hardware original.
4. **Lanzar una instancia de prueba** para verificar que todos los servidores de origen funcionan
   correctamente dentro del entorno de AWS **antes** de realizar el cutover.
5. **Cutover (transición):** una vez completadas las pruebas, se realiza el corte en una fecha y hora
   determinadas — MGN migra automáticamente los servidores de origen a instancias de corte (cutover
   instances) en AWS, completando la reubicación de la solución.

> ⚠️ Lanzar una instancia de prueba antes del cutover es un paso clave: permite validar que todo funciona
> como se espera en AWS antes de hacer el cambio definitivo desde el entorno de producción original.
