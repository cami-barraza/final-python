# final-python

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

## 🧰 Tecnologías utilizadas

- Python 3
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

## 👩‍💻 Autora

Camila Belén Barraza

Trabajo Final - Curso de Iniciación con Python (comisión 25009) - Talento Tech
