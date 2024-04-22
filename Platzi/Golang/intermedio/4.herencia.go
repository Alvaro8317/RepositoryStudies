package main

import "fmt"

/* En go no existe la herencia como tal, go lo que aplica es la composición
de clases */

type Person struct {
	name string
	age  int
}

type Employee3 struct {
	id int
}

type FullTimeEmployee struct {
	/* Se dejan estos campos anonimos, nada de person Person, esto da unos beneficios,
	como poder acceder de manera directa a los structs que componen al empleado de tiempo
	completo */
	Person
	Employee3
}

/*
	El polimorfismo no se puede aplicar de esta manera porque un fullTimeEmployee a pesar

de estar compuesto por un Person, no es un Person
*/
func GetMessage(person Person) {
	fmt.Printf("%s with age %d\n", person.name, person.age)
}

func composicionSobreHerencia() {
	fullTimeEmployee := FullTimeEmployee{}
	fullTimeEmployee.name = "Alvaro"
	fullTimeEmployee.age = 26
	fullTimeEmployee.id = 7
	fmt.Println(fullTimeEmployee) /* Output: {{Alvaro 26} {7}} */
	// GetMessage(fullTimeEmployee)
	/* Go para alcanzar este objetivo aplica el principio llamado
	"composition over inheritance | composición sobre la herencia" para que por medio
	de campos anónimos en un struct pueda heredar las propiedades y métodos */
}
