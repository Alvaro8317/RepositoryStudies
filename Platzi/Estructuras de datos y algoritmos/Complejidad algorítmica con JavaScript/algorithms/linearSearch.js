/**
 * Complejidad Temporal -> O( n )
 * Complejidad Espacial -> O( n )
 * Espacio Auxiliar = Complejidad espacial - espacio de entrada -> O( 1 )
 */
function linearSearch(arreglo /* O(n) */, clave) {
  for (let indice = 0; indice < arreglo.length; indice++) {
    /* O(1) */
    if (arreglo[indice] === clave) {
      return indice;
    }
  }
  return -1;
}
