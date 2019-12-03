import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from jogo import main
from bd_pontuacao import listar_pontuacoes

class Instrucoes(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Instrucoes", parent, 0,
            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(300, 300)

        label = Gtk.Label("Utilize o Mouse para se movimentar e a Barra de Espaco para disparar")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class MinhaJanela(Gtk.Window):

    def __init__(self, titulo):
        Gtk.Window.__init__(self, title=titulo)
        
        self.set_default_size(500, 300)
        self.set_border_width(20)
        self.v_box = Gtk.VBox(spacing=5)
        self.h_box0 = Gtk.HBox(spacing=20)
        self.h_box1 = Gtk.HBox(spacing=20)
        self.h_box2 = Gtk.HBox(spacing=20)
        self.h_box3 = Gtk.HBox(spacing=20)        
        self.h_box4 = Gtk.HBox(spacing=20)
        self.h_box5 = Gtk.HBox(spacing=20)        

        self.v_box.add(self.h_box0)
        self.v_box.add(self.h_box1)
        self.v_box.add(self.h_box2)
        self.v_box.add(self.h_box3)
        self.v_box.add(self.h_box4)
        self.v_box.add(self.h_box5)

        self.titulo = Gtk.Label("Space War")

        self.h_box0.add(self.titulo)

        self.b1 = Gtk.Button(label="            Jogar           ")
        self.h_box1.add(self.b1)

        self.b2 = Gtk.Button(label="            Instruções            ")
        self.h_box2.pack_start(self.b2, True, True, 0)

        self.b4 = Gtk.Button(label = "      Sair        ")
        self.h_box5.pack_start(self.b4, True, True, 0)

        self.add(self.v_box)

        self.b1.connect("clicked", self.jogar)
        self.b2.connect("clicked", self.ver_instrucoes)
        self.b4.connect("clicked", Gtk.main_quit)
    
    def ver_instrucoes(self, widget):
        dialog = Instrucoes(self)
        response = dialog.run()

        dialog.destroy()

    def jogar(self, widget):
        main()


janela = MinhaJanela("")
janela.connect("destroy", Gtk.main_quit)
janela.show_all()
Gtk.main()