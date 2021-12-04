from flask import request, jsonify, Blueprint
from datetime import datetime


from database import tasks #Archivo para interactuar con la base de datos

task_bp = Blueprint('route_task', __name__)

@task_bp.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    created_date = datetime.now().strftime("%x") #5/22/2021

    data = (title, created_date)
    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify({"task": task}) 
    return jsonify({"message": "Internal Error"})


@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Ruta para mostrar todas las tareas creadas
    """
    data = tasks.select_all_task()
    if data:
        return jsonify({"tasks" : data})
    elif data == False:
        return jsonify({"message": "Internal Error"})
    else:
        return jsonify({"message": {}}) 


@task_bp.route('/tasks', methods=['PUT'])
def update_task():
    title = request.json['title'] 
    id_arg = request.args.get('id')

    if tasks.update_task(id_arg,(title,)): #Si se ejecuto correctamente la actualizacion
        task = tasks.select_task_by_id(id_arg) #Muestra los cambos
        return jsonify(task)


@task_bp.route('/tasks', methods=['DELETE'])
def delete_task():
    id_arg = request.args.get('id') # recupera el id enviado en el link

    if tasks.delete_task(id_arg):
        return jsonify({"message": "task delete"})
    return jsonify({"message": "Initial Error"})
   

@task_bp.route('/tasks/completed', methods=['PUT'])
def complete_task():
    """
    Esta ruta indica si la tarea fue completada
    """
    id_arg = request.args.get('id')
    completed_arg = request.args.get('completed')

    if tasks.complete_task(id_arg,completed_arg):
        return jsonify({"message": "succesfully"})
    
    return jsonify({"message": "Internal Error"})