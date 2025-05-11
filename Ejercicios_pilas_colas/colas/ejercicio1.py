'''
En la ventanilla única de la Alcaldía de Managua, los ciudadanos hacen fila para trámites como
solicitudes de permisos de construcción, pagos de impuestos o certificaciones. 
Cada ciudadano se registra con su cédula, nombre completo, tipo de trámite y hora de llegada. Se requiere simular:
    ✔  El ingreso de ciudadanos a la fila,
    ✔	La visualización del orden de atención,
    ✔	El retiro del ciudadano atendido.
'''

from collections import deque

cola_ciudadanos = deque()

def ingresar_ciudadanos():
    n = int(input('Cuantos ciudadanos desea ingresar: '))
    for i in range (n):
        nombre = input(f'Ingrese el nombre del ciudadano numero {i+1}: ')
        cedula = input(f'Ingrese la cedula del ciudadano {nombre}: ')
        tipo = input(f'''Que tipo de tramite va a realizar:
        >>> 1) - Permiso de construccion
        >>> 2) - Pagos impuestos
        >>> 3) - Certificaciones
        >>> ''')
        agrup = f'Ciudadano {nombre} con numero de cedula {cedula} realizara un tramite de tipo {tipo}'
        cola_ciudadanos.append(agrup)
    print(cola_ciudadanos)
    
def retirar():
    seq = int(input('Cuantos pacientes desea retirar: '))
    if seq > len(cola_ciudadanos):
        print('No es posible realizar esta accion')
    else: 
        for i in range (seq):
            ciudadano = cola_ciudadanos.popleft()
            print(f'Retirando: {ciudadano}') 
        print(f'La cola despues de retirar esta asi: {cola_ciudadanos}')
def visualizar():
    print('La cola es la siguiente: ')
    for i in range(len(cola_ciudadanos)):
        print(f'{cola_ciudadanos[i]}')

ingresar_ciudadanos()
visualizar()
retirar()

