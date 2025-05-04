import math

# Lista de ubicaciones -> cada elemento es un diccionario con nombre y coordenadas (tupla)
ubicaciones = []

def registrar_ubicacion(nombre, latitud, longitud):
    coordenadas = (latitud, longitud)
    ubicacion = {'nombre': nombre, 'coordenadas': coordenadas}
    ubicaciones.append(ubicacion)
    print(f"Ubicación '{nombre}' registrada con coordenadas {coordenadas}.")

def mostrar_ubicaciones():
    if not ubicaciones:
        print("\nNo hay ubicaciones registradas.")
        return
    print("\n--- Ubicaciones registradas ---")
    for idx, u in enumerate(ubicaciones, 1):
        print(f"{idx}. {u['nombre']}: {u['coordenadas']}")

def buscar_ubicacion(nombre):
    for u in ubicaciones:
        if u['nombre'].lower() == nombre.lower():
            print(f"Ubicación encontrada: {u['nombre']} - {u['coordenadas']}")
            return
    print("Ubicación no encontrada.")

def distancia_aproximada(coord1, coord2):
    # Cálculo muy simplificado (no considera curvatura terrestre)
    x1, y1 = coord1
    x2, y2 = coord2
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

def calcular_distancia():
    nombre1 = input("Primera ubicación: ")
    nombre2 = input("Segunda ubicación: ")
    coords = {}
    for u in ubicaciones:
        if u['nombre'].lower() == nombre1.lower():
            coords['a'] = u['coordenadas']
        if u['nombre'].lower() == nombre2.lower():
            coords['b'] = u['coordenadas']
    if 'a' in coords and 'b' in coords:
        d = distancia_aproximada(coords['a'], coords['b'])
        print(f"Distancia aproximada entre '{nombre1}' y '{nombre2}': {d} unidades.")
    else:
        print("Una o ambas ubicaciones no fueron encontradas.")

# Menú
def menu():
    while True:
        print("\n--- Sistema de Ubicaciones GPS ---")
        print("1. Registrar ubicación")
        print("2. Mostrar ubicaciones")
        print("3. Buscar ubicación")
        print("4. Calcular distancia entre ubicaciones")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la ubicación: ")
            lat = float(input("Latitud: "))
            lon = float(input("Longitud: "))
            registrar_ubicacion(nombre, lat, lon)
        elif opcion == '2':
            mostrar_ubicaciones()
        elif opcion == '3':
            nombre = input("Nombre a buscar: ")
            buscar_ubicacion(nombre)
        elif opcion == '4':
            calcular_distancia()
        elif opcion == '5':
            print("Saliendo del sistema de ubicaciones...")
            break
        else:
            print("Opción inválida.")

menu()
