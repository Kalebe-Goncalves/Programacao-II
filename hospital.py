import os
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq = 'hospital.db'
db = SqliteDatabase (arq )

class BaseModel(Model):
    class Meta:
        database = db

class Setor(BaseModel):
    nome = CharField()
    localizacao = CharField()
    cor = CharField()
    tipo_setor = CharField()

class Especialidade(BaseModel):
    cod_especialidade = IntegerField()
    documento = CharField()
    desc_especialidade = CharField()        

class Medico(BaseModel):
    nome = CharField()
    id_medico = IntegerField()
    salario = FloatField()
    especialidade = ForeignKeyField(Especialidade)

class Paciente(BaseModel):
    nome = CharField()
    cpf = CharField()
    doenca = CharField()

class Exame(BaseModel):
    preco = FloatField()
    prazo_liberacao = IntegerField()
    nome = CharField()

class Requisicao(BaseModel):
    data = CharField()
    paciente = ForeignKeyField(Paciente)
    medico = ForeignKeyField(Medico)
    
class Exames_requisitados(BaseModel):
    exame = ForeignKeyField(Exame)
    requisicao = ForeignKeyField(Requisicao)

class Enfermeira(BaseModel):
    nome = CharField()
    cod_identificador = IntegerField()
    turno_atuacao = CharField()

class Cirurgia(BaseModel):
    nome_cirurgia = CharField()
    data = CharField()
    medico_atuante = ForeignKeyField(Medico)
    enfermeira = ForeignKeyField(Enfermeira)
    paciente = ForeignKeyField(Paciente)
    setor = ForeignKeyField(Setor)
    duracao = CharField()

class Hospital(BaseModel):
    nome = CharField()
    localizacao = CharField()

if __name__ == "__main__":
    db.connect()
    db.create_tables([Especialidade, Medico, Exame, Requisicao, Exames_requisitados, Enfermeira, Cirurgia, Setor, Hospital, Paciente])


    especialidade1 = Especialidade.create(cod_especialidade = 1, documento = "Conselho de Médicos Gerais (CMG)", desc_especialidade = "Especialista em problemas Respirátorios")
    medico1 = Medico.create(nome = "Dr. Grey", id_medico = 1, salario = 4050.50, especialidade = especialidade1)
    exame1 = Exame.create(preco = 50, prazo_liberacao = 2, nome = "triglicerideos")
    paciente1 =  Paciente.create(nome = "José da Silva Campos Sales Neto Filho", cpf = "111.111.111-11", doenca = "Aids e Hpv")
    requisicao1 = Requisicao.create(data = "10/08/2019", paciente = paciente1, medico = medico1)
    examerequisicao1 = Exames_requisitados.create(exame = exame1, requisicao = requisicao1)
    enfermeira1 = Enfermeira.create(nome = "Helga Pereira Mattos Vargas Pinheiro", cod_identificador = 1, turno_atuacao = "Geral")
    setor1 = Setor.create(nome = "Setor Cirúrgico A1", localizacao = "Prédio A", cor = "Vermelho", tipo_setor = "Cirúrgico")
    cirurgia1 = Cirurgia.create(nome_cirurgia = "Angioplastia Múltipla Invertida pelo método de grayson", data = "24/01/2020", medico_atuante = medico1, enfermeira = enfermeira1, paciente = paciente1, setor = setor1, duracao = "36 horas")
    hospital = Hospital.create(nome = "Grey-Sloan", localizacao = "Avenida Paulista Numero 523")

    json = list(map(model_to_dict, Hospital.select()))

    print(json)