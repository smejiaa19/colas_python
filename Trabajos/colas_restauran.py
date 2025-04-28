'''
Modificar la clase ColaCircular, en el programa del restaurante Chino, para: 
    - Permitir redimensionar la capacidad dinamicamente e implementar un metodo buscar(elemento) que retorne True si el elemento esta en la cola
'''

from collections import deque

class ColaCircular: 
    def __init__(self):
        self.cola_restaurante = deque()

    def enqueue(self):
        while True:
            try:
                seq = int(input('Cuantos platos desea agregar: '))
                if seq < 0:
                    raise ValueError
                elif not isinstance(seq, int):
                    raise TypeError
                break
            
            except (ValueError, TypeError) as e:
                print(e)
                print('Por favor ingrese un rango de numeros acorde (Mayores 0)')
            
        for i in range(seq):
            plato = input('Ingrese el nombre del plato: ')
            self.cola_restaurante.append(plato)
        self.menu()    
            
    def menu(self):
        while True:
            try:
                option = int(input(''' Que desea hacer? 
                (1) - Agregar platos
                (2) - Servir platos
                (3) - Imprimir cola
                (4) - Buscar plato
                (5) - Salir
                >>>   '''))
                if option < 0:
                    raise ValueError
                elif not isinstance(option, int):
                    raise TypeError
                break
            except (ValueError, TypeError) as e:
                print(e)
                print('Por favor ingrese un rango de numeros acorde (Mayores 0)')
                
        match option:
            case 1:
                self.enqueue()
            case 2:
                self.dequeue()
            case 3:
                self.imprimir_cola()
            case 4:
                self.buscar_elemento()
            case 5:
                print('Gracias por su visita')
                exit()
            case _:
                print('Opcion no valida')
                self.menu()
            
    def dequeue(self):
        while True: 
            try: 
                seq = int(input('Cuantos platos desea servir: '))
                if seq < 0: 
                    raise ValueError
                elif not isinstance(seq, int):
                    raise TypeError
                break

            except (ValueError, TypeError) as e:
                print(e)
                print('Por favor ingrese valores acordes (Mayores a 0)')
            
        for i in range(seq):
            if not self.cola_restaurante:
                print('No hay platos en la cola')
                break
            plato_servido = self.cola_restaurante.popleft()
            print(f'Plato servido: {plato_servido}')
        self.menu()
    
    def imprimir_cola(self):
        print(f'Cola: {list(self.cola_restaurante)}')
        self.menu()
    
    def buscar_elemento(self):
        plato = input('Que plato desea buscar: ')
        if plato in self.cola_restaurante:
            print(f'El plato {plato} se encuentra en la cola, en la posicion {self.cola_restaurante.index(plato) + 1}')
        else:
            print(f'El plato {plato} no se encuentra en la cola')
        self.menu()

comida_china = ColaCircular()
comida_china.menu()