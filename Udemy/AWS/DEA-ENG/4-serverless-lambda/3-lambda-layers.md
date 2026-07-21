# Lambda Layers

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## ¿Qué son las Lambda Layers?

Las **Lambda Layers** son una forma de gestionar **código y dependencias por separado** de la función
Lambda propiamente dicha. Permiten centralizar, por ejemplo, código compartido o dependencias comunes a
través de **múltiples funciones Lambda**, facilitando su gestión (por ejemplo, cuando hay que
actualizar varias funciones a la vez).

Una Lambda Layer es básicamente un **archivo ZIP** que puede incluir:

- Código adicional.
- Librerías / bibliotecas.
- **Runtimes personalizados**.
- Otras dependencias o archivos de configuración.

Las layers están **separadas** de la función principal, pero forman parte del **entorno de ejecución**
de la función: la función puede acceder a su contenido en tiempo de ejecución. Una misma layer se puede
externalizar y reutilizar desde **múltiples funciones**.

## Sin capas vs. con capas

### Sin Lambda Layers

Todo el código, dependencias y runtime personalizado forman parte de **cada función** directamente (no
están separados). Esto tiene desventajas:

- Es **tedioso** actualizar o compartir código entre varias funciones — hay que replicarlo en cada una.
- El **tamaño** del paquete de despliegue de cada función crece.

### Con Lambda Layers

1. **Empaquetar el contenido de la capa**: crear un archivo ZIP con las dependencias, de forma similar
   a preparar un paquete de despliegue.
2. **Crear la Lambda Layer**: subir ese ZIP a Lambda y registrarlo como una nueva layer.
3. **Añadir la capa a la función**: especificar en la configuración de la función que debe incluir esa
   layer durante la ejecución.
4. La función puede entonces **acceder al contenido de la layer** en tiempo de ejecución.

Si más adelante hace falta actualizar algo, se puede modificar y gestionar de forma **centralizada**
desde la propia Lambda Layer.

## Beneficios

| Beneficio                                         | Detalle                                                                                                                                                    |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compartir dependencias entre funciones**        | Una vez creada, una layer puede usarse en cualquier número de funciones dentro de la misma cuenta, reduciendo redundancia y simplificando actualizaciones. |
| **Separar la lógica central de las dependencias** | El código de la función y sus dependencias se gestionan de forma independiente, facilitando actualizaciones y mantenimiento en múltiples funciones.        |
| **Reducir el tamaño del paquete de despliegue**   | Al mover librerías y dependencias a una layer, se minimiza el tamaño del paquete de despliegue de la función Lambda.                                       |
