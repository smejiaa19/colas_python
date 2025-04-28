from collections import deque 

class clinica: 
    
    def __init__(self):
        self.cola_pacientes = deque()
    
    def pedir_pacientes(self):
        while True:
            try:
                x = int(input('Ingrese el numero de pacientes que desea registrar: '))
                if x < 0: 
                    raise ValueError('El numero de pacientes no puede ser negativo')
                elif not isinstance(x, int):
                    raise TypeError('El valor ingresado no es un numero')
                break
            
            except (ValueError, TypeError) as e:
                print(e)
                print('Por favor ingrese un rango de numeros acorde (Mayores 0)')
            
        for i in range (x):
            nombre = input('Ingrese el nombre del paciente: ')
            self.cola_pacientes.append(nombre)
        self.menu()
        
    def imprimir_cola(self):
        print(f'Cola inicial: {list(self.cola_pacientes)}') # Imprimimos la cola original
        self.menu()
        
    def atender_primer_paciente(self):
        while True:
            try:
                count = int(input('Ingrese cuantos clientes desea atender: '))
                if count < 0:
                    raise ValueError
                elif not isinstance(count, int):
                    raise TypeError
                break
            
            except (ValueError, TypeError) as e :
                print(e)
                print('Por favor ingrese un rango de numeros acorde (Mayores 0)')
            
        for i in range (count):
            if not self.cola_pacientes:
                print('No hay pacientes en la cola')
                break
            cliente_atendido = self.cola_pacientes.popleft() # Esto lo hacemos para remover el primer elemento de la cola
            print(f'Cliente atendido: {cliente_atendido}')
            print(f'Cola despues de atender: {list(self.cola_pacientes)}')
        self.menu()

    def menu(self):
        try:
            option = int(input('''Que desea hacer?
            (1) - Agregar pacientes
            (2) - Atender pacientes
            (3) - Imprimir cola
            (4) - Salir
            >>>  '''))
            
            if option <1 or option >4:
                raise ValueError('El valor ingresado no es valido')
                
            elif isinstance(option, str or float):
                raise TypeError('El valor ingresado no es un numero')
            
        except ValueError as e:
            print(e)
            print('Por favor ingrese un rango de valores acorde (1-4)')
            self.menu()
        
        except TypeError as e:
            print(e)
            print('Por favor igrese un tipo de dato valido (Entero)')
            self.menu()
                    
        match option:
            
            case 1:
                clinica.pedir_pacientes(self)
            
            case 2: 
                clinica.atender_primer_paciente(self)
            
            case 3:
                clinica.imprimir_cola(self)
            
            case 4: 
                quit()

test = clinica()
test.menu()