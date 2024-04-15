package main

func tiposDeDatos() {
	// Si se le especifica el tipo de dato, tendrá mas rendimiento el código
	// Enteros
	/* int -> depende del OS (32 o 64 bits)
	int8 -> 8 bits, de -128 a 127
	int16 -> 16 bits, de -2^15 a 2~15 - 1
	int32 -> 32 bits, de -2^31 a 2~31 - 1
	int64 -> 64 bits, de -2^64 a 2~64 - 1*/
	// Numeros enteros positivos (uint -> unsigned int)
	/* uint -> depende del OS (32 o 64 bits)
	uint8 -> 8 bits
	uint16 -> 16 bits
	uint32 -> 32 bits
	uint64 -> 64 bits*/
	// Numeros decimales
	/* float32 -> 32 bits
	float64 -> 64 bits.
	Cualquiera de estos dos puede ser positivo o negativo */
	// Textos y boleanos
	/* String -> con comillas dobles
	bool -> true o false */
	// Numeros complejos
	/* Numeros reales o imaginarios
	complex64 -> real e imaginario float32
	complex128 -> real e imaginario float64
	ejemplo c:= 10 + 8i */
}
