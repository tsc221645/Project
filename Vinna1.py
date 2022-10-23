'''Universidad del Valle de Guatemala
Algoritmos y Programacion Basica
Proyecto Final :)
Vista Login Vinna'''

from tkinter import *
from PIL import Image, ImageTk

#MAIN WINDOW --------------------------------------------------------------------------------------------------------------------------------------
main_window = Tk(className = 'Vinna') #Nombre de la ventana principal
main_window.geometry('1200x680') #Tamano de la ventana principal

#FUNCIONES ---------------------------------------------------------------------------------------------------------------------------------------
image2 = ImageTk.PhotoImage(file='botonmenu1.png') #Asignacion de una foto a image2
image = ImageTk.PhotoImage(file='img4.png')#Asignacion de imagen, la foto debe estar en el mismo folder que el documento .py


def desplegar(): #funcion para desplegar el canvas a la izquierda
    #Funcion para desplegar el menu

    global canvas2, login, about, contact, exit
    canvas2 = Canvas(width=100, height=800)
    canvas2.create_image(600,340, image = image) #no encuentro como quitar el outline blanco >:|
    canvas2.place(x=0,y=0)

    login = Button(main_window, text = ' Login ' ,bg = 'black',fg = 'white', font=('Cascadia Code', 12)) #trigger para la pantalla de login
    login.place(x=12, y=12)

    about = Button(main_window, text='About Us', fg = 'white', bg = 'black', font=('Cascadia Code', 12))
    about.place(x=12, y=112)

    contact = Button(main_window, text='Contact \nUs', fg = 'white', bg = 'black', font=('Cascadia Code', 12))
    contact.place(x=12, y=212)

    exit = Button(main_window, text='   X   ', fg = 'white', bg = 'black', font=('Cascadia Code', 12),command=destroymenu)
    exit.place(x=12, y=628)

def destroymenu():
    login.after(100, login.destroy)
    about.after(100, about.destroy)
    contact.after(100, contact.destroy)
    exit.after(100, exit.destroy)
    canvas2.after(100, canvas2.destroy)

def crear_boton1(): #funcion para crear el boton
    menu = Button(main_window ,bg = 'black', image = image2, compound=LEFT, command=desplegar) #Propiedades del boton, en este caso el fondo es la imagen
    menu.place(x=10, y = 10)#Posicionamiento del boton :)

#DEFINICION IMAGEN DE FONDO -----------------------------------------------------------------------------------------------------------------------
canvas = Canvas(width = 1200, height = 800) #Creacion del canvas, lugar para posicionar la foto
canvas.create_image(590,340, image = image) #Implementacion de la imagen en el canvas, los primeros dos valores son de un corrimiento
canvas.place(x=0, y= 0) #posicionamiento del canvas en la ventana

#BOTONES ------------------------------------------------------------------------------------------------------------------------------------------
boton1 = Button(main_window, text = '   ¡Crea tu usuario!   ', fg = 'white', bg = '#172b7c', font=('Cascadia Code', 18)) #Boton para crear usuario
boton1.place(x=430, y = 430) #Posicionamiento del boton
#trigger para activar la pantalla para registrarse
crear_boton1()


#LOOP MAIN WINDOW ----------------------------------------------------------------------------------------------------------------------------------
main_window.mainloop()