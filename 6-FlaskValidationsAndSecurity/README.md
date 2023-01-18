# Validación y seguridad

## Proceso de validación de datos

En ocasiones, nuestra web interactuará con los usuario solicitándoles ciertos datos. Antes de procesar esos datos, es necesario realizar un proceso de comprobación para verificar que los datos "tengan sentido" (ejs. el teléfono está compuesto por números? el correo electrónico tiene un arroba?, etc.).
Esta comprobación se realiza a través de la validación de datos utilizando las clases definidas en nuestro modelo. Para ello, crearemos un o múltiples métodos estáticos encargados de verificar las condiciones que nosotros consideremos para cada dato.

## Seguridad en contraseñas de usuario

Las contraseñas son un elemento sensible que debe ser almacenado con recaudo en nuestros sistemas de base de datos. Dejar nuestras contraseñas expuestas o almacenadas en texto plano es una brecha de seguridad importante tanto para nuesto entorno de desarrollo como para los usuarios de nuestra plataforma.
Es por ello que existen diferentes técnicas de almacenamiento de contraseñas de forma mucho más segura (o que al menos dificulte el trabajo de aquellos que puedan estar interesados en dichas contraseñas).
En este caso, utilizaremos la biblioteca Bcrypt de Python para almacenar nuestras contraseñas. Esta utiliza un algoritmo de cifrado que incluye dentro de un string largo:

- Un prefijo que indica que se está en presencia de una contraseña encriptada por bcrypt
- Un costo que indica la dificultad de desencriptar dicha contraseña
- La sal, la cual corresponde a un string de 22 caracteres
- La contraseña cifrada (hash)

Un ejemplo que incluye validación de datos y guardado de contraseñas con bcrypt puede ser encontrado en el ejemplo *1-login_app/*