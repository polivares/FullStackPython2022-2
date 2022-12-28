# Indicar las siguientes caracterı́sticas del número solicitado:
# ¿Es un número par o impar?
# ¿Es un número primo?
# ¿Cuál es el conjunto de divisores del número? 

def esPar(x):
    if x%2 == 0:
        return 1
    else:
        return 0
    
def esPrimo(x):
    for i in range(2, x):
        if x%i == 0:
            return 0
    return 1

def listaDivisores(x):
    lista_div = [1]
    for i in range(2, x):
        if x%i == 0:
            lista_div.append(i)
    lista_div.append(x)
    return lista_div

# Esta solución se basa en la metodología funcional