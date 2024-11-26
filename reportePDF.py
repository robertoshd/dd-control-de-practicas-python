from fpdf import FPDF
from conexion import DataBase
from tkinter import filedialog

class Reporte(FPDF):
    def __init__(self):
        self.bd = DataBase()

    def exportar_pdf(self):
        cursor = self.bd.cursor
        # Obtenga los datos que desea incluir en el reporte
        consulta = "SELECT docente, materia, descripcion, hora, fecha FROM practicas"
        cursor.execute(consulta)

        # Cree un objeto FPDF y agregue una página al documento
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", "", 16)
        #self.pdf.text(x=50, y=10, txt="Holaaaa")

        column_widths = [60, 50, 40, 20, 20]

        # Agregar el encabezado de la tabla
        self.pdf.set_font("Arial", "B", 10)
        self.pdf.cell(w=0, h=15, txt = "REPORTE DE PRACTICAS A REALIZAR", border=1, ln=1, align='C')
        self.pdf.cell(column_widths[0], 10, "Docente", 1, align='C')
        self.pdf.cell(column_widths[1], 10, "Materia", 1, align='C')
        self.pdf.cell(column_widths[2], 10, "Motivo", 1, align='C')
        self.pdf.cell(column_widths[3], 10, "Fecha", 1, align='C')
        self.pdf.cell(column_widths[4], 10, "Hora", 1, align='C')
        self.pdf.ln()

        # Agregar los datos a la tabla en el PDF
        for fila in cursor:
            for i in range(len(fila)):
                self.pdf.cell(column_widths[i], 10, str(fila[i]), 1, align='C')
            self.pdf.ln()


        '''nombreArchivo = filedialog.asksaveasfilename(defaultextension='.pdf')

        # Guarde el documento utilizando el método output
        pdf.output(nombreArchivo, 'F')'''

        return self.pdf
