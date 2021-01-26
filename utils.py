from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(name='Renan', age=25)
    print(pessoa)
    pessoa.save()


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(name='Renan').first()
    pessoa.idade = 26
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(name='Renan').first()
    print(pessoa.idade)


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(name='Renan').first()
    pessoa.delete()


if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()
