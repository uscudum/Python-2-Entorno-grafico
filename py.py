from tkinter import *
import tkinter.font as tkFont
    
#widget Tk, instanciamos la ventana principal 
app = Tk()
#Definimos las catacterísticas de la fuente a utilizar
fontStyle = tkFont.Font(family="Lucida Grande", size=15)
#Título de la ventana
app.title("Nombre de la ventana")
#Dimensiones de la ventana
app.geometry("400x200")
#Configuración del color de fondo
app.configure(background='#900C3F')

#Funión a ejecutarse en command del botón
def calculo():
    dato = var_1.get() * var_2.get()
    texto = " * "  * dato
    var_3.set(texto)

# Tipos de variables 
# IntVar - StringVar - BooleanVar()
var_1 = IntVar()
var_2 = IntVar()
var_3 = StringVar()

#Etiqueta título
lbl_1 = Label(app, text = "Ingrese dos datos y observe su resultado", bg="#900C3F", fg="black", font=fontStyle)
lbl_1.pack()
#Caja de texto 1
entrada_1 = Entry(app, textvariable=var_1, justify="center")
entrada_1.place(x=150,y=50,width=40)
#Caja de texto 2
entrada_2 = Entry(app, textvariable=var_2, justify="center")
entrada_2.place(x=210,y=50,width=40)
#Botón
boton = Button(app, text="Calcular", justify="center", command=calculo, bg="#09724F", fg="white")
boton.place(x=170,y=80,width=60)
#Etiqueta resultado
lbl_1 = Label(app, textvariable=var_3, bg="#900C3F", fg="black")
lbl_1.pack()

#esperando a que el usuario haga algo
app.mainloop()