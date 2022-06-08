from re import S
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana_revisar(Gtk.Dialog):
    def __init__(self):
        super().__init__()

        self.set_default_size(200, 100)
        # ventana de dialogo ya tiene una box definida por defecto
        box = self.get_content_area()
        # se crea un grid para luego añadirlo al box
        self.grid = Gtk.Grid()
        box.add(self.grid)

        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "revisar preguntas"
        self.set_titlebar(header_bar)

        image_button_open = Gtk.Image()
        button_open = Gtk.Button()
        image_button_open.set_from_icon_name("document-open", 
                                             Gtk.IconSize.BUTTON) # Se define el icono.
        button_open.add(image_button_open) # Se añade el icono al boton abrir.
        #button_open.connect("clicked", self.open)
        button_open.set_tooltip_text("Abrir archivo")
        header_bar.pack_start(button_open)
        
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)

        self.tree = Gtk.TreeView()
        self.scroll.add(self.tree)

        self.grid.attach(self.scroll,0,1,6,4)

        self.show_all()

    def open(self, btn=None):
        pass