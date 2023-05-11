#----------------------
# App plataforma
#----------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

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
lb_logo = Label(ventana_principal, image=logo, bg="white")
lb_logo.place(x=280, y=30)

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
img = PhotoImage(file="niño.png")
boton_niño = Button(text="test", width=150, height=150, image=img,justify="right")
boton_niño.place(x=50, y=500)

ventana_principal.mainloop()