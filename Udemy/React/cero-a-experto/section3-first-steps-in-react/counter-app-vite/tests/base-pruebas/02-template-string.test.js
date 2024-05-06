import { getSaludo } from "../../src/base-pruebas/02-template-string";

describe('Test of 02-template-string', () => {
  test('should return Hola Alvaro', () => {
    const name = "Alvaro";
    const message = getSaludo(name);
    expect(message).toBe(`Hola ${name}`)
  })
})