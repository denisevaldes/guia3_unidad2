import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Abrir_archivo(Gtk.FileChooserDialog):
    def __init__(self, pattern):

        super().__init__(action = Gtk.FileChooserAction.OPEN)
        
        self.set_title("abrir archivo")
        self.set_border_width(10)
        self.set_default_size(400, 450)

        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        self.pattern = pattern
        self.filtros(self)

        self.response = self.run()

    def tipo_respuesta(self, btn= None):
        """
        Dependiendo de si el usuario aprieta aceptar o cancelar, se dara una
        respuesta. En el caso de aceptar se ve de que tipo es el archivo y
        así seguir un camino de apertura distinto.
        """
        if self.response == Gtk.ResponseType.OK:
            
            new_file = self.get_filename() # Se obtiene el nombre del archivo 
            list_path = new_file.split("/")
            name_file = list_path.pop()
            name = name_file.split(".").pop()
            type_file = "".join(name) # Lista contenedora de tipo de archivo se vuelve str

            if type_file == "txt":

                with open(new_file, "r") as file: # se abre el archivo
                    lineas = file.readlines()
                    total_lineas = ""
                    for linea in lineas: 
                        total_lineas += linea
            else:
                with open(new_file,"r") as file:
                    total_lineas = file.readlines()
            self.destroy()        
            return name_file, total_lineas
        elif self.response == Gtk.ResponseType.CANCEL:
            self.destroy()

    def filtros(self, dialog):
        """
        Se restringen los archivos mostrados en la ventana de dialogo.
        """
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_pattern(self.pattern)
        dialog.add_filter(filter_text)

