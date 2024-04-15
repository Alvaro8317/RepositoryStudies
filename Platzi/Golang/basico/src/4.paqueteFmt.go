package main

import "fmt"

/* fmt tiene varias funcionalidades */
func packageFmt() {
	/* Declaración de variables */
	helloMessage := "Hello"
	worldMessage := "world!"
	/* PrintLn -> Un print con salto de línea */
	fmt.Println(helloMessage, worldMessage)
	fmt.Println(helloMessage, worldMessage)
	/* Printf -> Aparte de imprimir, agrega una función extra al string como valor de entrada */
	name := "Alvaro"
	course := 50
	/* %s para string, %d para digitos o enteros y %v cuando no se sabe el tipo de dato */
	/* Lo ideal es especificar el tipo de dato, dejar el %v como último recurso */
	fmt.Printf("%s tiene más de %d cursos finalizados\n", name, course)
	fmt.Printf("%v tiene más de %v cursos finalizados\n", name, course)
	/* Sprintf -> Formatea un string similar a printF pero retorna como resultado el string ya formateado */
	message := fmt.Sprintf("%s tiene más de %d cursos finalizados", name, course)
	fmt.Println(message)
	/* Con este paquete se puede saber también el tipo de dato de una variable */
	/* %T para el tipo de dato */
	fmt.Printf("helloMessage es de tipo: %T\n", helloMessage)
	fmt.Printf("course es de tipo: %T\n", course)
}
