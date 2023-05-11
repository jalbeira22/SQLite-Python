import sqlite3

def crear_tabla():
    conexion.execute("""CREATE TABLE IF NOT EXISTS articulos (
                          codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                          descripcion TEXT,
                          precio REAL
                      )""")
    print("Tabla articulos creada (si no existía)")

def insertar_articulo(descripcion, precio):
    conexion.execute("INSERT INTO articulos (descripcion, precio) VALUES (?, ?)", (descripcion, precio))
    conexion.commit()

def mostrar_articulos():
    cursor = conexion.execute("SELECT codigo, descripcion, precio FROM articulos")
    for fila in cursor:
        print(fila)

def mostrar_articulo_por_codigo(codigo):
    cursor = conexion.execute("SELECT descripcion, precio FROM articulos WHERE codigo=?", (codigo, ))
    fila = cursor.fetchone()
    if fila != None:
        print(fila)
    else:
        print("No existe un artículo con dicho código.")

def mostrar_articulos_por_precio_maximo(precio_maximo):
    cursor = conexion.execute("SELECT descripcion FROM articulos WHERE precio < ?", (precio_maximo, ))
    filas = cursor.fetchall()
    if len(filas) > 0:
        for fila in filas:
            print(fila)
    else:
        print("No existen artículos con un precio menor al ingresado.")

conexion = sqlite3.connect("bd1.db")
crear_tabla()

while True:
    print("\nMenú:")
    print("1. Insertar artículo")
    print("2. Mostrar todos los artículos")
    print("3. Mostrar artículo por código")
    print("4. Mostrar artículos con precio menor al ingresado")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        descripcion = input("Ingrese la descripción del artículo: ")
        precio = float(input("Ingrese el precio del artículo: "))
        insertar_articulo(descripcion, precio)
    elif opcion == 2:
        mostrar_articulos()
    elif opcion == 3:
        codigo = int(input("Ingrese el código de un artículo: "))
        mostrar_articulo_por_codigo(codigo)
    elif opcion == 4:
        precio_maximo = float(input("Ingrese un precio máximo: "))
        mostrar_articulos_por_precio_maximo(precio_maximo)
    elif opcion == 5:
        break
    else:
        print("Opción no válida, intente nuevamente.")

conexion.close()
