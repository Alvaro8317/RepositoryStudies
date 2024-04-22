package main

import (
	"fmt"
	"strconv"
	"time"
)

func repaso() {

	var x int
	x = 8
	y := 7
	fmt.Println(x)
	fmt.Println(y)

	// Capturando valor y error
	myValue, err := strconv.ParseInt("NaN", 0, 64)

	// Validando errores.
	if err != nil {
		fmt.Printf("%v\n", err)
	} else {
		fmt.Println(myValue)
	}

	// Mapa clave valor.
	m := make(map[string]int)
	m["key"] = 6
	fmt.Println(m["key"])

	// Slice de enteros.
	s := []int{1, 2, 3}
	for index, value := range s {
		fmt.Println(index)
		fmt.Println(value)
	}
	s = append(s, 16)
	for index, value := range s {
		fmt.Println(index)
		fmt.Println(value)
	}
	/* GoRoutines y apuntadores */
	/* Esto se ejecutará en una rutina distinta a main */
	/* La rutina main tiene la tarea de crear la subrutina de doSomething pero no la monitorea
	por esto son necesarios los canales */
	c := make(chan int)
	go doSomething(c)
	/* Se le especifica que espere a doSomething con <-c*/
	<-c
	g := 25
	fmt.Println(g)
	h := &g
	fmt.Println(h)  /* Dirección en memoria */
	fmt.Println(*h) /* Valor de la dirección en memoria */
}

func doSomething(c chan int) {
	time.Sleep(1 * time.Second)
	fmt.Println("Done")
	c <- 1
}
