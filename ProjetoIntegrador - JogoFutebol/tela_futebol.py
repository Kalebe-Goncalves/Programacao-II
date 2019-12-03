import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame as pg
import time as t

class JanelaTimes(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Selecao de Times", resizable=False)

        self.jogar = False
        self.lista_jogadores = []
        self.set_default_size(500, 300)
        self.set_border_width(50)
        self.h_box0 = Gtk.HBox(spacing=20)
        self.h_box1 = Gtk.HBox(spacing=20)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        times = Gtk.ListStore(str)
        countries = ["TEAMSchlei","TEAMKleber","TEAMFelipera","TEAMLopes"]
        for country in countries:
            times.append([country])

        country_combo = Gtk.ComboBox.new_with_model(times)
        country_combo.connect("changed", self.on_country_combo_changed)
        renderer_text = Gtk.CellRendererText()
        country_combo.pack_start(renderer_text, True)
        country_combo.add_attribute(renderer_text, "text", 0)
        self.h_box0.pack_start(country_combo, True, True, 0)

        times = Gtk.ListStore(str)
        countries = ["TEAMSchlei","TEAMKleber","TEAMFelipera","TEAMLopes"]
        for country in countries:
            times.append([country])

        country_combo2 = Gtk.ComboBox.new_with_model(times)
        country_combo2.connect("changed", self.on_country_combo_changed)
        renderer_text = Gtk.CellRendererText()
        country_combo2.pack_end(renderer_text, True)
        country_combo2.add_attribute(renderer_text, "text", 0)
        self.h_box0.pack_end(country_combo2, True, True, 0)


        self.b1 = Gtk.Button(label="        Jogar       ")
        self.b1.connect("clicked", self.iniciar_jogo)
        self.h_box1.pack_end(self.b1, False, True, 0)
        vbox.add(self.h_box0)
        vbox.add(self.h_box1)
        self.add(vbox)
        

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            team = model[tree_iter][0]
            self.team = team
            self.lista_jogadores.append(self.team)
            print("Selected: Team=%s" % team)

    def iniciar_jogo(self, widget):
        if self.jogar is False:
            pg.init()
            pg.key.set_repeat(1,50)
            pg.display.set_caption("Soccer Bauu")

            #Calculo Distancia
            def distancia(x,y,x2,y2):
                distancia = (((x-x2)**2)+((y-y2)**2)**(1/2))
                return distancia

            def texto(mensagem, cor, tamanho, pos_x, pos_y):
                font = pg.font.SysFont(None, tamanho, 4)
                texto = font.render(mensagem, True, cor)
                screen.blit(texto, [pos_x, pos_y])

            size = widht, height = 840, 500

            #Cores
            black = 0,0,0
            white = 255,255,255
            green = 0, 128, 0
            blue = 0, 0, 255
            grey = 160, 160, 160
            wood = 216,216,191
            red = 255,0,0

            #Posicoes
            inicio_linha = 0,500
            fim_linha = 840, 500

            inicio_linha2 = 0, 500
            fim_linha2 = 0, 0

            inicio_linha3 = 840, 0
            fim_linha3 = 840, 840

            inicio_linha4 = 420,69
            fim_linha4 = 420,20

            x_bola = 420
            y_bola = 480

            x_jogador1 = 120
            y_jogador1 = 415
            x_pe_jogador1 = 145
            y_pe_jogador1 = 480

            x_jogador2 = 720
            y_jogador2 = 415
            x_pe_jogador2 = 750
            y_pe_jogador2 = 480

            gol_jogador_1 = 0
            gol_jogador_2 = 0

            x_placar = 320
            y_placar = 20
            tamanho_placar = [200, 50]

            pos_x_jog1 = 380
            pos_y_jog1 = 30

            pos_x_jog2 = 433
            pos_y_jog2 = 30

            #Imagens
            lista_jogadores = {"TEAMSchlei":"SCHLEI.png","TEAMLopes":"LOPES.png","TEAMKleber":"KALEBE.png","TEAMFelipera":"FELIPE.png"}                   
            bola = pg.image.load('bola_futebol.png')
            background = pg.image.load('PI.jpg')
            jogador1 = pg.image.load(lista_jogadores[self.lista_jogadores[0]])
            jogador2 = pg.image.load(lista_jogadores[self.lista_jogadores[1]])
                    
    
            jogador1 = pg.transform.scale(jogador1,(60,60))
            jogador2 = pg.transform.scale(jogador2,(60,60))
            background = pg.transform.scale(background,(840,500))
            screen = pg.display.set_mode(size)

            tela_x = 0
            tela_y = 0
            dx = -tela_x
            dy = -tela_y

            tempo = pg.time.Clock()
            tempo.tick(120)
            fim = False

            while not fim:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                    if event.type == pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_LEFT]:
                            x_jogador2 -= 10
                            x_pe_jogador2 -= 10
                        if keys[pg.K_RIGHT]:
                            x_jogador2 += 10
                            x_pe_jogador2 += 10
                        """
                        if event.key == pg.K_UP: #arrumar gravidade
                            y_jogador2 -= 30
                            y_pe_jogador2 -= 30
                        """
                        if keys[pg.K_a]:
                            x_jogador1 -= 10
                            x_pe_jogador1 -= 10
                        if keys[pg.K_d]:
                            x_jogador1 += 10
                            x_pe_jogador1 += 10
                        """
                        if event.key == pg.K_w: #arrumar gravidade
                            y_jogador1 -= 30
                            y_pe_jogador1 -= 30
                        """
                
                pg.display.update()

                if x_jogador1 <= 5:
                    x_jogador1 += 10
                    x_pe_jogador1 += 10
                
                if x_jogador2 >= 775:
                    x_jogador2 -= 10
                    x_pe_jogador2 -= 10

                if distancia(x_jogador1 , y_jogador1, x_bola, y_bola) < 901 and y_pe_jogador1 == y_bola: #colisao em baixo
                    for valor in range(0,11):
                        x_bola += 1
                if distancia(x_jogador2, y_jogador2, x_bola, y_bola) < 101 and y_pe_jogador2 == y_bola:
                    for valor in range(0,11):
                        x_bola -= 1

                if distancia(x_jogador1, y_jogador1, x_jogador2, y_jogador2) <= 3400 and y_jogador1 == y_jogador2:
                    x_jogador1 -= 10
                    x_pe_jogador1 -= 10
                if distancia(x_jogador2, y_jogador2, x_jogador1, y_jogador1) <= 3400 and y_jogador2 == y_jogador1:
                    x_jogador2 += 10
                    x_pe_jogador2 += 10
                if distancia(x_bola, y_bola, 840, 800) <= 906: #arrumar posicoes iniciais
                    gol_jogador_1 += 1
                    x_jogador1 = 120
                    y_jogador2 = 415
                    x_pe_jogador1 = 150
                    y_pe_jogador1 = 480
                    x_jogador2 = 680
                    y_jogador2 = 440
                    x_pe_jogador2 = 680
                    y_pe_jogador2 = 480
                    x_bola = 420
                    y_bola = 480
                if distancia(x_bola, y_bola, 0, 40) <= 434: #arrumar posicoes iniciais
                    gol_jogador_2 += 1
                    x_jogador1 = 620
                    y_jogador2 = 415
                    x_pe_jogador1 = 180
                    y_pe_jogador1 = 480
                    x_jogador2 = 680
                    y_jogador2 = 440
                    x_pe_jogador2 = 680
                    y_pe_jogador2 = 480
                    x_bola = 420
                    y_bola = 480
  
            
                screen.blit(background, (dx,dy))
                screen.blit(bola, [x_bola, y_bola])
                screen.blit(jogador1, (x_jogador1, y_jogador1))
                screen.blit(jogador2, (x_jogador2, y_jogador2))
                pg.draw.circle(screen, blue, (x_pe_jogador1, y_pe_jogador1), 10)
                pg.draw.circle(screen, green, (x_pe_jogador2, y_pe_jogador2), 10)   
                pg.draw.line(screen, white, inicio_linha, fim_linha, 5) #linha_baixo
                pg.draw.line(screen, white, inicio_linha2, fim_linha2, 20) #linha_esquerda
                pg.draw.line(screen, white, inicio_linha3, fim_linha3, 20) #linha_direita
                pg.draw.rect(screen, grey, [x_placar, y_placar, tamanho_placar[0], tamanho_placar[1]])
                pg.draw.line(screen, wood, inicio_linha4, fim_linha4, 10) #linha_placar
                texto(str(gol_jogador_1), red, 64, pos_x_jog1, pos_y_jog1)
                texto(str(gol_jogador_2), red, 64, pos_x_jog2, pos_y_jog2)

