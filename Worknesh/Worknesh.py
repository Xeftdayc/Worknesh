from tkinter.messagebox import showinfo
#from tkinter import *
from tkinter import ttk 

import tkinter as tk
import sqlite3
import dbquery


# Estructure Page in Page
class appWork(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, Dashboard, modRegistro, modVacaciones, Viewlib):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Modulo Login
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbTitle = tk.Label(self, text = "Worknesh: Sistema de Login", font=('arial', 20))
        lbTitle.pack()
        #foto = tk.PhotoImage(file="LOGO.png")
        #tk.Label(self, image=foto).pack()

        lbUser = tk.Label(self, text="User ID:")
        lbUser.pack(pady=10,padx=10)
        USERNAME = tk.StringVar()
        tbUser = tk.Entry(self, textvariable=USERNAME)
        tbUser.pack(pady=10,padx=10)
        tbUser.focus()
        lbPswd = tk.Label(self, text="Password")
        lbPswd.pack(pady=10,padx=10)
        PASSWORD = tk.StringVar()
        tbPswd = tk.Entry(self, textvariable=PASSWORD, show="*")
        tbPswd.pack(pady=10,padx=10)
        lbl_text = tk.Label(self, text="Ingrese sus credenciales", fg="red")
        lbl_text.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Login", font=('new times roman', 14), width=10, bd=5, pady=2,
                            command=lambda: controller.show_frame(Dashboard))
        button1.pack()

        button2 = tk.Button(self, text="Back", font=('new times roman', 14), width=10, bd=5, pady=2,
                            command=lambda: controller.show_frame(Dashboard))
        button2.pack()

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.wind = parent

        label = tk.Label(self, text="Bienvenido Usuario")
        label.pack(pady=10,padx=10)

        lbTitle = tk.Label(self, text = "Worknesh: Panel de Administracion", font=('arial', 20))
        lbTitle.pack()
        
        # Creando el Contenedor del Frame
        frame2 = tk.LabelFrame(self.wind, text = 'Registrar Area')
        frame2.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Ingreso del Area
        tk.Label(frame2, text = 'Area: ').grid(row = 1, column = 0)
        self.Area = tk.Entry(frame2)
        self.Area.focus()
        self.Area.grid(row = 1, column = 1)

        btnRegistro = tk.Button(self, text="Modulo de Registro", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(modRegistro))
        btnRegistro.pack(fill="both")
        btnAsistencia = tk.Button(self, text="Modulo de Asistencia", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(Dashboard))
        btnAsistencia.pack(fill="both")
        btnVacaciones = tk.Button(self, text="Modulo de Vacaciones", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(modVacaciones))
        btnVacaciones.pack(fill="both")
        btnPapeletas = tk.Button(self, text="Modulo de Papeletas", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(Dashboard))
        btnPapeletas.pack(fill="both")

        button2 = tk.Button(self, text="Modulo de Vista de Elementos", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(Viewlib))
        button2.pack(fill="both")

        button3 = tk.Button(self, text="Delete Librarian", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(Dashboard))
        button3.pack(fill="both")

        button4 = tk.Button(self, text="Logout", font=('calibri', 14), bd=5, pady=5,
                            command=lambda: controller.show_frame(Dashboard))
        button4.pack()


class modRegistro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Variables
        tbArea = tk.StringVar()
        tbDetalle = tk.StringVar()

        # Frame
        Top = tk.Frame(self, bd=2)
        Top.pack()
        Form = tk.Frame(self, width=800, height=400)
        Form.pack()

        # Labels
        lbTitle = tk.Label(Top, text="Worknesh: Dashboard - Modulo de Registro", font=('arial black', 18))
        lbTitle.pack()
        lbBuscar = tk.Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
        lbBuscar.grid(row=0, column=0, sticky="e")
        lbCodigo = tk.Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
        lbCodigo.grid(row=0, column=2, sticky="e")
        lbArea = tk.Label(Form, text = "Area:", font=('arial', 14), bd=15)
        lbArea.grid(row=1, sticky="e",column=1)
        lbDetalle = tk.Label(Form, text = "Detalle:", font=('arial', 14), bd=15)
        lbDetalle.grid(row=2, sticky="e",column=1)
        lbLugar = tk.Label(Form, text = "Lugar:", font=('arial', 14), bd=15)
        lbLugar.grid(row=1, sticky="e",column=3)
        lbTipo = tk.Label(Form, text = "Tipo:", font=('arial', 14), bd=15)
        lbTipo.grid(row=2, sticky="e",column=3)

        # Entrys - Cajas de Texto
        tbBuscar = tk.Entry(Form, font=(14))
        tbBuscar.grid(row=0, column=1)
        tbCodigo = tk.Entry(Form, font=(14))
        tbCodigo.grid(row=0, column=3)
        tbArea = tk.Entry(Form, textvariable=tbArea, font=(14))
        tbArea.grid(row=1, column=2)
        tbDetalle = tk.Entry(Form, textvariable=tbDetalle, font=(14))
        tbDetalle.grid(row=2, column=2)
        tbLugar = tk.Entry(Form, font=(14))
        tbLugar.grid(row=1, column=4)
        tbTipo = tk.Entry(Form, font=(14))
        tbTipo.grid(row=2, column=4)

        btnInsert = tk.Button(self, text="Agregar Registro", command=lambda: dbquery.insert(tbArea.get(), tbDetalle.get()))
        btnInsert.pack()
        btnBack = tk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(Dashboard)) 
        btnBack.pack()

