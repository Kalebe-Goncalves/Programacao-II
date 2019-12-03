import os
from peewee import *

arq = 'pontuacao.db'
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db

class Pontuacao(BaseModel):
    nome_usuario = CharField()
    pontos = CharField()
    tempo = CharField()

    def __str__(self):
        return self.nome_usuario + " = " + self.pontos + " , Tempo: " + self.tempo


db.connect()
db.create_tables([Pontuacao])

def criar_pontuacao(nome, pont, temp):
    nova_pontuacao = Pontuacao.create(nome_usuario = nome, pontos = pont, tempo = temp)
    lista_pontuacao = Pontuacao.select()
    return lista_pontuacao

def listar_pontuacoes():
    return Pontuacao.select()

