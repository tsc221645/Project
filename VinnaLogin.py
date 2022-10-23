'''Universidad del Valle de Guatemala
Algoritmos y Programacion Basica
Proyecto Final :)
Vista Login Vinna'''

from tkinter import *
from PIL import Image, ImageTk


#FUNCIONES -------------------------------------------------------------
def act_boton1(): #Una vez activada debe hacer la busqueda en la base de datos de trabajadores
    email = email_input.get()
    password = pass_input.get()
    print("Ingresando como Trabajador...\n"
        "Email: ", email, "Password: ", password)

def act_boton2(): #Despues hace la busqueda en la base de datos de empleadores#
    email = email_input.get()
    password = pass_input.get()
    print("Ingresando como Empleador...\n"
        "Email: ", email, "Password: ", password)

#MAIN WINDOW ------------------------------------------------------------
main_window = Tk(className = 'Vinna')
#w = main_window.winfo_screenmmwidth()
#h = main_window.winfo_screenheight()
#main_window.geometry("%dx%d" % (w, h))
main_window.geometry('1180x900')

#DEFINICION IMAGEN DE FONDO ---------------------------------------------
image = ImageTk.PhotoImage(file='image6.png')
canvas = Canvas(width = 1300, height = 900)
canvas.create_image(600,400, image = image)
canvas.place(x=0, y=0)
#------------------------------------------------------------------------ DO NOT TOUCH THIS >:)

#FIGURAS GEOMETICAS (ESTETICA)-------------------------------------------
canvas_rect1 = Canvas(width=450, height=500)
canvas_rect1.create_rectangle(450,500,0,0, outline='white', fill='white', width=1)
canvas_rect1.place(x=125, y=150)

#LABELS -----------------------------------------------------------------
m_bien = Label(main_window, text = "BIENVENIDO DE VUELTA", bg= 'white' ,font=('Cascadia Code', 16), fg = 'black') #BIENVENIDO DE VUELTA
m_bien.place(x=200, y=220)
m_bien2 = Label(main_window, text = "Bienvenido, por favor ingresa tus credenciales.", bg= 'white' ,font=('Cascadia Code', 8), fg = 'grey')#ingresa credenciales
m_bien2.place(x=200, y=250)
email_l = Label(main_window, text = "Email", bg= 'white' ,font=('Cascadia Code', 14, 'bold'), fg = 'black')
email_l.place(x=200, y=280)
pass_l = Label(main_window, text = "Contraseña", bg= 'white' ,font=('Cascadia Code', 14, 'bold'), fg = 'black')
pass_l.place(x=200, y=360)

#INPUT LABELS -----------------------------------------------------------
email_input = Entry(main_window, width=20,bg='white',fg='black', font=('Cascadia Code', 14,)) #INPUT EMAIL
email_input.get()#variable que almacena el email
email_input.place(x=200, y=320)

pass_input = Entry(main_window, width=20, bg='white', fg = 'black', font=('Cascadia Code', 14,), show = '*')#INPUT PASSWORD
pass_input.get() #variable que almacena el password
pass_input.place(x=200, y=400)

#BOTONES ----------------------------------------------------------------
boton1 = Button(text='Ingresa como trabajador', bg = '#172b7c', fg = 'white', font=('Cascadia Code', 14, 'bold'), command=act_boton1)
boton1.place(x=200, y=450)
boton2 = Button(text='Ingresa como empleador', bg = 'white', fg = '#172b7c', font=('Cascadia Code', 14, 'bold'))
boton2.place(x=200, y=510)

#una vez ingresados el password y la contrasena se tendra que hacer una busqueda inicial en la base de datos para ver si
#la contrasena existe, si no existe --> registrarse 
#si existe, ver que la contrasena ingresada haga match con la que corresponde al correo
 
main_window.mainloop()