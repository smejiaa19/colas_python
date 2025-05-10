def crea_array():
    """
    Esta función crea un array (lista en Python),
    toma la entrada del usuario para llenarlo, y luego imprime el contenido del array.
    """

    A = [0] * 5  # Inicializa una lista llamada 'A' con 5 elementos, todos establecidos en 0.
                  # Las listas de Python tienen un tamaño dinámico, pero la pre-asignación puede ser una buena práctica.

    for i in range(5):  # Itera desde i = 0 hasta i = 4 
        print("Escriba el valor a almacenar:")  # Muestra el mensaje al usuario
        A[i] = input()  # Lee la entrada del usuario y la almacena en A[i].
                       # input() devuelve una cadena de forma predeterminada. #Si necesitas números, tendrás que convertirla.
#  A[i] = int(input())

    for k in range(5):  # Itera desde k = 0 hasta k = 4 
        print(f"A[{k + 1}] = {A[k]}")  # Imprime el elemento.
                                     # Las cadenas f son una forma concisa de incrustar variables en cadenas.
                                     # Usamos k+1 para coincidir con la indexación basada en 1 

# Ejemplo de cómo llamar a la función:
#crea_array()

class arreglo():
    
    def __init__(self):
        pass
    
    def pedir_datos(self):
        print('Cuantos elementos tiene el arreglo? ')
        n = int(input())
        self.lista = [0] * n
        for i in range(n):
            print(f'Escriba el valor a almacenar en la posicion {i}: ')
            self.lista[i] = input()
        self.mostrar_datos()
        self.ordenar_arreglo()
        
    def mostrar_datos(self):
        print('Los elementos del arreglo son: ')
        print(self.lista)
        
    def ordenar_arreglo(self):
        self.lista.sort()
        print('Los elementos del arreglo ordenados son: ')  
        print(self.lista)

arreglo = arreglo()
arreglo.pedir_datos()
        
 