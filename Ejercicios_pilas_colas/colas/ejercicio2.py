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

            tipo = input('''El vuelo es de tipo: 
            >>> 1) - Comercial 
            >>> 2) - Carga
            >>> 3) - Emergencia
            >>> ''')
            
            agrega = f'El vuelo {i+1} es: {tipo_nacion} con destino a: {destino} de tipo: {tipo}' 
            lista_vuelos.append(agrega)
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
            
            agrega = f'El vuelo {i+1} es: {tipo_nacion} con destino a: {destino} de tipo: {tipo}'
            lista_vuelos.append(agrega)
    
    for i in range (len(lista_vuelos)):
            print(agrega)
            
def priorizar_emergencia():
    pass
    
ingresar_cola()
