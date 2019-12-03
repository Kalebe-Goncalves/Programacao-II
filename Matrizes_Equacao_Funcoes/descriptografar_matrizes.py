import numpy as nmp

mensagem = [532,	575,	521,	503,	493,	529,	493,	496,	525,	515,	509,	514,	365,	352,
752,	805,	715,	709,	695,	747,	683,	700,	719,	713,	719,	730,	463,	452]
matriz_chave = [[2,3],[2,5]]
matriz_chave_inversa = nmp.linalg.inv(nmp.asarray(matriz_chave, dtype = nmp.float32)).tolist()
print(matriz_chave_inversa)

def converter_mensagem(mensagem):
  mensagem_convertida = []
  valor_convertido = ""
  for valor in mensagem:
    valor_convertido = chr(valor)
    mensagem_convertida.append(valor_convertido)
  return mensagem_convertida

def multiplicar_matriz(matriz_chave_inversa, matriz):
  return nmp.matmul(matriz_chave_inversa, matriz).tolist()

def converter_inteiro(matriz_descriptografada):
  primeira_linha = matriz_descriptografada[0]
  segunda_linha = matriz_descriptografada[1]
  primeira_linha_int = []
  segunda_linha_int = []
  matriz_descriptografada = []
  for valor in primeira_linha:
    primeira_linha_int.append(int(valor))
  for valor in segunda_linha:
    segunda_linha_int.append(int(valor))
  matriz_descriptografada.append(primeira_linha_int)
  matriz_descriptografada.append(segunda_linha_int)
  return matriz_descriptografada

tamanho = len(mensagem)
primeira_parte = mensagem[0:tamanho//2]
segunda_parte = mensagem[tamanho//2:tamanho]
matriz_descriptografada = [primeira_parte, segunda_parte]
matriz_descriptografada = multiplicar_matriz(matriz_chave_inversa, matriz_descriptografada)
matriz_descriptografada = converter_inteiro(matriz_descriptografada)
print(matriz_descriptografada)

#mensagem em texto
mensagem = converter_mensagem(matriz_descriptografada[0])
mensagem_completa = []
mensagem_completa.append(mensagem)
mensagem = converter_mensagem(matriz_descriptografada[1])
mensagem_completa.append(mensagem)
print(mensagem_completa)
