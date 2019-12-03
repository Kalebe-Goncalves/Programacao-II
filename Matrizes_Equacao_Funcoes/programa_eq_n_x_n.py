import numpy as np
import os

class Equacao(object):
    def __init__ (self, quantidade_equacoes, quantidade_variaveis):
        self.quant_eq = quantidade_equacoes
        self.lista = [] 
        self.lista_eq = []
        self.lista_eq_res = []
        self.quant_var = quantidade_variaveis

    def informar_valores(self):
        for valor in range(1, self.quant_eq+1):
            for valor1 in range(0, self.quant_var):
                self.valor = float(input("Valor da variavel " + str(valor) + " da equacao: "))
                self.lista.append(self.valor)
            self.lista_eq.append(self.lista)
            self.lista = []
            self.valor_y = float(input("Resultado da " + str(valor) + " equacao: "))
            self.equacao_resultado = [self.valor_y]
            self.lista_eq_res.append(self.equacao_resultado)

    def calcular_equacoes(self):
        self.valor = np.array(self.lista_eq)
        self.valor2 = np.array(self.lista_eq_res)
        try:
            self.resu = np.linalg.solve(self.valor, self.valor2)
            for i in self.resu:
                print(i)
        except np.linalg.linalg.LinAlgError:
            print("SI")

    def main(self):
        self.informar_valores()
        self.calcular_equacoes()

if __name__ == "__main__":
    os.system('clear')
    quantidade_equacoes = int(input("Digite a quantidade de equações: "))
    quantidade_var  = int(input("Digite a quantidade de variaveis: "))
    equacao = Equacao(quantidade_equacoes, quantidade_var)
    equacao.main()
