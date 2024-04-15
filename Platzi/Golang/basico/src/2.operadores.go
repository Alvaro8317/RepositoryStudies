package main

import (
	"fmt"
	"math"
)

func operators() {
	x := 10
	y := 50
	// Suma
	resultSuma := x + y
	fmt.Println("Suma: ", resultSuma)
	// Resta
	fmt.Println("Resta: ", y-x)
	// Multiplicación
	fmt.Println("Multiplicación: ", x*y)
	// División
	fmt.Println("División: ", y/x)
	// Residuo
	fmt.Println("Residuo: ", x%y)
	// Incremento
	x++
	fmt.Println("Incremento de X: ", x)
	// Decremento
	x--
	fmt.Println("Decremento de X: ", x)
	// Area rectangulo
	const base int = 5
	const altura int = 7
	fmt.Println("areaRectangulo: ", base*altura)
	// Area trapecio
	const baseTrapecioA int = 5
	const baseTrapecioB int = 7
	const alturaTrapecio int = 10
	fmt.Println("areaTrapecio: ", (baseTrapecioA+baseTrapecioB)/2*alturaTrapecio)
	// Area circulo
	const pi float64 = math.Pi
	const radio float64 = 4
	fmt.Println("areaCirculo: ", math.Pow(radio, 2)*pi)
}
