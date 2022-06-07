import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Abrir_ventana_about(Gtk.AboutDialog):
    def __init__(self):

        super().__init__()
        
        self.set_title("About")
        self.set_border_width(10)
        
        autores = ["Denise Valdes", "Sebastian Benavides"]
        self.set_authors(autores)
        self.set_program_name("Guia 3")
        self.set_version("1.0")
        self.set_logo_icon_name("help-about")

        self.show_all()

