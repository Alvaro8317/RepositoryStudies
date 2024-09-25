# Redes

Las redes desempeñan un papel importante en Azure, Azure permite administrar redes en la nube para la creación de soluciones escalables

## Azure Virtual Network

Proporciona una red privada aislada en el cloud y altamente configurable para ejecutar recursos de Azure de manera segura. Permite la creación y gestión de subredes dentro de la red virtual. Utiliza filtros de red y servicios de seguridad avanzados. Además, permite la asignación y gestión de bloques de direcciones IP privadas.

**¿Cuál de las siguientes opciones de Azure permite segmentar y aislar recursos de red en la nube?** Azure virtual network (Vnet)

### Subredes

Permiten particionar la red dentro de la Azure Virtual Network, cuenta con subred pública y una subred privada
Cada subred debe tener un intervalo de direcciones único, especificado en formado CIDR. Este intervalo de direcciones no puede superponerse con otras subredes de la red virtual.
Permite subdividir el espacio de direcciones en segmentos más pequeños, ejemplo, se puede tener una subred dentro de 10.0.0.0/16 podría ser 10.0.1.0/24. Se puede tener asignación automática con DHCP e IPs reservadas para uso de Azure y no estén disponibles para asignación.

### Vnet Peering

Permite conectar dos Vnet de forma privada utilizando la red de azure con una conexión directa y rápida entre redes, sin necesidad de atravesar la red pública de internet, no deben tener un CIDR superpuesto y la conexión VNet peering no es transitiva, es decir, si se tiene VNet A conectada con Vnet B y Vnet B con VNect C, no significa que automáticamente A y C estén ya conectados, se debe de establecer un Vnet peering por cada par de Vnets

### Espacio de direcciones

Son rangos de direcciones IP asignados a las redes virtuales y subredes

#### Rangos IPs

Un rango es como 10.0.0.0/16, para este rango dew IP se tiene que el rango empieza en 10.0.0.1 hasta 10.0.255.254, el 16 es la mascara de red, significa que los primeros 16 bits indican que están reservados para identificar la red, se puede usar la siguiente formula para saber cuantas direcciones IP se tienen: **2 \*\* 16 (32-16)** donde 16 es la mascara de red.
La 10.0.0.0 está reservada para el gateway y la 10.0.255.255 es broadcast.

## Grupo de seguridad de red

Permiten controlar tráfico entrante / saliente a recursos Azure, mediante reglas para permitir / denegar tráfico. Establece prioridades para evaluar reglas en orden específico, es aplicable tanto a instancias individuales como a subredes completas.

Las reglas de entrada y salida se evaluan por prioridad mediante la combinación de origen, puerto de origen, destino, puerto de destino y protocolo para permitir o denegar el tráfico. La regla de seguridad no puede tener la misma prioridad y dirección que una regla existente.

## Azure load balancer

Son servidores que reenvían el tráfico de internet a múltiples servidores (máquinas virtuales) en sentido descendente. Opera en el nivel 4 del modelo OSI, distribuye el tráfico de red entrante entre múltiples servidores para mejorar la disponibilidad y confiabilidad. Admite protocolos TCP y UDP, es el único punto de contacto de los clientes.

Este componente distribuye flujos de entrada que llegan al frontend del equilibrador de carga a las instancias del grupo de backend. Las instancias del grupo de backend pueden ser instancias de Azure o un scale set. Asegura la alta disponibilidad mediante la distribución equitativa del tráfico entre instancias de servidor saludables en múltiples zonas de disponibilidad.

### ¿Por qué utilizarlo?

Porque da equilibrio de carga del tráfico interno y externo, distribuye la carga entre múltiples instancias descendentes, expone un único punto de acceso DNS en la aplicación, maneja sin problemas los fallos, realiza comprobaciones periódicas del estado y proporciona terminación SSL para los sitios web, además da alta disponibilidad entre zonas.

## Azure VPN Gateway

Facilita conexiones seguras entre redes azure e infraestructuras on premise.

Soporta VPN Site to site, point to site, utiliza túneles VPN que establecen conexiones seguras cifrando los datos que pasan a través de ellos, permite personalizar las configuraciones de VPN y ofrece diferentes tamaños y tipos de gateway

### VPN S2s Site to site

Permite establecer una conexión segura y cifrada entre dos redes como en una cloud híbrida. Esta establece un tunel entre una red local y de nube, viajando la información cifrada.

