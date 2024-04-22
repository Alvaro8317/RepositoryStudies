package main

/*
* Con una interfaz una clase se compromete a implementar
* todos los componentes que define la interfaz con sus atributos
* La interfaz define que se debe de implementar pero la clase es la que
* se encarga de definir su implementación, la implementa como más le convenga
 */
import (
	"fmt"
)

type Person2 struct {
	name string
	age  int
}

type Employee4 struct {
	id int
}

type FullTimeEmployee2 struct {
	Person2
	Employee4
	endDate string
}

func (ftEmployee FullTimeEmployee2) getMessage() string {
	return "Full time employee"
}

func (tEmployee TemporaryEmployee) getMessage() string {
	return "Temporary employee"
}

/*
* Go no implementa interfaces de manera explicita como en typescript
* por esta razón toca generar la nueva función que es getMessage y retornar
* el método que se requiere.
* o lo hace de manera implícita lo que permite la reutilización de código y el polimorfismo
 */
func getMessage(interfaceParam PrintInfo) {
	fmt.Println(interfaceParam.getMessage())
}

type TemporaryEmployee struct {
	Person2
	Employee4
	taxRate int
}

type PrintInfo interface {
	getMessage() string
}

func interfaces() {
	fullTimeEmployee := FullTimeEmployee2{}
	fullTimeEmployee.name = "Alvaro"
	fullTimeEmployee.age = 26
	fullTimeEmployee.id = 7
	fmt.Println(fullTimeEmployee)
	temporaryEmployee := TemporaryEmployee{}
	getMessage(temporaryEmployee)
	getMessage(fullTimeEmployee)

}
