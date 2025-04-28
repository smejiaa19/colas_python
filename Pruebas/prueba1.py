'''
Quiero hacer clases para minecraft, digamos que voy a crear un personaje que sea steve.
Tambien voy a hacer animales, para que steve pueda hacerles daño.
Creo que las clases van a ser dos 
    1) Personaje
    2) Animales
        - De estas clases saldran atributos como: 
            1.1> Raza
            1.2> Vida
            1.3> Daño 
            -----------
            2.1> Raza
            2.2> Vida
            2.3> Color
            --------------
        - De estas clases saldran metodos como: 
            1.1> Correr
            1.2> Atacar
            1.3> Comer
            -----------
            2.1> Correr
            2.2> Comer
            2.3> Mirar

Despues de crear estas clases voy a hacer unas funciones, primero para poder pedirle al usuario que ingrese que tipo de arma desea que el personaje use
    Las opciones son: 
        1) Espada
        2) Arco 
        3) Hacha
    Dependiendo de estas opciones las armas haran mas o menos daño
    
Vamos a hacer funciones para subir de nivel a steve, para matar
Voy a hacer una funcion para verificar cuando un animal este muerto.
    
'''

'''

El codigo va funcionando muy bien, sin embargo creo que deberia de modificarlo para que lo primero que se muestra sean los atributos de los personajes 
De esta manera el usuario podra escojer que arma quiere para atacar a los animales. Siento que asi puede ser mas interactivo

Tambien quiero agregarle que los animales esten en un modo pacifico antes que los ataquen, comiendo y caminando. 
Cuando los empiecen a atacar quiero que estos ataquen de vuelta, restando puntos de vida a steve cada 2 turnos. Puedo hacer esto mediante un ciclo for for daño in range(2, 6, 2)
En ese ciclo for lo que hago es decir que vamos a iniciar haciendo un daño de 2 puntos y vamos a ir incrementando dos veces, es decir 2,4,6,8,10 y vamos a llegar a hacer 5 turnos de daño

Esto deberia tambien modificar los puntos de vida del personaje y del animal


'''

