# Computación

## Azure virtual machines (VM)

Es de los servicios más populares, conocido como IaaS o infraestructura como servicio, ¿Dónde se implementan las aplicaciones en el cloud? Se implementan con el alquiler de maquinas virtuales. Se puede configurar el balanceo de carga y autoescalado para varias máquinas virtuales, permite también automatizar el aprovisionamiento para las máquinas virtuales. Administra la conexión y la configuración de la red de las instancias de máquina virtual. Casos de uso

- Procesamiento de datos y análisis
- Configuración de instancias VM para servidores web
- Aplicaciones con alto performance

## Opciones de compra

### Pago por uso (Pay as you go)

Cargas de trabajo de corta duración con precios predecibles, facturación por _segundos de uso_, tiene el coste más elevado sin pagar por adelantado y sin compromiso a largo plazo.

### Planes de ahorro

De 1 y 3 años, para usuarios que pueden comprometerse con un volumen de uso específico a largo plazo, ideal para cargas de trabajo continuas y predecibles. Descuento basado en el uso a largo plazo (65%), se pueden pagar X usd cada hora durante 1 o 3 años. No se pueden cancelar ni reembolsar, además, se puede pagar un plan de ahorro por adelantado o mensual. El costo total del plan de ahorro por adelantado y mensual es el mismo. Al finalizar el plazo del plan, empezará a cobrar pago por uso. Los planes de ahorro son ideales para cargas de trabajo predecibles y estables que requerirán recursos de azure.

### Instancias reservadas

De 1 y 3 años, ofrecen un descuento significativo con respecto a pago por uso para ejecutar cualquier trabajo, ofrece un descuento del 72% con respecto al pago por uso, este plan significa que reservará los atributos de instancia especificados, puede cancelar el plan en cualquier momento. De 1 año da un descuento pero de 3 años da aún más descuento, permite pagar por adelantado o mensual y es recomendado para aplicaciones de uso constante como una BD

### Instancias spot

Cargas de trabajo esporádicas y flexibles con costos reducidos. Pueden ser interrumpidas. Descuento de hasta el 90% con respecto a pago por uso, instancias que se pueden perder si su precio máximo es inferior al precio spot actual. Las instancias más rentables de Azure. Útiles para trabajos por lotes, análisis de datos, procesamiento de imágenes, cargas de trabajo distribuidas, etc.

### Hosts dedicados de Azure (Azure dedicated host)

Proporciona servidores físicos dedicados para alojar máquinas virtuales, permitiendo control sobre la ubicación y el hardware dedicado. **Son servidores físicos capaces de hospedar una o varias instancias de Azure**. No se comparte la capacidad del servidor con otros clientes, permiten pago por uso, plan de ahorro y reservas, útil para empresas con fuertes necesidades de regulación o cumplimiento. (Es la más cara)

### Instancias aisladas

Ofrecen aislameinto a nivel de hardware, asegurando que ningún otro cliente comparta el hardware utilizado. Garantiza que la máquina virtual es la única que se ejecuta en un servidor físico, Azure ofrece tamaños de máquinas virtuales que están aislados para un tipo concreto de hardware y dedicados a un solo cliente. Útiles para cumplir requisitos normativos y de cumplimiento o aplicaciones críticas que requieren un ambiente controlado y aislado.

### Reservas de capacidad a petición

Permite reservar capacidad de proceso en una región de azure o una AZ durante cualquier periodo de tiempo. Permite reservar capacidad de instancias a petición, permite implementar y eliminar sin compromiso de permanencia, se puede combinar con instancias reservadas y adecuado para cargas de trabajo ininterrumpidas a corto plazo.

## Scale sets (Conjuntos de escalado)

Grupos de escalado, son un grupo de Virtual Machines idénticas con carga equilibrada, es un grupo lógico que puede configurarse y gestionarse como una sola unidad; Permite añadir más maquinas a medida que crece la demanda autoescalando, también permite reducir máquinas, se puede gestionar hasta 100 maquinas virtuales en un conjunto de escalado y puede configurar para aumentar esa cifra hasta 1000 maquinas virtuales. Opcionalmente se puede añadir un Load Balancer y distribuir instancias a través de múltiples AZ, permite escalado manual y automático

