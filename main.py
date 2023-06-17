import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import random

class Proyecto(Gtk.Window):
    default_img = 'img/default.png'

    def __init__(self):
        intentos = 0
        img_comp = [0, 0]
        ant_carta = None
        super().__init__(title="Formulario")
        self.set_default_size(600, 600)
        self.set_border_width(10)
        list_img1 = [
            'img/img1.png',
            'img/img2.png',
            'img/img3.png',
            'img/img4.png',
            'img/img5.png',
            'img/img6.png',
            'img/img7.png',
            'img/img8.png',
            'img/img1.png',
            'img/img2.png',
            'img/img3.png',
            'img/img4.png',
            'img/img5.png',
            'img/img6.png',
            'img/img7.png',
            'img/img8.png'
        ]
        list_img2 = [
    
        ]
        vbox = Gtk.VBox(spacing=2)
        self.add(vbox)

        hbox1 = Gtk.Box(spacing=2)
        hbox2 = Gtk.Box(spacing=2)
        hbox3 = Gtk.Box(spacing=2)
        hbox4 = Gtk.Box(spacing=2)

        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)
        vbox.pack_start(hbox4, True, True, 0)

        ev_box1 = Gtk.EventBox()
        ev_box2 = Gtk.EventBox()
        ev_box3 = Gtk.EventBox()
        ev_box4 = Gtk.EventBox()
        ev_box5 = Gtk.EventBox()
        ev_box6 = Gtk.EventBox()
        ev_box7 = Gtk.EventBox()
        ev_box8 = Gtk.EventBox()
        ev_box9 = Gtk.EventBox()
        ev_box10 = Gtk.EventBox()
        ev_box11 = Gtk.EventBox()
        ev_box12 = Gtk.EventBox()
        ev_box13 = Gtk.EventBox()
        ev_box14 = Gtk.EventBox()
        ev_box15 = Gtk.EventBox()
        ev_box16 = Gtk.EventBox()
        # ya pero es que las EventBox solo estaban mencionadas, no creadas
        # mano ahi no
        # hay que usar el ev_box.connect('button-press-event)
        # a breve

        img1 = Gtk.Image()
        img2 = Gtk.Image()
        img3 = Gtk.Image()
        img4 = Gtk.Image()
        img5 = Gtk.Image()
        img6 = Gtk.Image()
        img7 = Gtk.Image()
        img8 = Gtk.Image()
        img9 = Gtk.Image()
        img10 = Gtk.Image()
        img11 = Gtk.Image()
        img12 = Gtk.Image()
        img13 = Gtk.Image()
        img14 = Gtk.Image()
        img15 = Gtk.Image()
        img16 = Gtk.Image()

        img1.set_from_file(self.default_img)
        img2.set_from_file(self.default_img)
        img3.set_from_file(self.default_img)
        img4.set_from_file(self.default_img)
        img5.set_from_file(self.default_img)
        img6.set_from_file(self.default_img)
        img7.set_from_file(self.default_img)
        img8.set_from_file(self.default_img)
        img9.set_from_file(self.default_img)
        img10.set_from_file(self.default_img)
        img11.set_from_file(self.default_img)
        img12.set_from_file(self.default_img)
        img13.set_from_file(self.default_img)
        img14.set_from_file(self.default_img)
        img15.set_from_file(self.default_img)
        img16.set_from_file(self.default_img)

        ev_box1.add(img1)
        ev_box2.add(img2)
        ev_box3.add(img3)
        ev_box4.add(img4)
        ev_box5.add(img5)
        ev_box6.add(img6)
        ev_box7.add(img7)
        ev_box8.add(img8)
        ev_box9.add(img9)
        ev_box10.add(img10)
        ev_box11.add(img11)
        ev_box12.add(img12)
        ev_box13.add(img13)
        ev_box14.add(img14)
        ev_box15.add(img15)
        ev_box16.add(img16)

        ev_box1.connect("button-press-event", self.on_image_clicked)
        ev_box2.connect("button-press-event", self.on_image_clicked)
        ev_box3.connect("button-press-event", self.on_image_clicked)
        ev_box4.connect("button-press-event", self.on_image_clicked)
        ev_box5.connect("button-press-event", self.on_image_clicked)
        ev_box6.connect("button-press-event", self.on_image_clicked)
        ev_box7.connect("button-press-event", self.on_image_clicked)
        ev_box8.connect("button-press-event", self.on_image_clicked)
        ev_box9.connect("button-press-event", self.on_image_clicked)
        ev_box10.connect("button-press-event", self.on_image_clicked)
        ev_box11.connect("button-press-event", self.on_image_clicked)
        ev_box12.connect("button-press-event", self.on_image_clicked)
        ev_box13.connect("button-press-event", self.on_image_clicked)
        ev_box14.connect("button-press-event", self.on_image_clicked)
        ev_box15.connect("button-press-event", self.on_image_clicked)
        ev_box16.connect("button-press-event", self.on_image_clicked)

        imgs = [[img1, img2, img3, img4], [img5, img6, img7, img8],
                [img9, img10, img11, img12], [img13, img14, img15, img16]
                ]
        hbox1.pack_start(ev_box1, True, True, 0)
        hbox1.pack_start(ev_box2, True, True, 0)
        hbox1.pack_start(ev_box3, True, True, 0)
        hbox1.pack_start(ev_box4, True, True, 0)
        hbox2.pack_start(ev_box5, True, True, 0)
        hbox2.pack_start(ev_box6, True, True, 0)
        hbox2.pack_start(ev_box7, True, True, 0)
        hbox2.pack_start(ev_box8, True, True, 0)
        hbox3.pack_start(ev_box9, True, True, 0)
        hbox3.pack_start(ev_box10, True, True, 0)
        hbox3.pack_start(ev_box11, True, True, 0)
        hbox3.pack_start(ev_box12, True, True, 0)
        hbox4.pack_start(ev_box13, True, True, 0)
        hbox4.pack_start(ev_box14, True, True, 0)
        hbox4.pack_start(ev_box15, True, True, 0)
        hbox4.pack_start(ev_box16, True, True, 0)

        
    def on_image_clicked(self, evt_box, img, imgs, intentos, img_comp, ant_carta):
        random_img = imgs[random.randint(0, 4)][random.randint(0, 4)]
        img.set_from_file(random_img)
        intentos+= 1
        if intentos == 2:
            img_comp[1] = random_img
        elif intentos == 1:
            img_comp[0] = random_img
            ant_carta = img
        
        if (self.verificar(img_comp)):
            ant_carta.set_from_file(self.default_img)
            img.set_from_file(self.default_img)
        
    def verificar(self, img_comp):
        if img_comp[0] == img_comp[1]:
            return True
        else:
            return False
        

win = Proyecto()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
