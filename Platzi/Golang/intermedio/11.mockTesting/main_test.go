package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestGetFullTimeEmployeeById(t *testing.T) {
	table := []struct {
		id               int
		dni              string
		mockFunc         func()
		expectedEmployee FullTimeEmployee
	}{
		{
			id:  1,
			dni: "1",
			/* Estos son los mocks, no las funciones reales */
			mockFunc: func() {
				GetEmployeeByID = func(id int) (Employee, error) {
					return Employee{
						id:       1,
						Position: "CEO",
					}, nil
				}
				GetPersonByDni = func(dni string) (Person, error) {
					return Person{
						DNI:  "1016",
						name: "Alvaro Garzón",
						age:  26,
					}, nil
				}
			},
			expectedEmployee: FullTimeEmployee{
				Person: Person{
					DNI:  "1016",
					name: "Alvaro Garzón",
					age:  26,
				},
				Employee: Employee{
					id:       1,
					Position: "CEO",
				},
			},
		},
	}
	/* Aquí se refiere a la original, para preservarlas en caso de ser necesarias */
	originalGetEmployeeById := GetEmployeeByID
	originalGetPersonByDni := GetPersonByDni
	testifyVerifier := require.New(t)
	for _, test := range table {
		/* Aquí se sustituyen las funciones por los mocks */
		test.mockFunc()
		fulltime, error := GetFullTimeEmployeeById(test.id, test.dni)
		if error != nil {
			t.Errorf("Error getting employee :(")
		}
		testifyVerifier.Equal(test.expectedEmployee.age, fulltime.age, "Validate age")
	}
	/* Se deja las funciones originales a su función, para evitar que se usen los mocks en otros test */
	GetEmployeeByID = originalGetEmployeeById
	GetPersonByDni = originalGetPersonByDni
}
