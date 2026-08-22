# Amazon API Gateway

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Amazon API Gateway** permite crear, publicar, mantener y monitorizar **APIs seguras a escala**.
Se definen **recursos** que corresponden a un endpoint o ruta URL específica.

## Tipos de API

| Tipo | Descripción |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **REST API** | Sigue la arquitectura REST estándar. Se integra fácilmente con endpoints como funciones Lambda o servicios HTTP. Soporta rutas y métodos basados en recursos para operaciones **CRUD** (Create, Read, Update, Delete). |
| **WebSocket API** | Comunicación **full-duplex** y en tiempo real entre cliente y servidor mediante el protocolo WebSocket. Útil para aplicaciones de chat o actualizaciones/notificaciones en directo, soportando comunicación en tiempo real a través de varias rutas. |
| **HTTP API** | Permite crear APIs RESTful con **menor latencia** y **menor coste** que las REST API tradicionales. Soporta **OpenID Connect** y **OAuth 2.0**, e incluye soporte integrado para **CORS** (Cross-Origin Resource Sharing). Ofrece despliegues automáticos. |

> ⚠️ Para APIs RESTful de alto rendimiento y bajo coste, **HTTP API** suele ser preferible a
> **REST API** — a menos que se necesiten funcionalidades específicas de REST API no disponibles
> en HTTP API.

## Opciones de integración

| Tipo de integración | Descripción |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Lambda** | Invoca directamente una función Lambda al activarse el endpoint de la API — forma sencilla de manejar peticiones HTTP ejecutando código como respuesta. |
| **HTTP/HTTPS** | Reenvía solicitudes a endpoints HTTP/HTTPS — adecuado para microservicios alojados en EC2, contenedores, servidores on-premises, o APIs externas. |
| **Mock (simulada)** | Simula una respuesta de backend sin llamar a un backend real — útil para pruebas y para verificar la configuración inicial de la API. |
| **AWS Proxy** | Reenvía las solicitudes directamente a una función Lambda, pasándolas en un formato JSON estandarizado. |

## Control de tráfico: throttling, cuotas y rate limiting

Mecanismos para controlar y gestionar el tráfico hacia la API, garantizando la fiabilidad y
disponibilidad del backend y evitando abusos:

| Mecanismo | Descripción |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Throttling** (estrangulamiento) | Evita que la API se sature por picos de tráfico, estableciendo un límite de **peticiones por segundo**. |
| **Quotas** (cuotas) | Limita el número **total** de solicitudes que un cliente puede hacer en un periodo determinado (diario, semanal, mensual). Se aplican mediante **planes de uso** (*usage plans*), asociados a una **API key**. |
| **Rate limiting** | Combina throttling y cuotas para controlar el ritmo al que se aceptan las solicitudes de la API. |

## Tipos de endpoint

| Tipo de endpoint | Descripción |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Edge-optimized** | Reduce la latencia para clientes a nivel global usando **CloudFront** (la red CDN de AWS) para cachear las solicitudes/respuestas en ubicaciones edge. |
| **Regional** | Pensado para clientes dentro de la misma región de AWS donde se despliega la API; no usa caché de CloudFront por defecto — reduce la latencia para clientes in-region. |
| **Private** | Accesible únicamente dentro de una **VPC**, mediante un **VPC endpoint de interfaz**. Evita la exposición a Internet pública, proporcionando una conexión segura y privada. |

> ⚠️ La elección del tipo de endpoint depende de dónde estén los clientes (globales vs. dentro de
> la región) y de si la API debe permanecer privada dentro de una VPC.
