'''
Ejercicio 3.
En un local de comida rápida como Tip-Top Metrocentro, se desea simular la cola de atención para pedidos. 
Cada pedido incluye: número de orden, nombre del cliente, tipo de combo (Clásico, Familiar, Sándwich) 
y hora del pedido. El sistema debe:
✔	Agregar pedidos en orden de llegada,
✔	Mostrar la cola actual de pedidos,
✔	Atender (eliminar) el primer pedido.
'''

class tip_top():
    
    def __init__(self):
        pass
    
    def agregar_pedidos(self):
        self.lista_pedidos = []
        seq = int(input('Cuantos pedidos desea agregar: '))
        for i in range (seq): 
            i = 1
            self.numero_orden = i
            i =+ 1
            
            self.nombre_cliente = input('Ingrese el nombre del cliente que realiza el pedido: ')
            self.tipo_combo = int(input('''Que tipo de combo desea: 
            >>> 1) - Clasico
            >>> 2) - Familiar
            >>> 3) - Sandwich
            >>> '''))
            
            match self.tipo_combo:
            
                case 1:
                    self.tipo_combo = f'El combo con numero {self.numero_orden} es: Clasico'
                case 2: 
                    self.tipo_combo = f'El combo con numero {self.numero_orden} es Familiar'
                case 3:
                    self.tipo_combo = f'El combo con numero {self.numero_orden} es Sandwich'
                case _:
                    pass
            self.agrega = f'{self.tipo_combo} y esta a nombre de {self.nombre_cliente}'    
            self.lista_pedidos.append(self.agrega)
    
    def mostrar_cola(self):
        for i in range (len(self.lista_pedidos)):
            print(self.agrega)
    
    def atender(self):
        pass
    
new_tip_top = tip_top()
new_tip_top.agregar_pedidos()
new_tip_top.mostrar_cola()
    