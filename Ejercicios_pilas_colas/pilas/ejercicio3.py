'''
En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes 
se almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico,
se debe revertir el último registro. Implementa un sistema para registrar donantes (push), 
eliminar el último (pop), y mostrar el donante actual en proceso.
'''

class hospital():
    
    def __init__(self):
        pass
    
    def pedir_pacientes(self):
        self.pacientes = []
        seq = int(input('Cuantos pacientes desea agregar: '))
        for i in range(seq):
            nombre = input('Cual es el nombre del paciente: ')
            self.pacientes.append(nombre)
        print(self.pacientes)
        
    def atender_pacientes(self):
        print('Cuantos pacientes desea atender: ')
        n = int(input())
        if n > len(self.pacientes):
            print('Hay menos pacientes que el numero')
        else: 
            for i in range(n):
                self.pacientes.pop()
            print (self.pacientes)
        
    def problema_tecnico(self):  # Pensar como resolver esta parte de volver al commit anterior en el error. 
        print('Hubo un problema tecnico, volveremos al registro anterior')
    
new_hospital = hospital()
new_hospital.pedir_pacientes()
new_hospital.atender_pacientes()
new_hospital.problema_tecnico()