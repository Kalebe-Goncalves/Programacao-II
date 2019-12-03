import arcade
import math
import os
import random
from bd_pontuacao import criar_pontuacao

COMPRIMENTO_TELA = 800
ALTURA_TELA = 600
TITULO = "War Space"

class TurningSprite(arcade.Sprite):

    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class BulletSprite(TurningSprite):

    def update(self):
        super().update()
        if self.center_y > 800:
            self.kill()


class Jogo(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        caminho = os.path.dirname(os.path.abspath(__file__))
        os.chdir(caminho)

        arcade.set_background_color(arcade.color.BLACK)

        self.set_mouse_visible(False)

        self.frame_count = 0
        self.tempo = 0
        self.minutos = int(self.tempo) // 60
        self.segundos = int(self.tempo) % 60
        self.usuario = "Kalebe"
        self.pontuacao = 0
        
        self.vida = 100
        self.vida_extra = False
        self.dano_tiro = 5
        self.fim = False
        self.dificuldade = True
        self.vel_tiro_u = 6
        self.vel_tiro_i = 6
        self.q_inimigos = 1
        self.colisao = False
        self.vel_inimigo = 5
        self.img_player = 0
        self.quant_tiros = 1
        self.val_pontos = 20

        self.background = None
        self.lista_de_inimigos = None
        self.lista_de_tiros = None
        self.lista_de_players = None
        self.lista_de_tiros_player = None
        self.player = None
        self.lista_pos = []
        self.lista_imagens_player = ["Imagens/Player_ship.png", "Imagens/Player_ship2.png", "Imagens/Player_ship3.png", "Imagens/Player_ship4.png", "Imagens/Player_ship5.png", "Imagens/Player_ship6.png", "Imagens/Player_ship7.png", "Imagens/Player_ship8.png"]

        self.som_tiro = arcade.load_sound("sounds/laser1.wav")
        self.som_melhoria = arcade.load_sound("sounds/phaseJump1.wav")
        self.som_kill = arcade.load_sound("sounds/hit.wav")
        self.musica_fundo = arcade.load_sound("sounds/musica_fundo.mp3")

    def gerar_tiro(self):
        tiro = BulletSprite("Imagens/laserBlue01.png")

        tiro.change_y = math.cos(math.radians(
            self.player.angle)) * self.vel_tiro_u
        tiro.change_x = - \
            math.sin(math.radians(self.player.angle)) * self.vel_tiro_u

        tiro.center_x = self.player.center_x
        if self.quant_tiros == 2:
            tiro.center_x = self.player.center_x - 10
        tiro.center_y = self.player.center_y
        tiro.update()

        arcade.play_sound(self.som_tiro)
        self.lista_de_tiros_player.append(tiro)
        if self.quant_tiros == 2:
            tiro2 = BulletSprite("Imagens/laserBlue01.png")

            tiro2.change_y = math.cos(math.radians(
                self.player.angle)) * self.vel_tiro_u
            tiro2.change_x = - \
                math.sin(math.radians(self.player.angle)) * self.vel_tiro_u

            tiro2.center_x = self.player.center_x + 10
            tiro2.center_y = self.player.center_y 
            tiro2.update()

            self.lista_de_tiros_player.append(tiro2)
            if self.quant_tiros == 3:
                tiro3 = BulletSprite("Imagens/laserBlue01.png")

                tiro3.change_y = math.cos(math.radians(
                    self.player.angle)) * self.vel_tiro_u
                tiro3.change_x = - \
                    math.sin(math.radians(self.player.angle)) * self.vel_tiro_u

                tiro3.center_x = self.player.center_x - 10
                tiro3.center_y = self.player.center_y 
                tiro3.update()

                self.lista_de_tiros_player.append(tiro3)

    def gerar_pos_x(self, inimigo):
        if inimigo.center_x not in self.lista_pos:
            inimigo.center_x = random.randint(50, 750)
            pos_diferente = inimigo.center_x
            for pos in self.lista_pos:
                condicao = inimigo.center_x <= pos + 40 and inimigo.center_x >= pos - 40
                while condicao:
                    inimigo.center_x = random.randint(20, 780)
                    condicao = inimigo.center_x <= pos + 40 and inimigo.center_x >= pos - 40
            pos_diferente = inimigo.center_x
        self.lista_pos.append(pos_diferente)

    def gerar_inimigos(self):
        inimigo = arcade.Sprite("Imagens/enemy_ship.png", 0.5)
        inimigo.center_y = ALTURA_TELA - inimigo.height
        inimigo.angle = 180
        inimigo.center_x = 0
        self.gerar_pos_x(inimigo)
        self.lista_de_inimigos.append(inimigo)
        return self.lista_de_inimigos

    def verificar_fim(self):
        if self.vida_extra:
            self.vida = 100
        if self.vida <= 0 or self.colisao:
            self.fim = True
            lista = criar_pontuacao(self.usuario, str(self.pontuacao), self.mostrar_tempo.split("Tempo: ")[1])
            for i in lista:
                print(i)
            arcade.close_window()

    def aumentar_dificuldade(self):
        if self.pontuacao %200 == 0:
            self.vel_tiro_i += 0.5
            self.dano_tiro += 1
            self.vel_inimigo += 1
        if self.pontuacao %500 == 0:
            self.q_inimigos += 1
            self.melhoria_nave()
        self.dificuldade = False   

    def melhoria_nave(self):
        arcade.play_sound(self.som_melhoria)
        self.img_player += 1
        self.player = arcade.Sprite(self.lista_imagens_player[self.img_player], 0.5)
        self.player.center_x = COMPRIMENTO_TELA/2
        self.player.center_y = ALTURA_TELA/2
        self.lista_de_players[0].kill()
        self.lista_de_players.append(self.player)
        if self.img_player == 1:
            self.vel_tiro_u += 1
            self.vida = 100
        elif self.img_player == 2:
            self.vel_tiro_u += 1
            self.vida = 100
        elif self.img_player == 3:
            self.vel_tiro_u += 1
            self.vida = 100
            self.quant_tiros = 2
        elif self.img_player == 4:
            self.vida = 100
            self.quant_tiros = 1
        elif self.img_player == 5:
            self.vida = 100
        elif self.img_player == 6:
            self.vel_tiro_u += 1
            self.vida = 100
            self.val_pontos += 10
        elif self.img_player == 7:
            self.vel_tiro_u += 1
            self.vida = 100
            self.quant_tiros = 3
            self.vida_extra = True


    def configurar_jogo(self):

        self.lista_de_inimigos = arcade.SpriteList()
        self.lista_de_tiros = arcade.SpriteList()
        self.lista_de_players = arcade.SpriteList()
        self.lista_de_tiros_player = arcade.SpriteList()

        self.player = arcade.Sprite(self.lista_imagens_player[self.img_player], 0.5)
        self.lista_de_players.append(self.player)
        self.lista_de_inimigos = self.gerar_inimigos()
        #arcade.play_sound(self.musica_fundo)


    def on_draw(self):

        arcade.start_render()
        self.minutos = int(self.tempo) // 60
        self.segundos = int(self.tempo) % 60

        self.lista_de_inimigos.draw()
        self.lista_de_tiros.draw()
        self.lista_de_players.draw()
        self.lista_de_tiros_player.draw()

        self.mostrar_tempo = f"Tempo: {self.minutos:02d}:{self.segundos:02d}"
        arcade.draw_text(self.mostrar_tempo, 655, 582, arcade.color.WHITE, 15)
        mostrar_pontuacao = f"Pontos: {self.pontuacao}"
        arcade.draw_text(mostrar_pontuacao, 20, 20, arcade.color.WHITE, 20)
        arcade.draw_rectangle_filled(
            COMPRIMENTO_TELA-50, 10, self.vida, 20, arcade.color.GREEN)
        vida = f"{self.vida}%"
        arcade.draw_text(vida, COMPRIMENTO_TELA-60, 5, arcade.color.RED)
        if self.vida_extra:
            arcade.draw_triangle_filled(
                COMPRIMENTO_TELA-5, 25, COMPRIMENTO_TELA-25, 25, COMPRIMENTO_TELA-15, 40, arcade.color.YELLOW)
        
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player.center_x = x
        self.player.center_y = y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.gerar_tiro()

    def update(self, delta_time):
        if not self.fim:
            self.frame_count += 2
            self.tempo += delta_time

            for inimigo in self.lista_de_inimigos:

                start_x = inimigo.center_x
                start_y = inimigo.center_y

                dest_x = self.player.center_x
                dest_y = self.player.center_y

                x_diff = dest_x - start_x
                y_diff = dest_y - start_y

                angle = math.atan2(y_diff, x_diff)

                inimigo.angle = math.degrees(angle)-90

                if self.frame_count % 60 == 0:
                    tiro = arcade.Sprite("Imagens/laserBlue01.png")

                    tiro.center_x = start_x
                    tiro.center_y = start_y

                    tiro.angle = math.degrees(angle)

                    tiro.change_x = math.cos(angle) * self.vel_tiro_i
                    tiro.change_y = math.sin(angle) * self.vel_tiro_i

                    self.lista_de_tiros.append(tiro)
                    inimigo.center_y -= self.vel_inimigo
                    if inimigo.center_y <= inimigo.height - 10:
                        self.colisao = True

            for tiro in self.lista_de_tiros:
                dano = arcade.check_for_collision_with_list(
                    tiro, self.lista_de_players)
                if dano:
                    self.vida -= self.dano_tiro
                    tiro.kill()
                if tiro.top < 0:
                    tiro.kill()

            for tiro_jog in self.lista_de_tiros_player:
                dano_inimigo = arcade.check_for_collision_with_list(
                    tiro_jog, self.lista_de_inimigos)
                dano_inimigo2 = arcade.check_for_collision_with_list(
                    tiro_jog, self.lista_de_inimigos)
                if dano_inimigo:
                    for inimigo in dano_inimigo2:
                        inimigo.kill()
                        tiro_jog.kill()
                        arcade.play_sound(self.som_kill)
                        self.pontuacao += self.val_pontos

            self.lista_de_tiros.update()
            self.lista_de_tiros_player.update()
            self.verificar_fim()
            if len(self.lista_de_inimigos) == 0:
                self.lista_pos = []
                for i in range(0, self.q_inimigos):
                    self.gerar_inimigos()
            if self.pontuacao % 100 == 0 and self.dificuldade and self.pontuacao != 0:
                self.aumentar_dificuldade()
            if self.pontuacao % 100 != 0 and not self.dificuldade:
                self.dificuldade = True

def main():
    window = Jogo(COMPRIMENTO_TELA, ALTURA_TELA, TITULO)
    window.configurar_jogo()
    arcade.run()

if __name__ == "__main__":
    main()