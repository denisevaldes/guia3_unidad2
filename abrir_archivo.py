import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Abrir_archivo(Gtk.FileChooserDialog):
    def __init__(self):

        super().__init__()
        
        self.set_title("abrir archivo")
        self.set_border_width(10)
        self.set_default_size(400, 450)

        self.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.filtros(self)

        response = self.run()

        if response == Gtk.ResponseType.OK:
            #se obtiene el nombre del archivo deseado
            nuevo_archivo = self.get_filename()
            # se abre el archivo deseado y se le entrega el texto 
            # de dicho archivo a la ventana de text_view
            with open(nuevo_archivo, "r") as file:
                lineas = file.readlines()
                total = ""
                for x in lineas: 
                    total += x
            self.textbuffer.set_text(total)
        elif response == Gtk.ResponseType.CANCEL:
            self.destroy()

        self.destroy()

    def filtros(self, dialog):
        #se restringen los archivos mostrados en la ventana de dialogo
        # filechooser a textos planos
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)
        pass

