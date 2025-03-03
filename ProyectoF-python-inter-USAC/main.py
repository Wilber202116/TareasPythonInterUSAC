from tkinter import *
import tkinter as tk
from tkinter import messagebox
from person import Person
import database

def ventana_registro():
    ventana_registro = tk.Tk()
    ventana_registro.title("Registrarse")
    ventana_registro.geometry("310x350")
    Label(ventana_registro,text="Bienvenido al registro").grid(row=0, column=0, columnspan=4, pady=10,padx=10)
    Label(ventana_registro,text="Identificacion (DPI, etc...):").grid(row=1, column=0, sticky=E, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Nombre:").grid(row=2, column=0, sticky=E, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Apellido:").grid(row=3, column=0, sticky=E,  columnspan=2, pady=10,padx=10)
    Label(ventana_registro, text="edad").grid(row=4, sticky=E,  column=0, columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Correo electronico:").grid(row=5, column=0, sticky=E,  columnspan=2, pady=10,padx=10)
    Label(ventana_registro,text="Contraseña:").grid(row=6, column=0, sticky=E,  columnspan=2, pady=10,padx=10)

    entryiden = Entry(ventana_registro)
    entrynombre = Entry(ventana_registro)
    entryapellido = Entry(ventana_registro)
    entryedad = Entry(ventana_registro)
    entrycorreo1 = Entry(ventana_registro)
    entrycontra1 = Entry(ventana_registro)

    entryiden.grid(row=1, column=2, columnspan=2, pady=10,padx=10)
    entrynombre.grid(row=2, column=2, columnspan=2, pady=10,padx=10)
    entryapellido.grid(row=3, column=2, columnspan=2, pady=10,padx=10)
    entryedad.grid(row=4, column=2, columnspan=2, pady=10,padx=10)
    entrycorreo1.grid(row=5, column=2, columnspan=2, pady=10,padx=10)
    entrycontra1.grid(row=6, column=2, columnspan=2, pady=10,padx=10)

    Button(ventana_registro, text="Registrar cuenta").grid(row=7, column=0, columnspan=4, pady=10,padx=10)

def control_inicio():
    global user_actual
    correo = entryCorreo.get()
    contraseña = entryContra.get()

    mensaje, persona = Person.iniciar_sesion(correo, contraseña, database.personas)
    
    if persona:
        user_actual = persona
        ventana_inicio(user_actual)
    else:
        messagebox.showerror("Error", mensaje)



def ventana_inicio(user_actual):

    ventana_inicio = tk.Tk()
    ventana_inicio.title("Perfil de usuario")
    ventana_inicio.geometry("310x180")

    def cerrar_sesion():
        ventana_inicio.destroy()

    root.destroy()

    if user_actual:
        Label(ventana_inicio, text="Perfil").pack()
Label(ventana_inicio, text="Nombre:").pack()
Label(ventana_inicio, text="Apellido:").pack()
        Button(ventana_inicio, text="Cerrar sesion", command=cerrar_sesion)

root = tk.Tk()
root.title("Iniciar sesion")
root.geometry("310x180")

Label(root, text="Bienvenido al inicio de sesion", font=("arial", 12)).grid(row=0, column=0, columnspan=4, pady=10,padx=10)
Label(root, text="Correo electronico", font=("arial", 12)).grid(row=1, column=0, sticky=W, columnspan=2, pady=10,padx=10)
Label(root, text="Contraseña", font=("arial", 12)).grid(row=2, column=0, sticky=W, columnspan=2, pady=10,padx=10)

entryCorreo = Entry(root)
entryCorreo.grid(row=1, column=2, columnspan=2, pady=10,padx=10)
entryContra = Entry(root)
entryContra.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

btnlogin = Button(root, text="Continuar", command=control_inicio)
btnlogin.grid(row=3, column=2, columnspan=2, pady=10, padx=10)

btnreg = Button(root, text="Registrarse", command=ventana_registro)
btnreg.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()