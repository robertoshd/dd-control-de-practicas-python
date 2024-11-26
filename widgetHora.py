import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

class TimeEntry(ctk.CTkEntry):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(state='readonly')
        self.bind('<FocusIn>', self.clic_entry)
        self.bind('<Button-1>', self.clic_entry)

    def clic_entry(self, event):
        self.configure(state='normal')
        self.delete(0, 'end')
        self.unbind('<FocusIn>')
        self.unbind('<Button-1>')
        self.v_tiempo_emergente()

    def v_tiempo_emergente(self):
        top = ctk.CTkToplevel()
        top.grab_set()
        top.title("Hora")
        horaVar = ctk.StringVar()
        minutoVar = ctk.StringVar()
        #segundoVar = ctk.StringVar()
        turnoVar = ctk.StringVar()
        top.geometry("210x100")

        horaVar.set('00')
        minutoVar.set('00')
        #segundoVar.set('00')
        #turnoVar.set('AM')

        etdHora = ctk.CTkEntry(top, width=30, textvariable=horaVar)
        etdHora.place(x=20, y=5)

        lblPunto1 = ctk.CTkLabel(top, text=':', font=('TkDefaultFont', 20))
        lblPunto1.place(x=60, y=5)

        etdMinuto = ctk.CTkEntry(top, width=30, textvariable=minutoVar)
        etdMinuto.place(x=75, y=5)

        lblPunto2 = ctk.CTkLabel(top, text=':', font=('TkDefaultFont', 20))
        lblPunto2.place(x=115, y=5)

        #second_entry = ctk.CTkEntry(top, width=30, textvariable=second_var)
        #second_entry.place(x=130, y=5)

        def seleccion_tiempo():
            
            try:
                hora = int(horaVar.get())
                minuto = int(minutoVar.get())
                #second = int(segundoVar.get())
                turno = cmbTurno.get()

                if hora < 0 or hora > 23:
                    raise ValueError('La hora debe estar entre 0 y 23') # Indicar que se ha producido un error

                if minuto < 0 or minuto > 59:
                    raise ValueError('El minuto debe estar entre 0 y 59')

                #if second < 0 or second > 59:
                #    raise ValueError('El segundo debe estar entre 0 y 59')

                horaSeleccionada = '{:02d}:{:02d} - {}'.format(hora, minuto, turno)
                self.delete(0, 'end')
                self.insert(0, horaSeleccionada)
                self.configure(state='readonly')
                top.destroy() #Cerrar ventana emergente al seleccionar la hora

            except ValueError as e:
                messagebox.showerror('Error', str(e))

        cmbTurno = ctk.CTkComboBox(top, variable=turnoVar, width=60, state="readonly", 
                                values = ("AM", "PM"))
        cmbTurno.place(x=130, y=5)
        cmbTurno.bind("<<ComboboxSelected>>", seleccion_tiempo)

        button = ctk.CTkButton(top, text='Seleccionar', command=seleccion_tiempo)
        button.place(x=35, y=50)

if __name__ == '__main__':
    root = ctk.CTk()

    etdTiempo = TimeEntry(root, width=100, placeholder_text="Ingresa la hora")
    etdTiempo.pack(padx=10, pady=10)

    root.mainloop()
