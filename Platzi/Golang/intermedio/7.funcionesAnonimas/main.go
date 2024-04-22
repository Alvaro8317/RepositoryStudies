package main

import (
	"fmt"
	"time"
)

func main() {
	x := 5
	/* Las funciones anónimas son útiles cuando se va a utilizar solamente una vez la función */
	/* 
	* JS es donde más se ven estas funciones anónimas, go permite la creción de estas funciones
	* anónimas, aunque deben ser usadas con cuidado para evitar romper el principio DRY
	*/
	y := func() int {
		return x * 2
	}()
	// fmt.Println(y()) /* Opción 1, invocando y al final con () */
	fmt.Println(y) /* Opción 2 - Invocación al final de la función, si no, retorna el espacio en memoria */
	c := make(chan int)
	go func() {
		fmt.Println("Simulo un proceso largo, conectandose a la bd")
		time.Sleep(5 * time.Second)
		fmt.Println("Simulé un proceso largo")
		c <- 1
	}()
	<-c
}
