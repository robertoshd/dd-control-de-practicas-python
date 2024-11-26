import customtkinter as ctk
from customtkinter import *
from tkinter import ttk
from tkcalendar import Calendar

class DateEntry(ctk.CTkEntry):
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
        self.v_calendario_emergente()

    def v_calendario_emergente(self):
        top = ctk.CTkToplevel()
        top.grab_set()
        top.title("Calendario")
        cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)

        def seleccion_fecha():
            selected_date = cal.selection_get().strftime('%d-%m-%Y') # Formato de la fecha en el Entry
            self.delete(0, 'end')
            self.insert(0, selected_date)
            self.configure(state='readonly')
            top.destroy()

        button = ctk.CTkButton(top, text='Seleccionar', command=seleccion_fecha)
        button.pack(pady=10)

if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Date Entry Widget')

    date_entry = DateEntry(root, width=110, placeholder_text="Ingresa la fecha")
    date_entry.pack(padx=10, pady=10)

    root.mainloop()
