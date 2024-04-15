package mypcpackage

import "fmt"

// PC struct, has attributes of my PC
type Pc struct {
	Ram   int
	Disk  int
	Brand string
}

func (myPc Pc) Ping() {
	fmt.Println(myPc.Brand, "Pong")
}

/* Se le indica que accederá mediante puntero */
func (myPc *Pc) DuplicateRam() {
	myPc.Ram = myPc.Ram * 2
}
