import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MinhaJanela(Gtk.Window):

    def __init__(self, titulo):
        Gtk.Window.__init__(self, title=titulo)
        
        self.v_box = Gtk.VBox(spacing=5)
        self.h_box0 = Gtk.HBox(spacing=2)
        self.h_box1 = Gtk.HBox(spacing=2)
        self.h_box2 = Gtk.HBox(spacing=2)
        self.h_box3 = Gtk.HBox(spacing=2)
        self.h_box4 = Gtk.HBox(spacing=2)    
    

        self.v_box.add(self.h_box0)
        self.v_box.add(self.h_box1)
        self.v_box.add(self.h_box2)
        self.v_box.add(self.h_box3)
        self.v_box.add(self.h_box4)

        self.label = Gtk.Label(label="Insira a Frase: ")
        self.caixa_texto = Gtk.Entry()
        self.h_box0.add(self.label)
        self.h_box0.add(self.caixa_texto)

        self.label_2 = Gtk.Label(label="Quantidade de Palavras")
        self.h_box1.pack_start(self.label_2, True, True, 0)
        self.caixa_texto_quan_p = Gtk.Entry()
        self.h_box1.pack_end(self.caixa_texto_quan_p, True, True, 10)

        self.label_3 = Gtk.Label(label="Quantidade de Vogais")
        self.h_box2.pack_start(self.label_3, True, True, 0)
        self.caixa_texto_quan_v = Gtk.Entry()
        self.h_box2.pack_end(self.caixa_texto_quan_v, True, True, 10) 

        self.add(self.v_box)

        self.b1 = Gtk.Button(label="Contar Palavras")
        self.b2 = Gtk.Button(label="Contar Vogais")
        self.b3 = Gtk.Button(label="Fazer Tudo")
        
        self.h_box3.pack_start(self.b1, True, True, 0)
        self.h_box3.pack_start(self.b2, True, True, 0)
        
        self.h_box4.pack_start(self.b3, True, True, 0)

        self.b1.connect("clicked", self.contar_palavras)
        self.b2.connect("clicked", self.contar_vogais)
        self.b3.connect("clicked", self.fazer_tudo)

    def contar_palavras(self, widget):
        informacao = self.caixa_texto.get_text()
        informacao = informacao.split(" ")
        count = 0
        for valor in informacao:
            count += 1
        self.caixa_texto_quan_p.set_text(str(count))

    def contar_vogais(self, widget):
        informacao = self.caixa_texto.get_text()
        informacao = informacao.split(" ")
        count = 0 
        for valor in informacao:
            for valor_2 in valor:
                if self.verificar_vogal(valor_2):
                    count += 1
        self.caixa_texto_quan_v.set_text(str(count))

    def verificar_vogal(self, valor):
        lista_vogais = ['a', 'e', 'i', 'o', 'u']
        if valor.lower() in lista_vogais:
            return True
        return False
    
    def fazer_tudo(self, widget):
        self.contar_palavras(self)
        self.contar_vogais(self)


janela = MinhaJanela("Calculadora")
janela.connect("destroy", Gtk.main_quit)
janela.show_all()
Gtk.main()