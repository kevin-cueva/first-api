from flask import Flask
from flask_cors import CORS, cross_origin

from database import setup #Para crear la tabla

from resources.tasks import task_bp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
setup.create_table() # Crea la tabla

app.register_blueprint(task_bp)





if __name__ == '__main__':
    app.run(debug=False)