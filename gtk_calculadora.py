import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MeuGtk(Gtk.Window):
    def __init__(self, titulo):
        Gtk.Window.__init__(self, title = titulo)

        self.Vbox = Gtk.VBox(spacing=4)
        self.Hbox1 = Gtk.HBox(spacing= 4)
        self.Hbox2 = Gtk.HBox(spacing= 4)
        self.Hbox3 = Gtk.HBox(spacing= 4)
        self.Hbox4 = Gtk.HBox(spacing = 4)
        self.Hbox5 = Gtk.HBox(spacing = 4)
        self.Vbox.add(self.Hbox1)
        self.Vbox.add(self.Hbox2)
        self.Vbox.add(self.Hbox3)
        self.Vbox.add(self.Hbox4)
        self.Vbox.add(self.Hbox5)

        self.add(self.Vbox)

        self.label = Gtk.Label(label = "Resultado")
        self.texto = Gtk.Entry()

        self.b1= Gtk.Button(label="1")
        self.b2= Gtk.Button(label="2")
        self.b3= Gtk.Button(label="3")
        self.b4= Gtk.Button(label="4")
        self.b5= Gtk.Button(label="5")
        self.b6= Gtk.Button(label="6")
        self.b7= Gtk.Button(label="7")
        self.b8= Gtk.Button(label="8")
        self.b9= Gtk.Button(label="9")
        self.b0 = Gtk.Button(label="0")
        self.menos = Gtk.Button(label="-")
        self.mais = Gtk.Button(label="+")
        self.igual = Gtk.Button(label="=")
        self.vezes= Gtk.Button(label="*")
        self.dividir= Gtk.Button(label="/")
        self.limpar = Gtk.Button(label="LIMPAR")


        self.Hbox1.pack_start(self.label, True, True, 5)
        self.Hbox1.pack_end(self.texto, True, True, 5)
        self.Hbox2.pack_start(self.b1, True, True, 5)
        self.Hbox2.pack_start(self.b2, True, True, 5)
        self.Hbox2.pack_start(self.b3, True, True, 5)
        self.Hbox2.pack_end(self.mais, True, True, 5)
        self.Hbox3.pack_start(self.b4, True, True, 5)
        self.Hbox3.pack_start(self.b5, True, True, 5)
        self.Hbox3.pack_start(self.b6, True, True, 5)
        self.Hbox3.pack_end(self.menos, True, True, 5)
        self.Hbox4.pack_start(self.b7, True, True, 5)
        self.Hbox4.pack_start(self.b8, True, True, 5)
        self.Hbox4.pack_start(self.b9, True, True, 5)
        self.Hbox4.pack_end(self.vezes, True, True, 5)
        self.Hbox5.pack_start(self.limpar, True, True, 5)
        self.Hbox5.pack_start(self.b0, True, True, 5)
        self.Hbox5.pack_start(self.igual, True, True, 5)
        self.Hbox5.pack_end(self.dividir, True, True, 5)


        self.b1.connect("clicked", self.atualizar)
        self.b2.connect("clicked", self.atualizar)
        self.b3.connect("clicked", self.atualizar)
        self.b4.connect("clicked", self.atualizar)
        self.b5.connect("clicked", self.atualizar)
        self.b6.connect("clicked", self.atualizar)
        self.b7.connect("clicked", self.atualizar)
        self.b8.connect("clicked", self.atualizar)
        self.b9.connect("clicked", self.atualizar)
        self.b0.connect("clicked", self.atualizar)
        self.menos.connect("clicked", self.atualizar)
        self.mais.connect("clicked", self.atualizar)
        self.igual.connect("clicked", self.atualizar)
        self.dividir.connect("clicked", self.atualizar)
        self.vezes.connect("clicked", self.atualizar)
        self.limpar.connect("clicked", self.atualizar)


    def atualizar(self, widget):
        if widget.get_label() == "=":
            self.texto.set_text(str(eval(self.texto.get_text())))
        elif widget.get_label() == "LIMPAR":
            self.texto.set_text("")   
        else:
            self.texto.set_text(self.texto.get_text() + widget.get_label())
            
Minha = MeuGtk("Calculadora")
Minha.connect("destroy", Gtk.main_quit)
Minha.show_all()
Gtk.main()