Es importante: **Los conjuntos de escalado son máquinas virtuales idénticas. Pueden activarse según sea necesario, es una VM base en lo que se copia para formar las máquinas virtuales del conjunto. Solo se paga por la máquina virtual, almacenamiento y recursos de red, más no por el grupo de autoescalado.**

## Escalabilidad y alta disponibilidad

### Escalabilidad

Significa que una aplicación pueda adaptarse a mayores o menores cargas, existe escalabilidad vertical y horizontal. La horizontal es lo mismo que elasticidad. Escalabilidad es distinto a alta disponibilidad

### Alta disponibilidad

Va de la mano con escalado horizontal, significa ejecutar la aplicación / sistema en al menos 2 zonas de disponibilidad. EL objetivo de la alta disponibilidad es sobrevivir a la pérdida del centro de datos (desastre).

### Escalabilidad, elasticidad y agilidad

**Escalabilidad** es acomodar una acomodar una mayor carga reforzando el hardware o añadiendo nodos. **Elasticidad** es que una vez siendo escalable, signfiica que habrá cierto autoescalado. Por último, **agilidad** es que los nuevos recursos de TI están a un clic de distancia

## Apps service

Trabajando en el cloud se recomienda una arquitectura de 3 niveles que es:

1. Load balancer
2. Instancias alojadas en un grupo de escalado
3. Almacenamiento, donde están alojadas las bases de datos

Esta infraestructura requiere gestión de la infraestructura y saber lo que está haciendo, además, se debe desplegar el código, configurar las bases de datos, problemas de escalado y la mayoría tienen la misma arquitectura. Los desarrolladores muchas veces quieren es que su código se ejecute. **App service** soluciona este problema, es una solución robusta para desplegar, administrar y escalar aplicaciones web de manera eficiente y segura. _Equivalente a BeanStalk_, utiliza muchos componentes de azure donde los desarrolladores solo se enfocan en el código de la aplicación. App Service es **PaaS** y utilizarlo es gratuito pero se paga por los recursos subyacentes que genera.

Es una plataforma totalmente gestionada donde uno se concentra en el valor del negocio y la lógica del código, da ventajas como la configuración de la instancias y el SO es gestionado por App service, aprovisiona automáticamente la capacidad y balanceo de carga con monitoreo. **Casos de uso:**

- Web Apps
- Web App para contenedores (docker)
- API Apps

## Azure container instances (ACI)

Es el servicio de contenedores en Azure, con docker es una plataforma de desarrollo de software para desplegar aplicaciones empaquetando en contenedores que puedan ejecutarse en cualquier SO. Es decir, no hay problemas de compatibilidad, comportamiento predecible, menos trabajo, fácil de mantener y desplegar, funciona con cualquier lenguaje y amplia o reduce los contenedores muy rápido en segundos. Estos contenedores son ligeros, docker permite correr en maquinas locales, centros de datos, cloud, etc. Docker proporciona aislamiento entre los contenedores. ¿Dónde se almacenan las imágenes docker? Estas imagenes se almacenan en repositorios como públicos como docker-hub o privados, como ECR o ACR que es de Azure, es decir, Azure container registry.

ACI es un servicio que permite ejecutar contenedores en el cloud de Azure que sigue el siguiente flujo:

1. Ciclo de desarrollo de software
2. Aplicación situada en un contenedor
3. Se va a instancias de contenedor o ACI

Es un servicio:

- Enfocado a cargas de trabajo en contenedores, una carga de trabajo es un proceso o aplicación
- Bajo demanda, utiliza aplicaciones en contenedores para procesar bajo demanda, creando la imagen del contenedor cuando se necesite
- Permite seleccionar múltiples herrameintas como protal de Azure, Azure CLI o powershell

## Azure Kubernetes Service (AKS)

K8s es un sistema de orquestación de contenedores de código, es open source. Usado para automatizar el despliegue, escalado y gestión de aplicaciones. El logo es como un timón de un barco, k8s fue originalmente desarrollado por google. Cuenta con las siguientes características:

- Codigo abierto
- Orquestación
- Despliegue automático de aplicación (Proceso inicial)
- Escalado automático (Lanzamiento de pods)

