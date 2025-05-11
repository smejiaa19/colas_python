'''
Ejercicio 2.
El aeropuerto internacional necesita un sistema para organizar el despegue de vuelos nacionales 
(hacia Bluefields, Corn Island) e internacionales (hacia Panamá, Miami). Cada vuelo tiene: código 
de vuelo, aerolínea, destino y tipo (comercial, carga, emergencia). El sistema debe:
✔	Ingresar vuelos a la cola,
✔	Priorizar vuelos de emergencia,
✔	Autorizar el siguiente vuelo para despegar.
'''

from collections import deque

lista_vuelos = deque()

def ingresar_cola():
    seq = int(input('Cuantos vuelos desea ingresar: '))
    for i in range(seq):
        var = int(input(f'''El vuelo numero {i+1} es nacional o internacional? 
        >>> 1) - Nacional
        >>> 2) - Internacional
        >>> '''))
        
        if var == 1: 
            tipo_nacion = 'Nacional'
            destino = input('''Cual es su destino: 
            >>> 1) - Bluefields 
            >>> 2) - Corn Island
            >>> ''')
            
        elif var == 2:
            tipo_nacion = 'Internacional'
            destino = input('''Cual es su destino: 
            >>> 1) - Panama
            >>> 2) - Miami
            >>> ''')
        
        tipo = input('''El vuelo es de tipo: 
        >>> 1) - Comercial
        >>> 2) - Carga
        >>> 3) - Emergencia
        >>> ''')
            
        codigo_vuelo = int(input('Ingrese el codigo de su vuelo: '))
        aerolinea = input('Nombre de la aerolinea: ')
        
            
        agrega = f'El vuelo {codigo_vuelo} es: {tipo_nacion} con destino a: {destino} de tipo: {tipo} en la aerolinea: {aerolinea}'
        if tipo == 'Emergencia':
            lista_vuelos.appendleft(agrega)
        else:
            lista_vuelos.append(agrega)
            
def mostrar_cola():
    print('Lista de vuelos')
    for agrega in lista_vuelos:
        print(agrega)
        

def autorizar():
    n = int(input('Cuantos vuelos desea autorizar para despegar: '))
    for i in range (n):
        autorizado = lista_vuelos.popleft()
        print(f'{autorizado}')
        
ingresar_cola()
mostrar_cola()
autorizar()

