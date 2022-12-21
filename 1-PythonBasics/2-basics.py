# Este sería un comentario de una sola línea
# El comentario continúa en esta línea

'''  DOCSTRING
Esto de acá en un programa normal, correspondería
a un comentario de múltiples líneas
a la vez.
Formato de comentarios muy utilizado para la generación
de documentación.
'''

# Variables
x = 2  # x representa una variable con valor asignado 2
y = 5  # y sería una variable con valor asignado 5
z = x + y  # z es una variable con valor asignado x + y = 7
print(z)  # print muestra el contenido de lo que se entrega por entrada en la terminal

# ¿Qué cosas se pueden almacenar en variables python?
a1 = 10  # Números enteros. Tipo de dato integer - int
a2 = 15.3  # Números decimales (reales). Tipo de dato flotante - float
# Textos. Tipo de dato es string - str
a3 = "Este es un texto creado con comillas dobles"
a4 = 'Este es un texto creado con comillas simples'  # También es un string
# Valores de verdad. Pueden ser Verdadero (True) y Falso (False). Tipo de dato es boolean - bool
a5 = True
# Números complejos. Tienen una parte real y una parte imaginaria
# La parte imaginaria se indica acompañada de un# Quieres escribir por pantalla lo siguiente:
# El valor de la variable a1 es <valor de a1> y el valor de a2 es <valor de a2>
# Ej. El valor de la variable a1 es 10 y el valor de a2 es 15.3a j. Tipo de dato complex - complex
a6 = 3.3 + 5.1j

# Mostramos los valores almacenados en las variables por terminal
print(a1, a2, a3, a4, a5, a6)

