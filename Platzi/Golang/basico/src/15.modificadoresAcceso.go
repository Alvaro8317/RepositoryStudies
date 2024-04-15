package main

import (
	"fmt"
	pck "golang-platzi/src/mypackage"
	/* pck es el alias */)

/* La convención en go es que si es UpperCamelCase o PascalCase, es de acceso público el struct */
/* Se lowerCamelCase es de acceso privado y retorna excepción indicando que no existe el struct */
func modificadoresAcceso() {
	var myCar pck.CarPublic
	myCar.Brand = "Ferrari"
	myCar.Year = 2020
	fmt.Println(myCar)
	// var myOtherCar pck.carPrivate
	// fmt.Println(myOtherCar)
	pck.PrintMessage("Hola")
	/* Da error porque es privada */
	// pck.printMessagePrivate("Hola")
}

/* Los modificadores de acceso aplican para tipos de datos, métodos, etc. */
