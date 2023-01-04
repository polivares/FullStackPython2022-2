# Paso 1: agregamos la biblioteca Flask
from flask import Flask

# A partir de la clase Flask, crearemos un objeto de dicha
# clase (una instancia de clase)
app = Flask(__name__) # en la variable app tengo un objeto pertenienciente a la clase Flask

# Vamos a crear una página simple que muestre un mensaje 
# Hola Mundo!
# Para ello necesitamos crear
# 1) Una función Python que maneje esa página
# 2) Una url a la cual conectar esa función de manera tal que podamos
# acceder a dicha página

@app.route("/prueba/")
def hola_mundo():
    return "<h1>hola Mundo!</h1>"

if __name__=="__main__": # Se asegura de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True) # Ejecutamos la aplicación en modo depuración
