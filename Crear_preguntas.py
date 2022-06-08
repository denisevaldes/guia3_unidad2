import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from abrir_archivo import Abrir_archivo
from advertencia import Ventana_advertencia
import csv


class Ventana_crear_preguntas(Gtk.Dialog):
    
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
        header_bar.props.title = "Crear preguntas"
        self.set_titlebar(header_bar)

        image_button_open = Gtk.Image()
        button_open = Gtk.Button()
        image_button_open.set_from_icon_name("document-open", 
                                             Gtk.IconSize.BUTTON) # Se define el icono.
        button_open.add(image_button_open) # Se añade el icono al boton abrir.
        button_open.connect("clicked", self.open)
        button_open.set_tooltip_text("Abrir archivo")
        header_bar.pack_start(button_open)

        image_button_create_file = Gtk.Image()
        button_create_file = Gtk.Button()
        image_button_create_file.set_from_icon_name("document-new", 
                                                    Gtk.IconSize.BUTTON)
        button_create_file.add(image_button_create_file)
        button_create_file.connect("clicked", self.create_file)
        button_create_file.set_tooltip_text("Crear nuevo archivo")
        header_bar.pack_start(button_create_file)

        self.label_nombre = Gtk.Label(label = "nombre archivo")
        self.entrada_nombre = Gtk.Entry()
        self.entrada_nombre.connect("activate", self.nombre_csv)
        self.grid.attach(self.label_nombre, 1,1,1,1)
        self.grid.attach(self.entrada_nombre, 2,1,1,1)

        self.label_pregunta = Gtk.Label(label = "pregunta")
        self.entrada_pregunta = Gtk.Entry()
        self.entrada_pregunta.connect("activate", self.pregunta_csv)
        self.grid.attach(self.label_pregunta, 1,2,1,1)
        self.grid.attach(self.entrada_pregunta, 2,2,1,1)

        self.label_respuesta = Gtk.Label(label = "respuesta")
        self.entrada_respuesta = Gtk.Entry()
        self.entrada_respuesta.connect("activate", self.respuesta_csv)
        self.grid.attach(self.label_respuesta, 1,3,1,1)
        self.grid.attach(self.entrada_respuesta, 2,3,1,1)

        self.button_activar = Gtk.Button(label = "añadir")
        self.button_activar.connect("clicked", self.añadir_a_csv)
        self.button_activar.set_tooltip_text("añadir a archivo")
        self.grid.attach(self.button_activar, 1,4,1,1)

        self.show_all()

    def nombre_csv(self, ntd = None):
        self.nombre_archivo = self.entrada_nombre.get_text()
        self.nombre = self.nombre_archivo + ".csv"

    def pregunta_csv(self, ntd=None):
        self.pregunta = self.entrada_pregunta.get_text()
    
    def respuesta_csv(self, ntd=None):
        self.respuesta = self.entrada_respuesta.get_text()

    def open(self, btn= None):
        archivo = Abrir_archivo()
        self.nombre, contenido = archivo.tipo_respuesta()
        self.entrada_nombre.set_text(self.nombre)

    def create_file(self, btn=None):
        """
        falta que se pueda dar un nombre al csv, por que luego de crearlo
        cuando uno rellena el entry de nombre se crea otro archivo en vez de 
        cambiarle el nombre al archivo existente 
        """
        self.entrada_nombre.activate()
        try:
            if self.nombre_archivo != "":

                with open(self.nombre, "x") as csvfile:
                    fieldnames = ["pregunta", "respuesta"]
                    self.csvwriter = csv.writer(csvfile)
                    self.csvwriter.writerow(fieldnames)
            else:
                """
                se muestra dos veces la ventana de dialogo 
                1) sin nada
                2) se muestra con el mensaje 
                """
                self.ventana_mensaje = Ventana_advertencia(self,"no se ha ingresado nombre de archivo")
                self.ventana_mensaje.run()
                self.ventana_mensaje.destroy()
                print("nombre")
        except:
            self.ventana_mensaje = Ventana_advertencia(self,"el archivo ya existe" )
            self.ventana_mensaje.run()
            self.ventana_mensaje.destroy()
            print("archivo ya existe")


    def añadir_a_csv(self, ntd=None):

        self.entrada_pregunta.activate()
        self.entrada_respuesta.activate()
        with open(self.nombre, "a") as csvfile:
            self.csvwriter = csv.writer(csvfile)
            row = [self.pregunta,self.respuesta]
            self.csvwriter.writerow(row)
        self.entrada_pregunta.set_text("")
        self.entrada_respuesta.set_text("")
        
        
