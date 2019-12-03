import matplotlib.pyplot as plt
import numpy as num
import os

def funcao_seno(a, b, c, d, x):
    return a*num.sin(b*x+c)+d
    

def funcao_cosseno(a, b, c, d, x):
    return a*num.cos(b*x+c)+d

def funcao_tangente(a, b, c, d, x):
    return a*num.tan(b*x+c)+d

def limpar_tela(valor = 0):
    os.system('clear') 


if __name__== "__main__":
    #limpar_tela
    limpar_tela()

    #valores 
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    d = float(input("Digite o valor de d: "))
    opcao = input("Digite a T para tangente ou qualquer coisa para outra coisa: ")
    pi = num.pi

    #coordenadas
    x = num.arange(0.0, 2*(4*num.pi/b), 0.2)
    valor_y_seno = funcao_seno(a, b, c, d, x)
    valor_y_cosseno = funcao_cosseno(a, b, c, d, x)
    valor_y_tangente = funcao_tangente(a, b, c, d, x)

    #parte gráfica Tangente
    if opcao.upper() == "T":

        valor_y_tangente = funcao_tangente(a, b, c, d, x)
        fig, ax = plt.subplots()
        ax.plot(x, valor_y_tangente, color='orange', marker='None')
        ax.grid(True, color='green', linestyle='--')
        print('O maior valor de tangente é:', num.max(valor_y_tangente))
        print('O maior valor de tangente é:', num.min(valor_y_tangente))
        

        plt.show()  

    #parte gráfica Seno e Cosseno
    else:

        fig, ax = plt.subplots()
        ax.plot(x, valor_y_seno, color='red', marker='None')
        ax.plot(x, valor_y_cosseno, color='blue', marker='None')
        ax.grid(True, color='green', linestyle='--') 
        print('O maior valor de seno é:', num.max(valor_y_seno))
        print('O menor valor de seno é:', num.min(valor_y_seno))
        print('O maior valor de cosseno é:', num.max(valor_y_cosseno))
        print('O menor valor de cosseno é:', num.min(valor_y_cosseno))

        plt.show()