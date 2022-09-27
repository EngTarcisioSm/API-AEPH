from flask import Flask
from flask_restful import Resource, Api
from resources.indicador import Indicadores, IndicadorID, IndicadorNome

app = Flask(__name__)
api = Api(app)


api.add_resource(Indicadores, '/indicadores')
# 6. adição dos recursos criados IndicadorID e IndicadorNome para efetuar
# testes sobre o metodo get de ambos os recursos
api.add_resource(IndicadorID, '/indicador_id/<string:indicador_id>')
api.add_resource(IndicadorNome, '/indicador_nome/<string:nome_indicador>')


if __name__ == '__main__':
    app.run(debug=True)
