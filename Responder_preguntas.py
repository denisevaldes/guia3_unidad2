import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from abrir_archivo import Abrir_archivo


class Responder_pregunta(Gtk.Window):
    
    def __init__(self):
        super().__init__()
        self.set_title("Test")
        self.set_border_width(30)
        self.set_default_size(600, 600)

        header_bar = Gtk.HeaderBar() # Se crea Header Bar.
        header_bar.set_show_close_button(True) # Se muestra boton de cerrar.
        header_bar.props.title = "Guia 3"
        self.set_titlebar(header_bar) #se añade Header Bar a la ventana.

        """
        Se crea boton de abrir que va en header bar.
        """
        image_button_open = Gtk.Image()
        button_open = Gtk.Button()
        image_button_open.set_from_icon_name("document-open", 
                                             Gtk.IconSize.BUTTON) # Se define el icono.
        button_open.add(image_button_open) # Se añade el icono al boton abrir.
        button_open.connect("clicked", self.open_file)
        button_open.set_tooltip_text("Abrir archivo")
        header_bar.pack_start(button_open)

        """
        Se crea boton atras, para revisar preguntas anteriores.
        """
        self.button_back_ans = Gtk.Button(label="atras") 
        self.button_back_ans.set_hexpand(True)
        self.button_back_ans.connect("clicked", self.back_answer)

        """
        Se crea boton mostrar respuesta.
        """
        self.button_view_res= Gtk.Button(label="mostrar respuesta")
        self.button_view_res.set_hexpand(True)
        self.button_view_res.connect("clicked", self.view_response)

        """
        Se crea boton siguiente, para revisar preguntas siguientes.
        """
        self.button_next = Gtk.Button(label="siguiente")
        self.button_next.set_hexpand(True)
        self.button_next.connect("clicked", self.next_question)

        vbox =Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        vbox2 =Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

        self.add(vbox)
        vbox.pack_start(vbox2,True,True,0)
    
        """
        Text View izquierdo.
        """
        self.text_entry = Gtk.TextView() # Se agrega entrada
        self.textbuffer = self.text_entry.get_buffer()
        self.text_entry.set_vexpand(True)
        self.text_entry.set_editable(False)

        """
        Text View derecho.
        """
        self.text_response = Gtk.TextView()
        self.textbuffer2 = self.text_response.get_buffer()
        self.text_response.set_vexpand(True)
        self.text_response.set_editable(False)
        
        grid = Gtk.Grid()
        vbox2.pack_start(self.text_entry,True,True,0)
        vbox2.pack_end(self.text_response,True,True,0)
        vbox.pack_end(grid,True,True,0)

        """
        Se añaden botones a grid.
        """        
        grid.attach(self.button_back_ans, 0, 0, 1, 1)
        grid.attach(self.button_view_res, 1, 0, 1, 1)
        grid.attach(self.button_next, 2, 0, 1, 1)
        self.show_all()

        self.response = 0
        self.question = 0

    def open_file(self, btn = None):
       
        file = Abrir_archivo("*.csv")
        name, self.buffer_archivo = file.tipo_respuesta()
        self.content = [linea.strip().split(",") for linea in self.buffer_archivo[1:]]
        self.textbuffer.set_text(self.content[self.question][0])
    
    def back_answer(self, btn= None):
        """
        Se restan dos digitos de pregunta y respuesta para poder retroceder
        esto ya que en el boton de ver respuesta se le suma un digito
        a pregunta y respuesta
        """
        self.response -= 2
        self.question -=2
        self.textbuffer.set_text(self.content[self.question][0])
        self.textbuffer2.set_text("")

    def view_response(self, btn = None):

        """
        Se muestra la respuesta y se añade un digito a pregunta y respuesta
        """
        self.textbuffer2.set_text(self.content[self.response][1])
        
        self.response += 1
        self.question += 1

        if self.question == len(self.content):
            self.response = 0
            self.question = 0
        elif self.question == 0:
            self.response = len(self.content)
            self.question = len(self.content)
            
    def next_question(self, btn = None):

        """
        Se muestra la siguiente pregunta.
        """
        self.textbuffer.set_text(self.content[self.question][0])
        self.textbuffer2.set_text("")

