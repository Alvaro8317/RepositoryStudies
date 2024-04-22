package main

import "fmt"

/* Las funciones variádicas son útiles porque permiten utilizar como slices los argumentos
de funciones de las cuáles no se sabrá su longitud exacta  */

/* Solo permite recibir 2 argumentos  */
func sum(a, b int) int {
	return a + b
}

/* Estas son las funciones variadicas */
func sumTotal(values ...int) int {
	total := 0
	for _, num := range values {
		total += num
	}
	return total
}

func printNames(names ...string) {
	for _, name := range names {
		fmt.Println(name)
	}
}

/* Se permite guardar variables dentro del bloque */
// func getValues(x int) (int, int, int) { Primera forma, sin especificar el nombre de la variable
/* Los retornos con nombre permiten definir variables antes del cuerpo de la función, por lo que
solo se utilizaría return para devolverlos */
func getValues(x int) (doble int, triple int, cuadruple int) {
	doble = 2*x + 1
	triple = 3*x + 1
	cuadruple = 4*x + 1
	// return 2 * x, 3 * x, 4 * x
	return /* Go infiere el valor de las variables que se nombraron más arriba */
}

func main() {
	fmt.Println(sum(1, 2))
	/* El argumento se tratará un slice */
	fmt.Println(sumTotal(1, 2, 3, 4, 5))
	printNames("1", "2", "3", "4", "5")
	fmt.Println(getValues(3))
}
