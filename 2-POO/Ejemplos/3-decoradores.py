# Tomemos el siguiente caso de ejemplo: Crearemos una función que
# muestre si el número es par o impar

def esPar(x):
    if x % 2 == 0:
        return 1
    else:
        return 0

# print(esPar(3))

# Si quiero modificar mi función esPar para que ahora no solo
# entregue un 1 o un 0 para los casos par e impar, existen varias
# opciones

# Opción 1: Modifico directamente mi función. Esto dependiendo de lo
# que queremos como comportamiento de la función par, podría
# complicar bastante nuestro código

# Opción 2: Creamos una función aparte que se encargue de los mensajes
# y esa función la conectaremos con la función esPar()


def printEsPar(x):
    o = esPar(x)
    if o == 1:
        print(f"El número {x} es par")
    else:
        print(f"El número {x} es impar")

# Con este código, si solo quiero saber si el número es par o no
# puedo llamar directamente a la función esPar()
# print(esPar(5))

# Sin embargo, si yo quiero mostrar los mensajes de manera adicional
# puedo hacerlo llamando a la función encargada de ello. Es decir,
# la función printEsPar()
# printEsPar(5)

# Opción 3: Continuar con la idea de una función independiente,
# pero utilizaremos como base de modificación la sintaxis de uso
# de funciones como variables.


def printEsParMejorado(f, x):
    # En este caso x es el número a evaluar y f es la función
    # encargada de verificar si el número es par o impar
    # (sí, las funciones también se pueden operar como variables!!)
    o = f(x)
    if o == 1:
        print(f"El número {x} es par")
    else:
        print(f"El número {x} es impar")

# printEsParMejorado(esPar, 5)

# Continuemos con el concepto anterior pero ahora utilizando una
# notación de Python muy útil: decoradores
# Los decoradores, como su nombre indica, decoran una función
# extendiendo sus funcionalidades.


def printEsParDecorador(f):
    def mensaje(*args, **kwargs):
        o = f(*args, **kwargs)
        if o == 1:
            print(f"El número {args[0]} es par")
        else:
            print(f"El número {args[0]} es impar")
    return mensaje


@printEsParDecorador  # Decoramos la función esParUpd con el decorador printEsParDecorador
def esParUpd(x):
    if x % 2 == 0:
        return 1
    else:
        return 0


esParUpd(5)

# En resumen, el decorador se escribe como una función que indica
# cómo quieres extender el funcionamiento de tu función original.
# Utilizar el símbolo @ para indicar qué función será decorada
# con lo escrito en nuestra función de decoración

# Anexo: Qué es *args y **kwargs?

def f(*args, **kwargs):
    # *args almacena los parámetros posicionales de entrada a mi
    # función de manera dinámica (y en formato tupla)
    print("Valores de args:", args)
    # **kwargs almacena los parámetros no posicionales de entrada
    # a mi función también de manera dinámica (y en formato diccionar)
    print("Valores kwargs:", kwargs)

f(1, 3, 5, 2, d=7, f=4, h="hola", equis="pez")
 