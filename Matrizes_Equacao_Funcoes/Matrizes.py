import pygame as pg

pg.init()

def salvar_cordenadas(quantidade):
    lista_de_cordenadas = []
    for quantidade in range(0, quantidade):
        posicao_x = float(input("Digite posição x: "))
        posicao_y = float(input("Digite posição y: "))
        cordenada = (posicao_x, posicao_y)
        lista_de_cordenadas.append(cordenada)
    return lista_de_cordenadas 

quantidade = int(input("Digite a quantidade: "))
lista_cordenadas = salvar_cordenadas(quantidade)


size = widht, height = 50, 30
white = 255,255,255
black = 0,0,0

screen = pg.display.set_mode(size)

tempo = pg.time.Clock()
fim = False

while not fim:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
    

    screen.fill(black)
    pg.draw.lines(screen, white, False, lista_cordenadas, 5)
    pg.display.update()