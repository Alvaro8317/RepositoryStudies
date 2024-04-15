package main

import (
	"fmt"
	mypcpackage "golang-platzi/src/mypcpackage"
)

func cursores() {
	/* & apunta a la dirección de memoria
	* apunta al valor de la dirección de memoria */
	/* Los punteros son los accesos a la memoria */
	a := 50
	/* &a indica que apunte a la misma dirección de memoria */
	b := &a
	fmt.Println(a)
	/* Se obtiene la dirección de memoria */
	fmt.Println(b)
	/* Se obtiene valor */
	fmt.Println(*b)
	/* Se modifica al mismo espacio de memoria que a */
	*b = 100
	fmt.Println(*b)
	fmt.Println(a)
	myPc := mypcpackage.Pc{Ram: 32, Disk: 3000, Brand: "msi"}
	fmt.Println(myPc)
	myPc.Ping()
	fmt.Println("PC actual", myPc)
	myPc.DuplicateRam()
	fmt.Println("PC actualizado", myPc)

	// myPc.ram = 64
}
