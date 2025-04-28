class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): # Al implementar el metodo constructor estamos declarando con self que atributos del objeto se van a inicializar en el momento de crearse
        # self es un argumento que hace referencia asimismo al objeto 
        # No es necesario poner estos atributos se escriban al inicio de la clase porque estamos usando el constructor
        # En el construtor solo es necesario inicializar los atributos principales, luego pueden existir otros que salgan a partir de estos
        # Por ejemplo aguante puede ser self.aguante = fuerza * vida  
        self.__nombre = nombre 
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    
    def atributos(self):
        print(self.__nombre, ':', sep='')
        print('.Fuerza:', self.__fuerza)
        print('.Inteligencia:', self.__inteligencia)
        print('.Defensa:', self.__defensa)
        print('.Vida:' ,self.__vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        
    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, 'ha realizado', daño, 'puntos de daño a: ', enemigo.__nombre)
        if enemigo.esta_vivo():
            print('La vida de', enemigo.__nombre, 'es', enemigo.__vida)
        else:
            enemigo.__morir() 
            
    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print('Error, has introducido un valor negativo')
        else:
            self.__fuerza = fuerza
        
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        # Otra manera de usar el constructor de la clase que hereda es la siguiente
        #super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    def cambiar_arma(self):
        opcion = int(input('Elige un arma: (1) Acero Valyrio. (2) Matadragones: '))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else: 
            print('Ingrese una opcion valida')
        
    def atributos(self):
        super().atributos()
        print('.Espada:', self.espada)
        
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

class Mago(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        super().atributos()
        print('.Libro', self.libro)
        
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

        
Guts = Guerrero('Guts', 20, 15, 10, 100, 5)
Goku = Personaje('Goku', 20, 15, 10, 100)
Vanessa = Mago('Vanessa', 20, 15, 10, 100, 5)
Goku.atacar(Guts)
Guts.atacar(Vanessa)
Vanessa.atacar(Goku)
Guts.atributos()
Goku.atributos()
Vanessa.atributos()



