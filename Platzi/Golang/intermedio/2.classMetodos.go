package main

import "fmt"

type Employee struct {
	id   int
	name string
}

/* Métodos de los structs - Receiver functions, es lo mismo que un método pero diferente
a la sintaxis usual */
/* Aquí se le indica que este struct posee un método llamado SetId con la instancia de e*/
/* Aquí se recrea el comportamiento de clases con go */
/* Algunos lenguajes de programación implementan la filosofía que todo debe de ser un objeto, sin embargo, no es algo aplicable siempre. */
func (employee *Employee) SetId(id int) {
	employee.id = id
}

func (employee *Employee) SetName(name string) {
	employee.name = name
}

func (employee *Employee) GetId() int {
	return employee.id
}

func (employee *Employee) GetName() string {
	return employee.name
}

func mainMetodos() {
	myEmployee := Employee{id: 1, name: "Alvaro Garzón"}
	fmt.Println(myEmployee)
	myEmployee.SetId(5)
	myEmployee.SetName("Alvaro Eduardo")
	fmt.Println(myEmployee)
	fmt.Println(myEmployee.GetId())
	fmt.Println(myEmployee.GetName())
}
/* Los constructores permiten instanciar objetos en clases */