from flask import Flask

from database import setup #Para crear la tabla

from resources.tasks import task_bp

app = Flask(__name__)

setup.create_table() # Crea la tabla

app.register_blueprint(task_bp)



if __name__ == '__main__':
    app.run(debug=True)