AKS es un servicio que aparece en los examenes bastante, ALS reutiliza la arquitectura de contenedores gestionandola en K8s. Uno no debe de preocuparse por la infraestructura y el hardware. Además, da un alcance global con Azure Stack.

### Cluster AKS

Es un conjunto de recursos y servicios para orquestar contenedores con pods dentro, cada uno de los pods puede contener múltiples contenedores para que trabajen estrechamente entre sí. Estos pods pueden vivir en nodos, AKS al ser automático permite escalar nodos de manera fácil.

## Azure Virtual Desktop (Previamente llamado Windows Virtual Desktop)

Es una solución para virtualización de escritorio y aplicaciones en el cloud de Azure, ofrece una experiencia optimizada para Office 365, soporta varios usuarios y permite entorno de trabajo híbrido, desarrollo, testing y recuperación ante desastres.

Es **una solución de virtualización de escritorio y aplicaciones en cloud**

## Azure Functions

Funciones de azure, serverless en la que solo se despliega código, funciones, serverless es un nuevo paradigma en el que los servidores solo se enfocan en desplegar funciones, solo desplegar código, no significa que no existen, solo que uno no los gestiona, aprovisiona, etc.

Azure solo se ejecuta cuando es necesario, la función de Azure solo se ejecuta cuando hay datos por procesar. Permite ahorrar dinero, sin tráfico no se usan recursos. Esto significa que uno no paga por la función cuando no está en uso. Además, si hay fallas, no afecta a otras instancias de la función.

### IaaS / PaaS vs Función

Una función es el servicio de computación más pequeño de azure, una única función de computación, llamada o invocada a través de una dirección estándar, se ejecuta una vez y se detiene. En IaaS uno instala las propias aplicaciones, accede al SO, tiene visibilidad de los recursos y un servicio de aplicaciones no tiene acceso al SO, pero si a los recursos.

## Resumen

- Azure compute - Soluciones de computo
- Azure virtual machines (VM) - Servidores virtuales escalables
- Opciones de compra
- Scale sets
- Alta disponibilidad y escalabilidad
- App Service - Servicio para construir, hospedar y escalar aplicaciones web
- Azure container instances (ACI)
- Azurecontainer registry (ACR)
- Azure k8s service (AKS)
- Azure virtual desktop
- Azure functions

Azure Virtual Desktop (antes Windows Virtual Desktop) te ayuda a configurar rápidamente un entorno, e incluso te permite reutilizar cualquier licencia de Windows 10 que tengas.

La computación es uno de los tres componentes fundamentales del Cloud Computing. Los otros dos son la red y el almacenamiento. Esto significa que cualquier servicio que realice una función informática en Azure forma parte de "Compute" en Azure. No es un servicio único.

Los conjuntos de escalado permiten crear y gestionar un grupo de máquinas virtuales de carga equilibrada. El número de instancias de máquinas virtuales puede aumentar o disminuir automáticamente en respuesta a la demanda o a una programación definida. Los conjuntos de escalado proporcionan alta disponibilidad a las aplicaciones y permiten gestionar, configurar y actualizar de forma centralizada un gran número de máquinas virtuales. Con los conjuntos de escalado de máquinas virtuales, puedes crear servicios a gran escala para áreas como computación, big data y cargas de trabajo de contenedores.

Las máquinas virtuales de Azure eliminan la capa de hardware físico, por lo que no es necesario preocuparse por el mantenimiento del hardware físico. Microsoft se encarga de esto en su lugar.

Una plataforma totalmente gestionada significa que el proveedor gestiona la capa de infraestructura, como las máquinas virtuales, los discos, las redes y mucho más. Sólo tienes que centrarse en la funcionalidad principal de la aplicación. Los servicios totalmente gestionados de Azure están disponibles en todos los tipos de suscripción y no suponen ningún coste adicional.

Estos son los principales casos de uso de Azure App Service:

1. Web Apps
2. Web Apps para contenedores
3. API Apps

La infraestructura como Servicio (IaaS) incluye servicios que emulan hardware, como máquinas virtuales, redes y almacenamiento.

Esta es la definición que representa a Azure Functions: Servicio serverless que representa una función de computación (y es servicio de cómputo más pequeño de Azure).
