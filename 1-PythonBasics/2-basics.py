# Este sería un comentario de una sola línea
# El comentario continúa en esta línea

'''  DOCSTRING
Esto de acá en un programa normal, correspondería
a un comentario de múltiples líneas
a la vez.
'''

# Variables
x = 2 # x representa una variable con valor asignado 2
y = 5 # y sería una variable con valor asignado 5
z = x + y # z es una variable con valor asignado x + y = 7
print(z) # print muestra el contenido de lo que se entrega por entrada en la terminal

# ¿Qué cosas se pueden almacenar en variables python?
a1 = 10 # Números enteros. Tipo de dato integer - int
a2 = 15.3 # Números decimales (reales). Tipo de dato flotante - float
a3 = "Este es un texto creado con comillas dobles" # Textos. Tipo de dato es string - str
a4 = 'Este es un texto creado con comillas simples' # También es un string
a5 = True # Valores de verdad. Pueden ser Verdadero (True) y Falso (False). Tipo de dato es boolean - bool
# Números complejos. Tienen una parte real y una parte imaginaria
# La parte imaginaria se indica acompañada de un# Quieres escribir por pantalla lo siguiente:
# El valor de la variable a1 es <valor de a1> y el valor de a2 es <valor de a2>
# Ej. El valor de la variable a1 es 10 y el valor de a2 es 15.3a j. Tipo de dato complex - complex
a6 = 3.3 + 5.1j  

print(a1, a2, a3, a4, a5, a6) # Mostramos los valores almacenados en las variables por terminal

# Ejercicio planteado - manejo de print y strings
# Quieres escribir por pantalla lo siguiente:
# El valor de la variable a1 es <valor de a1> y el valor de a2 es <valor de a2>
# Ej. El valor de la variable a1 es 10 y el valor de a2 es 15.3
print("El valor de la variable a1 es", a1, "y el valor de a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de a2 es %.1f" % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de a2 es {a2}")




# Tipos de datos compuestos
# Existen 4 tipos de datos compuestos: listas, tuplas, los rangos y los diccionarios... 
# también están los objetos (después)

# Listas
lista1 = [1, 2, 3] # lista1 es una variable de tipo lista - list que contiene 3 elementos enteros
lista2 = [1, 9.5, "Texto", [1, 4.5, "prueba"]]
# Para acceder a los elementos de una lista, debes utilizar un índice.
# Ojo: Los índices parten en 0
# ej. Con el índice 1, estamos accediendo al segundo elemento
print("El elemento con índice 1 en lista1 es", lista1[1])
print(lista1)
# Cómo podemos modificar un elemento de mi lista?
# Ej. quiero modificar el primer elemento de lista1 para que
# en vez de ser 1, sea "Primer elemento"
lista1[0] = "Primer elemento" # Se reemplaza el valor almacenado en lista1[0]
print(lista1)