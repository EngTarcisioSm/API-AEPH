from flask_restful import Resource, reqparse

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

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_indicador')


def check_last_id():
    global indicadores
    last = 0
    for indicador in indicadores:
        last = indicador['indicador_id']
    return last

def check_name(nome: str):
    global indicadores
    answer = None
    for indicador in indicadores:
        if indicador['nome_indicador'] == nome:
            answer = 1
            break
    return answer


class Indicadores(Resource):

    def get(self):
        return {'indicadores': indicadores}


class IndicadorID(Resource):

    def get(self, indicador_id):
        try:
            id = int(indicador_id)
        except:
            return None
        for indicador in indicadores:
            if indicador['indicador_id'] == id:
                return indicador

    def post(self, indicador_id):
        dados = argumentos.parse_args()
        ultimo_id = check_last_id()

        novo_indicador = {
            'indicador_id': ultimo_id+1,
            'nome_indicador': dados['nome_indicador']
        }
        if not check_name(dados['nome_indicador']):
            indicadores.append(novo_indicador)
            return novo_indicador, 200
        return {'message': 'not included'}



class IndicadorNome(Resource):

    def get(self, nome_indicador):
        for indicador in indicadores:
            if indicador['nome_indicador'] == nome_indicador:
                return indicador

    def post(self, nome_indicador):
        dados = argumentos.parse_args()
        if dados['nome_indicador'] != nome_indicador:
            return {'message': 'not included'}

        ultimo_id = check_last_id()

        novo_indicador = {
            'indicador_id': ultimo_id + 1,
            'nome_indicador': dados['nome_indicador']
        }
        if not check_name(dados['nome_indicador']):
            indicadores.append(novo_indicador)
            return novo_indicador, 200
        return {'message': 'not included'}
