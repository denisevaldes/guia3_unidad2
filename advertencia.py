import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana_advertencia(Gtk.Dialog):
    def __init__(self, parent, contenido,):
        super().__init__(transient_for=parent, flags=0)
        self.set_default_size(200, 150)
        self.add_buttons(
        Gtk.STOCK_OK,
        Gtk.ResponseType.OK,
        )

        """
        Se crea un titulo y un label, label sera llenado con un str 
        dado cada vez que se llame la clase
        """
        self.set_title("mensaje usuario")
        self.label = Gtk.Label(label = contenido)
        self.vbox.pack_start(self.label,True,True,0)
        self.show_all() 

