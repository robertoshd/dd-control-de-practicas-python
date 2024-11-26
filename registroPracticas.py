import tkinter
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
#from tkcalendar import Calendar, DateEntry
from tkinter import messagebox as MessageBox # Mensaje dialogo
from widgetFecha import DateEntry
from widgetHora import TimeEntry

from conexion import DataBase

class registro:

    def __init__(self, root, treeview):
        self.ventanaR = root
        self.ventanaR = ctk.CTkToplevel()
        self.ventanaR.grab_set() # funcion para no generar mas ventanas mientras este abierta la ventana de login
        self.ventanaR.geometry("568x310+400+220")
        self.ventanaR.title("Registro")
        self.ventanaR.configure(fg_color="#9DCC98")

        self.bd = DataBase()
        self.tabla = treeview

        self.ventanaR.resizable(0,0)
        self.diseñoRegistro()

    # Función para ingresar una nueva practica
    def agregarDatos(self):
        cursor = self.bd.cursor

        materia = self.cmbMateria.get()
        docente = self.cmbDocente.get()
        descripcion = self.etdMotivo.get()
        fecha = self.etdFecha.get()
        hora = self.etdTiempo.get()
        datos = (materia, docente, descripcion, fecha, hora)

        if (materia != "" and docente != "" and descripcion != "" and fecha != "" and hora != ""):

            sql = "INSERT INTO practicas (materia, docente, descripcion, fecha, hora) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(materia, docente, descripcion, fecha, hora)
            cursor.execute(sql)
            self.bd.conexion.commit()

            MessageBox.showinfo("Registro", "La practica se ha registrado correctamente")
            #self.tabla.insert('', 'end', values=(materia, "Jesus Muñiz Blanco", descripcion, fecha, hora))
            self.etdMotivo.delete(0, 'end')
            self.etdFecha.delete(0, 'end')
            self.etdTiempo.delete(0, 'end')
            self.ventanaR.destroy()
            self.visualizarPracticas()
        else:
            MessageBox.showerror("Error", "Debe llenar todos los campos")

    def vaciarTabla(self):
        filas = self.tabla.get_children()
        for fila in filas:
            self.tabla.delete(fila)

    # Función para visualizar las practicas en la tabla
    def visualizarPracticas(self):
        self.vaciarTabla()
        cursor = self.bd.cursor
        
        consulta = "SELECT * FROM practicas"
        cursor.execute(consulta)
        filas = cursor.fetchall()

        for fila in filas:
            self.tabla.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5]))

    '''# Función para mostrar las materias en el ComboBox
    def consultaMaterias(self):
        consulta = "SELECT descripcion FROM materias"
        cursor = self.bd.cursor
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchall()

        # Crear una lista con los resultados obtenidos
        materias = []
        for row in resultado:
            materias.append(row[0])

        return materias
    
    # Función para mostrar los docentes en el ComboBox
    def consultaDocentes(self):
        consulta = "SELECT docente FROM docentes"
        cursor = self.bd.cursor
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchall()

        # Crear una lista con los resultados obtenidos
        materias = []
        for row in resultado:
            materias.append(row[0])

        return materias'''

    def diseñoRegistro(self):

        frameRegistro = ctk.CTkFrame(self.ventanaR, corner_radius=10, fg_color="#6EB470", width=548, height=290)
        frameRegistro.place(x=10, y=10)

        lblTRegistro = ctk.CTkLabel(frameRegistro, text="Registre su practica", font=("Bahnschrift SemiBold", 20), text_color="white")
        lblTRegistro.place(x=15, y=10)

        lblMateria = ctk.CTkLabel(frameRegistro, text="Seleccione la materia:", font=("Bahnschrift", 16))
        lblMateria.place(x=15, y=50)

        resultadoMateria = self.bd.consultaMaterias()
        self.cmbMateria = ctk.CTkComboBox(frameRegistro, values=resultadoMateria, state="readonly", width=240)
        self.cmbMateria.place(x=15, y=80)
        self.cmbMateria.bind("<<ComboBoxSelected>>", self.agregarDatos)

        lblMotivo = ctk.CTkLabel(frameRegistro, text="Docente:", font=("Bahnschrift", 16))
        lblMotivo.place(x=290, y=50)

        resultadoDocentes = self.bd.consultaDocentes()
        self.cmbDocente = ctk.CTkComboBox(frameRegistro, values=resultadoDocentes, state="readonly", width=240)
        self.cmbDocente.place(x=290, y=80)
        self.cmbDocente.bind("<<ComboBoxSelected>>", self.agregarDatos)

        lblMotivo = ctk.CTkLabel(frameRegistro, text="Motivo:", font=("Bahnschrift", 16))
        lblMotivo.place(x=15, y=130)
        self.etdMotivo = ctk.CTkEntry(frameRegistro, width=240)
        self.etdMotivo.place(x=15, y=160)

        lblFecha = ctk.CTkLabel(frameRegistro, text="Seleccione:", font=("Bahnschrift", 16))
        lblFecha.pack()
        lblFecha.place(x=290, y=130)

        self.etdFecha = DateEntry(frameRegistro, width=100, placeholder_text="Fecha")
        self.etdFecha.place(x=290, y=160)

        self.etdTiempo = TimeEntry(frameRegistro, width=100, placeholder_text="Hora")
        self.etdTiempo.place(x=400, y=160)

        btnGuardar = ctk.CTkButton(frameRegistro, text="Guardar", command=self.agregarDatos, fg_color="Purple", width=100, font=("Bahnschrift", 15))
        btnGuardar.place(x=430, y=230)

def main():
    raiz = ctk.CTk()
    ventanaPrincipal = registro(raiz,treeview=0)
    raiz.mainloop()

if __name__ == '__main__':
    main()