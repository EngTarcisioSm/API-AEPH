# 1. Imports necessários para criação da rest API
from flask import Flask
from flask_restful import Resource, Api

# 2. Instanciação do Objeto
app = Flask(__name__)
api = Api(app)

# 4. Criação do recurso base da rest api


class Indicadores(Resource):

    # 5. teste do recurso inicial get
    def get(self):
        # 6. Apenas Retorna uma mensagem simples
        return {'indicadores': 'meus indicadores'}



# 7. adicionando primeiro recurso da api, '/indicadores', devendo ser chamado 
# dessa forma na requisição
api.add_resource(Indicadores, '/indicadores')


if __name__ == '__main__':
    # 3. execucao da aplicação
    app.run(debug=True)
