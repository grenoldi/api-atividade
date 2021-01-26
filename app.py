from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'name':i.name, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        data = request.json
        pessoa = Pessoas.query.filter_by(name=data['pessoa']).first()
        atividade = Atividades(name=data['atividade'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'atividade': atividade.nome,
            'id': atividade.id
        }
        return response

#TODO: finish the class below
class Atividade(Resource):
    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class Pessoa(Resource):
    def get(self, _name):
        pessoa = Pessoas.query.filter_by(name=_name).first()
        try:
            response = {
                'name': pessoa.name,
                'age': pessoa.age,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'message': 'Pessoa com nome {} não existe.'.format(_name)
            }
        return response

    def put(self, _name):
        pessoa = Pessoas.query.filter_by(name=_name).first()
        dados = request.json
        if 'name' in dados:
            pessoa.name = dados['name']
        if 'age' in dados:
            pessoa.age = dados['age']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'name': pessoa.name,
            'age': pessoa.age
        }
        return response

    def delete(self, _name):
        pessoa = Pessoas.query.filter_by(name=_name).first()
        pessoa.delete()
        return {
            'status': 'sucesso',
            'message': 'Registro de pessoa {} deletado.'.format(_name)
        }


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'name': i.name, 'age': i.age} for i in pessoas]
        return response

    def post(self):
        data = request.json
        pessoa = Pessoa(name=data['name'], age=data['age'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'name': pessoa.name,
            'age': pessoa.age
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:_name>')
api.add_resource(ListaPessoas, '/pessoas/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
