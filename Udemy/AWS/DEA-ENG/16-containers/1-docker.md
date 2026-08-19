# Docker

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Ventajas de Docker

- **Coherencia:** garantiza que cada aplicación tenga su propio entorno aislado, incluso cuando varias
  aplicaciones se ejecutan en el mismo servidor. Esto evita conflictos entre aplicaciones y reduce el
  riesgo de que una afecte a otra, asegurando que todo funcione de forma fiable.
- **Aislamiento:** cada contenedor corre en su propio entorno independiente.
- **Portabilidad:** los contenedores Docker pueden trasladarse fácilmente entre distintos sistemas y
  entornos. Por ejemplo, una aplicación desarrollada en un portátil puede desplegarse después en un
  proveedor cloud o en un servidor on-premise sin preocuparse por problemas de compatibilidad.
- **Escalabilidad:** ante un aumento repentino de tráfico, se pueden activar contenedores adicionales
  para gestionar la carga, manteniendo un buen rendimiento.

## Casos de uso

- **Arquitectura de microservicios:** los contenedores son ideales para descomponer una aplicación en
  servicios más pequeños e independientemente desplegables.
- **Pipelines de CI/CD:** los contenedores permiten construcciones consistentes y reproducibles, lo que
  facilita construir, probar y desplegar aplicaciones de forma más eficiente.
- **Entornos de nube híbrida:** al ser portátiles, los contenedores permiten a las organizaciones crear y
  desplegar aplicaciones sin problemas entre plataformas on-premise y en la nube.
- **Big data y analítica:** cada vez más se usan para **contenerizar frameworks de procesamiento de
  datos** como Apache Hadoop, Spark o Kafka.

## Componentes principales

| Componente | Descripción |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Docker Engine** | Software central que permite la creación, gestión y despliegue de contenedores. |
| **Docker Image** | Plantilla de solo lectura usada para crear contenedores; contiene todo lo necesario para ejecutar la aplicación. |
| **Docker Container** | Instancia ejecutable de una imagen — esta es la diferencia clave entre imagen y contenedor. |
| **Docker Registry** | Almacena las imágenes Docker (ej. Docker Hub o un registro privado). |

## Registros de imágenes (Docker Registry)

### Docker Hub

- Mayor repositorio **público** de imágenes Docker del mundo.
- Alberga millones de imágenes preconstruidas para distintos casos de uso, bibliotecas y frameworks.
- Ofrece dos tipos de repositorios:
  - **Públicos:** de libre acceso para todos; los desarrolladores publican imágenes de código abierto y
    colaboran con la comunidad.
  - **Privados:** almacenamiento seguro de imágenes, con control de acceso — los desarrolladores pueden
    restringir la visibilidad y conceder acceso solo a los usuarios autorizados.

### Amazon ECR (Elastic Container Registry)

- Registro de contenedores Docker **totalmente gestionado** por AWS.
- Permite almacenar, gestionar y desplegar imágenes Docker de forma segura.
- Se integra con varios servicios de AWS (aunque no con todos).
- Admite tanto repositorios **públicos** como **privados**.

## Comandos esenciales

| Comando | Función |
| ------------- | --------------------------------------------------------------------------- |
| `docker build` | Crea una imagen Docker a partir de un **Dockerfile** (archivo de texto con las instrucciones de construcción). |
| `docker push` | Sube una imagen Docker desde la máquina local a un registro, haciéndola disponible para otros. |
| `docker pull` | Descarga una imagen Docker desde un registro a la máquina local. |
| `docker run` | Crea e inicia un contenedor Docker a partir de una imagen. |
