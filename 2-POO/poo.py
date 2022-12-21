
# Definición de una clase
# Ej. definir una clase Perro

class Perro:
    # En esta parte del código es donde definiremos
    # tanto las características (atributos) como
    # funcionalidades (métodos) que puede realizar
    # un objeto perteneciente a la clase (Perro)

    # Atributos: son aquellos elementos dentro de la
    # clase que definen su estado. En el caso de los 
    # perros, qué características me interesan de ellos
    # en mi código
    def __init__(self, name, age, r, date_v):
        # La función __init__() corresponde al constructor 
        # de la clase. Es decir, aquel método encargado
        # de inicializar los estados de mi nuevo objeto

        # Utilizaremos esta función para crear los atributos
        # de nuestra clase
        self.nombre = name
        self.edad = age
        self.raza = r 
        self.f_vacunacion = date_v
        
    # A continuación, escribiremos todos los métodos que puede
    # utilizar esta clase. Recordemos que los métodos son
    # las operaciones que puede realizar un  objeto perteneciente
    # a la clase y quedan definidas como "funciones" internas
    
    def cumple(self):
        self.edad = self.edad + 1 
        
    def updateFVacunacion(self, nueva_fvacunacion):
        self.f_vacunacion = nueva_fvacunacion

# Ya tenemos definida nuestra clase Perro. Cómo creamos objetos a partir de
# esta clase? Recordemos que un objeto es algo concreto dentro del grupo que
# se define a partir de la clase

