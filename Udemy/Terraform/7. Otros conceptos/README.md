# 7. Otros conceptos

## Dependencias

En terraform hay dependencias tanto implicitas como explicitas, terraform es un lenguaje de programación de tipo declarativo, significa que se le dice "qué quiero" pero no decir "como hacerlo".

## Dependencia implicita

en base a las dependencias es que terraform define que recursos crear primero y cuales no, ejemplo, si se tiene una subnet que depende de la vpc, infiere en que terraform creará primero la vpc y en base a esa, creará la subnet. Si se tienen dos subnets que ambas dependen de la misma VPC pero no dependen entre sí, se pueden desplegar de manera paralela.

## Dependencia explicita

Estas dependencias se declaran con la función `depends_on`:

```hcl
resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.vpc_virginia.id
  depends_on = [
    aws_subnet.public_subnet
  ]
}
```

De esta forma se le dice a terraform que debe de crear primero la subnet pública antes que este recurso.

## Targets

Los targets permiten desplegar recursos especificos sin necesidad de desplegar todos los archivos que encuentre terraform, este se usa con el comando `terraform apply --target aws_subnet.public_subnet`, este es útil cuando se requiere hacer cambios a un recurso y no al resto de los recursos que ya han sido modificados

## Bloques Data

Con estos bloques se usan para leer la infraestructura existente ya desplegada y usar estos datos en la IaC. Un ejemplo es un par de llaves para EC2 en los que terraform va hasta AWS, lee los datos según corresponda y ahora se puede utilizar ese código en la IaC de EC2

## Terraform State

Este archivo se genera luego de desplegar la infraestructura, este archivo va de la mano con los archivos de configuración .tf, ya que estos muestran la infraestructura deseada y el `tfstate` muestra la infraestructura desplegada, de esa razón si los recursos ya fueron desplegados, terraform puede identificar que está ya desplegado. NUNCA se debe de editar manualmente el tfstate. **Dentro de este archivo se pueden encontrar datos sensibles**

El archivo .tfstate.backup tiene la infraestructura que antes tenía desplegada, se llena después de un destroy.

Trabajando en una empresa, el tfstate debe de estar centralizado, en un repositorio remoto, se maneja un tfstate remoto pero NUNCA se debe de subir el state a un repositorio cualquiera por cuestiones de seguridad, este tiene información sensible y debe ser tratado con cuidado; Si se trabaja en AWS, se podría subir a un bucket s3 versionado, cifrado y acompañado de una tabla DynamoDB para asegurar que solo una persona use el tfstate. **Se debe de trabajar con un tfstate remoto pero no en repositorios de código cualquieras. Finalmente, se puede guardar el tfstate en la terraform cloud.**

## REFRESH: Comandos de terraform

- `terraform validate` -> Valida la sintaxis
- `terraform apply` -> Despliega o aplica los cambios
- `terraform fmt` -> Formatea el código
- `terraform show` -> Muestra los recursos desplegados, valida contra el tfstate
- `terraform apply --replace` -> Equivalente a hacer un destroy y después un apply sobre un recurso
- `terraform show --json` -> Lo mismo que show pero en JSON
- `terraform providers` -> Muestra los providers con los que se está trabajando y las constraints
- `terraform output` -> Visualiza las salidas escritas en los archivos tf, permite traer el output por su nombre especificando su nombre después del output
- `terraform plan` -> El plan muestra lo que planea y hace refrezca el tfstate en caso de encontrar algún cambio en la infraestructura desplegada
- `terraform refresh` -> Refrezca los cambios en caso que tenga una variación hecha manualmente desde la GUI
- `terraform graph` -> Genera una lista de las independencias y de como se relacionan entre ellos, permite generar un diagrama, se puede usar en conjunto con `terraform graph | dot -Tsvg > graph.svg`
- `terraform state list` -> Obtiene la lista de los recursos desplegados, a partir de aquí son los comandos propios para state, es decir, para modificar solamente los archivos state.
- `terraform state show nombreRecurso` -> Muestra el estado de un recurso especifico desplegado, **es para ver uno en especifico a diferencia del show**
- `terraform state mv` -> Mueve los recursos dentro del terraform state, es decir, sirve para cambiar el ID de un recurso, ejemplo, antes se llamaba subnet_publica y se puede llamar ahora subnet_publica_nueva, el ejemplo completo es `terraform state mv aws_subnet.old_name aws_subnet.new_nbame`, así, terraform no detectará cambios en los recursos y así no eliminará recursos o crear nuevos.
- `terraform state rm nombreRecurso` -> Borra recursos, no los borra desplegados, solo lo borra en el tfstate, esto puede ser útil cuando se tiene infraestructura desplegada ya con terraform y se desea que terraform ya no lo tenga en seguimiento y después ejecutar un apply