### VPN Point to site

Permite conectar a usuarios individuales conectarse de manera segura a una red remota como una red corporativa desde cualquier lugar.

## Azure Application Gateway - Equivalente a NLB

Es un equilibrador de carga de tráfico web que permite administrar el tráfico a las aplicaciones web. Con Azure Application Gateway distribuye el tráfico entrante entre múltiples servidores, optimizando el rendimiento. Facilita la configuración de reglas de redirección, ejemplo, de HTTP a HTTPS, soporta zonas de disponibilidad para proporcionar resistencia ante fallos en una zona. Es decir, permite redirigir peticiones a grupos de recurso en base al endpoint.

Además cuenta con cheques de salud para asegurar la distribución eficiente y confiable del tráfico hacia los servidores de backend. Las respuestas de los servidores se evalúan para determinar su estado de salud.

## Azure Content Delivery Network

Permite la entrega rápida y confiable, mejora el rendimiento de lectura, mejora UX, se integra sin problemas con otros servicios de azure y protege DDoS y reglas personalizadas para la defensa contra amenazas. Hace uso de los edge locations guardando en caché la respuesta para que en caso que otros usuarios pregunten por lo mismo, se guarde en caché local la información.

## Azure ExpressRoute

Ofrece una conexión privada y segura entre infraestructuras locales y Azure, proporciona alto rendimiento y baja latencia, la conexión es directa y no transita por el internet público y la nube de Azure, ideal para transferir grandes volúmenes de datos de manera eficiente.

## Resumen

- Azure Networking - Conjunto de servicios para recursos de red
- Azure Virtual Network - Red privada
- Espacio de direcciones - Rango de direcciones IP
- Grupo de seguridad de red - Filtro de tráfico de red que aplica reglas de seguridad a la red virtual
- Azure Load Balance - Distribuye el tráfico entrante entre servidores
- Azure VPN Gateway - Facilita conexiones seguras desde ubicaciones on premise
- Azure Application Gateway - Balanceador de carga que ofrece funcionalidades avanzadas a nivel de red
- Azure Content Delivery Network - CDN de Azure para localizaciones de borde
- Azure ExpressRoute - Conexión privada y segura entre redes Azure y on-premise

Un espacio de direcciones en una red virtual es un número de direcciones IP que son únicas sólo en la red virtual específica. Estas direcciones IP se asignan a los recursos conectados a la VNet, lo que permite a los recursos interactuar y comunicarse. No hay límite en el número de VNets que puedes tener, ni en el número de espacios de direcciones.

ExpressRoute te permite extender tus redes locales al Cloud de Microsoft a través de una conexión privada con la ayuda de un proveedor de conectividad. Con ExpressRoute, puedes establecer conexiones con servicios en la Nube de Microsoft, como Microsoft Azure y Microsoft 365.

Un Gateway VPN es una parte importante de una infraestructura híbrida de Azure. Permite que el tráfico cifrado fluya entre los servicios locales y los servicios de Azure.

El Load Balancer, ubicado ante dos o más máquinas virtuales, gestiona y equilibra la carga entre ellas basado en tráfico entrante o características específicas del mismo. Desvinculado de discos virtuales, puede manejar hasta 1.000 máquinas virtuales. Este garantiza que solo instancias en buen estado reciban tráfico, cesando el envío a servidores que no pasen controles de salud. Además, los Load Balancer de Azure registran el tráfico que los atraviesa.

El alojamiento multisitio en Application Gateway soporta hasta 100 sitios web por instancia, reduciendo costos y complejidad. Esta herramienta, similar a un balanceador de carga, redirige tráfico según atributos de peticiones HTTP. Además de actuar como Controlador de Entrega de Aplicaciones (ADC), ofrece funciones de seguridad como descarga SSL, firewall de aplicaciones web (WAF) y protección DDoS, gestionando eficazmente tráfico en múltiples aplicaciones web de manera segura y eficiente.

Una CDN guarda una copia reciente de tu aplicación web y puede entregarla mucho más rápido a los usuarios cercanos a un endpoint. Las CDN pueden manejar muchos más datos que un servidor web típico, lo que las hace ideales también para manejar picos de tráfico. Por lo general, las CDN no gestionan las reglas individuales de enrutamiento del tráfico, ni la seguridad.
