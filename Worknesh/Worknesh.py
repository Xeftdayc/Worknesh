from tkinter import ttk 
from tkinter import *
import tkinter as tk
import sqlite3

class Persona:
    # connection dir property
    db_name = 'dbworknesh.db'

    def __init__(self, window):
        # Inicialization de Ventana
        self.wind = window
        self.wind.title('Registro de Worknesh')

        # Creando el Contenedor del Frame
        frame = LabelFrame(self.wind, text = 'Registrar Area')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Ingreso del Area
        Label(frame, text = 'Area: ').grid(row = 1, column = 0)
        self.Area = Entry(frame)
        self.Area.focus()
        self.Area.grid(row = 1, column = 1)
        
        # Ingreso del Detalle
        Label(frame, text = 'Detalle: ').grid(row = 2, column = 0)
        self.Detalle = Entry(frame)
        self.Detalle.grid(row = 2, column = 1)

        # Button de Agregar Registro
        ttk.Button(frame,text = 'Guardar Datos', command = self.add_persona).grid(row = 3,columnspan = 2, sticky = W + E)

        # Mensajes de Salida
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W+E)
        
        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('1','2','3'), show="headings")
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('1', text ='ID')
        self.tree.column('1', width=30, anchor = 'center')
        self.tree.heading('2', text ='Area')
        self.tree.column('2', width=150, anchor = 'center')
        self.tree.heading('3', text ='Detalle')
        self.tree.column('3', width=250, anchor = 'center')

       
        # Botones
        ttk.Button(text = 'ELIMINAR').grid(row = 5, column = 0, stick = W + E)
        ttk.Button(text = 'EDITAR').grid(row = 5, column = 1, stick = W + E)

        # Mostrando datos en Rows
        self.get_persona()

    # Funcion de ejecucion de busqueda en la BD
    def run_query(self,query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    # Obtener datos de la Base de Datos
    def get_persona(self):
        # Limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Obteniendo Datos
        query = 'SELECT * FROM tArea ORDER BY area DESC'
        db_rows = self.run_query(query)
        # Buscando Datos
        for row in db_rows:
            self.tree.insert("", tk.END, values=row)
            print(row)


    # User input validation 
    def validation(self):
        return len(self.Area.get()) !=0 and len(self.Detalle.get()) !=0

    def add_persona(self):
        if self.validation():
            query = 'INSERT INTO tArea VALUES(NULL, ?, ?)'
            parameters = (self.Area.get(), self.Detalle.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Registro de Area {} añadido Satisfactoriamente'.format(self.Area.get())
            self.Area.delete(0,END)
            self.Detalle.delete(0,END)
        else:
            self.message['text'] = 'Invalido, Datos requeridos'
        self.get_persona()

if __name__ == '__main__':
    window = Tk()
    application = Persona(window)
    window.mainloop()