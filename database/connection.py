#Este archivo tendra la conexion a la base de datos y las crea
import sqlite3
from sqlite3 import Error
def create_connection():
    """"
    Se conecta y crea la base de datos

    """
    conn = None
    try:
        conn = sqlite3.connect("database/tasks.db") #Crea o conecta la base de datos
    except Error as e:
        print("Error connenting to database" + str(e)) #Ocurio un error al conectarse
        
    return conn

    
