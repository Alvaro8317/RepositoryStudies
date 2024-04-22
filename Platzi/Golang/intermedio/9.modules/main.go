package main
/* En noe se puede usar npm para generar un arbol de dependencias, con python es con pip
y con golan es con go modules, se pueden usar los siguientes comandos para la gestión de modulos
* go mod init github.com/username/module -> Inicializa un módulo
* go get github.com/donvito/hellomod -> Descarga una dependencia
* go mod tidy -> Elimina las dependencias que no se usan en el proyecto
* go mod download -json -> Elimina las dependencias que no se usan en el proyecto

*/
// import "fmt"
import (
	v1 "github.com/donvito/hellomod"
	v2 "github.com/donvito/hellomod/v2"
)

/* Al actualizar dependencias hay que tener cuidado con romper el código */
func main() {
	// fmt.Println("Hello world with go modules!")
	v1.SayHello()
	v2.SayHello("Alvaro")
}
