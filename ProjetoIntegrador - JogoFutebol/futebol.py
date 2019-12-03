import pygame as pg
import time as t

pg.init()

#Calculo Distancia
def distancia(x,y,x2,y2):
    distancia = (((x-x2)**2)+((y-y2)**2)**(1/2))
    return distancia

size = widht, height = 840, 500

#Cores
black = 0,0,0
white = 255,255,255
green = 0, 128, 0
blue = 0, 0, 255

#Posicoes
inicio_linha = 0,500
fim_linha = 840, 500

inicio_linha2 = 0, 500
fim_linha2 = 0, 0

inicio_linha3 = 840, 0
fim_linha3 = 840, 840

x_bola = 420
y_bola = 480

x_jogador1 = 180
y_jogador1 = 440
x_pe_jogador1 = 180
y_pe_jogador1 = 480

x_jogador2 = 680
y_jogador2 = 440
x_pe_jogador2 = 680
y_pe_jogador2 = 480


#Imagens
bola = pg.image.load('bola_futebol.png')
background = pg.image.load('PI.jpg')
"""
jogador1 = pg.image.load('jogador_1.png')
jagador2 = pg.image.load('jogador_2.png')
"""
screen = pg.display.set_mode(size)

tempo = pg.time.Clock()
tempo.tick(120)
fim = False

while not fim:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_jogador2 -= 10
                x_pe_jogador2 -= 10
            if event.key == pg.K_RIGHT:
                x_jogador2 += 10
                x_pe_jogador2 += 10
            if event.key == pg.K_UP: #arrumar gravidade
                y_jogador2 -= 30
                y_pe_jogador2 -= 30
            if event.key == pg.K_a:
                x_jogador1 -= 10
                x_pe_jogador1 -= 10
            if event.key == pg.K_d:
                x_jogador1 += 10
                x_pe_jogador1 += 10
            if event.key == pg.K_w: #arrumar gravidade
                y_jogador1 -= 30
                y_pe_jogador1 -= 30
        pg.display.update()

    if x_jogador1 <= 20:
        x_jogador1 += 10
        x_pe_jogador1 += 10
    
    if x_jogador2 >= 820:
        x_jogador2 -= 10
        x_pe_jogador2 -= 10
   
    if distancia(x_jogador1 , y_jogador1, x_bola, y_bola) < 150 and y_pe_jogador1 == y_bola: #colisao em baixo
        for valor in range(0,11):
            x_bola += 1
    if distancia(x_jogador2, y_jogador2, x_bola, y_bola) < 150 and y_pe_jogador2 == y_bola:
        for valor in range(0,11):
            x_bola -= 1

    if distancia(x_jogador1, y_jogador1, x_jogador2, y_jogador2) <= 3400 and y_jogador1 == y_jogador2:
        x_jogador1 -= 10
        x_pe_jogador1 -= 10
    if distancia(x_jogador2, y_jogador2, x_jogador1, y_jogador1) <= 3400 and y_jogador2 == y_jogador1:
        x_jogador2 += 10
        x_pe_jogador2 += 10
    if distancia(x_bola, y_bola, 840, 800) <= 906:
        print("GOL jogador 2")
        break
    if distancia(x_bola, y_bola, 0, 40) <= 434:
        print("GOL jogador 1")    
        break

            
    

    screen.fill(black)
    screen.blit(bola, [x_bola, y_bola])
    """
    screen.blit(jogador1, [x_jogador1, y_jogador1])
    screen.blit(jagador2, [x_jogador2, y_jogador2])
    """
    pg.draw.circle(screen, blue, (x_jogador1, y_jogador1), 30)
    pg.draw.circle(screen, blue, (x_pe_jogador1, y_pe_jogador1), 10)
    pg.draw.circle(screen, green, (x_jogador2, y_jogador2), 30) 
    pg.draw.circle(screen, green, (x_pe_jogador2, y_pe_jogador2), 10)   
    pg.draw.line(screen, white, inicio_linha, fim_linha, 5) #linha_baixo
    pg.draw.line(screen, white, inicio_linha2, fim_linha2, 20) #linha_esquerda
    pg.draw.line(screen, white, inicio_linha3, fim_linha3, 20) #linha_direita

    
