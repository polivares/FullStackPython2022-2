from login_app import app
from login_app.models.usuario import Usuario
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask import flash

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = Usuario.getEmail(email)
        # Verificación de contraseña para login utilizando hash
        if usuario is None or not bcrypt.check_password_hash(usuario.password, password):
            flash("Invalid Email/Password")
            return redirect('/')
        session["id"] = usuario.id
        return redirect('/profile')
    else:
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if request.form['password'] == request.form['confirm_password']:
            data = dict(request.form)
            # Generación de hash
            data['password'] = bcrypt.generate_password_hash(
                request.form['password'])
            if Usuario.validate_usuario(request.form):
                usuario = Usuario.save(data)
                session["id"] = usuario.id
                return redirect("/profile")
        else:
            flash("Password must be the same")
    return render_template('signup.html')


@app.route('/profile')
def profile():
    if session.get('id') == None:
        return redirect('/')
    else:
        usuario = Usuario.getId(session)
        return render_template("profile.html", usuario=usuario)


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/login')
