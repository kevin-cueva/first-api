#Lee el query y los ejecuta 
import sqlite3
from sqlite3 import Error

from .connection import create_connection

def read_file(path):
    """
    Funcion Para leer archivos
    """
    with open(path, 'r') as sql_file:
        return sql_file.read()


def create_table():
    """
    Funcion que crea la tabla del archivo sql/tables.sql
    """
    conn = create_connection()

    path = "database/sql/tables.sql" # Rura del archivo
    sql = read_file(path)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error in funtion create_tables  {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
