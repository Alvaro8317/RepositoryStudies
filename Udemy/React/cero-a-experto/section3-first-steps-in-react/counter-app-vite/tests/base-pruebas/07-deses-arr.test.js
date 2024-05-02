import { string } from "prop-types"
import { retornaArreglo } from "../../src/base-pruebas/07-deses-arr"

describe('Test un 07', () => {
  test('should return an string and number', () => {
    const [letters, numbers] = retornaArreglo()
    /* to be valida también el tipo de dato */
    expect(letters).toBe("ABC")
    expect(numbers).toBe(123)
    console.log(typeof letters, typeof numbers)
    /* Expects propios */
    expect(typeof letters).toBe("string")
    expect(typeof numbers).toBe("number")
    /* Alternativa a hacerlo con toBe */
    expect(letters).toEqual(expect.any(String))
  })
})