#logica de la bd
from database import conexion_creacion

def agregar_cliente(nombre,correo): #INSERTA CLIENTES
    conexion,cursor=conexion_creacion()
    cursor.execute(''' INSERT INTO clientes(nombre, email) VALUES (?,?)''',(nombre,correo))
    conexion.commit()
    conexion.close()

def ver_clientes(): #MUESTRA CLIENTES
    conexion,cursor=conexion_creacion()
    cursor.execute(''' SELECT id, nombre, email FROM clientes ''')
    clientes=cursor.fetchall()
    conexion.close()
    return clientes
