#llamada y conexion a la base de datos
import sqlite3

def conexion_creacion():
    try:
        conexion=sqlite3.connect('inventario.db')
        conexion.execute("PRAGMA foreign_keys = ON")
    except Exception as e:
        print("ERROR INESPERADO",e)
        print("Tipo de error:", type(e).__name__)
        return None,None
    try:
        cursor=conexion.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       correo TEXT NOT NULL)''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS productos (sku INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       precio real NOT NULL, 
                       stock INTEGER NOT NULL)''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS orden (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       fecha TEXT NOT NULL,
                       cliente_id INTEGER NOT NULL,
                       FOREIGN KEY (cliente_id) REFERENCES clientes(id))''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS detalle_orden (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       cantidad INTEGER NOT NULL, 
                       SUBTOTAL real NOT NULL,
                       orden_id INTEGER NOT NULL,
                       producto_id INTEGER NOT NULL,
                       FOREIGN KEY (orden_id) REFERENCES orden(id),
                       FOREIGN KEY (producto_id) REFERENCES productos(sku) ) ''')
        conexion.commit()
    except Exception as e:
        print("ERROR INESPERADO",e)
        print("Tipo de error:", type(e).__name__)
        conexion.close()
    return (conexion,cursor)