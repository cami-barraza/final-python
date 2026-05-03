# Trabajo Final - Gestión de Productos en Python

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar productos usando una base de datos SQLite.

## 👾 Características
- **CRUD completo** sobre la tabla `productos` de SQLite.
- Gestión de **errores** (entradas inválidas, problemas de conexión, inyección SQL).
- **Validaciones** de datos (nombre no vacío, precio entero positivo, ID numérico).
- **Búsqueda** por ID exacto o por nombre (coincidencia parcial).
- **Listado** colorido de productos:  
  - IDs y nombres con formato (mayúsculas/minúsculas).  
  - Categorías en mayúsculas.  
  - Mensajes en distintos colores para facilitar la lectura.
- **Interfaz de menú** dinámica y cíclica para navegación sencilla.

## 📌 Funcionalidades

- Agregar productos
- Mostrar todos los productos
- Buscar productos por ID o por nombre
- Eliminar productos por ID
- Actualizar precio o categoría de un producto

## Menú principal
```markdown
--- Menú de Productos ---
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Actualizar producto
6. Salir
```

Ingrese el número de la opción y siga las instrucciones en pantalla.

### Opciones disponibles

1. **Agregar producto** 
Solicita nombre, categoría y precio. Valida entradas y agrega a la base de datos con parámetros seguros.

2. **Mostrar productos** 
Lista todos los productos con formato:

```yaml
1. Nombre: Televisor, Categoría: ELECTRÓNICA, Precio: 500
```

3. **Buscar producto** 
- Por ID exacto (si el término es numérico). 
- Por nombre parcial (%término%). 
- Muestra la cantidad de resultados y sus detalles.

4. **Eliminar producto** 
Muestra primero el listado. Solicita ID a eliminar. 
Borra el registro y confirma en rojo.

5. **Actualizar producto** 
Muestra listado. 
Solicita ID y campo a modificar (precio o categoria). Valida nuevo valor y actualiza en la tabla.

6. **Salir** 
Finaliza la ejecución del programa.


## Descripción de funciones

- **crear_base()**
    Inicializa la BD y crea la tabla si no existe. Maneja excepciones de sistema y conexión.

- **agregar_producto()**
    Pide datos, valida y ejecuta INSERT. Usa strip() y parámetros para seguridad.

- **mostrar_productos()**
    Consulta y despliega todos los registros. Usa colores para mejorar legibilidad.

- **buscar_producto()**
    Permite búsquedas por ID o nombre parcial. Informa si no hay coincidencias.

- **eliminar_producto()**
    Lista productos, pide ID y hace DELETE. Confirma la acción en color rojo.

- **actualizar_producto()**
    Lista productos, pide ID y campo (precio/categoria), valida y ejecuta UPDATE.

- **menu()**
    Bucle principal que muestra opciones y despacha a las demás funciones. Controla salidas y errores de opción.

## Ejemplos de uso

### Agregar un producto
```bash
Nombre del producto: Camiseta
Categoría del producto: Ropa
Precio (sin centavos): 25
```

### Buscar por nombre
```bash
Ingrese ID o nombre para buscar: cami
Se encontraron 1 producto(s):
2. Nombre: Camiseta, Categoría: ROPA, Precio: 25
```

### Actualizar precio
```bash
Ingrese el ID del producto a actualizar: 2
¿Qué desea actualizar? (precio/categoria): precio
Nuevo valor: 30
Producto actualizado.
```

## 🧰 Tecnologías utilizadas

- Python 3.7+
- SQLite3
- Colorama (para resaltar mensajes en la terminal)

## ▶ Cómo ejecutar

1. Asegurate de tener Python instalado.
2. Instalá el módulo `colorama` (si no lo tenés):

   ```bash
   pip install colorama
   ```

3. Ejecutá el archivo desde la terminal:

   ```bash
   python main.py
   ```

4. Se creará automáticamente una base de datos llamada `inventario.db`.

## 📁 Archivos incluidos

- `main.py`: Código principal del programa.
- `manu.py`: Código del menú CRUD.
- `utils.py`: Las funciones principales.
- `inventario.db`: Base de datos SQLite (se crea automáticamente al ejecutar el programa).
- `README.md`: Este archivo con la descripción del proyecto.

## 👩‍💻 Alumna

Camila Belén Barraza

Trabajo Final - Curso de Iniciación con Python (comisión 25009) - Talento Tech
