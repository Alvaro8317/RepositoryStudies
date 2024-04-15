package main

import "fmt"

func arrayYSlices() {
	/* En muchos lenguajes se manejan listas, pero en go hay de dos tipos */
	/* Arrays -> Inmutables*/
	var array [4]int
	array[0] = 1
	array[1] = 2
	/* len da la longitud del array y cap la cantidad máxima de elementos del array */
	fmt.Println(array, len(array), cap(array))
	/* Slice -> Mutables */
	slice := []int{0, 1, 2, 3, 4, 5, 6}
	fmt.Println(slice, len(slice), cap(slice))
	/* Slicing, métodos en el slice */
	/* El primer elemento es inclusivo, el segundo es exclusivo */
	fmt.Println(slice[0])
	fmt.Println(slice[:3])
	fmt.Println(slice[2:4])
	fmt.Println(slice[4:])
	/* Append */
	slice = append(slice, 7)
	fmt.Println(slice)
	/* Agregar una lista con append */
	newSlice := []int{8, 9, 10}
	/* Los ... es que descomprime el slice y agrega los elementos */
	slice = append(slice, newSlice...)
	fmt.Println(slice)
}
