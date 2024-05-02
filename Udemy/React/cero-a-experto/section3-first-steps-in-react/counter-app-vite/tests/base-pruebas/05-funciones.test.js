import { getUser, getUsuarioActivo } from "../../src/base-pruebas/05-funciones"

describe('Test in funciones', () => {
  test('getUser should return an object', () => {
    const testUser = {
      uid: 'ABC123',
      username: 'El_Papi1502'
    }
    const userToEvaluate = getUser();
    /* Se puede usar toEqual o toStrictEqual para validar objetos */
    expect(testUser).toStrictEqual(userToEvaluate)
  })
  test('getUsuario should return an object', () => {
    const name = "Alvaro"
    const testUser = {
      uid: 'ABC567',
      username: name
    }
    const userToEvaluate = getUsuarioActivo(name)
    /* La diferencia entre toEqual y toStrictEqual es que toEqual ignora los undefined en properties, items en array, escaces de matriz o mismatch en tipos de objeto, para evaluar estos se puede usar toStrictEqual*/
    expect(testUser).toEqual(userToEvaluate)
  })
})