from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "esta es mi llave"

grupos = []  # Esta variable almacena una lista, donde cada elemento es un grupo


@app.route('/')
# Por omisión, el tipo de solicitud que se atiende acá es de tipo GET
@app.route('/register')
def register():
    # Verificamos la información de cuál es el número del grupo
    # que se está registrando
    if len(grupos) == 0:
        id = 1  # Id es la variable que represente el id del grupo a ser almacenado
    else:
        id = grupos[-1].id + 1
    return render_template("register.html", id=id)


@app.route('/agrega_grupo', methods=['POST', 'GET'])
def add_group():
    if request.method == "POST":
        # Esto quiere decir que nuestra solicitud es efectivamente
        # de tipo POST
        if len(grupos) == 0:  # Si es el primer grupo a registrarse
            id = 1  # Pongo id en 1
        else:  # Sino es el primer grupo
            id = grupos[-1].id + 1  # El id es igual al último + 1
        integrante1 = request.form.get("integrante1")
        integrante2 = request.form.get("itegrante2")
        integrante3 = request.form.get("integrante3")
        integrantes = [integrante1, integrante2, integrante3]
        tema = request.form.get("project_title")
        descripcion = request.form.get("project_description")
        group = Grupo(id, integrantes, tema, descripcion)
        grupos.append(group)  # Aquí agregamos un objeto de la clase Grupo a
        # nuestra lista de grupos
        return redirect("/lista_grupos")
    else:
        return redirect("/")


@app.route('/lista_grupos', methods=["GET"])
def list_groups():
    return render_template("list_groups.html", grupos=grupos)


class Grupo:
    def __init__(self, id, integrantes, tema, descripcion):
        self.id = id  # Tipo entero
        self.integrantes = integrantes  # Lista de integrantes
        self.tema = tema  # String
        self.descripcion = descripcion  # String


if __name__ == '__main__':
    app.run(debug=True)
