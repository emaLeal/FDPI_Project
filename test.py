import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
import random

NUM_CARTAS = 8
ANCHO_CARTA = 100
ALTO_CARTA = 100

class JuegoParejas(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Juego de Parejas")
        self.set_border_width(10)

        self.cartas = []
        self.parejas_encontradas = 0
        self.primer_carta = None
        self.segunda_carta = None
        self.bloqueado = False

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.crear_cartas()
        self.distribuir_cartas()

    def crear_cartas(self):
        for i in range(NUM_CARTAS):
            pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, True, 8, ANCHO_CARTA, ALTO_CARTA)
            pixbuf.fill(0x000000ff)  # Colocar el color de fondo de la carta
            carta = Gtk.Image.new_from_pixbuf(pixbuf)
            carta.connect("button-press-event", self.on_carta_clicked, i)
            self.cartas.append(carta)

    def distribuir_cartas(self):
        posiciones = list(range(NUM_CARTAS)) * 2  # Duplicar las posiciones
        random.shuffle(posiciones)  # Barajar las posiciones

        for i, carta in enumerate(self.cartas):
            x = i % 4
            y = i // 4
            self.grid.attach(carta, x, y, 1, 1)

            if posiciones[i] < NUM_CARTAS:
                # Aquí puedes cargar la imagen correspondiente a la carta desde un archivo
                # y establecerla en el pixbuf de la carta utilizando GdkPixbuf.Pixbuf.new_from_file()
                # por ejemplo: carta.get_pixbuf().load_from_file("ruta_de_la_imagen.png")
                pass

        self.show_all()

    def on_carta_clicked(self, widget, event, indice):
        if self.bloqueado:
            return

        if self.primer_carta is None:
            self.primer_carta = indice
            self.mostrar_carta(indice)
        elif self.segunda_carta is None:
            self.segunda_carta = indice
            self.mostrar_carta(indice)
            GLib.timeout_add(1000, self.verificar_pareja)
        
    def mostrar_carta(self, indice):
        # Aquí puedes cargar la imagen correspondiente a la carta desde un archivo
        # y establecerla en el pixbuf de la carta utilizando GdkPixbuf.Pixbuf.new_from_file()
        # por ejemplo: self.cartas[indice].get_pixbuf().load_from_file("ruta_de_la_imagen.png")
        pass

    def ocultar_carta(self, indice):
        pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, True, 8, ANCHO_CARTA, ALTO_CARTA)
        pixbuf.fill(0x000000ff)  # Colocar el color de fondo de la carta
        self.cartas[indice].set_from_pixbuf(pixbuf)

    def verificar_pareja(self):
        carta1 = self.cartas[self.primer_carta]
        carta2 = self.cartas[self.segunda_carta]

        if self.primer_carta != self.segunda_carta and carta1.get_pixbuf().equal(carta2.get_pixbuf()):
            self.parejas_encontradas += 1
            self.cartas[self.primer_carta].set_sensitive(False)
            self.cartas[self.segunda_carta].set_sensitive(False)

            if self.parejas_encontradas == NUM_CARTAS // 2:
                mensaje = Gtk.MessageDialog(
                    parent=self,
                    flags=Gtk.DialogFlags.MODAL,
                    type=Gtk.MessageType.INFO,
                    buttons=Gtk.ButtonsType.OK,
                    message_format="¡Felicidades, has ganado!"
                )
                mensaje.run()
                mensaje.destroy()
                self.close()
        else:
            self.ocultar_carta(self.primer_carta)
            self.ocultar_carta(self.segunda_carta)

        self.primer_carta = None
        self.segunda_carta = None
        self.bloqueado = False

        return False

juego = JuegoParejas()
juego.connect("destroy", Gtk.main_quit)
Gtk.main()


