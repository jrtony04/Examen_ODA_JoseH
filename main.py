import os

ruta = "C:/Users/joseh/OneDrive/Documents/Chuchadas de la universidad/Organizacion de archivos/Equipos.txt"


def imprimir_inventario():
    if not os.path.exists(ruta) or os.stat(ruta).st_size == 0:
        print("\nEl inventario está vacío.\n")
        return

    with open(ruta, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 5:
                print(f"ID: {datos[0]} | Nombre: {datos[1]} | Tipo: {datos[2]} | "
                      f"Calibración: {datos[3]} | Mantenimiento: {datos[4]}")


def agregarequipo():
    ID = input("Introduce el identificador del equipo: ")
    nombre = input("Introduce el nombre del equipo: ")
    tipo = input("Introduce el tipo del equipo: ")
    calibracion = input("Introduce la calibración del equipo: ")
    mantenimiento = input("Introduce la fecha de mantenimiento (DD/MM/AAAA): ")

    with open(ruta, "a") as archivo:
        archivo.write(f"{ID},{nombre},{tipo},{calibracion},{mantenimiento}\n")

    print("Equipo agregado correctamente.\n")


def buscar_equipo():
    if not os.path.exists(ruta) or os.stat(ruta).st_size == 0:
        print("\nEl inventario está vacío o no existe.\n")
        return

    id_buscar = input("Ingrese el ID del equipo a buscar: ")

    encontrado = False
    with open(ruta, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 5 and datos[0] == id_buscar:
                print(f"ID: {datos[0]}")
                print(f"Nombre: {datos[1]}")
                print(f"Tipo: {datos[2]}")
                print(f"Calibración: {datos[3]}")
                print(f"Mantenimiento: {datos[4]}")
                encontrado = True
                break

    if not encontrado:
        print(f" No se encontró ningún equipo con ID {id_buscar}.\n")


def crear_indice():
    indice = {}
    if not os.path.exists(ruta) or os.stat(ruta).st_size == 0:
        return indice

    with open(ruta, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 5:
                tipo = datos[2].strip()
                if tipo not in indice:
                    indice[tipo] = []
                indice[tipo].append(datos)
    return indice


def buscar_por_tipo():
    indice = crear_indice()

    if not indice:
        print("\nNo hay equipos registrados o el archivo está vacío.\n")
        return

    tipo_buscar = input("Ingrese el tipo de equipo a buscar: ").strip()

    if tipo_buscar in indice:
        for datos in indice[tipo_buscar]:
            print(f"ID: {datos[0]} | Nombre: {datos[1]} | Calibración: {datos[3]} | Mantenimiento: {datos[4]}\n")
    else:
        print(f" No se encontraron equipos del tipo '{tipo_buscar}'.\n")

print("Bienvenido al sistema de gestión de equipos CHEPETRÓNICA")

while True:
    print("¿Qué desea realizar?")
    print("1) Visualizar inventario")
    print("2) Agregar equipo")
    print("3) Buscar equipo por ID (acceso directo)")
    print("4) Buscar por tipo de equipo (índice)")
    print("5) Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print(" Ingrese un número válido.\n")
        continue

    match opcion:
        case 1:
            imprimir_inventario()
        case 2:
            agregarequipo()
        case 3:
            buscar_equipo()
        case 4:
            buscar_por_tipo()
        case 5:
            print("Saliendo del sistema...")
            break
        case _:
            print(" Opción no válida.\n")
