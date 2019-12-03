import os
from peewee import *

# conexão com o banco de dados do SQLLite
arq = 'estoque_roupas.db'
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db

# declaração da classe herdando características da classe BaseModel


class Roupa(BaseModel):
    # atributos do tipo texto
    codigo_roupa = CharField()
    categoria = CharField()
    tamanho = CharField()
    cor = CharField()
    genero = CharField()
    # o método __str__ agrega estilo de exibição de informações da classe

    def __str__(self):
        return self.codigo_roupa + "," + self.categoria + " tamanho: " + self.tamanho+" da cor " + self.cor


db.connect()
db.create_tables([Roupa])

roupa1 = Roupa.create(codigo_roupa="01_a", categoria="Vestido",
                      tamanho="P", cor="Azul", genero="Feminino")
roupa2 = Roupa.create(codigo_roupa="02_a", categoria="Vestido",
                      tamanho="M", cor="Azul", genero="Feminino")
roupa3 = Roupa.create(codigo_roupa="03_a", categoria="Vestido",
                      tamanho="G", cor="Azul", genero="Feminino")
roupa4 = Roupa.create(codigo_roupa="01_p", categoria="Vestido",
                      tamanho="P", cor="Preto", genero="Feminino")
roupa5 = Roupa.create(codigo_roupa="02_p", categoria="Vestido",
                      tamanho="M", cor="Preto", genero="Feminino")
roupa6 = Roupa.create(codigo_roupa="03_p", categoria="Vestido",
                      tamanho="G", cor="Preto", genero="Feminino")
roupa7 = Roupa.create(codigo_roupa="01_r", categoria="Vestido",
                      tamanho="P", cor="Rosa", genero="Feminino")
roupa8 = Roupa.create(codigo_roupa="02_r", categoria="Vestido",
                      tamanho="M", cor="Rosa", genero="Feminino")
roupa9 = Roupa.create(codigo_roupa="03_r", categoria="Vestido",
                      tamanho="G", cor="Rosa", genero="Feminino")
roupa10 = Roupa.create(codigo_roupa="01_v", categoria="Vestido",
                       tamanho="P", cor="Vermelho", genero="Feminino")
roupa11 = Roupa.create(codigo_roupa="02_v", categoria="Vestido",
                       tamanho="M", cor="Vermelho", genero="Feminino")
roupa12 = Roupa.create(codigo_roupa="03_v", categoria="Vestido",
                       tamanho="G", cor="Vermelho", genero="Feminino")


def listar_roupas():
        roupas = Roupa.select()
        return roupas
