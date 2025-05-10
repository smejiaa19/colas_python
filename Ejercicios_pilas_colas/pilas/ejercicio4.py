'''
Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan 
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek), 
todo usando una pila.
'''

class secundaria():
    
    def __init__(self):
        pass
    
    def pedir_tareas(self):
        self.tareas = []
        seq = int(input('Cuantas tareas desea agregar: '))
        for i in range(seq):
            nombre = input('Ingrese el nombre de la tarea: ')
            self.tareas.append(nombre)
        print(self.tareas)
        
    def revisar_tareas(self):
        seq = int(input('Cuantas tareas desea revisar: '))
        if seq > len(self.tareas):
            print('No se puede realizar esta accion')
        else: 
            for i in range(seq):
                print(f'revisando tarea {self.tareas[i]}')    
                self.tareas.pop()
                
    def mostrar_pila(self):
        print('Tareas pendientes: ')
        for i in range(len(self.tareas)):
            print(f'Tarea numero {i+1} {self.tareas[i]}')
            
new_secundaria = secundaria()
new_secundaria.pedir_tareas()
new_secundaria.revisar_tareas()
new_secundaria.mostrar_pila()