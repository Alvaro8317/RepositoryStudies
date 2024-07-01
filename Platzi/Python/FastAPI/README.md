# Curso de FastAPI de Platzi

FastAPI es un framework que es precisamente como dice su nombre, crear una API de manera rápida ya que en muchas
ocasiones, para muchos proyectos, se suele requerir frecuentemente una API.

## Comandos en la CLI

Para correr la aplicación FastAPI en conjunto con uvicorn, se debe de correr los siguientes comandos:

```bash
# Ejecución normal en el puerto por defecto
uvicorn main:app
# Cambio de puerto
uvicorn main:app --port 8081
# Reload para que aplique los cambios sin bajar la aplicación
uvicorn main:app --port 8081 --reload
# Lo publica en la red accesible a otros dispositivos dentro de la red
uvicorn main:app --port 8081 --reload --host 0.0.0.0
```

## Swagger

FastAPI genera documentación basada en swagger en base al código con la siguiente
URL: [WebApp docs](http:localhost:8081/docs)

## Pydantic

Es una librería ya usada para la validación de datos en python.

## Autenticación con JWT

Para generar un JWT que se encarga de autenticar y autorizar, se debe de:

1. Generar una ruta para una inicio de sesión, para esto se crea una ruta POST donde se solicita datos como email y
   contraseña
2. Creación y envío de token, luego que el usuario ingrese los datos, obtiene el token y este se envía al momento de
   hacer una petición
3. Validación de token, al momento que la API recibe la petición, valida el token y da acceso.

Un JWT consta de 3 partes:

1. Encabezado (header), contiene información sobre como se ha creado el JWT, como el tipo de token y el algoritmo de
   firma
2. Cuerpo (payload), contiene la información que se transmite en el token, puede incluir claims (afirmaciones),
   predefinidos o personalizados
3. Firma, parte final del token y se utiliza para verificar que el remitente del token es quién dice ser y para
   garantizar que el contenido del token no ha cambiado

## ORM

¿Qué es un ORM? Es una librería que permite la manipulación de tablas de una DB como si fueran objetos de la aplicación,
un ORM de los más conocidos es SQLAlchemy, esta facilita el acceso a una BD relacional mapeando tablas SQL a clases