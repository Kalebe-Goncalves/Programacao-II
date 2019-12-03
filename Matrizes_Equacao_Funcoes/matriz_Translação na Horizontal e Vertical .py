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

def rotacionar_y(lista_cordenada):
   lista_nova = []
   for valor in lista_cordenada:
       valor = valor * -1
       valor += 7
       lista_nova.append(valor)
   return lista_nova   

quantidade = int(input("Digite a quantidade de cordenadas: "))
lista_x = passar_cordenadas_x(quantidade)
lista_y = passar_cordenadas_y(quantidade)
valor_soma = int(input("Digite o valor de soma: ")) #Maior Cordenada X - Menor Cordenada X
lista_valores_matriz = [lista_x]

lista_y = rotacionar_y(lista_y)
plt.plot(lista_x, lista_y)
nova_matriz = transformar_cordenadas(valor_soma, lista_x)
lista_valores_matriz.append(nova_matriz)
plt.plot(nova_matriz, lista_y)
nova_matriz = transformar_cordenadas(valor_soma, nova_matriz)
lista_valores_matriz.append(nova_matriz)
plt.plot(nova_matriz, lista_y)
nova_matriz = transformar_cordenadas(valor_soma, nova_matriz)
lista_valores_matriz.append(nova_matriz)
plt.plot(nova_matriz, lista_y)
valor_soma = int(input("Digite o valor soma y: "))
nova_matriz = transformar_cordenadas(valor_soma, lista_y)   
for valor in lista_valores_matriz:
   plt.plot(valor, nova_matriz)
nova_matriz = transformar_cordenadas(valor_soma, nova_matriz)
for valor in lista_valores_matriz:
   plt.plot(valor, nova_matriz)
nova_matriz = transformar_cordenadas(valor_soma, nova_matriz)
matriz_y_3 = nova_matriz
for valor in lista_valores_matriz:
   plt.plot(valor, nova_matriz)

print("MATRIZ X:", lista_valores_matriz[3])
print("MATRIZ Y", matriz_y_3)


plt.axis([0, 32, 0, 32])
plt.show()
