# Práctica: Configurar un Workgroup en Athena

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Ubicación en la consola

En la consola de **Athena**, en el panel de navegación izquierdo:

- **Editor de consultas**: donde se ejecutan las consultas SQL.
- **Administración → Grupos de trabajo (Workgroups)**: donde se gestionan los Workgroups.

El Workgroup **`primary`** ya existe por defecto, usa el motor **Athena SQL** y es el que se
selecciona automáticamente al ejecutar una consulta desde el editor si no se elige otro.

## Crear un nuevo Workgroup

Pasos para crear un Workgroup nuevo (ej. para un equipo de generación de informes):

1. **Nombre**: identificar el Workgroup según su propósito (ej. equipo o tipo de carga de trabajo).
2. **Motor de consulta**:
   - **Athena SQL** — para consultas interactivas (opción por defecto).
   - **Apache Spark** — motor Spark serverless, como alternativa.
3. **Autenticación**: se puede dejar la configuración por defecto.
4. **Ubicación de resultados de la consulta**: especificar un bucket de S3 propio para este
   Workgroup (opcional; si no se indica, se usa la configuración por defecto).
5. **Control de uso**: opcionalmente se pueden definir:
   - **Límites de datos escaneados**.
   - **Alertas de uso**.

Estas opciones permiten aislar y monitorizar el coste de forma independiente por equipo o carga de
trabajo.

## Uso del Workgroup

- Al crear el Workgroup, este queda disponible casi de inmediato, junto con sus propias
  **métricas** de uso y coste.
- Desde el **editor de consultas**, se puede elegir entre el Workgroup `primary` u otro Workgroup
  creado (ej. el de generación de informes) antes de ejecutar una consulta.

> ⚠️ El Workgroup activo en el editor de consultas determina qué configuración (motor, ubicación de
> resultados, límites de coste) se aplica a la consulta que se va a ejecutar.
