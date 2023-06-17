import gi
import random
import time

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib

timeout = 1000

class ventana(Gtk.Window):
    def __init__(self):
        super().__init__(title="Formulario")
        self.set_default_size(600, 600)
        self.set_border_width(10)
        
        # Caja Vertical
        vbox = Gtk.VBox(spacing=2)
        self.add(vbox)

        # Hileras de Cajas Horizontales Agregadas
        hbox1 = Gtk.Box(spacing=2)
        vbox.pack_start(hbox1, True, True, 0)

        hbox2 = Gtk.Box(spacing=2)
        vbox.pack_start(hbox2, True, True, 0)

        hbox3 = Gtk.Box(spacing=2)
        vbox.pack_start(hbox3, True, True, 0)

        hbox4 = Gtk.Box(spacing=2)
        vbox.pack_start(hbox4, True, True, 0)

        # Lista Números y con random la aleatorizamos
        # Cambiar a una lista de imágenes con la dirección de todas las imágenes
        lista_pares = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
        # random.shuffle(lista_pares)

        # Lista Botones, la lista incia vacía porque por alguna razón me da problemas luego al querer acceder a ella

        lista_botones = []

        # Variables y otras listas

        contador = 0
        lista_respuesta = []
        lista_pos = []

        # Botones agregados en grupos de 4 a una caja horizontal

        """
        Cambiar el Gtk.Button.new_with_label a Gtk.Button.new_from_icon_name("img\default.png")
        """
        b0 = Gtk.Button.new_with_label("?")
        lista_botones.append(b0)
        b0.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox1.pack_start(b0, True, True, 0)
        
        b1 = Gtk.Button.new_with_label("?")
        lista_botones.append(b1)
        b1.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox1.pack_start(b1, True, True, 0)

        b2 = Gtk.Button.new_with_label("?")
        lista_botones.append(b2)
        b2.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox1.pack_start(b2, True, True, 0)

        b3 = Gtk.Button.new_with_label("?")
        lista_botones.append(b3)
        b3.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox1.pack_start(b3, True, True, 0)

        b4 = Gtk.Button.new_with_label("?")
        lista_botones.append(b4)
        b4.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox2.pack_start(b4, True, True, 0)

        b5 = Gtk.Button.new_with_label("?")
        lista_botones.append(b5)
        b5.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox2.pack_start(b5, True, True, 0)

        b6 = Gtk.Button.new_with_label("?")
        lista_botones.append(b6)
        b6.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox2.pack_start(b6, True, True, 0)

        b7 = Gtk.Button.new_with_label("?")
        lista_botones.append(b7)
        b7.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox2.pack_start(b7, True, True, 0)

        b8 = Gtk.Button.new_with_label("?")
        lista_botones.append(b8)
        b8.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox3.pack_start(b8, True, True, 0)

        b9 = Gtk.Button.new_with_label("?")
        lista_botones.append(b9)
        b9.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox3.pack_start(b9, True, True, 0)

        b10 = Gtk.Button.new_with_label("?")
        lista_botones.append(b10)
        b10.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox3.pack_start(b10, True, True, 0)

        b11 = Gtk.Button.new_with_label("?")
        lista_botones.append(b11)
        b11.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox3.pack_start(b11, True, True, 0)
        
        b12 = Gtk.Button.new_with_label("?")
        lista_botones.append(b12)
        b12.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox4.pack_start(b12, True, True, 0)

        b13 = Gtk.Button.new_with_label("?")
        lista_botones.append(b13)
        b13.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox4.pack_start(b13, True, True, 0)

        b14 = Gtk.Button.new_with_label("?")
        lista_botones.append(b14)
        b14.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox4.pack_start(b14, True, True, 0)

        b15 = Gtk.Button.new_with_label("?")
        lista_botones.append(b15)
        b15.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, contador)
        hbox4.pack_start(b15, True, True, 0)

        # Lista Botones Post Definición

        # Funciones

    def verifcartas(self, lista_botones, lista_pos, lista_respuesta):
        # Cuando la lista de respuestas es 2, comenzamos a comprar si son los mismos o no.
        print("Estamos en verifcartas y esta es la lista de botones:", lista_botones)
        print("Estamos en verifcartas y esta es la lista de pos:", lista_pos, "\n", "---------------")
        # Cambiar a .set_image("img\default.png")
        lista_botones[lista_pos[0]].set_label("?")
        lista_botones[lista_pos[0]].set_sensitive(True)
        lista_botones[lista_pos[1]].set_label("?")
        lista_botones[lista_pos[1]].set_sensitive(True)
        lista_respuesta.clear()
        lista_pos.clear()
        return False


    def on_button_clicked(self, boton, lista_botones, lista_pares, lista_respuesta, lista_pos, contador):
        # print(lista_botones)
        # print("El largo de la lista de botones es:", len(lista_botones))
        pos_boton = lista_botones.index(boton)
        lista_pos.append(pos_boton)
        # print(lista_pos)
        # print(len(lista_pos))

        # De acuerdo al botón presionado, ya teniendo la posición del botón (index), lo usamos para seleccionar una respuesta de la lista de pares y agregarla a una lista de respuestas para comparar
        lista_respuesta.append(lista_pares[pos_boton])
        # Acá ya no sería .set_label, sino .set_image("[ruta de la imagen]")
        boton.set_label(str(lista_pares[pos_boton]))
        boton.set_sensitive(False)
        print("Estamos en el botón y la lista de respuesta es:", lista_respuesta)
        print("Estamos en el botón y la len de lista_respuesta es:", len(lista_respuesta))
        print("En el botón y la lista pos es:", lista_pos, "\n", "---------------")

        if len(lista_respuesta) == 2:
            if lista_respuesta[0] == lista_respuesta[1]:
                print("Par")
                lista_respuesta.clear()
                lista_pos.clear()
            else:
                print("No par")
                GLib.timeout_add(timeout, self.verifcartas, lista_botones, lista_pos, lista_respuesta)
        


win = ventana()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
