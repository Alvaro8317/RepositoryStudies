# 1. Introducción a terraform

Permite desplegar IaC en diferentes proveedores como Azure, GCP, AWS, Alibaba, Oracle, etc. Pero no solo se limita a cloud providers, también soporta K8s. Es una herramienta agnóstica, permite trabajar con muchísimos proveedores.

## ¿Qué se verá en el curso?

- Conceptos de IaC
- Terraform vs otras herramientas de la IaC
- Principios de terraform
- Implementar y administrar el tfstate
- Trabajar con modulos
- Terraform Workflow
- Leer, mantener y modificar la configuración de los entornos
- Comprender y trabajar con terraform cloud
- Complementos externos utiles
- Construir un entorno de trabajo profesional

## Instalación de terraform

Se puede instalar terraform desde la página web oficial de Hashicorp que es Hashicorp Developer, para la instalación se puede dejar el .exe en windows en Windows/System32 y así las terminales reconocerán siempre el comando "terraform", en linux es un proceso similar pero dejando el ejecutable en la carpeta usr/bin, finalmente se puede usar `terraform --version` para confirmar la correcta instalación.

## Introducción a IaC

IaC no es algo nuevo, Docker también se considera como IaC, existe:

1. IaC orientado a la configuración -> La finalidad es instalar y gestionar software (aprovisionamiento de servidores). Permite mantener un estándar en los servidores y se puede tener un control de versiones de los despliegues, un ejemplo es **Ansible o Puppet**
2. IaC orientado a servidores (templates) -> Aprovisiona contenedores, permite tener preinstalado el software y las dependencias necesarias, funciona tanto como VM como para contenedores y en los ejemplos es Docker, Packer o Vagrant. **La infraestructura es inmutable, es decir, no se accede al contenedor para hacer un cambio, si hay que hacer un cambio, se debería de generar una nueva imagen**
3. IaC para aprovisionamiento -> Es infraestructura como codigo declarativo, un ejemplo es CloudFormation y Terraform, esto de declarativo se dice qué montar pero no el cómo. Permite aprovisionar recursos inmutables en la infraestructura, permite desplegar toda clase de recursos como instancias, bases de datos, buckets, vpc, etc. Se puede desplegar infraestructura en multiples proveedores

## Introducción a HCL

HCL hace referencia a Hashicorp Configuration Language - Es un lenguaje declarativo y propio de terraform, un ejemplo es como el siguiente: `resource "local_file" "mensaje"` cuenta con los siguientes elementos:

- Tipo de bloque -> resource, los recursos
- Tipo de recurso -> local_file, donde local es el proveedor y file es el recurso, en cada tipo de recurso hay diferentes argumentos, estos argumentos se consultan en la [documentación de terraform](https://registry.terraform.io/)
- Nombre del recurso -> Mensaje

El tipo de bloque y el tipo de recurso son palabras reservadas de terraform, el ejemplo completo de terraform sería así:

```hcl
resource "local_file" "mensaje" {
  content = "Este es un archivo"
  filename = "archivo.txt"
}
```

Los archivos de terraform tienen la extensión tf

## Comandos terraform

Lo primero que se debería de hacer es crear el archivo `terraform.tf`, ya creado con el tipo de provider que para este caso fue local_file, se ejecuta el comando `terraform init`, para este caso, terraform deducirá el tipo de provider y creará el archivo .terraform.lock.hcl, luego, se recomienda correr `terraform plan` para saber que es lo que hará, este comando se puede ejecutar múltiples veces ya que no creará nada, solo mostrará lo que se planea crear. Si se quiere llevar a cabo el plan, se debe de ejecutar `terraform apply`, en el fondo crea un plan y lo presenta, no necesariamente se basa en el creado por plan, lleva por defecto un implicito plan.

Terraform al manejar el concepto de inmutabilidad, está mal llegar a modificar un recurso directamente sin pasar por terraform, por lo que se recomienda modificar es el archivo terraform con el que se crearon los recursos y de ahí, modificar lo necesario.

Finalmente, se puede hacer uso de `terraform destroy` para destruir los recursos
