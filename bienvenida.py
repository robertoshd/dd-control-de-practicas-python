# Importación de librerias
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

# Importación de clases
from inicioSesion import inicioSesion
from registroUsuario import registroUsuario

ctk.set_default_color_theme("green") # Tema para el sistema: "blue" (estandar), "green", "dark-blue"

class bienvenidaP:

    # Inicializar variables
    def __init__(self, root): # Parametro "self", y "root" = raiz
        self.ventanaP = root  # Se asigna a la variable self.ventanaP el parametro "root"
        self.ventanaP.geometry("580x580+325+80") # Tamaño y posición de la ventana
        self.ventanaP.title("")
        self.ventanaP.resizable(0,0) # No maximizar
        self.diseñoBienvenida()  # Función que contiene el diseño de bienvenida

    def diseñoBienvenida(self): # Función diseño del registro

        # Frame de la imagen
        frameImagen=ctk.CTkFrame(self.ventanaP, width=580, height=500, fg_color="#CCA9DD")
        frameImagen.place(x=0, y=0)

        # Titulo
        labelTitulo = ctk.CTkLabel(frameImagen, text="CONTROL DE PRACTICAS \n LABORATORIO DE COMPUTO", font=("Bahnschrift Bold", 22), text_color="purple")
        labelTitulo.place(x=140, y=30)

        # Imagen de alumnos
        imgAlumnos = ctk.CTkImage(Image.open("./images/maestra_alumnos.png"), size=(450, 420))
        lblImagen = ctk.CTkLabel(frameImagen, image=imgAlumnos, text="")
        lblImagen.place(x=65, y=80)

        # Logo del itsp
        imgLogoTec = ctk.CTkImage(Image.open("./images/escudo_itsp.png"), size=(90, 90))
        lbllogoTec = ctk.CTkLabel(frameImagen, image=imgLogoTec, text="")
        lbllogoTec.place(x=10, y=10)

        # Logo de la carrera
        imgLogoISC = ctk.CTkImage(Image.open("./images/logoisc.png"), size=(130, 90))
        lbllogoISC = ctk.CTkLabel(frameImagen, image=imgLogoISC, text="")
        lbllogoISC.place(x=440, y=10)

        # Botón que manda a la ventana de iniciar sesión
        # Para cambiar el tamaño del botón, se debe ajustar el tamaño de la letra
        btnIni = ctk.CTkButton(master=self.ventanaP, text="Iniciar sesión", font=("Bahnschrift SemiBold", 18), command=self.mostrarSesion, width=180, height=40, fg_color="green")
        btnIni.place(x=100, y=520)

        # Botón que manda a la ventana de registro
        btnReg = ctk.CTkButton(master=self.ventanaP, text="Registarse", font=("Bahnschrift SemiBold", 18), command=self.mostrarRegistro, width=180, height=40, fg_color="green")
        btnReg.place(x=300, y=520)

    def mostrarSesion(self): # Función para mostrar la ventana de inicio de sesión
        ventanaInicioSesion = inicioSesion(self.ventanaP) # Objeto de tipo inicioSesion con parametro de la ventana actual
        self.ventanaP.withdraw()
        
    def mostrarRegistro(self): # Función para mostrar la ventana de registro
        ventanaRegistroUsuario = registroUsuario(self.ventanaP) # Objeto de tipo registroUsuario con parametro de la ventana actual

def main(): # Función para inicializar el programa
    raiz = ctk.CTk() # Se almacena la clase "CustomTkinter"
    ventanaPrincipal = bienvenidaP(raiz) # Objeto de tipo "inicioSesión"
    raiz.mainloop()

if __name__ == '__main__': # Si el modulo se ejecuta en el programa principal
    main()