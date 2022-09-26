from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# 1. lista basica de indicadores fixada em uma lista
indicadores = [
    {
        'indicador_id': 1,
        'nome_indicador': 'chao_fabrica'
    },
    {
        'indicador_id': 2,
        'nome_indicador': 'externo'
    },
    {
        'indicador_id': 3,
        'nome_indicador': 'recebimento'
    }
]


class Indicadores(Resource):

    def get(self):
        # 2. entregando todos os indicadores registrados
        return {'indicadores': indicadores}


api.add_resource(Indicadores, '/indicadores')


if __name__ == '__main__':
    # 3. execucao da aplicação
    app.run(debug=True)
