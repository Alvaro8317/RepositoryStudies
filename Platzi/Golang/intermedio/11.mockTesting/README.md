## Mock
Los mocks se utilizan cuando se requiere un test unitario y que un método hace una consulta a una base de datos, los mock service simulan la base de datos

Cuando se escribe un test unitario se suelen tener dependencias en diferentes servicios, con esto nace la necesidad de crear mocks que emulen comportamientos de estos servicios con el fin que el test se encargue de probar una única funcionalidad más no las dependencias.