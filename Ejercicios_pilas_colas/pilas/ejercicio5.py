'''
En un mercado de Chinandega, los sacos con productos se cargan en camiones uno encima de otro. 
Al llegar a destino, el primer saco que se descarga es el último que se cargó. Simula este proceso 
con una pila que permita apilar sacos (push), descargar uno (pop) y visualizar el que está encima (peek).
'''

class mercado():
    
    def __init__(self):
        pass
    
    def pedir_sacos(self):
        self.sacos = []
        seq = int(input('Cuantos sacos desea agregar: '))
        for i in range(seq):
            nombre = (input(f'Ingrese el nombre del saco {i+1}: '))
            self.sacos.append(nombre)
        print(self.sacos)
            
    def descargar_sacos(self):
        print('Cuantos sacos desea descargar: ')
        n = int(input())
        if n > len(self.sacos):
            print('Esta accion no se puede realizar')
        else:
            for i in range(n):
                print(f'Descargando el saco numero {i+1}')
                self.sacos.pop()
            print('Pila restante: ')
            print(self.sacos)
                
    def mostrar_pila(self):
        for i in range (len(self.sacos)):
            print(f'Revisando saco con nombre: {self.sacos[i]}')
    
new_mercado = mercado()
new_mercado.pedir_sacos()
new_mercado.descargar_sacos()
new_mercado.mostrar_pila()
