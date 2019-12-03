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

def transformar_cordenadas(valor_soma, lista_cordenadas):
   lista_nova = []
   for valor in lista_cordenadas:
       valor += valor_soma
       lista_nova.append(valor)
   return lista_nova

def rotacionar(lista_cordenada):
   lista_nova = []
   for valor in lista_cordenada:
       valor = valor * -1
       valor += 7
       lista_nova.append(valor)
   return lista_nova

def rotacionar_y(lista_cordenada):
   lista_nova = []
   for valor in lista_cordenada:
       valor = valor * -1
       valor += 14
       lista_nova.append(valor)
   return lista_nova


quantidade = int(input("Digite a quantidade de cordenadas: "))
lista_x = passar_cordenadas_x(quantidade)
lista_x = rotacionar(lista_x)
lista_y = passar_cordenadas_y(quantidade)
valor_soma = int(input("Digite o valor de soma: ")) #Maior Cordenada X - Menor Cordenada X
valor_soma_y = int(input("Digite o valor de soma: ")) #Maior Cordenada Y - Menor Cordenada Y

lista_valores_matriz = []
lista_valores_matriz_y = []


plt.plot(lista_x, lista_y)

nova_matriz_y = rotacionar_y(lista_y)
nova_matriz_x = rotacionar(lista_x)
plt.plot(nova_matriz_x, nova_matriz_y)

matriz = transformar_cordenadas(2*valor_soma_y, lista_y)
plt.plot(lista_x, matriz)

matriz = transformar_cordenadas(2*valor_soma_y, nova_matriz_y)
plt.plot(nova_matriz_x, matriz)

nova_matriz_x_2 = transformar_cordenadas(valor_soma, lista_x)
nova_matriz_y_2 = transformar_cordenadas(valor_soma_y, lista_y)
plt.plot(nova_matriz_x_2, nova_matriz_y_2)

nova_matriz_x = transformar_cordenadas(valor_soma, nova_matriz_x)
nova_matriz_y = transformar_cordenadas(valor_soma_y, nova_matriz_y)
plt.plot(nova_matriz_x, nova_matriz_y)


nova_matriz_x_2 = transformar_cordenadas(valor_soma, nova_matriz_x_2)
nova_matriz_y_2 = transformar_cordenadas(valor_soma_y, nova_matriz_y_2)
plt.plot(nova_matriz_x_2, nova_matriz_y_2)
lista_valores_matriz.append(nova_matriz_x_2)
lista_valores_matriz_y.append(nova_matriz_y_2)

nova_matriz_x = transformar_cordenadas(valor_soma, nova_matriz_x)
nova_matriz_y = transformar_cordenadas(valor_soma_y, nova_matriz_y)
plt.plot(nova_matriz_x, nova_matriz_y)

nova_matriz_x_2 = transformar_cordenadas(valor_soma, nova_matriz_x_2)
nova_matriz_y_2 = transformar_cordenadas(valor_soma_y, nova_matriz_y_2)
plt.plot(nova_matriz_x_2, nova_matriz_y_2)
lista_valores_matriz.append(nova_matriz_x_2)
lista_valores_matriz_y.append(nova_matriz_y_2)

nova_matriz_x = transformar_cordenadas(valor_soma, nova_matriz_x)
nova_matriz_y = transformar_cordenadas(valor_soma_y, nova_matriz_y)
plt.plot(nova_matriz_x, nova_matriz_y)

nova_matriz_y = rotacionar(lista_y)
nova_matriz_y = transformar_cordenadas(valor_soma*3, lista_y)
nova_matriz_x = transformar_cordenadas(valor_soma, lista_x)
plt.plot(nova_matriz_x, nova_matriz_y)

matriz_x_1 = lista_x
matriz_x_1 = rotacionar(matriz_x_1)
matriz_y_1 = rotacionar(lista_y)
plt.plot(transformar_cordenadas(valor_soma, matriz_x_1), matriz_y_1)

nova_matriz_x = rotacionar(lista_x)
nova_matriz_x = transformar_cordenadas(valor_soma*2, lista_x)
plt.plot(nova_matriz_x, lista_y)


nova_matriz_y = rotacionar_y(lista_y)
nova_matriz_x = rotacionar(lista_x)
plt.plot(transformar_cordenadas(valor_soma*2, nova_matriz_x), nova_matriz_y)

matriz_y = transformar_cordenadas(valor_soma_y, lista_y)
matriz_x = transformar_cordenadas(3*valor_soma, lista_x)
plt.plot(matriz_x, matriz_y)

matriz_y_1 = rotacionar(lista_y)
matriz_x_1 = rotacionar(lista_x)
matriz_x_1 = transformar_cordenadas(3*valor_soma, matriz_x_1)
plt.plot(matriz_x_1, matriz_y_1)


matriz_y_1 = rotacionar_y(lista_y)
matriz_y_1 = transformar_cordenadas(valor_soma_y, matriz_y_1)
matriz_x_1 = rotacionar(lista_x)
matriz_x_1 = transformar_cordenadas(3*valor_soma, matriz_x_1)
plt.plot(matriz_x_1, matriz_y_1)


print("MATRIX X:", lista_valores_matriz[0])
print("MATRIX Y:", lista_valores_matriz_y[0])
print("MATRIX X:", lista_valores_matriz[1])
print("MATRIX Y:", lista_valores_matriz_y[1])


plt.axis([0, 28, 0, 28])
plt.show()
