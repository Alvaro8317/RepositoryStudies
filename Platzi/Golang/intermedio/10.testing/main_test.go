package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

/*
t *testing.T es para verificar todo lo relacionado del test,
tiene información incluso como el test coverage
*/
func TestSum(t *testing.T) {
	result := Sum(5, 5)
	if result != 10 {
		t.Errorf("Sum is incorrect, got %d but the expected was %d", result, 10)
	}
	/* Alternativa, similar al parametrize de pytest, con una tabla */
	tables := []struct {
		firstNumber    int
		secondNumber   int
		resultExpected int
	}{
		{1, 2, 3},
		{4, 5, 9},
		{6, 7, 13},
	}
	testifyVerifier := require.New(t)
	for _, item := range tables {
		fmt.Println(item)
		total := Sum(item.firstNumber, item.secondNumber)
		testifyVerifier.Equal(item.resultExpected, total)
	}
}

func TestSumMax(t *testing.T) {
	testifyVerifier := require.New(t)
	tablesToEvaluate := []struct {
		a int
		b int
		c int
	}{
		{4, 2, 4},
		{3, 2, 3},
		{3, 4, 4},
	}
	for _, item := range tablesToEvaluate {
		max := GetMax(item.a, item.b)
		testifyVerifier.Equal(item.c, max)
	}
}

func TestFinobacci(t *testing.T) {
	testVerifier := require.New(t)
	tablesToEvaluate := []struct {
		numberFinobacci int
		expectFinobacci int
	}{
		{1, 1},
		{8, 21},
		{50, 12586269025},
	}
	for _, values := range tablesToEvaluate {
		fib := Finobacci(values.numberFinobacci)
		testVerifier.Equal(values.expectFinobacci, fib)
	}
}
