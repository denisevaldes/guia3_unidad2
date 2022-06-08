# guia3_unidad2

Se crea una aplicación enfocada en ayudar a los estudiantes en su estudio. La aplicación esta basada en el metodo de estudio active-recall, por lo que a primera vista se tiene una pestaña en la cual se encuentra un editor de texto y en donde se pueden abrir archivos existentes, archivos nuevos y guardar los archivos, además de eso se encuentran 3 botones, los cuales tienen como finalidad crear preguntas, revisar las preguntas y test.

# Autores 

  - Denise Valdés
  - Sebastian Benavides
 
 # Ventana principal
 
 Esta clase(Ventana_principal) hereda de Gtk.Window y es la ventana principal del programa.
 En esta ventana se tiene un grid, un notebook y un header bar, los cuales actuan como contenedores de los demas widgets.
 Dentro del header bar se crean 4 botones, los cuales son:
 1. abrir archivo, en el cual abre un archivo ya existente mediante una ventana de dialogo filechooser 
 2. guardar archivo, el cual guarda archivos mediante una ventana de dialogo filechooser 
 3. crear archivo nuevo, el cual abre un nuevo tab en notebook con el nombre "sin titulo" 
 4. boton que lleva directo a una ventana about. 
 
 Debajo de header bar se encuentran 3 botones ingresados en grid, los cuales llevan a distintas ventanas de dialogo, bajo estos botones se encuentra un notebook en el cual se mostraran archivos de texto.
 
 # abrir_archivo
 
 clase que hereda de filechooserDialog a la cual se le entrega el pattern de los archivos que se desean arbrir para incorporarlos en los filtros.
 En esta ventana se abren los archivos escogidos ya sean csv o txt. 
 
 # Guardar archivo
 
 clase que hereda de filechooserDialog, encargada de guardar los archivos de texto txt
 
 # Ventana advertencia 
 
 clase que hereda de Gtk.Dialog, la cual aparece cuando usuario a cometido un error
 el mensaje que de depende del str entregado dependiendo de la situacion. 
 
 # Ventana crear preguntas 
 
 Clase que hereda de Gtk.Dialog, la cual tiene una grilla y un headbar como contenedores.
 En el headbar se tienen dos botones:
 1. abrir archivo ya existente 
 2. abrir archivo nuevo 
 Ademas de eso se tienen labels y entrys, esta ventana sirve para añadir preguntas y respuestas a archivos de clase csv. 
 
 # revisar preguntas 
 
 clase que hereda de Gtk.Dialog y en la cual se tiene una grilla y un headbar, en el head bar solo contiene un boton para abrir archivos csv, al momento de abrir el archivo este se mostrara en un treeview dentro de la ventana. 
 
 # responder preguntas
 
 clase que hereda de Gtk.Window y en la cual se muestran las preguntas y respuestas de algún archivo elegido.
 
 
 
