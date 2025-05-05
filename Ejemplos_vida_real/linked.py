class Paciente:
    def __init__(self, nombre, urgencia=False):
        self.nombre = nombre
        self.urgencia = urgencia
        self.siguiente = None

class ListaDeEspera:
    def __init__(self):
        self.inicio = None

    def agregar_paciente(self, nombre, urgencia=False):
        nuevo_paciente = Paciente(nombre, urgencia)

        if self.inicio is None:
            self.inicio = nuevo_paciente
        elif urgencia:
            # Insertar al principio si es urgente
            nuevo_paciente.siguiente = self.inicio
            self.inicio = nuevo_paciente
        else:
            # Insertar al final
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_paciente

    def mostrar_lista(self):
        actual = self.inicio
        if not actual:
            print("La lista de espera está vacía.")
            return
        while actual:
            tipo = "URGENTE" if actual.urgencia else "Normal"
            print(f"{actual.nombre} ({tipo})")
            actual = actual.siguiente

    def atender_paciente(self):
        if self.inicio is None:
            print("No hay pacientes en la lista.")
            return
        atendido = self.inicio
        self.inicio = self.inicio.siguiente
        print(f"Paciente atendido: {atendido.nombre}")

    def buscar_paciente(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre.lower() == nombre.lower():
                tipo = "URGENTE" if actual.urgencia else "Normal"
                print(f"{actual.nombre} está en la lista. Tipo: {tipo}")
                return
            actual = actual.siguiente
        print(f"{nombre} no está en la lista de espera.")
        

# Ejemplo de uso
def main():
    espera = ListaDeEspera()

    espera.agregar_paciente("Ana")
    espera.agregar_paciente("Carlos")
    espera.agregar_paciente("Luisa", urgencia=True)
    espera.agregar_paciente("Pedro")

    print("Lista de espera actual:")
    espera.mostrar_lista()

    print("\nBuscando a Carlos:")
    espera.buscar_paciente("Carlos")

    print("\nAtendiendo al siguiente paciente:")
    espera.atender_paciente()

    print("\nLista de espera actual:")
    espera.mostrar_lista()

main()