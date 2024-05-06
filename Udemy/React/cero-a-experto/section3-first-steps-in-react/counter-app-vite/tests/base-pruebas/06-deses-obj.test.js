import { usContext } from "../../src/base-pruebas/06-deses-obj"

describe('Tests of 05', () => {
  test('should return an object', () => {
    expect(usContext({ clave: 123, edad: 26 })).toEqual({
      nombreClave: 123,
      anios: 26,
      latlng: {
        lat: 14.1232,
        lng: -12.3232
      }
    })
  })
})