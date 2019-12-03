import matplotlib.pyplot as plt

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


quantidade = int(input("Digite a quantidade de cordenadas: "))

for valor in range(0,16):
    plt.plot(passar_cordenadas_x(quantidade), passar_cordenadas_y(quantidade))

plt.axis([0, 32, 0, 32])
plt.show()