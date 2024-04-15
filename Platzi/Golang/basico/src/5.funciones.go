package main

import "fmt"

func printHolaFunction(messageToPrint string) {
	fmt.Println(messageToPrint)
}

// func threeParametersOfFunction(a int, b int, c string) { No tan buena practica
func threeParametersOfFunction(a, b int, c string) { /* Mejor practica */
	fmt.Println(a, b, c)
}

func returnIntegerValue(number int) int {
	return number * 2
}

func doubleReturn(a int) (c, d int) {
	return a, a * 2
}

func funciones() {
	printHolaFunction("Hola funciones")
	printHolaFunction("Hola funciones 2")
	printHolaFunction("Hola funciones 3")
	threeParametersOfFunction(5, 6, "")
	var result int = returnIntegerValue(5)
	fmt.Println(result)
	var value1, value2 int = doubleReturn(6)
	fmt.Println(value1, value2)
	/* Si solo se requiere una variable y no otra, se puede usar _ */
	var value3, _ int = doubleReturn(6)
	fmt.Println(value3)
}
