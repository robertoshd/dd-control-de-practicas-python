import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image # Imagenes

class Acercade:

    # Inicializar valores
    def __init__(self, root): # Parametro "self", y "root" = raiz
        self.ventanaS = root # Se asigna a la variable self.ventanaS el parametro "root"
        self.ventanaS = ctk.CTkToplevel() # Muestra esta clase como ventana emergente
        self.ventanaS.grab_set() # Funcion para no generar mas ventanas mientras este abierta esta clase
        self.ventanaS.geometry("630x340+300+200") # Tamaño y posición de la ventana
        self.ventanaS.title("Acerca de")
        self.ventanaS.configure(fg_color="#CCA9DD") # Color para la ventana
        self.ventanaS.resizable(0,0) # No maximizar
        self.diseñoAcerca() # Función que contiene el diseño del inicio de sesión

    def diseñoAcerca(self): # Función diseño de la sesión
        # Frame
        frameInicio=ctk.CTkFrame(master=self.ventanaS, width=270, height=300, fg_color="white")
        frameInicio.place(x=340, y=20) 
        
        # Imagen
        fondo = ctk.CTkImage(Image.open("./images/sesion_usuario2.png"), size=(300, 300))
        lblImagen = ctk.CTkLabel(self.ventanaS, image=fondo, text="")
        lblImagen.place(x=20, y=20)

        # Titulo
        label = ctk.CTkLabel(master=frameInicio, text="Control de practicas", font=("Bahnschrift SemiBold", 18), text_color="black")
        label.place(x=15, y=100)

        label = ctk.CTkLabel(master=frameInicio, text="© Derechos reservados. 2023", font=("Bahnschrift SemiBold", 18), text_color="black")
        label.place(x=15, y=130)

        label = ctk.CTkLabel(master=frameInicio, text="v 1.0.0", font=("Bahnschrift SemiBold", 18), text_color="black")
        label.place(x=15, y=160)

def main(): # Función para inicializar el programa
    raiz = ctk.CTk() # Se almacena la clase "CustomTkinter"
    ventana = Acercade(raiz) # Objeto de tipo "inicioSesión"
    raiz.mainloop()

if __name__ == '__main__': # Si el modulo se ejecuta en el programa principal
    main()
