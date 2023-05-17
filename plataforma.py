#----------------------
# App plataforma
#----------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox,ttk

# abrir toplevel datos del niño
def abrir_toplevel_datos_niño():
    global toplevel_datos_niño
    toplevel_datos_niño = Toplevel()
    toplevel_datos_niño.title("informacion del estudiante")
    toplevel_datos_niño.resizable(False, False)
    toplevel_datos_niño.geometry("500x600")
    toplevel_datos_niño.config(bg="white")

    # etiqueta para informacion academica
    lb_informacion = Label(toplevel_datos_niño, text = "INFORMACION ACADEMICA ")
    lb_informacion.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_informacion.place(x=100, y=20)

    # etiqueta para los datos del estudiante
    lb_datos = Label(toplevel_datos_niño, text = "ASIGNATURAS: ")
    lb_datos.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_datos.place(x=20, y=150)

    combo = ttk.Combobox(toplevel_datos_niño, state="reandonly",values=["valores","sociales","castellano","fisica","matematicas","ciencias politicas","religion","edu. fisica","filosofia","ingles","artistica","quimica","sistemas","estadistica"])
    combo.place(x=200,y=150)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "cognitivo: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=200)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=200)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "procediemental: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=250)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=250)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "actitudinal: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=300)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=300)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "actitudinal: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=350)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=350)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "autoevalucacion: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=400)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=400)

    # etiqueta para nota
    lb_nota = Label(toplevel_datos_niño, text = "bimestral: ")
    lb_nota.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota.place(x=20, y=450)

    #caja de texto para nota 
    entry_nota = Entry(toplevel_datos_niño)
    entry_nota.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_nota.focus_set()
    entry_nota.place(x=200, y=450)

    # etiqueta para nota definitiva
    lb_nota_definitiva = Label(toplevel_datos_niño, text = "NOTA DEFINITIVA: ")
    lb_nota_definitiva.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_definitiva.place(x=20, y=550)





#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()


# titulo de la ventana
ventana_principal.title("plataforma_estudiantes")

# tamaño de la ventana
ventana_principal.geometry("800x800")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

# logo de la app
logo = PhotoImage(file = "estudiantes.png")
lb_logo = Label(image=logo, bg="white")
lb_logo.place(x=290, y=30)

# etiqueta para los datos del estudiante
lb_datos = Label(ventana_principal, text = "DATOS DEL ESTUDIANTE: ")
lb_datos.config(bg="white", fg="black", font=("Helvetica", 15))
lb_datos.place(x=260, y=20)

# etiqueta para numero de telefono
lb_numero = Label(ventana_principal, text = "NUMERO DE TELEFONO: ")
lb_numero.config(bg="white", fg="black", font=("Helvetica", 15))
lb_numero.place(x=10, y=250)

#caja de texto para numero de telefono
entry_numero = Entry(ventana_principal)
entry_numero.config(bg="white", fg="black", font=("times new romann", 12), width=50)
entry_numero.focus_set()
entry_numero.place(x=260, y=247)

# etiqueta para el nombre
lb_nombre = Label(ventana_principal, text = "NOMBRE: ")
lb_nombre.config(bg="white", fg="black", font=("Helvetica", 15))
lb_nombre.place(x=10, y=300)

#caja de texto para el nombre
entry_nombre = Entry(ventana_principal)
entry_nombre.config(bg="white", fg="black", font=("times new romann", 12), width=50)
entry_nombre.focus_set()
entry_nombre.place(x=120, y=300)

# etiqueta para el grado
lb_nombre = Label(ventana_principal, text = "GRADO: ")
lb_nombre.config(bg="white", fg="black", font=("Helvetica", 15))
lb_nombre.place(x=10, y=350)

#caja de texto para el grado
entry_nombre = Entry(ventana_principal)
entry_nombre.config(bg="white", fg="black", font=("times new romann", 12), width=50)
entry_nombre.focus_set()
entry_nombre.place(x=100, y=350)

# etiqueta para la edad
lb_edad = Label(ventana_principal, text = "EDAD: ")
lb_edad.config(bg="white", fg="black", font=("Helvetica", 15))
lb_edad.place(x=10, y=400)

#caja de texto para la edad
entry_edad = Entry(ventana_principal)
entry_edad.config(bg="white", fg="black", font=("times new romann", 12))
entry_edad.focus_set()
entry_edad.place(x=90, y=400)

#boton niño
ing = PhotoImage(file="niño1.png")
boton_niño = Button(text="test", width=150, height=150, image=ing, justify="right", command=abrir_toplevel_datos_niño)
boton_niño.place(x=50, y=500)

#boton niña
img = PhotoImage(file="niña1.png")
boton_niña = Button(text="test", width=150, height=150, image=img, justify="right")
boton_niña.place(x=500, y=500)

ventana_principal.mainloop()