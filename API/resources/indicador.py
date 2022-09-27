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

# 3. modificação de retorno da função


def check_name(nome: str):
    global indicadores
    for indicador in indicadores:
        if indicador['nome_indicador'] == nome:
            return indicador
    return None

# 2. faz busca de um indicador por seu ID


def check_id(id: int):
    global indicadores
    for indicador in indicadores:
        if indicador['indicador_id'] == id:
            return indicador
    return None


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

    def put(self, indicador_id):
        # 1. coletando os dados passados
        dados = argumentos.parse_args()

        try:
            id = int(indicador_id)
        except:
            return {'message': 'Indicador Not Found!'}, 404

        indicador = check_id(id)

        novo_indicador = {'indicador_id': id, **dados}

        if check_name(dados['nome_indicador']):
            return {'message': 'Error Request'}

        # 4. caso o id exista o indicador tem seu nome atualizado
        if indicador:
            indicador.update(novo_indicador)
            return novo_indicador, 200

        # 5. caso o id não exista é criado um novo indicador com o proximo id
        # disponivel
        novo_id = check_last_id()
        novo_indicador['indicador_id'] = novo_id+1
        indicadores.append(novo_indicador)

        return novo_indicador, 201


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

    def put(self, nome_indicador):

        dados = argumentos.parse_args()

        # verifica a existencia do indicador 
        indicador = check_name(nome_indicador)

        # verifica se o dado passado na url veio vazio
        if dados['nome_indicador'] is None:
            return {'message': 'Error Request'}

        # verifica se ja existe um indicador com o nome passado para o novo 
        # nome 
        if check_name(dados['nome_indicador']):
            return {'message': 'Error Request'}

        if indicador:
            novo_indicador = {
                'indicador_id': indicador['indicador_id'], **dados}
            indicador.update(novo_indicador)
            return novo_indicador, 200

        novo_id = check_last_id()
        novo_indicador = {'indicador_id': novo_id+1, **dados}
        indicadores.append(novo_indicador)

        return novo_indicador, 201