## Lifecycles

Es un metaargumento, permite indicarle a terraform de como comportarse ante algunos cambios en los recursos. Por defecto, ante algunos cambios disruptivos, terraform destruye y después crea, eso se puede cambiar con un lifecycle, de la siguiente manera:

```hcl

resource "aws_instance" "instance_test" {
  ami           = "ami-0ae8f15ae66fe8cda"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  key_name      = data.aws_key_pair.ec2_key_pair.key_name
  tags = {
    Name = "Instance test"
  }
  lifecycle {
    create_before_destroy = true
  }
}

```

Así, terraform por defecto primero creará y después destruirá la instancia, existen otros atributos que pueden ser:

- `prevent_destroy = false`, así, bajo ningún concepto, terraform eliminará el recurso. Este lifecycle se puede usar con recursos muy críticos.
- `ignore_changes = []`, sirve para ignorar cambios que recibe múltiples argumentos, ejemplo, si se deja dentro el atributo ami, significa que cuando se cambie el ami, se ignorará el cambio a pesar de la diferencia entre el tfstate y los archivos tf.
- `replace_triggered_by = []`, se dejan una lista de recursos que si sufren de un cambio, va a disparar el reemplazo del recurso, ejemplo, si una instancia ec2 tiene este lifecycle y tiene una subnet que no tiene relación, entonces si se cambia así sea un tag en el lifecycle, se redesplegará la instancia

### Notas adicionales

#### Auto-approve

Se puede hacer uso de este parámetro en un apply como `terraform apply --auto-approve=true`
para aprobar de manera automática un despliegue, no se recomienda del todo, pero existe, es equivalente al `confirm_changeset` de AWS. Este parámetro aplica para el apply y para el destroy.

#### Diagramas de infraestructura

