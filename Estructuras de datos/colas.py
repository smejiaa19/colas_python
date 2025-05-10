from collections import deque 

cola_pacientes = deque()

def pedir_pacientes():
    cant = int(input('Cuantos pacientes desea agregar: '))
    for i in range (cant):
        paciente = input('Ingrese el nombre del paciente: ')
        cola_pacientes.append(paciente)
    menu()

def atender_pacientes():
    attend = int(input('Cuantos pacientes desea atender: '))
    for i in range (attend):
        paciente_atendido = cola_pacientes.popleft() # Esto lo hacemos para remover el primer elemento de la cola
        print(f'Paciente atendido: {paciente_atendido}')
        print(f'Cola despues de atender: {list(cola_pacientes)}') 
    menu()
    
def mostrar_cola():
    print('Cola de pacientes: ')
    print(cola_pacientes)
    menu()

def menu():
    opcion = int(input('''Que desea hacer? 
    (1) - Agregar pacientes
    (2) - Atender pacientes
    (3) - Mostrar cola
    (4) - Salir
    >>>> '''))

    match opcion:
        case 1:
            pedir_pacientes()
        case 2: 
            atender_pacientes()
        case 3:
            mostrar_cola()
        case 4:
            exit()
        case _:
            print('Opcion invalida')
            menu()

menu()
