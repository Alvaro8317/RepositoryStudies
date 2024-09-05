# Arquitectura y servicios

Azure es un proveedor con una infraestructura global, cuenta con unas piezas que se lo permiten distribuidas en:

- Regiones de Azure (Regiones emparejadas / Regiones soberanas)
- Zonas de disponibilidad de Azure
- Centros de datos de Azure
- Puntos de presencia de Azure

## Regiones

Las regiones se deben de construir en base al principal público para evitar la latencia, una región es una ubicación geográfica específica para alojar los recursos, obteniendo alta disponibilidad, baja latencia y cumplimiento de las regulaciones gubernamentales.

En cumplimiento de los requisitos legales y de gobernanza de datos, los datos nunca salen de una región sin un permiso explícito. Considerar una región implica la proximidad a los clientes, los servicios disponibles en una región y los precios ya que estos varian en base a la región.

### Regiones emparejadas

Cada región está emparejada con otra región en el mismo límite geopolítico para proporcionar resistencia si se produce un error catastrófico en la región.
Los objetivos de la región emparejada son:

- Mejorar la resiliencia y disponibilidad
- Asegurar la continuidad del negocio y la recuperación ante desastres
- Permiten separar geográficamente para resistir fallos en una sola región

### Regiones soberanas

Regiones con centros de datos específicamente diseñados para cumplir con los requisitos reglamentarios y de cumplimiento de una jurisdicción o nación particular. Microsoft no las administra necesariamente y podrían estar restringidas a determinados tipos de clientes, estas regiones tienen como objetivo garantizar la soberanía de los datos, satisfacen reglamentos locales, operan y residen los datos dentro de fronteras especificas y cuenta con conexiones de red más aisladas y específicas de la región. Ejemplo: Azure China 2 / Azure Government EEUU

## Zonas de disponibilidad AZ

Permiten lograr alta disponibilidad en la misma región, una AZ es uno o varios centros de datos discretos con alimentación, red y conectividad redundante. Las zonas de disponibilidad de una región están conectadas mediante un enlace de baja latencia (inferior a 2 ms), están separadas unas de otras para aislar las catastrofes. No todas las regiones de Azure tienen zonas de disponibilidad.

## Punto de presencia (PoP)

Se refiere a un punto físico de interconexión entre diferentes redes que facilita la entrega rápida y confiable de contenido y servicios a los usuarios finales.

Las ventajas de los PoP es que proveen rendimiento mejorado y expansión global, son similares a una AZ, pero estos están distribuidos en puntos cercanos a los usuarios.

## Desafios + Soluciones

Una aplicación está desplegada en Londres, ¿Los desafios? Esa app en china puede tener alta latencia y puede tener baja disponibilidad, se soluciona implementando en múltiples regiones la aplicación con múltiples centros de datos y con PoP para la latencia.

## Recursos y grupos de recursos

**Un recurso es un elemento administrable disponible en Azure**, ejemplo, maquinas virtuales, bases de datos, etc. Los grupos de recursos, las suscripciones, los grupos de administración y las etiquetas también son ejemplos de recursos.

Por otro lado, **un grupo de recurso es un contenedor que almacena los recursos relacionados con una solución de Azure**, permite incluir todos los recursos de la solución o solo aquellos que se desean administrar en grupo. Los grupos de recursos almacenan metadatos acerca de los recursos que contienen. Un recurso ya creado se puede añadir a un grupo de recursos.

## Suscripciones

Permiten organizar y controlar el acceso, costos y facturación, es decir, permiten separar prod, dev y test. Además, cada suscripción tiene límites en la cantidad y tipo de recursos que se puede crear. Se factura por suscripción, permitiendo un seguimiento detallado de los costos. **Mediante el control de acceso IAM permite definir el acceso a diferentes personas dentro de la organización**. Es posible tener múltiples suscripciones dentro de la misma cuenta de Azure. Útiles para segmentar departamentos o proyectos.

## Grupos de administración

Es una estructura jerárquica que permite organizar y administrar múltiples suscripciones de Azure. Las características clave de los grupos son que organiza suscripciones en forma de arbol, aplica políticas e iniciativas, establece roles, etc. Útil para defenciar departamentos en una organización y para distintos entornos.

## Servicios globales y regionales

Un servicio global es que está en múltiples regiones y que no está atado a una sola región, ejemplo, Azure Active Directory o Azure Traffic Manager. Por otro lado, los regionales están ligados a su respectiva región, puede que un servicio o una particularidad esté ligada a una región. Esto no significia que no se pueda tener alta disponibilidad multi-region, un ejemplo de estos servicios son Azure Virtual Machines, Azure App Service o Azure Functions

## Resumen

Se habló de

1. Regiones - Áreas geograficas, divididas en regiones emparejadas y regiones soberanas
2. Zonas de disponibilidad - Centros de datos separados físicamente dentro de una región para proporcionar resistencia a fallas
3. Puntos de presencia (PoP) - Equivalente a Edge Locations
4. Recursos y grupos de recursos - Unidades individuales de servicios y sus agrupaciones lógicas
5. Suscripciones - Permiten organizar y controlar el acceso, costos y facturación
6. Grupos de administración - Estructura jerárquica que permite organizar suscripciones
7. Servicios globales y regionales

La capacidad es ilimitada en el Cloud, no tienes que preocuparte por ella. Los 4 puntos a tener en cuenta a la hora de elegir una región de Azure son: la conformidad con la normativa de datos y los requisitos legales, la proximidad a los clientes, los servicios y características disponibles dentro de una región y el precio.

Azure Active Directory (Azure AD) es un servicio global (abarca todas las regiones).

Las regiones emparejadas en Azure se utilizan para proporcionar redundancia y continuidad del negocio. Están diseñadas para permitir la recuperación ante desastres y evitar puntos únicos de fallo.

La infraestructura global de Azure se diseñó para ofrecer una amplia gama de servicios de computación en la nube a escala mundial, como bases de datos, almacenamiento y mucho más.

Las Zonas de Disponibilidad se diseñan para proteger las aplicaciones y los datos de los fallos del centro de datos, proporcionando redundancia y capacidad de recuperación.

Los Puntos de Presencia (PoP) actúan como puertas de enlace entre la infraestructura local del usuario y la red global de Azure, mejorando así la velocidad y la fiabilidad.

Los grupos de recursos son contenedores que contienen los recursos relacionados necesarios para una solución en particular, facilitando su gestión y organización.

Las suscripciones en Azure actúan como una forma de organizar el acceso y el pago de los recursos de Azure.

Los Grupos de Administración se utilizan para gestionar varias suscripciones en Azure. Esto es especialmente útil para las organizaciones que tienen múltiples suscripciones y necesitan aplicar políticas de gobernabilidad de manera coherente.

Agrupar recursos similares en un mismo grupo de recursos facilita su administración, seguimiento y gobernanza, permitiendo un manejo más eficiente y organizado.
