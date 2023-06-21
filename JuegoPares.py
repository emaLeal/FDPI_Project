'''
Nombre: Emanuel Leal Arce
Codigo: 2323555
Correo: emanuel.leal@correounivalle.edu.co

Nombre: Gian Manuel Pineda
Codigo: 2324151
Correo: gian.pineda@correounivalle.edu.co

Nombre: Sebastian Riascos
Codigo: 2371774
Correo: Daniel.sebastian.riascos@correounivalle.edu.co

Paso 1: Analisis del problema:

Descripción: Desarrolle un programa en Python para el juego de parejas. 
El programa tiene un tablero de 4x4 para encontrar las parejas de imágenes.
Por defecto se debe cargar una imagen de base para que el usuario pueda ir descubriendo las parejas de imágenes. 
Cree una función que permita cargar la imagen de base cuando se inicie el programa. 
Las imágenes ocultas deben cargarse en forma aleatoria cada vez que se inicie el juego.
Escriba una función que permita ir descubriendo las imágenes. Cuando el usuario encuentre una pareja de imágenes, el sistema debe desactivarlas. En caso contrario, el programa debe volver a ocultar las imágenes cargando la imagen de base
Cuando el jugador encuentre todas las parejas se debe imprimir un mensaje donde se indique que el jugador ganó. Esto se debe mostrar en un label al final del tablero. Adicionalmente, debe imprimir el número de intentos fallidos y el número total de intentos.


Clases: ventana
Funciones: __init__(), on_button_clicked(), ocultaimagen()
Variables: timeout, intentos, intentosfallidos, respcorrecta, vbox, hbox1-hbox4, img0-img15, b0-b15, lista_pares, lista_botones, lista_respuesta, lista_pos, label_gana
Entradas: b0-b15, lista_respuesta
Procesos: if len(lista_respuesta) < 2, if len(lista_respuesta) == 2, if respcorrecta == 8
Salidas: ¡Felicitaciones, ha encontrado todos los pares!, Su número total de intentos fallidos fue: n, Su número total de intentos fue: n

Paso 2: Pseudocódigo

Inicio

importar random
gi requiere Gtk en version 3.0

desde el repository de gi importar Gtk, GLib

clase Ventana hereda de Window de Gtk
	timeout = 500
	intentos = 0
	intentosfallados = 0
	respcorrecto = 0
	
	constructor() entonces
		constructor de clase heredada con titulo=’Juego de Parejas’
		tamaño de ventana(600 de ancho, 600 de alto)
		ancho de borde(10)
		
		vbox = Vertical Box de Gtk(spaciado=2, homogeneo = Verdadero)
		ejecutar funcion add(vbox)

		hbox1 = Horizontal Box de Gtk(spaciado = 2, homogeneo = Verdadero)
		añadir a vbox(hbox1)
		
		hbox2 = Horizontal Box de Gtk(spaciado = 2, homogeneo = Verdadero)
		añadir a vbox(hbox2)
 		hbox3 = Horizontal Box de Gtk(spaciado = 2, homogeneo = Verdadero)
		añadir a vbox(hbox3)
	
		hbox4 = Horizontal Box de Gtk(spaciado = 2, homogeneo = Verdadero)
		añadir a vbox(hbox4)

		img0 = Imagen de Gtk desde archivo(‘img/default.png’)
		img1 = Imagen de Gtk desde archivo(‘img/default.png’)
		img2 = Imagen de Gtk desde archivo(‘img/default.png’)
		img3 = Imagen de Gtk desde archivo(‘img/default.png’)
		img4 = Imagen de Gtk desde archivo(‘img/default.png’)
		img5 = Imagen de Gtk desde archivo(‘img/default.png’)
		img6 = Imagen de Gtk desde archivo(‘img/default.png’)
		img7 = Imagen de Gtk desde archivo(‘img/default.png’)
		img8 = Imagen de Gtk desde archivo(‘img/default.png’)
		img9 = Imagen de Gtk desde archivo(‘img/default.png’)
		img10 = Imagen de Gtk desde archivo(‘img/default.png’)
		img11 = Imagen de Gtk desde archivo(‘img/default.png’)
		img12 = Imagen de Gtk desde archivo(‘img/default.png’)
		img13 = Imagen de Gtk desde archivo(‘img/default.png’)
		img14 = Imagen de Gtk desde archivo(‘img/default.png’)
		img15 = Imagen de Gtk desde archivo(‘img/default.png’)


		lista_pares = ["img/img1.png", "img/img1.png", "img/img2.png", 						"img/img2.png", 
			"img/img3.png", "img/img3.png", "img/img4.png", "img/img4.png", 
			"img/img5.png", "img/img5.png", "img/img6.png", "img/img6.png", 
			"img/img7.png", "img/img7.png", "img/img8.png", "img/img8.png"]

		randomizar lista_pares

		lista_botones = []
		lista_respuesta = []
		lista_pos = []
		
		label_gana = Label de Gtk con texto ‘’
		añadir a vbox(label_gana)

		b0 = Button nuevo de Gtk
		ajustar b0 con imagen img0
		añadir a lista_botones(b0)
		b0.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox1(b0)

		b1 = Button nuevo de Gtk
		ajustar b1 con imagen img1
		añadir a lista_botones(b1)
		b1.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox1(b1)

		b2 = Button nuevo de Gtk
		ajustar b2 con imagen img2
		añadir a lista_botones(b2)
		b2.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox1(b2)

		b3 = Button nuevo de Gtk
		ajustar b3 con imagen img3
		añadir a lista_botones(b3)
		b3.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox1(b3)

		b4 = Button nuevo de Gtk
		ajustar b4 con imagen img0
		añadir a lista_botones(b4)
		b4.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox2(b4)

		b5 = Button nuevo de Gtk
		ajustar b5 con imagen img5
		añadir a lista_botones(b5)
		b5.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox2(b5)

		b6 = Button nuevo de Gtk
		ajustar b6 con imagen img6
		añadir a lista_botones(b6)
		b6.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox2(b6)

		b7 = Button nuevo de Gtk
		ajustar b7 con imagen img0
		añadir a lista_botones(b7)
		b7.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox2(b7)

		b8 = Button nuevo de Gtk
		ajustar b8 con imagen img8
		añadir a lista_botones(b8)
		b8.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox3(b8)

		b9 = Button nuevo de Gtk
		ajustar b9 con imagen img9
		añadir a lista_botones(b9)
		b9.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox3(b9)

		b10 = Button nuevo de Gtk
		ajustar b10 con imagen img10
		añadir a lista_botones(b10)
		b10.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox3(b10)

		b11 = Button nuevo de Gtk
		ajustar b11 con imagen img11
		añadir a lista_botones(b11)
		b11.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox3(b11)

		b12 = Button nuevo de Gtk
		ajustar b12 con imagen img12
		añadir a lista_botones(b12)
		b12.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox4(b12)

		b13 = Button nuevo de Gtk
		ajustar b13 con imagen img13
		añadir a lista_botones(b13)
		b13.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox4(b13)

		b14 = Button nuevo de Gtk
		ajustar b14 con imagen img14
		añadir a lista_botones(b14)
		b14.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox4(b0)

		b15 = Button nuevo de Gtk
		ajustar b15 con imagen img15
		añadir a lista_botones(b15)
		b15.click(on_button_clicked, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		
		añadir a hbox4(b15)

	funcion on_button_clicked(boton, lista_botones, lista_pares, lista_respuesta, lista_pos, label_gana)
		si la cantidad de lista_respuesta < 2 entonces
			pos_boton = lista_botones.indice(boton)
			añadir a lista_pos(pos_boton)

			añadir a lista_respuesta(lista_pares[pos_boton]
			
			img_boton = boton.imagen()
			img_boton.ajustar_desde_archivo(lista_pares[pos_boton])
			boton.ajustar_sensitividad(falso)

			si cantidad de lista_respuesta == 2 entonces
				this.intentos = this.intentos + 1
				si lista_respuesta[0] == lista_respuesta[1] entonces
					this.respcorrecta = this.repcorrecta + 1
					lista_respuesta.limpiar()
					lista_pos.limpiar()
				sino entonces
					this.intentosfallidos = this.intentosfallidos + 1
					Glib.añadir_temporizador(this.timeout, oculta_imagen, lista_botones, lista_pos, lista_respuesta)

			si this.repcorrecta == 8 entonces
				txt_intentosfall = "Su número total de intentos fallidos fue: " + cadena(self.intentosfallidos) + "."
				txt_intentos = "Su número total de intentos fue: " + cadena(this.intentos) + "."
				label_gana.ajustar_texto("¡Felicitaciones, ha encontrado todos los pares!" + "\n" + txt_intentosfall + "\n" + txt_intentos + "\n)

	funcion ocultaimagen(lista_botones, lista_pos, lista_respuesta)

		imgboton1 = lista_botones[lista_pos[0]].ajustar_imagen()
		imgboton1.ajustar_desde_archivo(‘img/default.png’)
		lista_botones[lista_pos[0]].ajustar_sensitivo(verdadero)

		imgboton2 = lista_botones[lista_pos[1]].ajustar_imagen()
		imgboton2.ajustar_desde_archivo(‘img/default.png’)
		lista_botones[lista_pos[1]].ajustar_sensitivo(verdadero)
		
		lista_respuesta.limpiar()
		lista_pos.limpiar()
		retornar Falso

win = Ventana()
win.conectar(‘destruir’, Gtk.main_quit)
Gtk.main()

Fin

Paso 3: Pruebas de escritorio

Ver documento "ProyectoFDPI - LealPinedaRiascos.pdf" adjunto.

Paso 4: Código Python
'''

# Inicio

import gi
import random
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib

class ventana(Gtk.Window):
    timeout = 500
    intentos = 0
    intentosfallidos = 0
    respcorrecta = 0
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
                self.intentos += 1
                if lista_respuesta[0] == lista_respuesta[1]:
                    self.respcorrecta += 1
                    # Se limpian los valores de la lista de posiciones y de respuesta para poder seguir ingresando el resto de números
                    lista_respuesta.clear()
                    lista_pos.clear()
                else:
                    self.intentosfallidos += 1
                    # Método para que se complete la función del botón y después de un tiempo determinado se aplique la función de ocultar las imágenes
                    GLib.timeout_add(self.timeout, self.ocultaimagen, lista_botones, lista_pos, lista_respuesta)

            # Teniendo en cuenta que hay 8 pares, cuando respcorrecta sea 8 se le da contenido al label final
            if self.respcorrecta == 8:
                txt_intentosfall = "Su número total de intentos fallidos fue: " + str(self.intentosfallidos) + "."
                txt_intentos = "Su número total de intentos fue: " + str(self.intentos) + "."
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

# Fin