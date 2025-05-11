'''
En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja.
El primero que se vende es el último que se colocó. Simula el proceso de agregar 
panes a la bandeja (push), vender uno (pop), y visualizar qué tipo de pan está listo 
para vender (peek).
'''

class Panaderia:
    
    def __init__(self):
        pass
    
    def pedir_panes(self):
        self.panes = []
        seq = int(input('¿Cuántos panes deseas agregar a la bandeja?: '))
        for i in range(seq):
            tipo_pan = input(f'Ingresa el tipo de pan para el pan #{i + 1}: ')
            self.panes.append(tipo_pan)
        print(f'Panes en la bandeja: {self.panes}') 
    
    def vender_panes(self):
        if len(self.panes) == 0: 
            print('No hay panes para vender')        
        else: 
            print('¿Cuántos panes deseas vender?: ')
            seq = int(input())
            if seq > len(self.panes):
                print('Hay menos panes que la cantidad indicada')
            else: 
                for i in range(seq):
                    self.panes.pop()
                print(f'La cantidad de panes pendientes es de: {self.panes}')
    
    def peek(self):
        if len(self.panes) == 0:
            print('No hay panes en la bandeja')
        else:
            print(f'El pan listo para vender es: {self.panes[-1]}')                
                
# crear instancia de la clase Panaderia y ejecutar metodos
new_panaderia = Panaderia()
new_panaderia.pedir_panes()
new_panaderia.peek()  # peekeando para ver cual tipo de pan esta listo para vender
new_panaderia.vender_panes()
