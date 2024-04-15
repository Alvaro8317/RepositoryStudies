package mypackage

import "fmt"

// CarPublic Car with public access
type CarPublic struct {
	Brand string
	Year  int
}

type carPrivate struct {
	brand string
	year  int
}

// PrintMessage imprime un mensaje, la documentación es necesaria en paquetes públicos
func PrintMessage(text string) {
	fmt.Println(text)
}
func printMessagePrivate(text string) {
	fmt.Println(text)
}
