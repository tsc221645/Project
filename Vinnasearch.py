'''Universidad del Valle de Guatemala
Algoritmos y Programacion Basica
Proyecto Final :)
Vista Login Vinna'''

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#MAIN WINDOW ----------------------------------------------------------------
main_window = Tk(className =' Vinna search') #Ventana + nombre
main_window.geometry('1180x900')

#VIEWS -----------------------------------------------------------------------
canvas_rect1 = Canvas(width=1180, height=900)
canvas_rect1.create_rectangle(1180,900,0,0, outline='white', fill='#172b7c', width=1)
canvas_rect1.place(x=0, y=0)

#Rectangulos blancos
canvas_rect3 = Canvas(width=1100, height=600)
canvas_rect3.create_rectangle(1100,600,0,0,  fill='white', width=1, outline = 'white')
canvas_rect3.place(x=30, y=140)


#TREES ---------------------------------------------------------------------------

db_view = ttk.Treeview(main_window)
db_view['columns'] = ("Nombre Empleado", "Teléfono", "Ubicación", "Profesion", "Edad",'Correo','Experiencia')

db_view.column('#0',width=0,minwidth=0)
db_view.column("Nombre Empleado", width=200, minwidth=200)
db_view.column("Teléfono", width=150, minwidth=150)
db_view.column("Ubicación", width=150, minwidth=150)
db_view.column("Profesion", width=150, minwidth=150)
db_view.column('Edad', width=150,minwidth=150)
db_view.column('Correo', width=150, minwidth=150)
db_view.column('Experiencia',width=150,minwidth=15)

db_view.heading("Nombre Empleado", text="Nombre Empleado")
db_view.heading("Teléfono", text="Teléfono")
db_view.heading("Ubicación", text="Ubicación")
db_view.heading("Profesion", text='Profesion')
db_view.heading('Edad', text='Edad')
db_view.heading('Correo',text='Correo')
db_view.heading('Experiencia', text='Experiencia')

db_style = ttk.Style()
db_style.theme_use("clam")
db_style.configure("Treeview.Heading", font=("Cascadia Code", 16))
db_view.place(x=30,y=140)

#LABELS ----------------------------------------------------------------------
logo = Label(main_window, fg = 'white', text = 'Vinna', font = ('Cascadia Code', 12,'bold', 'underline'), bg = '#172b7c')
logo.place(x = 1100, y = 20)
title = Label(main_window, fg = 'white', text='Search', font=('Cascadia Code', 30, 'bold'), bg = '#172b7c')
title.place(x=30,y =20)

main_window.mainloop() #Main loop del programa