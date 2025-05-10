
class vuelos():
    
    def __init__(self):
        pass
        
    def ingresar_cola(self):
        self.lista_vuelos = deque()
        seq = int(input('Cuantos vuelos desea ingresar? '))
        for i in range (seq):
            var = int(input(f'''El vuelo numero {i+1} es nacional o internacional?
            >>> 1) - Nacional
            >>> 2) - Internacional
            >>> '''))
            
            if var == 1:
                self.tipo_nacion = 'nacional'
                self.destino = input('''Cual es su destino: 
                >>> 1) - Bluefields 
                >>> 2) - Corn Island
                >>> ''')
                
                self.tipo = input('''El vuelo es de tipo: 
                >>> 1) - Comercial
                >>> 2) - Carga
                >>> 3) - Emergencia
                >>> ''')
                
            self.lista_vuelos.append(self.tipo_nacion, self.destino, self.tipo)
        print(self.lista_vuelos)
                           
    
    def emergencia(self):
        pass
    
    def autorizar(self):
        pass    

