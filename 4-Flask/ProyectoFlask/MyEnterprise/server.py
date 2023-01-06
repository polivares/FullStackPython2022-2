# Importamos la clase Flask
# Agregamos la función render_template para el proceso de renderizado
from flask import Flask, render_template 

app = Flask(__name__)  # Creamos una instancia de la clase Flask


@app.route('/')  # Decorador de ruta
def index():  # Función que se ejecuta cuando se accede a la ruta raíz
    return "<h1>Hola Mundo Flask!!</h1>"  # Devolvemos una cadena de

@app.route('/description/')
def description():
    return "<h1>Página de descripcion</h1>"

@app.route('/contact/office/')
def contact():
    return "<h1>Datos de contacto oficina: +56 9 11111111 </h1>"

# Ruta para saludar a un usuario según su nombre, apelido y edad.
@app.route('/hola/<nombre>/<apellido>/<int:edad>')
def hola(nombre, apellido, edad):
    # return "<h1>Hola {0} {1} de {2} años</h1>".format(nombre, apellido, edad)
    return f"<h1>Hola {nombre} {apellido} de {edad} años</h1>"

# Ejemplo de renderizado de plantillas
@app.route('/user/<nombre>/<apellido>/<int:edad>')
def user(nombre, apellido, edad):
    return render_template('user.html', nombre=nombre, apellido=apellido, edad=edad)

# Ejemplo de jinja: repetición de texto
@app.route('/repeat/<int:num>/<string:texto>')
def repeat(num, texto):
    return render_template('repeat.html', num=num, texto=texto)

# Ejemplo de jinja para archivos estáticos
@app.route('/president/')
def president():
    return render_template('president.html')

# Ejemplo de jinja para archivos estáticos
@app.route('/test/<color>')
def test(color):
    return render_template('test.html', color=color)

if __name__ == "__main__":  # Se asegura de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)  # Ejecutamos la aplicación en modo depuración
