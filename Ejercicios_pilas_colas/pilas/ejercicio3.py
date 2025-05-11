'''
En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes 
se almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico,
se debe revertir el último registro. Implementa un sistema para registrar donantes (push), 
eliminar el último (pop), y mostrar el donante actual en proceso.
'''

class Hospital:
    
    def __init__(self):
        self.pacientes = []  # stack principal
        self.historial = []  #auxiliar para deshacer cambios
    
    def pedir_pacientes(self):
        seq = int(input('Cuantos pacientes desea agregar: '))
        for i in range(seq):
            nombre = input('Cual es el nombre del paciente: ')
            self.pacientes.append(nombre)
            print(f"Paciente {nombre} agregado.")
        print(f"Lista actual de pacientes: {self.pacientes}")
        
    def atender_pacientes(self):
        print('Cuantos pacientes desea atender: ')
        n = int(input())
        if n > len(self.pacientes):
            print('Hay menos pacientes que el número ingresado.')
        else: 
            for i in range(n):
                paciente_atendido = self.pacientes.pop()
                self.historial.append(paciente_atendido)  # se guarda el paciente eliminado en el historial
                print(f"Paciente {paciente_atendido} atendido.")
            print(f"Lista actual de pacientes: {self.pacientes}")
        
    def mostrar_donante_actual(self):
        if self.pacientes:
            print(f"Donante actual en proceso: {self.pacientes[-1]}")
        else:
            print("No hay donantes en proceso.")
        
    def problema_tecnico(self):
        if self.historial:
            ultimo_paciente = self.historial.pop()  #recuperando el ultimo paciente que se elimino
            self.pacientes.append(ultimo_paciente)  # se reinserta al stack original
            print(f"Hubo un problema técnico. Se ha revertido el registro del paciente {ultimo_paciente}.")
        else:
            print("No hay registros previos que revertir.")

#instancia y llamada a metodos
new_hospital = Hospital()
new_hospital.pedir_pacientes()
new_hospital.mostrar_donante_actual()
new_hospital.atender_pacientes()
new_hospital.problema_tecnico()
