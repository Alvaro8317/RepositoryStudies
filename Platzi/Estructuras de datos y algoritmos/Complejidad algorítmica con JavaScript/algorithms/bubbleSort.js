/**
 * Complejidad Temporal -> O( n² )
 * Complejidad Espacial -> O( n )
 * Espacio Auxiliar -> O( 1 )
 */
function bubbleSort(arreglo) {
  let longitud = arreglo.length;
  for (let i = 0; i < longitud; i++) {
    for (let j = 0; j < longitud; j++) {
      if (arreglo[j] > arreglo[j + 1]) {
        let temporal = arreglo[j];
        arreglo[j] = arreglo[j + 1];
        arreglo[j + 1] = temporal;
      }
    }
  }
  return arreglo;
}
