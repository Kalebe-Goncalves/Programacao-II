import matplotlib.pyplot as plt

"""
INFORMACOES IMPORTANTES
Ao informar o número de coordenadas é necessário informar uma a mais, esta seria repetir o valor da primeira coordenada
x[0 7 7 4 5 6 6 3 4 3]
y[7 7 0 3 4 3 6 6 5 4]
neste exemplo a primeira coordenada é o 0 para x e esta será repetida, ou seja na quantidade neste exemplo será passado 11
"""


def passar_cordenadas_x(quantidade):
   lista_cordenadas_x = []
   for valor in range(0,quantidade):
       cordenada_x = int(input("Digite o valor da cordenada x: "))
       lista_cordenadas_x.append(cordenada_x)
   return lista_cordenadas_x

def passar_cordenadas_y(quantidade):
   lista_cordenadas_y = []
   for valor in range(0,quantidade):
       cordenada_y = int(input("Digite o valor da cordenada y: "))
       lista_cordenadas_y.append(cordenada_y)
   return lista_cordenadas_y

def rotacionar_matriz(lista):
   lista_transformada = []
   for valor in lista:
       valor = valor * -1
       lista_transformada.append(valor)
   return lista_transformada

def multiplicar(valor_soma, lista_x):
   lista_x_transformada = []
   for valor in lista_x:
       valor += valor_soma
       lista_x_transformada.append(valor)
   return lista_x_transformada


quantidade = int(input("Digite a quantidade de cordenadas: "))
lista_x = passar_cordenadas_x(quantidade)
lista_y = passar_cordenadas_y(quantidade)
valor_soma = int(input("Digite o valor soma: ")) #Maior Cordenada X - Menor Cordenada X
valor_soma_y = int(input("Digite o valor de soma: ")) #Maior Cordenada Y - Menor Cordenada Y

lista = []
lista.append(lista_x)
lista_repetida = []
lista_repetida_y = []
lista_valores_matriz = []
lista_valores_matriz_y = []

plt.plot(lista_x, lista_y)
lista_repetida.append(lista_x)
lista_repetida_y.append(lista_y)
lista_nova_x = rotacionar_matriz(lista_x)
lista_nova_x = multiplicar(2*valor_soma, lista_nova_x)
lista.append(lista_nova_x)


plt.plot(lista_nova_x, lista_y)
lista_repetida.append(lista_nova_x)

for valor in lista:
   lista_nova_y = rotacionar_matriz(lista_y)
   lista_nova_y = multiplicar(2*valor_soma_y, lista_nova_y)
   plt.plot(valor, lista_nova_y)
   lista_repetida.append(valor)
   lista_repetida_y.append(lista_nova_y)

for valor in lista_repetida_y:
   for valor_2 in lista_repetida:
       valor_2 = multiplicar(valor_soma*2 ,valor_2)
       plt.plot(valor_2, valor)

for valor in lista_repetida_y:
   valor = multiplicar(valor_soma_y*2, valor)
   for valor_2 in lista_repetida:
       plt.plot(valor_2, valor)

for valor in lista_repetida_y:
   valor = multiplicar(valor_soma_y*2, valor)
   for valor_2 in lista_repetida:
       valor_2 = multiplicar(valor_soma*2, valor_2)
       plt.plot(valor_2, valor)
       lista_valores_matriz.append(valor_2)
   lista_valores_matriz_y.append(valor)


print("MATRIX X:", lista_valores_matriz[0])
print("MATRIX Y:", lista_valores_matriz_y[0])
print("MATRIX X:", lista_valores_matriz[1])
print("MATRIX Y:", lista_valores_matriz_y[0])
print("MATRIX X:", lista_valores_matriz[2])
print("MATRIX Y:", lista_valores_matriz_y[2])
print("MATRIX X:", lista_valores_matriz[3])
print("MATRIX Y:", lista_valores_matriz_y[2])

plt.axis([0, 32, 0, 32])
plt.show()
