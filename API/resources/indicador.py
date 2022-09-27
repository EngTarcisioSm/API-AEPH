# 1. Para conseguir receber novos indicadores é necessário incluir uma
# biblioteca para tratar requisições "reqparse"
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

# 8. criacao do parse para receber os dados enviados pela requisicao
argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_indicador')

# 9. funcao auxiliar temporaria de checagem do ultimo id da lista, futuramente
# essa função vem a ser modificada


def check_last_id():
    global indicadores
    last = 0
    for indicador in indicadores:
        last = indicador['indicador_id']
    return last


# 10. checa se um nome de indicador ja existe
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


# 2. É criado um novo recurso chamado IndicadorID para tratar cada indicador de
# forma totalmente individualizada


class IndicadorID(Resource):
    # 4. pesquisa efetuada no banco de dados por indicadores baseada em
    # indicador_id
    def get(self, indicador_id):
        try:
            id = int(indicador_id)
        except:
            # 7. Caso o Parametro não seja possivel de ser convertido não é
            # retornado nada
            return None
        for indicador in indicadores:
            if indicador['indicador_id'] == id:
                return indicador

    # 11. inclusão do metodo post
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


# 3. É criado um novo recurso chamado IndicadorNome para tratar cada indicador
# de forma totalmente individualizada


class IndicadorNome(Resource):
    def get(self, nome_indicador):
        # 5. pesquisa efetuada no banco de dados por indicador baseada em
        # nome_indicador
        for indicador in indicadores:
            if indicador['nome_indicador'] == nome_indicador:
                return indicador

    # 12. inclusão do metodo post
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
