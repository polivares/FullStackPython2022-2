
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
a = 10 # Esto crea una variable que almacena un entero
print(type(a))

perroA = Perro("Toto", 7, "Poodle", "10-10-2022") # Esto crea una variable que almacena un "Perro"
perroB = Perro("Lara", 6, "Schnauzer", "08-09-2022")
print(type(perroA))

# Cuál es el nombre de los perritos?
print(perroA.nombre) # Esto accede al nombre que hayamos definido para perroA (Toto)
print(perroB.nombre)

# Cómo utilizamos los método internos de una clase a partir del objeto creado?
print("Antes de cumplir años:", perroA.edad)
perroA.cumple() # Esto hará que perroA cumpla años.
print("Después de cumplir años:", perroA.edad)

# Herencia
# Es la creacioón de una clase "base" que agrupa aquelos elemntos
# que son comunes entre una o varias clases. Esto permite agrupar
# características (y funcionalidades) comunes entre dichas clases.
class Felino:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido
    
    def emitirSonido(self):
        return self.sonido
    
class Gato(Felino):
    # En este punto, debido a la herencia que definimos, la clase Gato
    # puede hacer TODO lo que puede hacer la clase Felino
    def __init__(self, nombre, edad, dueno):
        super().__init__(nombre, edad, "Miau")
        self.dueno = dueno
        
class Leon(Felino):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Grrrr")
        
        
cat = Gato("Garfield", 7, "John")
lion = Leon("Leoncio", 10)

print("El gato hace:", cat.emitirSonido())
print("El león hace:", lion.emitirSonido())

# Actividad
# Cree las clases Cuenta y Banco donde cada clase tiene las siguientes características
# Clase Cuenta: contiene un número de cuenta (id de cuenta) y un saldo. Además, posee 
# métodos para ver y actualizar el saldo de dicha cuenta
# Clase Banco: Un banco posee múltiples cuentas bancarias. Además posee un 
# método el cual permite realizar transferencias desde una cuenta origen
# a una cuenta destino a partir de sus números de cuenta. Ojo, no se puede 
# transferir desde una cuenta con saldo menor al monto a transferir!