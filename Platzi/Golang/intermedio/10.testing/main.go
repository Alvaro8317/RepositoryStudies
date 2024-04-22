package main

func Sum(x, y int) int {
	return x + y
}
func GetMax(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Finobacci(n int) int {
	if n <= 1 {
		return n
	}
	return Finobacci(n-1) + Finobacci(n-2)
}
