import time
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from abrir_archivo import Abrir_archivo


class Ventana_principal(Gtk.Window):
    def __init__(self):
        
        super().__init__()
        
        self.set_border_width(10)
        self.set_default_size(400, 450)
        
        self.grid = Gtk.Grid() # Se crea grilla.
        self.add(self.grid) # Se añade la grilla a la ventana.

        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "HeaderBar example"
        self.set_titlebar(header_bar) #se añade Header Bar a la ventana.

        """
        Se crea botón de abrir el cual contiene un icono. 
        icono se crea con la clase Gtk.Image().
        """
        image_button_open = Gtk.Image()
        image_button_open.set_from_icon_name("document-open", Gtk.IconSize.BUTTON) # Se define el icono.
        button_open = Gtk.Button()
        button_open.add(image_button_open) # Se añade el icono al boton abrir.
        button_open.connect("clicked", self.open)
        button_open.set_tooltip_text("Abrir archivo") # Se crea una etiqueta que será mostrada cuando el mouse este sobre el boton.
        header_bar.pack_start(button_open) # Pack start es usado para poner el boton al inicio del Header Bar.

        self.notebook = Gtk.Notebook() # Se crea notebook
        self.grid.attach(self.notebook,2,0,8,8) # Attach(child, left, top, width, height) se añade notebook a grid
        
        """
        Se crea la primera pág mostrada en el notebook.
        """
        self.page1 = Gtk.ScrolledWindow() 
        self.page1.set_hexpand(True)
        self.page1.set_vexpand(True)
        
        self.text_view = Gtk.TextView() # Se crea text view.
        self.textbuffer = self.text_view.get_buffer() # Buffer se refiere al espacio en memoria utilizado
        self.page1.add(self.text_view) # Se añade a text view a scrol.
        self.notebook.append_page(self.page1,Gtk.Label(label="3"))

    def open(self, btn = None):
        Abrir_archivo()


if __name__ == "__main__":

    ventana1 = Ventana_principal()
    ventana1.show_all()
    ventana1.connect("destroy", Gtk.main_quit)
    Gtk.main()