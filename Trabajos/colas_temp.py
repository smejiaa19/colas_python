from collections import deque
from datetime import datetime

class ColaTemperatura:
    
    def __init__(self):
        self.cola_temperatura = deque()
        
    def agregar_temperatura(self):
        try:
            seq = int(input('¿Cuántas temperaturas desea agregar? '))
            if seq <= 0:
                raise ValueError('Debe ingresar un número mayor a 0.')
            elif not isinstance(seq, int):
                raise TypeError
        except (ValueError, TypeError) as e:
            print('Error:', e)
            return  # No sigas si el número no es válido

        for _ in range(seq):
            try:
                temp = float(input('Ingrese la temperatura: '))
                if temp < 0:
                    raise ValueError('La temperatura no puede ser negativa.')
                elif not isinstance(temp, float):
                    raise TypeError
                hora = datetime.now().strftime("%H:%M:%S")
                self.cola_temperatura.append((temp, hora))
            except (ValueError, TypeError) as e:
                print('Error:', e)
    
    def mostrar_temperaturas(self):
        if not self.cola_temperatura:
            print('No hay temperaturas registradas.')
            return

        print('Cola de temperaturas:')
        for temp, hora in self.cola_temperatura:
            print(f'Temperatura: {temp}°C, Hora: {hora}')
    
    def calcular_promedio(self):
        if not self.cola_temperatura:
            print('No hay temperaturas registradas.')
            return
        
        temperaturas = [temp for temp, _ in self.cola_temperatura]
        promedio = sum(temperaturas) / len(temperaturas)
        print(f'Promedio de temperaturas: {promedio:.2f}°C')
    
    def temperaturas_mayores_30(self):
        if not self.cola_temperatura:
            print('No hay temperaturas registradas.')
            return

        print('Temperaturas mayores a 30°C:')
        mayores_30 = list(filter(lambda registro: registro[0] > 30, self.cola_temperatura))
        if mayores_30:
            for temp, hora in mayores_30:
                print(f'Temperatura: {temp}°C, Hora: {hora}')
        else:
            print('No hubo temperaturas mayores a 30°C.')

    def menu(self):
        while True:
            try:
                option = int(input('''\n¿Qué desea hacer?
                (1) - Agregar temperatura
                (2) - Mostrar temperaturas
                (3) - Calcular promedio
                (4) - Mostrar temperaturas mayores a 30°C
                (5) - Salir
                >>> '''))
                
                match option:
                    case 1:
                        self.agregar_temperatura()
                    case 2:
                        self.mostrar_temperaturas()
                    case 3:
                        self.calcular_promedio()
                    case 4:
                        self.temperaturas_mayores_30()
                    case 5:
                        print('Saliendo del programa. ¡Hasta luego!')
                        break
                    case _:
                        print('Opción no válida.')
            except ValueError:
                print('Debe ingresar un número entero válido.')

temperatura = ColaTemperatura()
temperatura.menu()
