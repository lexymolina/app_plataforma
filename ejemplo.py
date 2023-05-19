
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
    toplevel_datos_niño.title("Lexy Juliana Mato Molina")
    toplevel_datos_niño.resizable(False, False)
    toplevel_datos_niño.geometry("500x500")
    toplevel_datos_niño.config(bg="white")

    # etiqueta para informacion academica
    lb_informacion = Label(toplevel_datos_niño, text = "INFORMACION ACADEMICA ")
    lb_informacion.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_informacion.place(x=100, y=30)

    # etiqueta para los datos del estudiante
    lb_datos = Label(toplevel_datos_niño, text = "ASIGNATURAS: ")
    lb_datos.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_datos.place(x=20, y=150)

    combo = ttk.Combobox(toplevel_datos_niño, state="reandonly",values=["valores","sociales","castellano","fisica","matematicas","ciencias politicas","religion","edu. fisica","filosofia","ingles","artistica","quimica","sistemas","estadistica"])
    combo.place(x=200,y=150)

    # etiqueta para nota cognitiva
    lb_nota_cognitiva = Label(toplevel_datos_niño, text = "cognitivo: ")
    lb_nota_cognitiva.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_cognitiva.place(x=20, y=200)

    #caja de texto para nota cognitiva
    entry_nota_cognitiva = Entry(toplevel_datos_niño)
    entry_nota_cognitiva.place(x=200, y=200)

    # etiqueta para nota procediemental
    lb_nota_procedimental = Label(toplevel_datos_niño, text = "procediemental: ")
    lb_nota_procedimental.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_procedimental.place(x=20, y=250)

    #caja de texto para nota procedimental
    entry_nota_procedimental = Entry(toplevel_datos_niño)
    entry_nota_procedimental.place(x=200, y=250)

    # etiqueta para nota actitudinal
    lb_nota_actitudinal = Label(toplevel_datos_niño, text = "actitudinal: ")
    lb_nota_actitudinal.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_actitudinal.place(x=20, y=300)

    #caja de texto para nota actitudinal
    entry_nota_actitudinal = Entry(toplevel_datos_niño)
    entry_nota_actitudinal.place(x=200, y=300)

    # etiqueta para nota autoevalucacion
    lb_nota_autoevaluacion = Label(toplevel_datos_niño, text = "autoevalucacion: ")
    lb_nota_autoevaluacion.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_autoevaluacion.place(x=20, y=350)

    #caja de texto para nota autoevaluacion
    entry_nota_autoevaluacion = Entry(toplevel_datos_niño)
    entry_nota_autoevaluacion.place(x=200, y=350)

    # etiqueta para nota bimestral
    lb_nota_bimestral = Label(toplevel_datos_niño, text = "bimestral: ")
    lb_nota_bimestral.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_nota_bimestral.place(x=20, y=400)

    #caja de texto para nota bimestral
    entry_nota_bimestral = Entry(toplevel_datos_niño)
    entry_nota_bimestral.place(x=200, y=400)

    # etiqueta para nota definitiva
    nota_definitiva = Label(toplevel_datos_niño, text = "NOTA DEFINITIVA: ")
    nota_definitiva.config(bg="white", fg="black", font=("Helvetica", 15))
    nota_definitiva.place(x=20, y=450)

    #--------------------------------
    # frame resultados
    #--------------------------------
    frame_resultados = Frame(toplevel_datos_niño)
    frame_resultados.config(bg="black", width=120, height=30)
    frame_resultados.place(x=350, y=450)

    # area de texto para los resultados
    resultados = Text(frame_resultados)
    resultados.config(bg="red", fg="red", font=("Courier", 18))
    resultados.place(x=350,y=450,width=460,height=40)

    def calcular_nota_definitiva():
     nota_bimestral = float(entry_nota_bimestral.get())
     nota_cognitiva = float(entry_nota_cognitiva.get())
     nota_procedimental = float(entry_nota_procedimental.get())
     nota_actitudinal = float(entry_nota_actitudinal.get())
     nota_autoevaluacion = float(entry_nota_autoevaluacion.get())
     messagebox.showinfo(f"toplevel_datos_niño", "resultados encontrados")
     calcular_nota_definitiva = (0.3*nota_cognitiva) + (0.3*nota_procedimental) + (0.1*nota_actitudinal) + (0.1*nota_autoevaluacion) + (0.2*nota_bimestral)
     resultados.insert = {INSERT, f"\n{nota_definitiva}"}


    # boton para sumar
    bt_convertir = Button(toplevel_datos_niño,command=calcular_nota_definitiva, text="calcular")
    bt_convertir.place(x=210, y=450, width=100, height=25)




# abrir toplevel datos del niño
def abrir_toplevel_datos_niño1():
    global toplevel_datos_niño1
    toplevel_datos_niño1 = Toplevel()
    toplevel_datos_niño1.title("Lexy Juliana Mato Molina")
    toplevel_datos_niño1.resizable(False, False)
    toplevel_datos_niño1.geometry("300x300")
    toplevel_datos_niño1.config(bg="white")

    # etiqueta para datos de imc
    lb_informacion = Label(toplevel_datos_niño1, text = "DATOS DE IMC ")
    lb_informacion.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_informacion.place(x=55, y=10)

    # etiqueta para el peso
    lb_peso = Label(toplevel_datos_niño1, text = "peso: ")
    lb_peso.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_peso.place(x=30, y=50)

    #caja de texto para el peso
    entry_peso = Entry(toplevel_datos_niño1)
    entry_peso.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_peso.focus_set()
    entry_peso.place(x=120, y=50)

    # etiqueta para la estatura
    lb_estatura = Label(toplevel_datos_niño1, text = "estatura: ")
    lb_estatura.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_estatura.place(x=30, y=100)

    #caja de texto para la estatura
    entry_estatura = Entry(toplevel_datos_niño1)
    entry_estatura.config(bg="white", fg="red", font=("times new romann", 12), width=10)
    entry_estatura.focus_set()
    entry_estatura.place(x=120, y=100)

    # etiqueta para calculo del imc
    lb_calculo_IMC = Label(toplevel_datos_niño1, text = "calculo IMC: ")
    lb_calculo_IMC.config(bg="white", fg="black", font=("Helvetica", 15))
    lb_calculo_IMC.place(x=30, y=200)

    # boton para sumar
    bt_convertir = Button(toplevel_datos_niño1,text="calcular")
    bt_convertir.place(x=150, y=200, width=100, height=25)

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()


# titulo de la ventana
ventana_principal.title("Lexy Juliana Mato Molina")

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
boton_niña = Button(text="test", width=150, height=150, image=img, justify="right",command=abrir_toplevel_datos_niño1 )
boton_niña.place(x=500, y=500)

ventana_principal.mainloop()