A medida que crece la infraestructura, se puede volver complejo el entender la infraestructura viendo solo el código, por esa razón, se recomienda realizar [draw.io](https://app.diagrams.net/) para realizar el diseño de la infraestructura.

## Provisioners

En Terraform, un provisioner es un bloque de configuración que se utiliza para ejecutar scripts o comandos una vez que un recurso ha sido creado o destruido. Los provisioners permiten realizar tareas adicionales que no se pueden manejar directamente a través de la definición del recurso en sí, como la instalación de software, la configuración de archivos, o la ejecución de scripts de configuración en máquinas virtuales.

Tipos de Provisioners

- local-exec: Ejecuta un comando o script en la máquina local donde se está ejecutando Terraform. Es útil para tareas que necesitan interacción con el sistema local, como la generación de archivos o el envío de notificaciones.

- remote-exec: Ejecuta un comando o script en un recurso remoto, generalmente una máquina virtual. Se conecta al recurso a través de SSH o WinRM para realizar la ejecución.

- file: Copia archivos o carpetas desde la máquina local al recurso remoto.

Estos provisioner a pesar de ser una buena opción, no son lo más recomendable, en la vida real se usa user-data para AWS por ejemplo

## Terraform taint

Se puede traducir taint a como manchado o marcado para que se destruya y se vuelva a recrear, se utiliza con `terraform taint nombre_recurso`, también, se puede desmanchar con `terraform untaint`, se utilizaba para reemplazar los recursos pero fue reemplazado por `terraform apply --replace`

Taint es importante porque hay casos donde ciertos recursos pueden fallar en su despliegue o destrucción y terraform los puede dejar como manchados, ejemplo, si con un provisioner llega a fallar, se desplegará el recurso, pero terraform lo deja como manchado con taint y así sugiere reemplazarlo, en caso que no se quiera reemplazar, se debe de usar `untaint` y ya quedaría.

## Terraform logging / Debug

Terraform Logging se refiere al sistema de registro y salida que Terraform utiliza para proporcionar información sobre lo que está sucediendo durante la ejecución de comandos, como terraform plan, terraform apply, y otros. Los registros (logs) de Terraform pueden ser útiles para depurar errores, entender el flujo de ejecución, y monitorear la actividad de Terraform.

### Tipos de Logs en Terraform

1. Output Logs:
   Estos son los mensajes estándar que se muestran en la consola mientras se ejecutan los comandos de Terraform.
   Muestran información sobre las acciones que Terraform está tomando, como la creación, destrucción o actualización de recursos, así como el resultado del plan o aplicación.

2. Debug Logs:
   Terraform puede generar logs detallados (debug logs) que contienen información más específica sobre el proceso interno.
   Estos logs son útiles cuando necesitas depurar un problema o entender más a fondo lo que Terraform está haciendo.

### Configuración de Terraform Logging

Terraform utiliza la variable de entorno TF_LOG para controlar el nivel de detalle de los logs. Aquí están los niveles disponibles:

- TRACE: Muestra todos los logs de depuración posibles, incluidos los detalles más bajos de las operaciones internas.
- DEBUG: Proporciona información detallada útil para depurar, pero menos extensa que TRACE.
- INFO: Muestra información general sobre lo que está haciendo Terraform (este es el nivel por defecto).
- WARN: Solo muestra advertencias que podrían ser problemas potenciales.
- ERROR: Solo muestra errores que causan fallos.
- OFF: Desactiva el logging.

### Cómo Habilitar Terraform Logging

Para habilitar los logs en Terraform, se puede exportar la variable de entorno TF_LOG con el nivel deseado antes de ejecutar un comando de Terraform. Por ejemplo:

```bash
export TF_LOG=DEBUG
export TF_LOG_PATH=./terraform.log
terraform apply
```

### Log Path

Esta variable permite especificar la ubicación de los logs, si no se especifica, se mostrarán en la consola.

## Importar recursos

Cuando hay recursos desplegados por la GUI o directamente desde la CLI, se puede aún así importar estos recursos, cada recurso de terraform se puede importar en base al id del recurso, para importar un recurso es con `terraform import aws_instance.mywebserver id`, el recurso de mywebserver se debió de haberse creado previamente a pesar de estar vacío, el import no modifica los archivos actuales .tf, lo que si modifica es el .tfstate, ya después se puede hacer uso de `terraform state list` y `terraform state show nombreRecurso`, con esto se verá todo el detalle del recurso, copiarlo, pegarlo en los archivos .tf eliminando los innecesarios y ya se finalizaría la importación.

## Workspaces

Los workspaces permiten reutilizar el código para desplegarlo en diferentes entornos como desarrollo, producción, etc. Es breve y puede que no se pregunte en la certificación.

Comandos:

- `terraform workspace list` -> Lista los espacios de trabajo disponibles
- `terraform workspace new` -> Crea un nuevo espacio de trabajo
- `terraform workspace select` -> Equivalente a checkout de git, cambia de un ambiente a otro
- `terraform workspace show` -> Muestra en qué workspace está
- `terraform workspace delete` -> Elimina un espacio de trabajo

Se puede hacer uso de la función lookup para poder tener variables en base al workspace, ejemplo, `lookup(var.virginia_cidr, terraform.workspace)` donde la variable de virginia_cidr debe de ser un map.

El uso de workspaces en Terraform ha disminuido en popularidad principalmente porque no siempre es la solución ideal para gestionar entornos de infraestructura como código (IaC) en proyectos complejos. Además, que podría incurrir en accidentes y diferentes estrategias de backend, por estas razones, no se usa comunmente terraform workspaces
