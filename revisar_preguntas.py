import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from abrir_archivo import Abrir_archivo


class Ventana_revisar(Gtk.Dialog):
    def __init__(self):
        super().__init__()

        self.set_default_size(600, 600)
        box = self.get_content_area() # Ventana de dialogo ya tiene una box definida por defecto.
        self.grid = Gtk.Grid()# Se crea un grid para luego añadirlo al box.
        box.add(self.grid)

        """
        Se crea header bar
        """
        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "revisar preguntas"
        self.set_titlebar(header_bar)

        """
        Se añade boton para abrir archivo y se agrega a header bar.
        """
        image_button_open = Gtk.Image()
        button_open = Gtk.Button()
        image_button_open.set_from_icon_name("document-open", 
                                             Gtk.IconSize.BUTTON) # Se define el icono.
        button_open.add(image_button_open) # Se añade el icono al boton abrir.
        button_open.connect("clicked", self.open)
        button_open.set_tooltip_text("Abrir archivo")
        header_bar.pack_start(button_open)
        
        """
        Se crea scroll y treeview, este ultimo va dentro de scroll.
        """
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)

        self.tree = Gtk.TreeView() # Se crea treeview
        self.cell = Gtk.CellRendererText()
        self.scroll.add(self.tree)

        self.grid.attach(self.scroll,0,1,6,4)

        self.show_all()

    def open(self, btn=None):
        """
        Se abre archivo, contenido se vuelve lista y se añade a treeview.
        """
        open_file = Abrir_archivo("*.csv")
        self.file, self.content = open_file.tipo_respuesta()
        """ 
        Se separa el titulo del resto del archivo y se convierte en una lista.
        """
        self.title = self.content[0].strip().split(",") 
        self.lista = Gtk.ListStore(*([str]*len(self.title)))
        self.tree.set_model(model=self.lista)
        """
        Resto del archivo tambien se convierte en lista
        """
        self.content = [linea.strip().split(",") for linea in self.content[1:]]

        for content in self.content:
            self.lista.append(content)

        for i in range(len(self.title)):
            col = Gtk.TreeViewColumn(self.title[i], self.cell, text=i)
            self.tree.append_column(col)


