# Seguridad

## Defensa en profundidad

Se refiere a una estrategia que emplea múltiples capas de seguridad compuesta por algunos compónentes o capas:

- Políticas y procedimientos
- Seguridad física
- Perímetro
- Redes
- Hosts
- Aplicaciones
- Datos (El concepto más valioso)

## Endpoints

Por defecto, existen riesgos de exposición pública en azure, como servicios gestionados accesibles vía internet o se pueden tener recursos críticos visibles públicamente.

Para eliminar o limitar la exposición pública se puede tener:

1. Puntos de conexión de servicio - Protección adicional sin eliminar el acceso público ->
2. Puntos de conexión privados - Conexión segura a través de red privada, minimizando la exposición pública -> Conexión directa desde la subred a servicios Azure, la conexión se realiza a través de la infraestructura privada de Microsoft, además se puede restringir el acceso a direcciones IP públicas específicas.

### Acceso seguro únicamente para redes virtuales (VNets)

- No hay acceso privado desde las instalaciones locales
- Se debe permitir el acceso desde las instalaciones físicas a través de la IP pública
- El endpoint público del servicio todavía existe
- Los endpoints de servicio proporcionan acceso a un servicio completo

Teniendo en cuenta estas limitaciones, se tienen los endpoints privados

### Endpoints privados

Permiten a los usuarios tener conexiones seguras y privadas dentro de una red virtual a los servicios gestionados de Azure como Azure Storage o SQL Database. Se puede establecer una interfaz de red gestionada (NIC) que es un recurso que permite que una red virtual se comunique con el servicio Azure a través de una IP privada, además, permite deshabilitar por completo el acceso público a un servicio conectado. Para finalizar, tiene disponibilidad a través de redes conectadas y así sin exponer un recurso sensible. Además, se puede establecer una comunicación con la red por medio de una VPN.

### Caso práctico

Se requiere establecer una conexión segura desde casa a una VNet debido a que ahí está una base de datos con información sensible; Con exposición a internet público así sea por VPN puede implicar riesgos de seguridad y exposición de datos sensibles

Para solucionarlo, se debe de usar un endpoint privado donde se utiliza este para conectar la VNet directamente y de manera privada con la BD y aún así se establece la VPN con la VNet. Finalmente se puede deshabilitar el acceso público a la BD

## Azure Key Vault

Es un almacenamiento de llaves seguro equivalente al secrets manager, permite almacenar secretos y el acceso a estos de forma segura. Ni si quiera Microsoft puede acceder a las claves que contiene, permite aislamiento entre aplicaciones y tiene una escalabilidad global.

## Microsoft Defender for Cloud (Antes conocido como Azure Security Center)

Es una plataforma de protección de aplicaciones nativas de la nube, provee alertas contra amenazas, preparado para arquitecturas híbridas y cada VM tiene un agente instalado que envía los datos. Azure analiza la información y alerta de ser necesario.

- Evaluación continua
- Políticas personalizables
- Detección avanzada
- Protección VM
- Recomendaciones de seguridad
- Integración completa
- Visualización de seguridad
- Respuesta a incidentes
- Cumplimient regulatorio
- Multinube (Extiene la protección a AWS o GCP)

### Uso

1. Definición de políticas
2. Protección de recursos
3. Responde ante alertas de seguridad

### Inventario

Este servicio provee una interfaz con recomendaciones relacionadas a la seguridad de los servicios en la nube

## Azure Sentinel

Es una herramienta SIEM (Información de seguridad y gestión de eventos), permite:

1. Colección de datos
2. Agregación y normalización
3. Análisis y detección de amenazas
4. investigación y validación

### Beneficios

Sentinel analiza el comportamiento, tiene escalabilidad, se integra con AWS y provee seguridad

## Resumen

- Defensa en profundidad - Estrategia para proteger a todo nivel
- Puntos de conexión:
  - De servicio - Provee acceso por IP públicas
  - Privados - Facilitan conexiones segturas y directas usando una IP privada
- Azure Key Vault - Administración centralizada de secretos, claves de cifrado y certificados
- Microsoft Defender for cloud - Solución que salvaguarda los recursos de Azure mediante identificación y mitigación de amenazas y vulnerabilidades
- Sentinel - SIEM que proporciona viión avanzada y respuesta automatizada frente a amenazas cloud

La defensa en profundidad busca crear múltiples capas de protección en una infraestructura de IT

Un endpoint privado en Azure es una dirección IP dentro de una red virtual que permite el acceso privado a servicios de Azure

Azure Key Vault es un servicio para almacenar y gestionar claves criptográficas y otros secretos de manera segura

Microsoft Defender for Cloud proporciona herramientas para monitorear y gestionar la postura de seguridad en entornos Azure

Azure Sentinel es una solución SIEM y SOAR basada en la nube

Un SIEM, como Azure Sentinel, está diseñado para gestionar y analizar eventos de seguridad en tiempo real

Azure Key Vault está diseñado para almacenar y administrar de manera segura claves criptográficas y otros secretos como cadenas de conexión

Azure Sentinel es una solución SIEM y SOAR que permite detectar y responder a amenazas en tiempo real

Un endpoint es un punto de conexión remoto que permite acceder a servicios o recursos en la nube

Microsoft Defender for Cloud proporciona herramientas para proteger cargas de trabajo híbridas en entornos de nube y on-premises
