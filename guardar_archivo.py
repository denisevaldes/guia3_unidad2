import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Guardar_archivo(Gtk.FileChooserDialog):
    def __init__(self, texto):

        super().__init__(action = Gtk.FileChooserAction.SAVE)
        
        self.texto = texto
        self.set_title("guardar archivo")
        self.set_border_width(10)
        self.set_default_size(400, 450)
        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )

        self.response = self.run()

        if self.response == Gtk.ResponseType.OK:

            """
            Se obtiene path de la carpeta en donde se
            quiere guardar archivo.
            Se obtiene el nombre del archivo,
            el cual es entregado a una variable
            """
            path  = self.get_current_folder()
            name_file_text = self.get_current_name()
            name_file = f"{path}/{name_file_text}.txt"
            """
            Se crea el archivo y se le entrega el texto que tenía dentro
            """
            with open(name_file, "w") as file:
                file.write(self.texto)
            self.destroy()
        elif self.response == Gtk.ResponseType.CANCEL:
            self.destroy()