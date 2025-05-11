'''
Ejercicio 3.
En un local de comida rápida como Tip-Top Metrocentro, se desea simular la cola de atención para pedidos. 
Cada pedido incluye: número de orden, nombre del cliente, tipo de combo (Clásico, Familiar, Sándwich) 
y hora del pedido. El sistema debe:
✔	Agregar pedidos en orden de llegada,
✔	Mostrar la cola actual de pedidos,
✔	Atender (eliminar) el primer pedido.
'''
from collections import deque

lista_pedidos = deque()

def agregar_pedidos():
    n = int(input('Cuantos pedidos desea agregar: '))
    contador = 1
    hora = 9.00
    for i in range (n):
        nombre = input('Ingrese el nombre de la persona: ')
        seleccion = int(input('''Que tipo de combo desea ordenar: 
        >>> 1) - Clasico
        >>> 2) - Familiar 
        >>> 3) - Sandwich
        >>> '''))
        
        match seleccion:
            case 1:
                tipo = 'Clasico'
            case 2:
                tipo = 'Familiar'
            case 3:
                tipo = 'Sandwich'
            case _:
                pass
            
        agregar = f'Combo numero {contador} de tipo {tipo} a nombre de {nombre}, pedido a las {hora:.2f} horas'
        lista_pedidos.append(agregar)
        contador += 1
        hora += 0.15
    
def mostrar_cola():
    print('Mostrando cola actual: ')
    for agregar in lista_pedidos:
        print(agregar)
        
def atender():
    seq = int(input('Cuantas ordenes desea atender: '))
    for i in range (seq):
        elimina = lista_pedidos.popleft()
        print(f'Eliminando orden {elimina}')

agregar_pedidos()
mostrar_cola()
atender()

        
