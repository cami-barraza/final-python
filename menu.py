from utils import *

def menu():
    """
    Función principal que gestiona el menú interactivo de la aplicación.

    Funcionalidades:
    - Inicializa base de datos al comenzar
    - Presenta menú cíclico con 6 opciones
    - Llama a funciones correspondientes según selección
    - Permite salir del programa
    - Maneja selecciones inválidas con mensaje en rojo

    Opciones del menú:
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Actualizar producto
    6. Salir
    """

    crear_base()
    while True:
        print(Fore.BLUE + "\n--- Menú de Productos ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Actualizar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print(Fore.RED + "Opción inválida.")