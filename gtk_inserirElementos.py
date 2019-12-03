import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DialogExample(Gtk.Dialog):

    def __init__(self, janela_pai):
        Gtk.Dialog.__init__(self, "Caixa Dialog", janela_pai,
                            Gtk.DialogFlags.USE_HEADER_BAR ,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                            Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.add_buttons(Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        self.set_default_size(150, 100)
        self.set_resizable(False)

        self.show_all()

class JanelaPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Última avaliação")

        self.v_box = Gtk.VBox(spacing=5)
        self.h_box0 = Gtk.HBox(spacing=2)
        self.lista_widgets = []
        self.lista_widgets2 = []

        self.label1 = Gtk.Label("Tipo:")
        self.texto1 = Gtk.Entry()
        self.label2 = Gtk.Label("Nome:")
        self.texto2 = Gtk.Entry()
        self.b1 = Gtk.Button("Criar")
        self.b2 = Gtk.Button("Renomear")

        self.h_box0.add(self.label1)
        self.h_box0.add(self.texto1)
        self.h_box0.add(self.label2)
        self.h_box0.add(self.texto2)
        self.h_box0.add(self.b1)
        self.h_box0.add(self.b2)
        self.v_box.add(self.h_box0)

        self.add(self.v_box)

        
        self.b1.connect("clicked", self.CriarWidget)
        self.b2.connect("clicked", self.Renomear)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def Renomear(self, widget):
        dialog = DialogExample(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            if self.texto1.get_text() in self.lista_widgets:
                for i in self.lista_widgets2:
                    if self.texto1.get_text() == i.get_label():
                        widget = i
                        widget.set_label(self.texto2.get_text())
                        self.lista_widgets2.append(widget)
                        self.lista_widgets.append(widget.get_label())
        elif response == Gtk.ResponseType.CANCEL:
            self.texto1.set_text("")
            self.texto2.set_text("")
                 

        dialog.destroy()

    def CriarWidget(self, widget):
        if self.texto2.get_text() not in self.lista_widgets:
            if self.texto1.get_text() == "label": 
                self.label = Gtk.Label(self.texto2.get_text())
                self.hbox = Gtk.HBox(spacing=2)
                self.lista_widgets.append(self.label.get_label())
                self.lista_widgets2.append(self.label)
                self.hbox.add(self.label)
                self.v_box.add(self.hbox)
                self.show_all()
            elif self.texto1.get_text() == "button":
                self.b = Gtk.Button(self.texto2.get_text())
                self.hbox = Gtk.HBox(spacing=2)
                self.lista_widgets.append(self.b.get_label())
                self.lista_widgets2.append(self.b)
                self.hbox.add(self.b)
                self.v_box.add(self.hbox)
                self.show_all()



win = JanelaPrincipal()
Gtk.main()