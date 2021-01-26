from models import Pessoas, Users


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


def insert_user(login, password):
    user = Users(login=login, password=password)
    user.save()


def list_all_users():
    users = Users.query.all()
    print(users)


if __name__ == '__main__':
    insert_user('bob', '1234')
    list_all_users()
    insert_user('renoldi', '1234')
    list_all_users()