class Instrucoes(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Instrucoes", parent, 0,
            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(300, 300)

        label = Gtk.Label("Aqui estarao as instrucoes")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class MinhaJanela(Gtk.Window):

    def __init__(self, titulo):
        Gtk.Window.__init__(self, title=titulo)
        
        self.set_default_size(500, 300)
        self.set_border_width(20)
        self.v_box = Gtk.VBox(spacing=5)
        self.imagem_fundo = Gtk.Image.new_from_file("fundo_pronto.jpg")
        self.h_box0 = Gtk.HBox(spacing=20)
        self.h_box1 = Gtk.HBox(spacing=20)
        self.h_box2 = Gtk.HBox(spacing=20)
        self.h_box2.add(self.imagem_fundo)
        

        self.v_box.add(self.h_box0)
        self.v_box.add(self.h_box1)
        self.v_box.add(self.h_box2)

        self.titulo = Gtk.Label("Super Bouu")

        self.h_box0.add(self.titulo)

        self.b1 = Gtk.Button(label="            Jogar           ")
        self.h_box1.add(self.b1)

        self.b2 = Gtk.Button(label="            Instrucoes            ")
        self.h_box2.pack_start(self.b2, True, True, 0)

        self.add(self.v_box)

        self.b2.connect("clicked", self.on_button_clicked)
        self.b1.connect("clicked", self.iniciar_janela_times)
    
    def on_button_clicked(self, widget):
        dialog = Instrucoes(self)
        response = dialog.run()

        dialog.destroy()

    def iniciar_janela_times(self, widget):
        janela = JanelaTimes()
        janela.connect("destroy", Gtk.main_quit)
        janela.show_all()
        Gtk.main()
    
if __name__ == "__main__":

    janela = MinhaJanela("")
    janela.connect("destroy", Gtk.main_quit)
    janela.show_all()
    Gtk.main()

   