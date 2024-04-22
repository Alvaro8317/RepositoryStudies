package main

import "fmt"

type Employee2 struct {
	id       int
	name     string
	vacation bool
}

func NewEmployee(id int, name string, vacation bool) *Employee2 {
	return &Employee2{
		id:       id,
		name:     name,
		vacation: vacation,
	}
}

func instancias() {
	/* Forma número 1 de instanciar */
	employee := Employee2{} /* Se le asignan los zero values */
	fmt.Println(employee)
	/* Forma número 2 de instanciar */
	employee2 := Employee2{
		id:       1,
		name:     "Alvaro",
		vacation: true,
	}
	fmt.Println(employee2)
	/* Forma número 3 de instanciar */
	employee3 := new(Employee2) /* Retorna el apuntador cuando se usa un new */
	fmt.Println(*employee3)
	employee3.id = 1
	employee3.name = "Eduardo"
	fmt.Println(*employee3)
	/* Forma ideal, generalizar las instancias con un "constructor" */
	employee4 := NewEmployee(1, "Papucho", true)
	fmt.Println(*employee4)
}
