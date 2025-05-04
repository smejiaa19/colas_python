'''
Crear un gestor de tareas pendientes (To Do List) que permita al usuario agregar, eliminar y mostrar tareas.
'''

actividades = []

def pedir_actividades():
    cant = int(input('Cuantas actividades desea agregar: '))
    for i in range(cant):
        actividad = input('Ingrese la actividad pendiente: ')
        actividades.append(actividad)
    menu()

def eliminar_actividades():
    print('Actividades pendientes: ')
    print(actividades)
    
    cont = int(input('Cuantas actividades desea eliminar: '))
    for i in range(cont):
        actividad = input('Ingrese la actividad a eliminar: ')
        if actividad in actividades:
            actividades.remove(actividad)
        else:
            print(f'La actividad "{actividad}" no se encuentra en la lista.')
        print('Actividades restantes: ', (actividades))
    menu()
    
def mostrar_actividades(actividades):
    print(actividades)
    menu()

def menu():
    opcion = int(input(''' Que desea hacer? 
    (1) - Agregar actividades
    (2) - Eliminar actividades
    (3) - Mostrar actividades
    (4) - Salir
    >>>> '''))
    
    match opcion: 
        case 1: 
            pedir_actividades()
        case 2:
            eliminar_actividades()
        case 3:
            mostrar_actividades(actividades)    
        case 4:
            quit()
        case _:
            print('Opcion no valida')
            return menu()
        
menu()