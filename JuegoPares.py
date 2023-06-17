import gi
import random

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib

timeout = 500
intentos = 0
intentosfallidos = 0
respcorrecta = 0

class ventana(Gtk.Window):
    def __init__(self):
        super().__init__(title="Juego de Parejas")
        self.set_default_size(600, 600)
        self.set_border_width(10)
        
        # Caja Vertical
        vbox = Gtk.VBox(spacing=2, homogeneous = True)
        self.add(vbox)

        # Hileras de Cajas Horizontales Agregadas
        hbox1 = Gtk.Box(spacing=2, homogeneous = True)
        vbox.pack_start(hbox1, True, True, 0)

        hbox2 = Gtk.Box(spacing=2, homogeneous = True)
        vbox.pack_start(hbox2, True, True, 0)

        hbox3 = Gtk.Box(spacing=2, homogeneous = True)
        vbox.pack_start(hbox3, True, True, 0)

        hbox4 = Gtk.Box(spacing=2, homogeneous = True)
        vbox.pack_start(hbox4, True, True, 0)

        # Lista Números y con random la aleatorizamos
        # Cambiar a una lista de imágenes con la dirección de todas las imágenes
    
        # Imágenes

        img0 = Gtk.Image.new_from_file("img/default.png")
        img1 = Gtk.Image.new_from_file("img/default.png")
        img2 = Gtk.Image.new_from_file("img/default.png")
        img3 = Gtk.Image.new_from_file("img/default.png")
        img4 = Gtk.Image.new_from_file("img/default.png")
        img5 = Gtk.Image.new_from_file("img/default.png")
        img6 = Gtk.Image.new_from_file("img/default.png")
        img7 = Gtk.Image.new_from_file("img/default.png")
        img8 = Gtk.Image.new_from_file("img/default.png")
        img9 = Gtk.Image.new_from_file("img/default.png")
        img10 = Gtk.Image.new_from_file("img/default.png")
        img11 = Gtk.Image.new_from_file("img/default.png")
        img12 = Gtk.Image.new_from_file("img/default.png")
        img13 = Gtk.Image.new_from_file("img/default.png")
        img14 = Gtk.Image.new_from_file("img/default.png")
        img15 = Gtk.Image.new_from_file("img/default.png")

        lista_pares = ["img/img1.png", "img/img1.png", "img/img2.png", "img/img2.png", 
                       "img/img3.png", "img/img3.png", "img/img4.png", "img/img4.png", 
                       "img/img5.png", "img/img5.png", "img/img6.png", "img/img6.png", 
                       "img/img7.png", "img/img7.png", "img/img8.png", "img/img8.png"]
        random.shuffle(lista_pares)

        # Lista Botones, la lista incia vacía porque por alguna razón me da problemas luego al querer acceder a ella

        lista_botones = []

        # Variables y otras listas

        lista_respuesta = []
        lista_pos = []

        # Label Gana

        label_gana = Gtk.Label.new("")
        vbox.pack_start(label_gana, True, True, 0)

        # Botones agregados en grupos de 4 a una caja horizontal

        b0 = Gtk.Button.new()
        b0.set_image(img0)
        lista_botones.append(b0)
        b0.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox1.pack_start(b0, True, True, 0)
        
        b1 = Gtk.Button.new()
        b1.set_image(img1)
        lista_botones.append(b1)
        b1.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox1.pack_start(b1, True, True, 0)

        b2 = Gtk.Button.new()
        b2.set_image(img2)
        lista_botones.append(b2)
        b2.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox1.pack_start(b2, True, True, 0)

        b3 = Gtk.Button.new()
        b3.set_image(img3)
        lista_botones.append(b3)
        b3.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox1.pack_start(b3, True, True, 0)

        b4 = Gtk.Button.new()
        b4.set_image(img4)
        lista_botones.append(b4)
        b4.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox2.pack_start(b4, True, True, 0)

        b5 = Gtk.Button.new()
        b5.set_image(img5)
        lista_botones.append(b5)
        b5.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox2.pack_start(b5, True, True, 0)

        b6 = Gtk.Button.new()
        b6.set_image(img6)
        lista_botones.append(b6)
        b6.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox2.pack_start(b6, True, True, 0)

        b7 = Gtk.Button.new()
        b7.set_image(img7)
        lista_botones.append(b7)
        b7.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox2.pack_start(b7, True, True, 0)

        b8 = Gtk.Button.new()
        b8.set_image(img8)
        lista_botones.append(b8)
        b8.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox3.pack_start(b8, True, True, 0)

        b9 = Gtk.Button.new()
        b9.set_image(img9)
        lista_botones.append(b9)
        b9.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox3.pack_start(b9, True, True, 0)

        b10 = Gtk.Button.new()
        b10.set_image(img10)
        lista_botones.append(b10)
        b10.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox3.pack_start(b10, True, True, 0)

        b11 = Gtk.Button.new()
        b11.set_image(img11)
        lista_botones.append(b11)
        b11.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox3.pack_start(b11, True, True, 0)
        
        b12 = Gtk.Button.new()
        b12.set_image(img12)
        lista_botones.append(b12)
        b12.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox4.pack_start(b12, True, True, 0)

        b13 = Gtk.Button.new()
        b13.set_image(img13)
        lista_botones.append(b13)
        b13.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox4.pack_start(b13, True, True, 0)

        b14 = Gtk.Button.new()
        b14.set_image(img14)
        lista_botones.append(b14)
        b14.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox4.pack_start(b14, True, True, 0)

        b15 = Gtk.Button.new()
        b15.set_image(img15)
        lista_botones.append(b15)
        b15.connect("clicked", self.on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
        hbox4.pack_start(b15, True, True, 0)

        # Funciones

    def on_button_clicked(self, boton, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana):
        # Declaraciones de Variables Globales
        global intentos
        global intentosfallidos
        global respcorrecta

        # Inicio de Proceso

        # Para evitar que se pueda presionar más de 2 botones.
        if len(lista_respuesta) <2:

            # Se toma la posición del boton presionado y se agrega a una lista.
            pos_boton = lista_botones.index(boton)
            lista_pos.append(pos_boton)

            # Se agrega a la lista de respuestas la imagen que se encuentra en la misma posición del botón
            lista_respuesta.append(lista_pares[pos_boton])

            # Se toma el Widget de imagen correspondiente al boton seleccionado, se le cambia la imagen de acuerdo al str contenido en lista_pares y se invalidan las acciones para ese botón.
            imgboton = boton.get_image()
            imgboton.set_from_file(lista_pares[pos_boton])
            boton.set_sensitive(False)

            # Cuando se presionan dos botones la lista de respuesta es igual a 2, se procede a comparar los dos valores contenidos en lista_respuesta
            if len(lista_respuesta) == 2:
                intentos += 1
                if lista_respuesta[0] == lista_respuesta[1]:
                    respcorrecta += 1
                    # Se limpian los valores de la lista de posiciones y de respuesta para poder seguir ingresando el resto de números
                    lista_respuesta.clear()
                    lista_pos.clear()
                else:
                    intentosfallidos += 1
                    # Método para que se complete la función del botón y después de un tiempo determinado se aplique la función de ocultar las imágenes
                    GLib.timeout_add(timeout, self.ocultaimagen, lista_botones, lista_pos, lista_respuesta)

            # Teniendo en cuenta que hay 8 pares, cuando respcorrecta sea 8 se le da contenido al label final
            if respcorrecta == 8:
                txt_intentosfall = "Su número total de intentos fallidos fue: " + str(intentosfallidos) + "."
                txt_intentos = "Su número total de intentos fue: " + str(intentos) + "."
                label_gana.set_text("¡Felicitaciones, ha encontrado todos los pares!" + "\n" + txt_intentosfall + "\n" + txt_intentos + "\n")

        # Fin del Proceso
                

    def ocultaimagen(self, lista_botones, lista_pos, lista_respuesta):
        # Obtenemos el Widget de imagen correspondiente al boton de acuerdo a lista_pos, cambiamos la imagen a la predeterminada y permitimos la interacción con el botón
        imgboton1 = lista_botones[lista_pos[0]].get_image()
        imgboton1.set_from_file("img/default.png")
        lista_botones[lista_pos[0]].set_sensitive(True)
        
        imgboton2 = lista_botones[lista_pos[1]].get_image()
        imgboton2.set_from_file("img/default.png")
        lista_botones[lista_pos[1]].set_sensitive(True)

        # Se limpian los valores de la lista de posiciones y de respuesta para poder seguir ingresando el resto de números
        lista_respuesta.clear()
        lista_pos.clear()
        return False

win = ventana()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()