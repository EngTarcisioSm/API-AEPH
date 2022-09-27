from flask_restful import Resource

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
        return {'indicadores': indicadores}