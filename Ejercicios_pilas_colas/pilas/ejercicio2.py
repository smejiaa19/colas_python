'''
En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja.
El primero que se vende es el último que se colocó. Simula el proceso de agregar 
panes a la bandeja (push), vender uno (pop), y visualizar qué tipo de pan está listo 
para vender (peek).
'''

class panaderia():
    
    def __init__(self):
        pass
    
    def pedir_panes(self):
        self.panes = []
        seq = int(input('Cuantos panes hay en la bandeja: '))
        self.pan = 1
        for i in range(seq):
            self.panes.append(self.pan)
            self.pan += 1
        print(f'Panes en la bandeja: {self.panes}') 
    
    def vender_panes(self):
        if len(self.panes) == 0: 
            print('No hay panes para vender')        
        else: 
            print('Cuantos panes desea vender: ')
            seq = int(input())
            if seq > len(self.panes):
                print('Hay menos panes q la cantidad indicada')
            else: 
                for i in range(seq):
                    self.panes.pop()
                print(f'La cantidad de panes pendientes es de: {self.panes}')
                
                
new_panaderia = panaderia()
new_panaderia.pedir_panes()
new_panaderia.vender_panes()