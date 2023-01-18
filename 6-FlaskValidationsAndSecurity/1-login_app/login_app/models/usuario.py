from flask import flash
import re # Biblioteca importada para el manejo de expresiones regulares
from login_app.config.mysqlconnection import connectToMySQL

# Expresión regular que calza con los correos electrónicos
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def getEmail(cls, email):
        query = "select * from usuario where email = %(email)s;"
        mysql = connectToMySQL('login')
        data = {
            'email': email
        }
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def getId(cls, data):
        query = "select * from usuario where id = %(id)s;"
        mysql = connectToMySQL('login')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def save(cls, data):
        query = "insert into usuario (first_name, last_name, email, password) values "\
                "(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        mysql = connectToMySQL('login')
        result = mysql.query_db(query, data)
        print(result)
        data_usuario = {'id': result}
        return cls.getId(data_usuario)
    
    # Método estático para validación de datos de formulario
    @staticmethod
    def validate_usuario(usuario):
        is_valid = True # Flag marcado como True inicialmente. Se cambia dependiendo de la validación
        if len(usuario['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(usuario['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(usuario['email']) < 5:
            flash("Email must be at least 5 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(usuario['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(usuario['password']) < 3:
            flash("Password must be at least 3 characters.")
            is_valid = False
        
        # Si en este punto is_valid sigue siendo True,
        # quiere decir que todas las validaciones fueron
        # correctamente procesadas.
        # Si es false, alguna validación fallo
        return is_valid 
    
    
    
    

