package main

import "fmt"

type figuras2D interface {
	area() float64
}

type cuadrado struct {
	base float64
}

type rectangulo struct {
	base   float64
	altura float64
}

func (c cuadrado) area() float64 {
	return c.base * c.base
}

func (r rectangulo) area() float64 {
	return r.base * r.altura
}

func calcular(f figuras2D) {
	fmt.Println("Area: ", f.area())
}

func interfaces() {
	/* Las interfaces son métodos que pueden compartir otros métodos, ej. un método aplica a
	otros structs */
	myCuadrado := cuadrado{base: 4}
	myRectangulo := rectangulo{base: 4, altura: 2}
	calcular(myCuadrado)
	calcular(myRectangulo)
	/* Lista de interfaces */
	/* En otros lenguajes, se puede tener arrays o listas flexibles */
	/* Ej [1, "1", True] */
	/* Para esto existen las listas interfaces */
	myInterface := []interface{}{"Hola", 12, 4.98}
	fmt.Println(myInterface...)
}
