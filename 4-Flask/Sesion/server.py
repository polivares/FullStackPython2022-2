from flask import Flask, render_template, request, redirect, session
# La variable importada llamada session, es una variable de tipo
# DICCIONARIO (sí, diccionaro como los que ya conocemos :-) )
# encargada de manejar aquellos datos que se deben mantener
# activos durante una sesión

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/process", methods=['POST'])
def process():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "polivares@codingdojo.cl" and password == "123456789":
            # Ahora, como recibí un email y una contraseña correctamente
            # y ambas corresponde a las del usuario, se creará una nueva sesión
            # Basta que haya al menos UN CAMPO en tu variable session para que
            # se considere la sesión como activa
            session["email"] = email
            session["password"] = password
            # Ojo, guardar la contraseña en una variable de sesión no es una buena
            # idea. Esto es un ejemplo :)
            return redirect("/profile")
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    if session.get("email") == None:
        # Si no hay una sesión activa, redirijo al login
        return redirect('/login')
    else:
        # Si hay una sesión activa, muestra mi página de perfil
        print(session["email"])
        return render_template("profile.html", email=session["email"], pwd=session["password"])


@app.route('/logout')
def logout():
    # Esta función será encargada de eliminar/liberar la sesión activa
    # forma correcta de liberar sesión
    session.clear()

    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