class Personaje():
    
    def __init__(self, raza, nombre, vida, daño): # Constructor de la clase personaje 
        self.raza = raza
        self.vida = vida
        self.daño = daño
        self.nombre = nombre
        
    def mostrar_atributos_personaje(self): # Metodo para mostrar atributos del personaje, esto resulta realmente util porque tenemos el metodo escojer arma, que modifica el atributo daño
        print(f'''Los atributos del personaje {self.nombre} son los siguientes: 
        >>> Raza: {self.raza}
        >>> Nombre: {self.nombre}
        >>> Vida: {self.vida}
        >>> Daño: {self.daño}''')

    def menu(self): # Aqui tenemos el metodo para mostrar el menu principal, aqui le damos la oportunidad al usuario de escojer lo que desea hacer.
        try:
            menu_option = int(input(f'''Que desea hacer {self.nombre}: 
            (1) - Ecoger armas
            (2) - Caminar 
            (3) - Comer
            (4) - Ver animales 
            >>> '''))
            if menu_option <= 0 | menu_option > 4:
                raise ValueError
            elif isinstance(menu_option, str | float):
                raise TypeError
        except TypeError as e:
            print(f'Error: {e}')
            print('Por favor ingrese datos correctos (ENTEROS)')
            return self.menu()
        except ValueError as e:
            print(f'Error: {e}')
            print('Por favor ingrese numeros dentro del rango (1-4)')
            return self.menu()
        match menu_option:
            case 1:
                Personaje.escoger_arma(self)
            case 2: 
                Personaje.caminar(self)
            case 3:
                Personaje.comer(self)
            case 4: 
                Personaje.ver_animales(self)

    def caminar(self):
        try:
            bloques = int(input(f'''Cuantos bloques desea caminar {self.nombre}? 
                >>> '''))
            if bloques < 0:
                raise ValueError
            elif isinstance(bloques, str | float):
                raise TypeError
            else:
                print(f'{self.nombre} esta caminando {bloques} bloques.....')
        except TypeError as e:
            print(f'Error: {e}')
            print('Por favor ingrese datos correctos (Enteros)')
            return self.caminar()
            
        except ValueError as e:
            print(f'Error: {e}')
            print('Por favor ingrese valores correctos (>0)')
            return self.caminar()

    def comer(self):
        try:
            comida = int(input(f'''Que deseas que coma {self.nombre}? 
            (1) - Pollo frito
            (2) - Pan
            (3) - Pastel
            (4) - Carne cocinada
            (5) - Carne de cerdo cocinada
            >>> '''))
            if comida <= 0 | comida > 6:
                raise ValueError
            elif isinstance(comida, str | float):
                raise TypeError
            match comida:
                case 1:
                    print(f'{self.nombre} esta comiendo: Pollo frito')
                    print('Ha recuperado 7 corazones de vida')
                case 2:
                    print(f'{self.nombre} esta comiendo: Pan')
                    print('Ha recuperado 2 corazones de vida')
                case 3:
                    print(f'{self.nombre} esta comiendo: Pastel')
                    print('Ha recuperado 3 corazones de vida')
                case 4:
                    print(f'{self.nombre} esta comiendo: Carne cocinada')
                    print('Ha recuperado 5 corazones de vida')
                case 5:
                    print(f'{self.nombre} esta comiendo: Carne de cerdo cocinada')
                    print('Ha recuperado 6 corazones de vida')
        except TypeError as e:
            print(f'Error: {e}')
            print('Por favor ingrese tipos de datos correctos (ENTEROS)')
            return self.comer()
        except ValueError as e:
            print(f'Error: {e}')
            print('Por favor ingrese numeros dentro del rango (1-5)')
            return self.comer()
    
    def escoger_arma(self):
        try:
            option = int(input(f'''Que tipo de arma desea usar {self.nombre}: 
            (1) - Espada
            (2) - Hacha
            (3) - Arco
            >>> '''))
            if option <= 0 and option > 3:
                raise ValueError
            elif isinstance(option, str | float):
                raise TypeError
        except TypeError as e: 
            print(f'{e}')
            print('Por favor ingrese un tipo de dato correcto (ENTERO)')
            return self.escoger_arma()
        except ValueError as e:
            print(f'Error: {e}')
            print('Por favor ingrese numeros dentro del rango (1-3)')
            return self.escoger_arma()
        match option:
            case 1: 
                self.daño = 25
                print(f'La espada hace: {self.daño} puntos de daño')
                self.mostrar_atributos_personaje
            
            case 2: 
                self.daño = 50
                print(f'El arco hace: {self.daño} puntos de daño')
                self.mostrar_atributos_personaje
            
            case 3:
                self.daño = 75
                print(f'El hacha hace: {self.daño} puntos de daño')
                self.mostrar_atributos_personaje
                
    def esta_vivo(self):
        return self.vida > 0
    
    def atacar(self):
        pass
    
    def matar(self):
        pass
    
    def ver_animales(self):
        pass    
    
    
'''Esta clase la definimos para poder heredarla mas adelante a la clase de Animales, tambien puede heredar a la clase personajes, pero eso no lo tome en cuenta anteriormente'''    
class Entidad():
    
    def __init__(self, raza, vida, daño):
        self.raza = raza   
        self.vida = vida
        self.daño = daño
        
        
'''Esta clase es la de los animales, aqui vamos a tener los metodos de mostrar atributos, correr, comer, mirar y estoy pensando si hacer uno para atacar, morir, etc.'''
class Animal(Entidad):
    
    def __init__(self, raza, vida, daño, color): # Este es el constructor, donde decimos que heredamos de la clase Entidad los atributos de raza, vida
        super().__init__(raza, vida, daño)
        self.color = color
        
    def mostrar_atributos_animal(self): # Aqui tenemos metodo para mostrar los atributos del animal, esto resulta importante para ver como van cambiando estos atributos con el tiempo
        print(f'''Los atributos del animal son:
        >>> Raza: {self.raza}
        >>> Puntos de vida: {self.vida}
        >>> Puntos de daño: {self.daño}
        >>> Color: {self.color}
        ''')
    
    def correr(self): # Tengo pensando hacer un modo por asi decirlo que mientras steve le pegue al animal, este corra 5 bloques.
        pass
    
    def comer(self): # El animal estara comiendo si nada lo esta atacando
        if self.vida == 100:
            print(f'El animal {self.raza} esta comiendo para nutrirse')
    
    def mirar(self): # El animal mirara a Steve cuando este a punto de morir
        pass
    
    def atacar(self):
        pass
    
steve = Personaje('Humano', 'Steve', 10, 100)
vaca = Animal('Vaca', 100, 2, 'Negra')
print(vaca.mostrar_atributos_animal())
steve.menu()
steve.mostrar_atributos_personaje()