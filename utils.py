import sqlite3
from colorama import init, Fore

# Inicializar colorama para dar color a los textos de la terminal
init(autoreset=True)


def crear_base():
    """
    Inicializa la base de datos SQLite 'inventario.db' y crea la tabla 'productos' 
    si no existe previamente.

    La tabla incluye columnas:
    - id: Clave primaria autoincremental
    - nombre: Texto obligatorio del producto
    - categoria: Texto opcional de categorización
    - precio: Entero obligatorio del precio

    Maneja excepciones de:
    - FileNotFoundError: Problemas con el directorio o permisos
    - AttributeError: Errores en la conexión o cursor

    Utiliza CREATE TABLE IF NOT EXISTS para prevenir errores si la tabla ya existe.
    """
    try:
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT,
                precio INTEGER NOT NULL
            )
        """)
        conn.commit()
    except FileNotFoundError:
        print(Fore.RED + "Error: No se puede crear/acceder al archivo de base de datos.")
    except AttributeError:
        print(Fore.RED + "Error: Problema con la conexión a la base de datos.")
    finally:
        conn.close()


# --------------------------------------------------------------------------------------------
def agregar_producto():
    """
    Solicita al usuario los datos de un nuevo producto e inserta el registro en la base de datos.

    Realiza las siguientes validaciones:
    - Nombre no puede estar vacío
    - Precio debe ser un número entero positivo

    Maneja excepciones de:
    - ValueError: Entrada inválida de precio
    - TypeError: Problemas con tipos de datos

    Usa parámetros con '?' para prevenir inyección SQL.
    Aplica strip() para eliminar espacios en las entradas.

    Muestra mensaje de confirmación en verde al agregar producto.
    """
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            raise ValueError("Nombre vacío")
        
        categoria = input("Categoría del producto: ").strip()
        
        precio_str = input("Precio (sin centavos): ").strip()
        if not precio_str.isdigit():
            raise ValueError("Precio inválido")
        
        precio = int(precio_str)

        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)",
                       (nombre, categoria, precio))
        conn.commit()
        print(Fore.GREEN + f"Producto '{nombre}' agregado.")
    
    except ValueError as e:
        print(Fore.RED + f"Error de entrada: {e}")
    except TypeError:
        print(Fore.RED + "Error: Tipo de dato incorrecto")
    except sqlite3.Error:
        print(Fore.RED + "Error al insertar producto en la base de datos")
    finally:
        conn.close()


# --------------------------------------------------------------------
def mostrar_productos():
    """
    Recupera y muestra todos los productos almacenados en la base de datos.

    Características de presentación:
    - Muestra ID, nombre (con primera letra mayúscula)
    - Categoría en mayúsculas
    - Color cian para los resultados
    - Mensaje en amarillo si no hay productos

    Permite visualizar rápidamente el inventario completo.
    """

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()

    if productos:
        for p in productos:
            print(Fore.CYAN + f"{p[0]}. Nombre: {p[1].title()}, Categoría: {p[2].upper()}, Precio: {p[3]}")
    else:
        print(Fore.YELLOW + "No hay productos registrados.")

# -------------------------------------------------------------------
def buscar_producto():
    """
    Permite buscar productos por ID exacto o nombre parcial.

    Funcionalidades:
    - Búsqueda por ID numérico
    - Búsqueda por nombre (coincidencia parcial)
    - Usa parámetros con '?' para prevenir inyección SQL
    - Aplica strip() para eliminar espacios en la entrada

    Maneja excepciones de:
    - IndexError: Problemas con índices de resultados
    - TypeError: Problemas con tipos de datos en la búsqueda

    Muestra resultados con:
    - Número de productos encontrados
    - Detalles de cada producto
    - Mensaje en rojo si no se encuentran resultados
    """
    try:
        termino = input("Ingrese ID o nombre para buscar: ").strip()
        
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        
        if termino.isdigit():
            cursor.execute("SELECT * FROM productos WHERE id = ?", (int(termino),))
        else:
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + termino + '%',))
        
        resultados = cursor.fetchall()
        
        if not resultados:
            raise IndexError("No se encontraron productos")
        
        print(Fore.CYAN + f"Se encontraron {len(resultados)} producto(s):")
        for p in resultados:
            print(f"{p[0]}. Nombre: {p[1].title()}, Categoría: {p[2].upper()}, Precio: {p[3]}")
    
    except IndexError as e:
        print(Fore.RED + str(e))
    except TypeError:
        print(Fore.RED + "Error: Tipo de dato incorrecto en la búsqueda")
    except sqlite3.Error:
        print(Fore.RED + "Error en la base de datos durante la búsqueda")
    finally:
        conn.close()


# -----------------------------------------------------------------------
def eliminar_producto():
    """
    Elimina un producto de la base de datos según su ID.

    Proceso:
    - Muestra lista de productos previamente
    - Solicita ID del producto a eliminar
    - Valida que el ID sea un número
    - Usa parámetros con '?' para prevenir inyección SQL
    - Aplica strip() para eliminar espacios

    Muestra confirmación de eliminación en rojo.
    """

    mostrar_productos()
    id_str = input("Ingrese el ID del producto a eliminar: ").strip()
    if not id_str.isdigit():
        print(Fore.RED + "ID inválido.")
        return
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (int(id_str),))
    conn.commit()
    conn.close()
    print(Fore.RED + f"Producto con ID {id_str} eliminado.")


def actualizar_producto():
    """
    Permite modificar el precio o categoría de un producto existente.

    Flujo de actualización:
    - Muestra lista de productos
    - Solicita ID del producto
    - Permite elegir campo a modificar (precio/categoría)
    - Valida entrada de nuevo valor
    - Usa parámetros con '?' para prevenir inyección SQL
    - Aplica strip() para eliminar espacios

    Características:
    - Validación de ID numérico
    - Restricción de campos modificables
    - Validación de precio como número entero
    - Mensaje de confirmación en amarillo
    """

    mostrar_productos()
    id_str = input("Ingrese el ID del producto a actualizar: ").strip()
    if not id_str.isdigit():
        print(Fore.RED + "ID inválido.")
        return
    campo = input("¿Qué desea actualizar? (precio/categoria): ").lower()
    if campo not in ["precio", "categoria"]:
        print(Fore.RED + "Campo inválido.")
        return
    nuevo_valor = input("Nuevo valor: ").strip()
    if campo == "precio" and not nuevo_valor.isdigit():
        print(Fore.RED + "Precio inválido.")
        return

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE productos SET {campo} = ? WHERE id = ?", (nuevo_valor, int(id_str)))
    conn.commit()
    conn.close()
    print(Fore.YELLOW + "Producto actualizado.")
