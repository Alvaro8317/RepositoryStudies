package main

import "fmt"

/* Clases tienen atributos y métodos, en go no existen las clases, pero si los structs */
/* Para esto, se debe de crear un type (que es un tipo de dato) */
type car struct {
	brand string
	year  int
}

func mainStruct() {
	/* Instancia de un struct */
	/* Primera manera */
	myCar := car{brand: "Ford", year: 2020}
	fmt.Println(myCar)
	/* Segunda manera */
	var otherCar car
	otherCar.brand = "Ferrari"
	fmt.Println(otherCar)

}
