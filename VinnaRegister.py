'''Universidad del Valle de Guatemala
Algoritmos y Programacion Basica
Proyecto Final :)
Vista Login Vinna'''

from tkinter import *
from PIL import Image, ImageTk

#FUNCIONES ---------------------------------------------------------------------------------------------------------------------------------
def ingreso_emp():
    nombre_emp = nombre1.get()
    correo_emp = correo1.get()
    edad_emp = edad1.get()
    telefono_emp = telefono1.get()
    area_emp = area1.get()

    print("Nombre: ", nombre_emp, "correo: ", correo_emp, "edad: ", edad_emp, "telefono: ", telefono_emp, "Area: ", area_emp)

def ingreso_trab():
    nombre_trab = nombre2.get()
    correo_trab = correo2.get()
    edad_trab = edad2.get()
    telefono_trab = telefono2.get()
    area_trab = area2.get()
    profesion_trab = profesion1.get()
    descripcion_trab = descripcion1.get()

    print("Nombre: ", nombre_trab, "correo: ", correo_trab, "edad: ", edad_trab, "telefono: ", telefono_trab, "Area: ", area_trab)


#MAIN WINDOW -------------------------------------------------------------------------------------------------------------------------------
main_window = Tk(className = 'Vinna')
main_window.geometry('1180x900')

#FIGURAS GEOMETICAS (ESTETICA)--------------------------------------------------------------------------------------------------------------
    #Fondo Azul
canvas_rect1 = Canvas(width=1180, height=900)
canvas_rect1.create_rectangle(1180,200,0,0, outline='white', fill='#172b7c', width=1)
canvas_rect1.place(x=0, y=0)
    #Cuadro Blanco
canvas_rect2 = Canvas(width=1000, height=500)
canvas_rect2.create_rectangle(1000,500,0,0, outline='white', fill='white', width=1)
canvas_rect2.place(x=75, y=130)

#LABELS -------------------------------------------------------------------------------------------------------------------------------------
logo = Label(main_window, text = 'Vinna', fg = 'white', bg = '#172b7c', font=('Cascadia Code',20 , 'underline'))
logo.place(x=50, y=20)

#INGRESO EMPLEADOR -------------------------------------------------------------------------------------------------------------------------
foto1 = Label(main_window, text = 'Sube tu fotografia', fg = 'black', bg = 'white', font = ('Cascadia Code', 12))
foto1.place(x=300, y=150)

n1 = Label(main_window, text='Nombre', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
n1.place(x=150, y=250)

e1 = Label(main_window, text='Edad', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
e1.place(x=150, y=320)

t1 = Label(main_window, text='Telefono', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
t1.place(x=300, y=320)

c1 = Label(main_window, text='Correo', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
c1.place(x=150, y=380)

a1 = Label(main_window, text='Area geografica', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
a1.place(x=150, y=440)

#INGRESO TRABAJADOR ---------------------------------------------------------------------------------------------------------------------------
foto2 = Label(main_window, text = 'Sube tu fotografia', fg = 'black', bg = 'white', font = ('Cascadia Code', 12))
foto2.place(x=700, y=150)

n2 = Label(main_window, text='Nombre', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
n2.place(x=550, y=250)

e2 = Label(main_window, text='Edad', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
e2.place(x=550, y=320)

t2 = Label(main_window, text='Telefono', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
t2.place(x=700, y=320)

c2 = Label(main_window, text='Correo', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
c2.place(x=550, y=380)

a2 = Label(main_window, text='Area geografica', fg = 'black', bg = 'white', font=('Cascadia Code', 12))
a2.place(x=550, y=440)

p1 = Label(main_window, text = 'Profesion', fg = 'black', bg = 'white', font = ('Cascadia Code', 12))
p1.place(x=850, y=250)

d1 = Label(main_window, text = 'Descripcion', fg = 'black', bg = 'white', font = ('Cascadia Code', 12))
d1.place(x=850, y=320)

#INPUTS ------------------------------------------------------------------------------------------------------------------
#Campos empleadores (input o label con el numero 1 de seguido hacen referencia a los empleadores)
nombre1 = Entry(main_window, width=29,bg='white',fg='black', font=('Cascadia Code', 12,)) 
nombre1.get()
nombre1.place(x=150, y=280)

edad1 = Entry(main_window, width=12,bg='white',fg='black', font=('Cascadia Code', 12,)) 
edad1.get()
edad1.place(x=150, y=350)

telefono1 = Entry(main_window, width=12,bg='white',fg='black', font=('Cascadia Code', 12,))
telefono1.get()
telefono1.place(x=300, y=350)

correo1 = Entry(main_window, width=29,bg='white',fg='black', font=('Cascadia Code', 12,)) 
correo1.get()
correo1.place(x=150, y=410)

area1 = Entry(main_window, width=29,bg='white',fg='black', font=('Cascadia Code', 12,))
area1.get()
area1.place(x=150, y=470)

#-----------------------------------------------------------------------------------------------------
#Campos trabajadores (input o label con el numero 2 de seguido hacen referencia a los trabajadores)
nombre2 = Entry(main_window, width=24,bg='white',fg='black', font=('Cascadia Code', 12,)) #INPUT Nombre
nombre2.get()#variable que almacena el email
nombre2.place(x=550, y=280)

edad2 = Entry(main_window, width=12,bg='white',fg='black', font=('Cascadia Code', 12,)) #INPUT Edad
edad2.get()#variable que almacena el email
edad2.place(x=550, y=350)

telefono2 = Entry(main_window, width=12,bg='white',fg='black', font=('Cascadia Code', 12,)) #INPUT Telefono
telefono2.get()#variable que almacena el email
telefono2.place(x=700, y=350)

correo2 = Entry(main_window, width=29,bg='white',fg='black', font=('Cascadia Code', 12,)) 
correo2.get()
correo2.place(x=550, y=410)

area2 = Entry(main_window, width=29,bg='white',fg='black', font=('Cascadia Code', 12,))
area2.get()
area2.place(x=550, y=470)

profesion1 = Entry(main_window, width=20,bg='white',fg='black', font=('Cascadia Code', 12,)) #INPUT Nombre
profesion1.get()#variable que almacena el email
profesion1.place(x=850, y=280)

descripcion1 = Entry(main_window, width=20,bg='white',fg='black', font=('Cascadia Code', 12,)) #INPUT Nombre
descripcion1.get()#variable que almacena el email
descripcion1.place(x=850, y=350)

#Hace falta pedir una contrasena para ambos perfiles.... Eso alterara la vista

#BOTONES -----------------------------------------------------------------------------------------------------------------
boton1 = Button(text='Ingresa como trabajador', bg = 'white', fg = '#172b7c', font=('Cascadia Code', 14, 'bold'), command=ingreso_emp)
boton1.place(x=150, y=520)
boton2 = Button(text='Ingresa como empleador', bg = '#172b7c', fg = 'white', font=('Cascadia Code', 14, 'bold'), command=ingreso_trab)
boton2.place(x=630, y=520)

#Hacen faltas las tildes y la logica para SQL
#Sin idea de como redondear botones y hacer lo de las fotografias
#Considero que se deberian delimitar las areas geograficas y las posibles edades

main_window.mainloop()