#Esta funcion ejecuta los vervos SELECT, INSERT, UPDATE, DELECT 
# de la tabla task

import sqlite3
from sqlite3 import Error

from .connection import create_connection

def insert_task(data):
    """"
    Funcion para insertar  datos (titulo, la fecha de creacion)
    """
    conn = create_connection()

    sql = f"""INSERT INTO tasks (title, created_date)
              VALUES(?, ?)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid #id del registro
    
    except Error as e:
        print(f"error at the insert_task() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()


def select_task_by_id(_id):
    """
    Trae una tarea con el parametro id 
    """
    conn = create_connection()
    sql = f"""SELECT * FROM tasks WHERE id={_id}"""

    try:
        conn.row_factory = sqlite3.Row #convierte la tupla en un objeto mas simple
        cur = conn.cursor()
        cur.execute(sql)
        task = dict(cur.fetchone())
        return task
    except Error as e:
        print(f"Errorn at select_task_by_id: {str(e)}")
        return False

    finally:
        if conn:
            cur.close()
            conn.close()   


def select_all_task():
    """
    Mustra todas las tareas
    """
    conn = create_connection() #Esta funcion crea la conexion
    sql = "SELECT * FROM tasks"

    try:
        conn.row_factory = sqlite3.Row #conviertelo en una lista de objetos
        cur = conn.cursor()
        cur.execute(sql)
        task_rows = cur.fetchall()
        task = [dict(row) for row in task_rows] #Cada lista combiertela en diccionario
        return task
    except Error as e:
        print(f"Error at select_all_tasks {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()
        

def update_task(_id, data):
    """"
    Funcion para actualizar  datos (titulo, la fecha de creacion)
    (id, data)
    id: is the id to update
    data: is the data to changes in format tuple
    """
    conn = create_connection()

    sql = f"""UPDATE tasks SET title = ? 
              WHERE id = {_id}
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    
    except Error as e:
        print(f"error at the update_task() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_task(_id):
    """
    Elimina una tarea pasandole el id correspondiente
    """
    conn = create_connection()

    sql = f"""DELETE FROM tasks WHERE id = {_id} """

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True

    except Error as e:
        print(f"Error at delete_task() {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()


def complete_task(_id, completed):
    conn = create_connection()

    sql = f"""UPDATE tasks SET completed = {completed}
              WHERE id = {_id}"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Erroar at comlete_task {str(e)}")
    finally:
        if conn:
            cur.close()
            conn.close()
        