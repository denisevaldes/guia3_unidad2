import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from abrir_archivo import Abrir_archivo
from guardar_archivo import Guardar_archivo
from Crear_preguntas import Ventana_crear_preguntas
from ventana_about import Abrir_ventana_about
from revisar_preguntas import Ventana_revisar
from Responder_preguntas import Responder_pregunta

class Ventana_principal(Gtk.Window):
    def __init__(self):    
        super().__init__()
        
        self.set_border_width(10)
        self.set_default_size(400, 450)
        
        self.grid = Gtk.Grid() # Se crea grilla.
        self.add(self.grid) # Se añade la grilla a la ventana.

        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "Guia 3"
        self.set_titlebar(header_bar) #se añade Header Bar a la ventana.

        """
        Se crea boton de abrir.
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
        Creacion de boton about
        """
        image_button_about = Gtk.Image()
        button_about = Gtk.Button()
        image_button_about.set_from_icon_name("help-about",
                                              Gtk.IconSize.BUTTON)
        button_about.add(image_button_about)
        button_about.connect("clicked", self.about_window)
        button_about.set_tooltip_text("información sobre programa")
        header_bar.pack_end(button_about)

        """
        Se crea boton guardar.
        """
        image_button_save = Gtk.Image()
        button_save = Gtk.Button()
        image_button_save.set_from_icon_name("document-save",
                                             Gtk.IconSize.BUTTON)
        button_save.add(image_button_save)
        button_save.connect("clicked", self.save)
        button_save.set_tooltip_text("Guardar archivo")
        header_bar.pack_start(button_save)


        image_button_create_file = Gtk.Image()
        button_create_file = Gtk.Button()
        image_button_create_file.set_from_icon_name("document-new", 
                                                    Gtk.IconSize.BUTTON)
        button_create_file.add(image_button_create_file)
        button_create_file.connect("clicked", self.create_file)
        button_create_file.set_tooltip_text("Crear nuevo archivo")
        header_bar.pack_start(button_create_file)

        """
        Creacion de boton crear pregunta
        """
        self.button_create_question = Gtk.Button()
        self.button_create_question.set_label("Crear preguntas")
        self.button_create_question.connect("clicked", self.create_question)
        self.grid.attach(self.button_create_question,0,0,1,1)

        """
        Se crea boton para revisar preguntas
        """
        self.button_questions_view = Gtk.Button()
        self.button_questions_view.set_label("revisar preguntas")
        self.button_questions_view.connect("clicked", self.view_questions)
        self.grid.attach(self.button_questions_view,1,0,1,1)

        """
        Se crea boton para active-recall/ practicar preguntas
        """
        self.button_answer_question = Gtk.Button()
        self.button_answer_question.set_label("test")
        self.button_answer_question.connect("clicked", self.answer_questions)
        self.grid.attach(self.button_answer_question,2,0,1,1)

        """
        Creacion de notebook.
        """        
        self.notebook = Gtk.Notebook(vexpand=True, hexpand = True) # Se crea notebook
        self.grid.attach(self.notebook,0,1,8,8) # se añade notebook a grid
        
        """
        Se crea la primera pag mostrada en el notebook.
        """
        self.create_tab_notebook("", "sin titulo")

    def about_window(self, btn=None):
        about = Abrir_ventana_about()

    def answer_questions(self, btn= None):
        dialog_answer = Responder_pregunta()

    def view_questions(self, btn= None):
        view_ques = Ventana_revisar()

    def create_question(self, btn = None):
        create_ques = Ventana_crear_preguntas()

    def create_file(self, btn = None):
        """
        Cuando se crea una pagina nueva en notebook, se llama al 
        metodo de la clase encargado de crearlas y se le asigna el nombre de
        "sin titulo"
        """
        self.create_tab_notebook("","sin titulo")

    def on_tab_close(self, btn = None):
        """
        Se remmueve pagina de notebook
        """
        self.notebook.remove_page(self.notebook.get_current_page())


    def open(self, btn = None):
        """
        Se abre archivo.
        """
        try:
            archivo = Abrir_archivo("*.txt")
            nombre, buffer_archivo = archivo.tipo_respuesta()
            self.create_tab_notebook(buffer_archivo,nombre)
        except:
            print("se cancelo la apertura de archivo")
    
    def save(self, btn = None):
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        self.text  = self.textbuffer.get_text(start_iter, end_iter, True)
        #self.text = self.textbuffer.props.text
        save_file = Guardar_archivo(self.text)

    def create_tab_notebook(self,buffer, nombre):
        """
        tendría que pasar el buffer y el nombre
        """
        self.scroll = Gtk.ScrolledWindow()
        self.text_view1 = Gtk.TextView() # Se crea text view.
        self.textbuffer = self.text_view1.get_buffer() # Buffer se refiere al espacio en memoria utilizado
        self.textbuffer.set_text(buffer)
        self.scroll.add(self.text_view1) # Se añade a text view a scrol.

        header1 = Gtk.HBox()
        self.label1 = Gtk.Label(label = nombre)
        image = Gtk.Image()
        image.set_from_icon_name("window-close", Gtk.IconSize.BUTTON)
        close_button1 = Gtk.Button()
        close_button1.add(image)
        close_button1.set_relief(Gtk.ReliefStyle.NONE) # se quitan los bordes de boton
        close_button1.connect("clicked", self.on_tab_close)
        header1.pack_start(self.label1,expand = True,
                           fill = True, padding = 0)
        header1.pack_end(close_button1, expand = False,
                         fill = False, padding = 0)

        self.notebook.insert_page(self.scroll,header1,0)
        self.show_all()
        header1.show_all()

if __name__ == "__main__":

    win = Ventana_principal()
    win.show_all()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()

