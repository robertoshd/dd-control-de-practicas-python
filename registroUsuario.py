# Importación de librerias
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox # Mensaje dialogo
from PIL import ImageTk, Image # Imagenes

from conexion import DataBase

class registroUsuario:

    # Parametro "self", y "root" = raiz. Inicializar valores
    def __init__(self, root, *args): # Quitar argumento treeview
        self.ventanaR = root # Se asigna a la variable self.ventanaR el parametro "root"
        self.ventanaR = ctk.CTkToplevel() # Muestra esta clase como ventana emergente
        self.ventanaR.grab_set() # Funcion para no generar mas ventanas mientras este abierta esta clase
        self.ventanaR.geometry("630x310+300+180") # Tamaño y posición de la ventana
        self.ventanaR.title("Registro del docente")
        self.bd = DataBase() # Instancia de la clase DatabBase
        self.correo = StringVar()
        self.contraseña = StringVar()
        self.correo = "" # Inicialización para el correo
        self.contraseña = "" # y contraseña
        self.ventanaR.configure(fg_color="#CCA9DD")  # Color para la ventana
        self.ventanaR.resizable(0,0) # No maximizar
        self.diseñoRegistro() # Función que contiene el diseño de registro


    def diseñoRegistro(self): # Función diseño del registro

        # Frame
        frameRegistro=ctk.CTkFrame(master=self.ventanaR, width=270, height=270, fg_color="white")
        frameRegistro.place(x=340, y=20)

        # Imagen
        fondo = ctk.CTkImage(Image.open("./images/registro_usuario.png"), size=(320, 330))
        lblImagen = ctk.CTkLabel(self.ventanaR, image=fondo, text="")
        lblImagen.place(x=0, y=-30)

        # Titulo
        label = ctk.CTkLabel(master=frameRegistro, text="REGISTRO DEL DOCENTE", font=("Bahnschrift SemiBold", 20), text_color="black")
        label.place(x=23, y=30)

         # Campos correo y contraseña
        self.etdCorreo = ctk.CTkEntry(master=frameRegistro, placeholder_text="Ingrese un correo electrónico", textvariable=self.correo, width=220, height=40)
        self.etdCorreo.place(x=25, y=80)

        self.etdContraseña = ctk.CTkEntry(master=frameRegistro, placeholder_text="Ingrese una contraseña", textvariable=self.contraseña, show="*", width=220, height=40)
        self.etdContraseña.place(x=25, y=140)

        # Botón para registrar
        btnIniciar = ctk.CTkButton(master=frameRegistro, text="Registrar", font=("Bahnschrift SemiBold", 16), command=self.guardarDatos, width=220, height=40, fg_color="purple")
        btnIniciar.place(x=25, y=200)

    def guardarDatos(self): # Función para guardar los datos
        correo = self.etdCorreo.get().strip() # strip elimina los espacio en blanco
        contraseña = self.etdContraseña.get().strip()

        # === Validar datos ingresados ===
        # len verifica la longitud de una cadena.
        #Si longitud de correo es igual a 0 y contraseña también, que muestre el mensaje
        if len(correo) == 0 and len(contraseña) == 0:
            MessageBox.showwarning("Mensaje", "Debe llenar todos los campos.")
            return
        
        if len(correo) == 0: # Si la longitud del campo usuario es igual a 0
            MessageBox.showwarning("Mensaje", "El campo correo electrónico es obligatorio.")
            return
        
        if len(contraseña) == 0:
            MessageBox.showwarning("Mensaje", "El campo contraseña es obligatorio.")
            return

        # Si el campo correo es diferente de vacio y el campo contraseña también, que muestre el mensaje
        if (correo != "" and contraseña != ""):
            sql = "INSERT INTO usuarios (correo, contrasena) VALUES ('{0}', '{1}')".format(correo, contraseña)
            self.bd.cursor.execute(sql)
            self.bd.conexion.commit()
            MessageBox.showinfo("Registro de usuario", "¡Datos guardados correctamente!")
            self.ventanaR.destroy() # Cierra la ventana de registro

        # === Fin del registro ===


def main():
    raiz = ctk.CTk()
    ventanaPrincipal = registroUsuario(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    main()