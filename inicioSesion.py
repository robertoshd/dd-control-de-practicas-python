# Importación de librerias
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox # Mensaje dialogo
from PIL import ImageTk, Image # Imagenes

# Importación de clases
from registroUsuario import registroUsuario
from menu import menuPrincipal
from conexion import DataBase

class inicioSesion:

    # Inicializar valores
    def __init__(self, root): # Parametro "self", y "root" = raiz
        self.ventanaS = root # Se asigna a la variable self.ventanaS el parametro "root"
        self.ventanaS = ctk.CTkToplevel() # Muestra esta clase como ventana emergente
        self.ventanaS.grab_set() # Funcion para no generar mas ventanas mientras este abierta esta clase
        self.ventanaS.geometry("630x340+300+200") # Tamaño y posición de la ventana
        self.ventanaS.title("Inicio de sesión")
        self.bd = DataBase()
        self.correo = StringVar()
        self.contraseña = StringVar()
        self.correo = ""  # Inicialización para el correo
        self.contraseña = "" # y contraseña
        self.ventanaS.configure(fg_color="#CCA9DD") # Color para la ventana
        self.ventanaS.resizable(0,0) # No maximizar
        self.diseñoSesion() # Función que contiene el diseño del inicio de sesión

    def diseñoSesion(self): # Función diseño de la sesión
        # Frame
        frameInicio=ctk.CTkFrame(master=self.ventanaS, width=270, height=300, fg_color="white")
        frameInicio.place(x=340, y=20) 
        
        # Imagen
        fondo = ctk.CTkImage(Image.open("./images/sesion_usuario2.png"), size=(300, 300))
        lblImagen = ctk.CTkLabel(self.ventanaS, image=fondo, text="")
        lblImagen.place(x=20, y=20)

        # Titulo
        label = ctk.CTkLabel(master=frameInicio, text="INICIO DE SESIÓN", font=("Bahnschrift SemiBold", 20), text_color="black")
        label.place(x=55, y=30)

        # Campos correo y contraseña
        self.etdCorreo = ctk.CTkEntry(master=frameInicio, placeholder_text="Correo electrónico", textvariable=self.correo, width=220, height=40)
        self.etdCorreo.place(x=25, y=80)

        self.etdContraseña = ctk.CTkEntry(master=frameInicio, placeholder_text="Contraseña", textvariable=self.contraseña, show="*", width=220, height=40)
        self.etdContraseña.place(x=25, y=140)

        # Botón para iniciar sesión
        btnIniciar = ctk.CTkButton(master=frameInicio, text="Iniciar", font=("Bahnschrift SemiBold", 16), command=self.validarDatos, width=220, height=40, fg_color="purple")
        btnIniciar.place(x=25, y=200)

        # Texto
        labelNoCuenta = ctk.CTkLabel(master=frameInicio, text="¿No tienes una cuenta?", font=("Bahnschrift", 14), text_color="black")
        labelNoCuenta.place(x=25, y=250)

        # Selección del texto con el evento "Click"
        labelRegistrar = Label(master=frameInicio, text="Registrate", font=("Bahnschrift", 10), cursor ="hand2", fg="purple", background="white")
        labelRegistrar.bind("<Button-1>", self.registrarUsuario) # Bind para asignar el evento al texto
        labelRegistrar.place(x=180, y=252)

    def registrarUsuario(self, *args): # Función para mostrar la ventana de registro de usuario
        self.ventanaS.destroy() # Destruye la ventana de inicio de sesión
        ventanaRegistroUs = registroUsuario(self.ventanaS, *args) # Se crea un objeto de la clase "registroUsuario"

    def validarDatos(self): # Función para validar los datos del registro
        correo = self.etdCorreo.get().strip() # strip elimina los espacio en blanco
        contraseña = self.etdContraseña.get().strip()

        sql = "SELECT * FROM usuarios WHERE correo = '"+correo+"' AND contrasena = '"+contraseña+"' "
        self.bd.cursor.execute(sql) # Almacenar en una variable el cursor
        #self.bd.conexion.commit()

        # === Validar datos ingresados ===
        # len verifica la longitud de una cadena.
        if len(correo) == 0 and len(contraseña) == 0: # Si la longitud del campo usuario es igual a 0
            MessageBox.showwarning("Mensaje", "Debe llenar todos los campos.")
            return
    
        if len(correo) == 0: # Si la longitud del campo usuario es igual a 0
            MessageBox.showwarning("Mensaje", "El campo correo electrónico es obligatorio.")
            return
        
        if len(contraseña) == 0:
            MessageBox.showwarning("Mensaje", "El campo contraseña es obligatorio.")
            return

        # Con la función fetchal
        if (self.bd.cursor.fetchall()):
            #ventana2.geometry("300x150+500+300")
            MessageBox.showinfo("Inicio de sesión", "¡Bievenida(o)! La sesión es correcta.")  # Cuadro de diálogo
            ventanaMenu = menuPrincipal(self.ventanaS) # Muestra la ventana de menu
            self.ventanaS.destroy() # Cierra la ventana de inicio de sesión

        # Si no, muestra el siguiente mensaje"
        else:
            MessageBox.showwarning("Inicio de sesión", "Lo siento, los datos son incorrectos. \nVerifique su correo y la contraseña.")
            self.etdCorreo.delete(0, END)
            self.etdContraseña.delete(0, END)
        
        # === Fin de la validación ===

def main(): # Función para inicializar el programa
    raiz = ctk.CTk() # Se almacena la clase "CustomTkinter"
    ventanaPrincipal = inicioSesion(raiz) # Objeto de tipo "inicioSesión"
    raiz.mainloop()

if __name__ == '__main__': # Si el modulo se ejecuta en el programa principal
    main()