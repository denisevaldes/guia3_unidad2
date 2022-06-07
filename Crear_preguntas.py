import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from abrir_archivo import Abrir_archivo
import csv


class Ventana_crear_preguntas(Gtk.Dialog):
    
    def __init__(self):
        super().__init__()

        self.set_title("mensaje")
        self.set_default_size(200, 150)
        # ventana de dialogo ya tiene una box definida por defecto
        box = self.get_content_area()
        # se crea un grid para luego añadirlo al box
        self.grid = Gtk.Grid()
        box.add(self.grid)

        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "HeaderBar example"
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
        archivo.tipo_respuesta()

    def create_file(self, btn=None):
        
        self.nombre = "sin titulo.csv"

        with open(self.nombre, "w") as csvfile:
            fieldnames = ["pregunta", "respuesta"]
            self.csvwriter = csv.writer(csvfile)
            self.csvwriter.writerow(fieldnames) 

    def añadir_a_csv(self, ntd=None):
        self.entrada_pregunta.activate()
        self.entrada_respuesta.activate()
        with open(self.nombre, "a") as csvfile:
            self.csvwriter = csv.writer(csvfile)
            row = [self.pregunta,self.respuesta]
            self.csvwriter.writerow(row)
        
