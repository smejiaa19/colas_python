pila_notas = []

def agregar_notas():
    cant = int(input('Cuantas notas desea agregar: '))
    for i in range(cant):
        nota = input('Ingrese la nota: ')
        pila_notas.append(nota)
    menu()

def eliminar_notas():
    print('Notas actuales: ')
    print(pila_notas)

    cant = int(input('Cuantas notas desea eliminar: '))
    for i in range (cant):
        pila_notas.pop()
    print(f'Notas restantes: {pila_notas}')
    menu()
    
def mostrar_notas():
    print('Notas actuales: ')
    print(pila_notas)
    menu()
    
def menu():
    opcion = int(input('''Que desea hacer?
    (1) - Agregar notas
    (2) - Eliminar notas
    (3) - Mostrar notas
    (4) - Salir
    >>> '''))
    
    match opcion:
        case 1:
            agregar_notas()
        case 2:
            eliminar_notas()
        case 3: 
            mostrar_notas()
        case 4:
            exit()
        case _:
            print('Opcion invalida')
            menu()
            
menu()