class modVacaciones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Variables
        tbTitle = tk.StringVar()
        tbBuscar = tk.StringVar()
        tbCodigo = tk.StringVar()
        tbTipo = tk.StringVar()
        tbPeriodo = tk.StringVar()
        tbAsistencia = tk.StringVar()
        tbVacaciones = tk.StringVar()
        tbDetalle = tk.StringVar()

        # Frame
        Top = tk.Frame(self, bd=2)
        Top.pack()
        Form = tk.Frame(self, width=800, height=400)
        Form.pack()

        # Labels
        lbTitle = tk.Label(Top, text="Worknesh: Dashboard - Modulo de Vacaciones", font=('arial black', 18))
        lbTitle.pack()
        lbBuscar = tk.Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
        lbBuscar.grid(row=0, column=0, sticky="e")
        lbCodigo = tk.Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
        lbCodigo.grid(row=0, column=2, sticky="e")
        lbTipo = tk.Label(Form, text = "Tipo:", font=('arial', 14), bd=15)
        lbTipo.grid(row=1, sticky="e",column=1)
        lbPeriodo = tk.Label(Form, text = "Periodo:", font=('arial', 14), bd=15)
        lbPeriodo.grid(row=2, sticky="e",column=1)
        lbLAsistencia = tk.Label(Form, text = "Asistencia:", font=('arial', 14), bd=15)
        lbLAsistencia.grid(row=1, sticky="e",column=3)
        lbVacaciones = tk.Label(Form, text = "Vacaciones:", font=('arial', 14), bd=15)
        lbVacaciones.grid(row=2, sticky="e",column=3)
        lbDetalle = tk.Label(Form,text = "Detalle:", font=('arial',14), bd=15)
        lbDetalle.grid(row=3,sticky="e",column=3)

        # Entrys - Cajas de Texto
        tbBuscar = tk.Entry(Form,textvariable=tbBuscar, font=(14))
        tbBuscar.grid(row=0, column=1)
        tbCodigo = tk.Entry(Form,textvariable=tbCodigo ,font=(14))
        tbCodigo.grid(row=0, column=3)
        tbTipo = tk.Entry(Form, textvariable=tbTipo, font=(14))
        tbTipo.grid(row=1, column=2)
        tbPeriodo = tk.Entry(Form, textvariable=tbPeriodo, font=(14))
        tbPeriodo.grid(row=2, column=2)
        tbAsistencia = tk.Entry(Form, textvariable=tbAsistencia,font=(14))
        tbAsistencia.grid(row=1, column=4)
        tbVacaciones = tk.Entry(Form,textvariable=tbVacaciones,font=(14))
        tbVacaciones.grid(row=2, column=4)
        tbDetalle = tk.Entry(Form, textvariable=tbDetalle,font=(14))
        tbDetalle.grid(row=3, column=4)


        btnInsert = tk.Button(self, text="Add Libraian", command=lambda: dbquery.insert(tbArea.get(), tbDetalle.get()))
        btnInsert.pack()
        btnBack = tk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(Dashboard)) 
        btnBack.pack()


class Viewlib(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        db = sqlite3.connect("dbworknesh.db")
        cur=db.cursor()
        cur.execute("SELECT * from tArea")
        for row in cur:
            Libcontect_label = tk.Label(self, text= row)
            Libcontect_label.pack(pady=10,padx=10)

        btnBack = tk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(Dashboard)) 
        btnBack.pack()
        #return cur.fetchall()
        #cur.close()

    

app = appWork()
app.mainloop()