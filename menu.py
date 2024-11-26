from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox # Mensaje dialogo
from tkinter import filedialog

from registroPracticas import registro
from acercaDe import Acercade
from conexion import DataBase
from reportePDF import Reporte

class menuPrincipal(Frame):
    
    def __init__(self, root):
        Frame.__init__(self, root)
        self.ventanaMenu = root
        self.ventanaMenu = ctk.CTkToplevel()
        self.ventanaMenu.grab_set() # Funcion para no generar mas ventanas mientras este abierta esta clase
        menu = Menu(self.ventanaMenu)
        self.ventanaMenu.config(menu=menu)
        self.ventanaMenu.geometry('970x510+140+100')
        self.ventanaMenu.title("Practicas laboratorio de computo")
        self.ventanaMenu.configure(fg_color="#9DCC98")
        self.ventanaMenu.resizable(0,0)

        self.bd = DataBase()
        self.reporte = Reporte()
        
        
        fileMenu = Menu(menu, tearoff=False)
        fileMenu.add_command(label="Nueva practica", command=self.mostrarRegistro)
        fileMenu.add_command(label="Salir", command=self.exitProgram)
        menu.add_cascade(label="Archivo", menu=fileMenu)

        practicasMenu = Menu(menu, tearoff=False)
        practicasMenu.add_command(label="Eliminar", command=self.eliminarPractica)
        menu.add_cascade(label="Practicas", menu=practicasMenu)

        reportesMenu = Menu(menu, tearoff=False)
        reportesMenu.add_command(label="Exportar a PDF", command=self.generar_pdf)
        menu.add_cascade(label="Reportes", menu=reportesMenu)

        acercaMenu = Menu(menu, tearoff=False)
        acercaMenu.add_command(label="Derechos reservados", command=self.mostrarAcercade)
        menu.add_cascade(label="Acerca de", menu=acercaMenu)

        self.diseñoVentana()
        self.diseñoTabla()

    def exitProgram(self):
        exit()

    def mostrarRegistro(self):
        ventanaRegistro = registro(self.ventanaMenu, self.tabla)

    def mostrarAcercade(self):
        ventanaAcercade = Acercade(self.ventanaMenu)

    def generar_pdf(self):
        pdf = self.reporte.exportar_pdf()
        nombreArchivo = filedialog.asksaveasfilename(defaultextension='.pdf')

        # Guarde el documento utilizando el método output
        pdf.output(nombreArchivo, 'F')

        # Función para mostrar las materias en el ComboBox
    def consultaPracticas(self):
        consulta = "SELECT * FROM practicas"
        cursor = self.bd.cursor
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchall()

        # Crear una lista con los resultados obtenidos
        materias = []
        for fila in resultado:
            self.tabla.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5]))
    
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
        return filas


    def eliminarPractica(self):
        seleccion = self.tabla.focus()
        
        id = self.tabla.item(seleccion, 'text')
        print(id)

        if id == '':
            MessageBox.showwarning("Sistema", "Debe seleccionar un elemento")
        else:
            valores = self.tabla.item(seleccion, 'values')
            dato = valores[0] + " con " + valores[1]
            respuesta = MessageBox.askquestion("Sistema", "¿Deseas eliminar la practica? \n"+dato)

            if respuesta == MessageBox.YES:
                n = self.bd.eliminar_practica(id)
                if n == 1:
                    MessageBox.showinfo("Sistema", "Practica eliminada correctamente")
                    self.visualizarPracticas()
                else:
                    MessageBox.showerror("Sistema", "No fue posible eliminar la practica")
                pass
            else:
                pass
            

    def diseñoVentana(self):
        #editar = modificar(self.ventanaMenu, self.tabla)
        frameTitulo = ctk.CTkFrame(self.ventanaMenu, corner_radius=10, fg_color="#6EB470")
        frameTitulo.place(x=260, y=20)

        lblTitulo = ctk.CTkLabel(frameTitulo, text="Practicas en el laboratorio de sistemas", font=("Bahnschrift SemiBold", 24), text_color="white")
        lblTitulo.pack(pady=12, padx=10)

    def diseñoTabla(self):
        self.frameTabla = ctk.CTkFrame(self.ventanaMenu, width=870, height=350, fg_color="#6EB470")
        self.frameTabla.place(x=50, y=90)

        self.tabla = ttk.Treeview(self.frameTabla, columns=("Materia", "Docente", "Motivo", "Fecha", "Hora"))
        self.tabla.column("#0", width=80, anchor="center")
        self.tabla.column("Materia", width=210, anchor="center")
        self.tabla.column("Docente", width=180, anchor="center")
        self.tabla.column("Motivo", width=170, anchor="center")
        self.tabla.column("Fecha", width=90, anchor="center")
        self.tabla.column("Hora", width=90, anchor="center")

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("Materia", text="Materia")
        self.tabla.heading("Docente", text="Docente")
        self.tabla.heading("Motivo", text="Motivo")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Hora", text="Hora")
        self.tabla.place(x=10, y=11, width=850, height=328)
        self.tabla['selectmode'] = 'browse'
        self.consultaPracticas()
        
def main():
    raiz = ctk.CTk()
    ventanaPrincipal = menuPrincipal(raiz)
    #ventanaPrincipal.consultaPracticas()
    raiz.mainloop()

if __name__ == '__main__':
    main()