# Ejercicio planteado - manejo de print y strings
# Quieres escribir por pantalla lo siguiente:
# El valor de la variable a1 es <valor de a1> y el valor de a2 es <valor de a2>
# Ej. El valor de la variable a1 es 10 y el valor de a2 es 15.3
print("El valor de la variable a1 es", a1, "y el valor de a2 es", a2)
print("El valor de la variable a1 es " +
      str(a1) + " y el valor de a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de a2 es %.1f" % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de a2 es {a2}")

# Tipos de datos compuestos
# Existen 4 tipos de datos compuestos: listas, tuplas, los rangos y los diccionarios...
# también están los objetos (después)

# Listas
# lista1 es una variable de tipo lista - list que contiene 3 elementos enteros
lista1 = [1, 2, 3]
lista2 = [
    1,  # Este es el primer elemento (índice 0) ==> lista2[0]
    9.5,  # Este es el segundo elemento (índice 1) ==> lista2[1]
    "Texto",  # Este es el tercer elemento (índice 2) ==> lista2[2]
    [1, 4.5, "prueba"]  # Este es el cuarto elemento (índice 3) ==> lista2[3]
]
# Para acceder a los elementos de una lista, debes utilizar un índice.
# Ojo: Los índices parten en 0
# ej. Con el índice 1, estamos accediendo al segundo elemento
print("El elemento con índice 1 en lista1 es", lista1[1])
print(lista1)
# Cómo podemos modificar un elemento de mi lista?
# Ej. quiero modificar el primer elemento de lista1 para que
# en vez de ser 1, sea "Primer elemento"
lista1[0] = "Primer elemento"  # Se reemplaza el valor almacenado en lista1[0]
print(lista1)
# Es posible acceder a los elementos de la lista interna a lista2?
# Ej. Quiero acceder al tercer elemento de la lista interna -> "prueba"
print(lista2[3][2])
# Agregar un elemento a una lista
# Existen dos formas de agregar elementos
# 1) Método append(), agrega elementos al final de la lista
lista1.append(20)
print(lista1)
# 2) Método insert(), agrega elementos en cualquier posición de la lista
lista1.insert(1, "pez")
print(lista1)
# Quitar elementos de una lista se realiza con un método llamado pop()
elemento1 = lista1.pop()  # En elemento1 se almacenará el elemento borrado desde lista1
print(lista1, elemento1)
# El método pop también puede ser utilizado para eliminar elementos en
# una posición específica
elemento2 = lista1.pop(1)
print(lista1, elemento2)
# Por supuesto, uniendo todo lo que hemos visto, es posible eliminar/agregar elementos
# dentro de una lista interna (ej. lista2)
# Ej agregar elemento
lista2[3].append("pollo")
print(lista2)
elemento3 = lista2[3].pop()
print(lista2, lista2[3], elemento3)
# Puedo acceder a más de un elemento a la vez de mis listas? R: Sí, se puede :)
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Notación de acceso por rangos: lista[pos_inicio:pos_final:paso]
# OJO: pos_final, es la "muralla que no puedes traspasar",
# no la posición a la que llega
print(lista3[0:5:1])
# Prueba cambiar cada uno de estos números!
print(lista3[2:8:3])
# También se puede recorrer la lista de manera inversa
print(lista3[-1::-1])
# Esta notación tiene elementos por omisión
print(lista3[::])  # Esto es equivalente a lista3[0:len(lista3):1] => lista3
# Cómo sabemos cual es el largo de una lista?
# Se utiliza la función len()
print(len(lista3))  # Te indica el largo de la lista

# Tuplas: Son básicamente iguales a las listas... pero INMUTABLES!
tupla1 = (1, 2, 3, 4)
print(tupla1[1:3:1])
# tupla1[2] = "pez" # Esto lanzaría error!
tupla2 = (1, "hola", [1, 2, 3])
print(tupla2)
# Ojo: en tupla2, sí puedes modificar los elementos DENTRO de la lista interna
# Lo que no puedes hacer es REEMPLAZAR esa lista
tupla2[2][0] = "Primer elemento"  # Esto es válido
print(tupla2)
# tupla2[2] = 4 # Esto NO es válido
# print(tupla2)

# Rangos/range: Normalmente, necesitamos hacer de manera rápida conjuntos de datos
# que son exclusivamente númericos y enteros. Para resolver este problema, Python
# propone el tipo range.
# Ej. Necesito los números entre el -5 y el 5 (sin incluir) de 3 en 3
rango1 = range(-5, 5, 3)
print(rango1)  # Rango completo generado en la línea anterior
print(rango1[0])  # Accediendo a un elemento del rango

# Diccionarios: tipo de dato compuesto cuyo acceso se puede dar con diferentes tipos de
# índices. El índice dentro de un diccionario puede ser CUALQUIER COSA...
# siempre y cuando ese índice sea un dato INMUTABLE (incluyendo las tuplas!)
dict1 = {
    0: "Texto para llave 0",
    "llave1": "Texto para la llave1",
    (1, 2, 3): "Texto para la llave tupla (1, 2, 3)"
}
# Ejemplo de acceso a elementos de un diccionario
print(dict1[0], dict1["llave1"], dict1[(1, 2, 3)])

# Condicionales, bucles y funciones
###################################

# Condicionales: if, elif (contracción de else e if), else
x = 40  # Prueba cambiar el valor de x!

if x < 4:
    print("El valor de x es menor que 4")
    print("Esta linea si se encuentra en el if")
elif x > 1 and x < 15:  # También se puede escribir como 1<x<15
    print("El valor de x es", x)
elif x < 20:
    print("El valor de x es menor que 20")
else:
    print("El valor de x no cumple ninguna de las condiciones")

# Bucle:
# Existen dos tipos de bucles: for y while

# Bucle for
# Permite repetir sobre un conjunto de datos agrupados
lista5 = [4, 2, 8, 6, 3, 4]

for i in lista5:
    print("Estoy iterando")
    print("La variable i tiene valor", i)
    
# El bucle for de Python se puede utilizar de manera similar a como lo
# hacíamos en javascript (con un contador)
for i in range(0, len(lista5), 1): # range(0, 6)
    print(f"El valor del elemento índice {i} en lista5 es", lista5[i])
    
# Bucle while (mientras)
# El bucle while, a diferencia del bucle for, repite un conjunto de líneas de código
# MIENTRAS se cumpla una condición
k = 1
while k < 10:
    print(k)
    k+=1 # Esto es equivalente a k = k + 1. Desafortunadamente en Python no hay k++
print("El valor de k una vez terminado el while es", k)

# Funciones
# Funciones son bloques de código que pueden ser llamados
def suma_num(a, b):
    suma = a + b
    return suma

# Para utilizar esta función, debemos llamarla a partir de su nombre
x = 10
y = 7
z = suma_num(x, y) # A la variable z se le asigna el retorno de suma_num => 17
print(f"La suma de {x} y {y} es: {z}")

# Las funciones pueden tener cero parámetros de entrada y no tener un retorno
def getMessage():
    return "Este es mi mensaje"

print(getMessage())

def printMessage():
    print("Este es mi nuevo mensaje")
    
printMessage()

# Recursión: Una recursión es cuando una función se llama a sí misma
def factorial_sin_recursion(n):
    mult = 1
    for i in range(1, n+1):
        mult = mult*i
    return mult

print(factorial_sin_recursion(4))
print(factorial_sin_recursion(3))

def factorial_con_recursion(n):
    if n == 1:
        return 1
    
    return n*factorial_con_recursion(n-1)
    
print(factorial_con_recursion(4))
print(factorial_con_recursion(3))

# Escriba un código Python que entregue ciertas caracterı́sticas 
# de un número solicitado. Para esto, el programa deberá realizar 
# las siguientes tareas:
# Solicitar al usuario un número entero positivo perteneciente al rango [2,1000].
#(Para solicitar datos, buscar la función input() de python) 
# Su programa debe verificar esta condición. En caso contrario, se debe pedir 
# otro número hasta que se cumpla la condición.
# Indicar las siguientes caracterı́sticas del número solicitado:
# ¿Es un número par o impar?
# ¿Es un número primo?
# ¿Cuál es el conjunto de divisores del número? 
# (Se dice que y es divisor de x si el resultado de x ÷ y es un número entero).
# Una vez indicada las caracterı́sticas del número, el programa debe finalizar. 
# Ejemplo de funcionamiento:

# Ingrese un número: 6
# Número par
# No es un número primo
# Conjunto de divisores:
# 1
# 2
# 3
# 6