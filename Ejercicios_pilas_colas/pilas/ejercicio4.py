'''
Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan 
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek), 
todo usando una pila.
'''

class secundaria():
    
    def __init__(self):
        self.tareas = []  
    
    def pedir_tareas(self):
        seq = int(input('Cuántas tareas desea agregar: '))
        for i in range(seq):
            nombre = input('Ingrese el nombre de la tarea: ')
            self.tareas.append(nombre)
        print('Tareas registradas:', self.tareas)
        
    def revisar_tareas(self):
        seq = int(input('Cuántas tareas desea revisar: '))
        if seq > len(self.tareas):
            print('No se puede realizar esta acción.')
        else: 
            for i in range(seq):
                tarea = self.tareas.pop()  
                print(f'Revisando tarea {i+1}: {tarea}')  
                
    def mostrar_pila(self):
        print('Tareas pendientes:')
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i in range(len(self.tareas)):
                print(f'Tarea número {i+1}: {self.tareas[i]}')
    
    def mostrar_siguiente_tarea(self):  # peek
        if len(self.tareas) == 0:
            print("No hay tareas pendientes.")
        else:
            print(f"La siguiente tarea a revisar es: {self.tareas[-1]}")  
            
# instancia
new_secundaria = secundaria()
new_secundaria.pedir_tareas()
new_secundaria.revisar_tareas()
new_secundaria.mostrar_pila()
new_secundaria.mostrar_siguiente_tarea()
