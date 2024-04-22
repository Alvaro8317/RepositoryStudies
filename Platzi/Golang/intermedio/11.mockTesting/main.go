package main

import "time"

type Person struct {
	DNI  string
	name string
	age  int
}

type Employee struct {
	id       int
	Position string
}

type FullTimeEmployee struct {
	/* Se dejan estos campos anonimos, nada de person Person, esto da unos beneficios,
	como poder acceder de manera directa a los structs que componen al empleado de tiempo
	completo */
	Person
	Employee
}

var GetPersonByDni = func(dni string) (Person, error) {
	time.Sleep(5 * time.Second)
	/* SELECT * FROM PERSONA .... */
	return Person{}, nil
}

// var GetEmployeeByID = func(id int) (Employee, error) { #Es lo mismo que la linea siguiente
var GetEmployeeByID = func(id int) (Employee, error) {
	time.Sleep(5 * time.Second)
	/* SELECT * FROM Employees .... */
	return Employee{}, nil
}

func GetFullTimeEmployeeById(id int, dni string) (FullTimeEmployee, error) {
	var fullTimeEmp FullTimeEmployee
	employee, err := GetEmployeeByID(id)
	/* Go no tiene excepciones, entonces se debe de validar el error */
	if err != nil {
		return fullTimeEmp, err
	}
	fullTimeEmp.Employee = employee
	person, err := GetPersonByDni(dni)
	if err != nil {
		return fullTimeEmp, err
	}
	fullTimeEmp.Person = person
	return fullTimeEmp, nil
}

func main() {

}
