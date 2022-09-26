from flask import Flask
from flask_restful import Resource, Api
from resources.indicador import Indicadores

app = Flask(__name__)
api = Api(app)


api.add_resource(Indicadores, '/indicadores')


if __name__ == '__main__':
    app.run(debug=True)
