// El primer archivo que debe de iniciar en go
/* Un package es el nombre de la carpeta donde está guardado */
package main

import "fmt"

func variables() {
	fmt.Println("Hola mundo")
	// Variables
	// Declaración de constantes
	const pi float64 = 3.141516
	const pi2 = 3.14
	fmt.Println("pi", pi)
	fmt.Println("pi2", pi2)
	// Declaracion de variables enteras,
	// si una variable no se ha usado anteriormente, se puede usar :=, esto significa que la crea
	base := 12 // No se dice tipo de dato, agrega el valor y parsea el tipo de dato
	var altura int = 14
	var area int
	fmt.Println(base, altura, area)
	// Si no se usa una variable, dará error, esto es bueno porque no usa el espacio en memoria
	// Zero values, en python asigna None, pero en go depende del tipo de dato
	var a int
	var b float64
	var c string
	var d bool
	fmt.Println(a, b, c, d)
	// Calculo de area de un cuadrado
	const baseCuadrado = 10
	areaCuadrada := baseCuadrado * baseCuadrado
	fmt.Println("Area cuadrada: ", areaCuadrada)
}

/* Se pueden ejecutar los siguientes dos comandos para correr código go:
1. go build main.go \
./ main.go
2. go run main.go
El segundo es menos eficiente, lo que hace es que compila en una carpeta tmp, lo ejecuta
y lo muestra, ideal para dev */
