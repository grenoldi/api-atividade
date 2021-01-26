from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

base = declarative_base()
base.query = db_session.query_property()


class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String(30))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.add(self)
        db_session.commit()


class Pessoas(base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True)
    age = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Atividades(base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividade {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
