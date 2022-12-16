lista_numeros = [1, 4, 7, 2, 3, 9, 6, 3, 7, 2, 4, 3, 6, 8]
# Split divide un texto según una coincidencia con un caracter.
# Ej: "Mi mamá me mima", si se hace un split por el caracter espacio
# "Mi" "mamá" "me" "mima"

def split_lista(lista_numeros, sep):
    # lista_separada se utiliza para almacenar los 
    # subconjuntos de elementos obtenidos
    lista_separada = []
    # lista_temporal se utiliza para guardar los elementos entre
    # separadores
    lista_temporal = []
    # Recorro la lista completa de lista_numers y por cada
    # número n hago lo siguiente
    for n in lista_numeros:
        # Corroboro si el número n es igual al separador
        # Si es igual, quiere decir que debo
        # 1) Cerrar la lista_temporal, agregándola a lista_separada
        # 2) Resetear/reiniciar la lista_temporal sin elementos
        if n == sep:
            lista_separada.append(lista_temporal)
            lista_temporal = []
        else:
            # Si el número n no es el separador, simplemente
            # agrego el número a mi lista_temporal
            lista_temporal.append(n)
    # En la última iteración, al no aparecer el separador explícitamente
    # debemos agregar la lista_temporal manualmente a lista_separada
    lista_separada.append(lista_temporal)
    # Retornamos lista_separada
    return lista_separada

print(split_lista(lista_numeros, 3))


