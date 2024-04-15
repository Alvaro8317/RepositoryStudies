package main

import "fmt"

func maps() {
	/* Los maps son equivalentes a los diccionarios en python */
	/* Make sirve para hacer más que solo diccionarios */
	ageMap := make(map[string]int)
	ageMap["José"] = 14
	ageMap["Alvaro"] = 26
	fmt.Println(ageMap)
	/* La separación entre elementos de un map no es por comas, sino por espacios */
	/* Recorrido de un map */
	for indice, value := range ageMap {
		/* No se tendrá un orden de recorrido, si se requiere orden, mejor usar slicing */
		fmt.Printf("La persona %s tiene una edad de %d\n", indice, value)
	}
	value := ageMap["Alvaro"]
	fmt.Println(value)
	/* En caso que se acceda a una llave que no exista, retorna el value con un zero value */
	value2 := ageMap["Joseph"]
	fmt.Println(value2)
	/* Para solucionar esto, el ok indica si existe o no un elemento en un map */
	/* El intentar llamar un valor de un elemento que no existe, no modifica el ageMap original */
	value3, ok := ageMap["Joseph2"]
	fmt.Println(value3, ok)
	fmt.Println(ageMap)
	/* Los maps son más efectivos porque ya aplican la concurrencia */
}
