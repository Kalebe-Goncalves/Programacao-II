import numpy as nmp

mensagem = "essa_eh_uma_mensagem_facil12"
mensagem = list(mensagem)
matriz_chave = [[2, 3], [2, 5]]


def converter_mensagem(mensagem):
    mensagem_convertida = []
    valor_convertido = ""
    for valor in mensagem:
        valor_convertido = ord(valor)
        mensagem_convertida.append(valor_convertido)
    return mensagem_convertida


mensagem = converter_mensagem(mensagem)
tamanho = len(mensagem)
primeira_parte = mensagem[0:tamanho // 2]
segunda_parte = mensagem[tamanho // 2:tamanho]
matriz_criptografada = [primeira_parte, segunda_parte]


def multiplicar_matriz(matriz_chave, matriz):
    return nmp.matmul(matriz_chave, matriz).tolist()


matriz_criptografada = multiplicar_matriz(matriz_chave, matriz_criptografada)
print(matriz_criptografada)
