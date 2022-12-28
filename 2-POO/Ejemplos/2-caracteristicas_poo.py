# Resolviendo el problema utilizando POO

class Numero:
    def __init__(self, x):
        # Capturamos este número x como un atributo interno
        self.x = x
        
    # A continuación vamos a escribir los métodos de esta clase
    def esPar(self):
        if self.x%2 == 0:
            return 1
        else:
            return 0
        
    def esPrimo(self):
        for i in range(2, self.x):
            if self.x%i == 0:
                return 0
        return 1
    
    def listaDivisores(self):
        lista_div = [1]
        for i in range(2, self.x):
            if self.x%i == 0:
                lista_div.append(i)
        lista_div.append(self.x)
        return lista_div
    

n1 = Numero(4)
n2 = Numero(7)

# Para saber si n1 es par simplemente hago
print(n1.listaDivisores())