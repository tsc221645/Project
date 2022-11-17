from tkinter import *
from PIL import Image, ImageTk
from subprocess import call

# WINDOWS -----------------------------------------------------------------------------------------------------------------------
def call_window_home():
    call(["python", "VinnaHome.py"])

def home_main():
    main_window.destroy()
    call_window_home()

# MAIN WINDOW -------------------------------------------------------------------------------------------------------------------
main_window = Tk(className='Vinna')
main_window.geometry("1180x900")

# CREACIÓN DE RECTANGULO LATERAL ------------------------------------------------------------------------------------------------
canvas_rect1 = Canvas(width=1180, height=900)
canvas_rect1.create_rectangle(590,900,0,0, outline='white', fill='#172b7c', width=1)
canvas_rect1.place(x=0, y=0)

# CREACIÓN DE IMAGEN ------------------------------------------------------------------------------------------------------------
image = ImageTk.PhotoImage(file='img12.jpg')
canvas = Canvas(width=800, height=800)
canvas.create_image(10,570, image = image)
canvas.place(x=590, y=0)

# HOME BUTTON ------------------------------------------------------------------------------------------------------------------
home_button = Button(main_window,text = "Vinna", font = ("Cambria",14), fg='white', bg='#172b7c', command=home_main)
home_button.place(x=10,y=10)

# TEXTO DE PARRAFO ------------------------------------------------------------------------------------------------------------
etiqueta2 = Label(main_window,text = "¡Contacta al equipo Vinna!", font = ("Cambria",20), fg='white', bg='#172b7c')
etiqueta2.place(x=147,y=200)
etiqueta3 = Label(main_window,text = "En Vinna es un gusto poder atenderte,", font = ("Cambria",18), fg='white', bg='#172b7c')
etiqueta3.place(x=70,y=280)
etiqueta4 = Label(main_window,text = "envíanos tus comentarios o consultas y", font = ("Cambria",18), fg='white', bg='#172b7c')
etiqueta4.place(x=70,y=320)
etiqueta5 = Label(main_window,text = "nuestro equpo se estará poniendo", font = ("Cambria",18), fg='white', bg='#172b7c')
etiqueta5.place(x=70,y=360)
etiqueta6 = Label(main_window,text = "en contacto contigo", font = ("Cambria",18), fg='white', bg='#172b7c')
etiqueta6.place(x=70,y=400)

main_window.mainloop()