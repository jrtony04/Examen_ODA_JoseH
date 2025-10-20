import os

ruta = "C:/Users/joseh/OneDrive/Documents/Chuchadas de la universidad/Organizacion de archivos/Equipos.txt"


def imprimir_inventario():
    if not os.path.exists(ruta) or os.stat(ruta).st_size == 0:
        print("\nEl inventario está vacío.\n")
        return

    print("\n--- INVENTARIO DE EQUIPOS ---")
    with open(ruta, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 5:
                print(f"ID: {datos[0]} | Nombre: {datos[1]} | Tipo: {datos[2]} | "
                      f"Calibración: {datos[3]} | Mantenimiento: {datos[4]}")
    print("-----------------------------\n")


def agregarequipo():
    print("\n--- AGREGAR NUEVO EQUIPO ---")
    ID = input("Introduce el identificador del equipo: ")
    nombre = input("Introduce el nombre del equipo: ")
    tipo = input("Introduce el tipo del equipo: ")
    calibracion = input("Introduce la calibración del equipo: ")
    mantenimiento = input("Introduce la fecha de mantenimiento (DD/MM/AAAA): ")

    with open(ruta, "a") as archivo:
        archivo.write(f"{ID},{nombre},{tipo},{calibracion},{mantenimiento}\n")

    print("✅ Equipo agregado correctamente.\n")


# Programa principal
print("Bienvenido al sistema de gestión de equipos CHEPETRÓNICA")

while True:
    print("¿Qué desea realizar?")
    print("1) Visualizar inventario")
    print("2) Agregar equipo")
    print("3) Salir")

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
            print("Saliendo del sistema...")
            break
        case _:
            print(" Opción no válida.\n")