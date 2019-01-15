from tkinter.messagebox import showinfo
#from tkinter import *
import tkinter as tk
import sqlite3
import dbquery
from tkinter import *

# Estructure Page in Page
class appWork(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, Dashboard, modTester, modRegistro, modVacaciones, Viewlib):
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

        btnLogin = tk.Button(self, text="Login", font=('new times roman', 14), width=10, bd=5, pady=2,
                            command=lambda: controller.show_frame(Dashboard))
        btnLogin.pack()

        btnBack = tk.Button(self, text="Back", font=('new times roman', 14), width=10, bd=5, pady=2,
                            command=lambda: controller.show_frame(Dashboard))
        btnBack.pack()

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

        btnTest = tk.Button(self, text="Modulo de Registro", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(modTester))
        btnTest.pack(fill="both")

        btnRegistro = tk.Button(self, text="Modulo de Registro", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(modRegistro))
        btnRegistro.pack(fill="both")
        btnAsistencia = tk.Button(self, text="Modulo de Asistencia", font=('calibri', 18), bd=10, pady=5,
                            command=lambda: controller.show_frame(modAsistencia))
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

class modTester(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        10
        # Variables
        tbArea = tk.StringVar()
        tbDetalle = tk.StringVar()

        # Frame
        Top = tk.Frame(self, bd=2)
        Top.pack()
        Form = tk.Frame(self, width=800, height=400)
        Form.pack()

        # Creando el Contenedor del Frame
        lframe = tk.Frame(self, bd=2)
        lframe.pack()

        # Ingreso del Area
        tk.Label(lframe, text = 'Area: ').grid(row = 1, column = 0)
        self.Area = tk.Entry(lframe)
        self.Area.focus()
        self.Area.grid(row = 1, column = 1)

        # Ingreso del Detalle
        tk.Label(lframe, text = 'Detalle: ').grid(row = 2, column = 0)
        self.Detalle = tk.Entry(lframe)
        self.Detalle.grid(row = 2, column = 1)
        
        # Button de Agregar Registro
        #btn12 = tkk.Button(lframe, text = "Guardar Datos")
        #btn12.pack()

        # Ingreso del Detalle
        self.btn3 = tk.Button(lframe, text="Guardar Datos")
        self.btn3.grid(row = 3, columnspan = 2, sticky="we")

        # Mensajes de Salida
        self.message = tk.Label(lframe, text="error", fg="red")
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = "we")

        # Table
        

        

        #lbBuscar = tk.Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
        #lbBuscar.grid(row=0, column=0, sticky="e")

        # Labels
        lbTitle = tk.Label(Top, text="Worknesh: Dashboard - Modulo de Testeo", font=('arial black', 18))
        lbTitle.pack()
        lbBuscar = tk.Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
        lbBuscar.grid(row=0, column=0, sticky="e")
        lbCodigo = tk.Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
        lbCodigo.grid(row=0, column=2, sticky="e")
        lbArea = tk.Label(Form, text = "Area:", font=('arial', 14), bd=15)
        lbArea.grid(row=1, sticky="e",column=1)
        lbDetalle = tk.Label(Form, text = "Detalle:", font=('arial', 14), bd=15)
        lbDetalle.grid(row=2, sticky="e",column=1)

        # Entrys - Cajas de Texto
        tbBuscar = tk.Entry(Form, font=(14))
        tbBuscar.grid(row=0, column=1)
        tbCodigo = tk.Entry(Form, font=(14))
        tbCodigo.grid(row=0, column=3)
        tbArea = tk.Entry(Form, textvariable=tbArea, font=(14))
        tbArea.grid(row=1, column=2)
        tbDetalle = tk.Entry(Form, textvariable=tbDetalle, font=(14))
        tbDetalle.grid(row=2, column=2)

        list1 = tk.Listbox(Form,height=20,width=59)
        list1.grid(row=1,column=3, rowspan=6, columnspan=2)


        btnInsert = tk.Button(self, text="Add Libraian", command=lambda: dbquery.insert(tbArea.get(), tbDetalle.get()))
        btnInsert.pack()
        btnBack = tk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(Dashboard)) 
        btnBack.pack()


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


class modAsistencia(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Variables
        tbFactual = tk.StringVar()
        tbCheckin = tk.StringVar()
        tbIndetalle = tk.StringVar()
        tbCheckout = tk.StringVar()
        tbOutdetalle = tk.StringVar()

        # Frame
        Top = tk.Frame(self, bd=2)
        Top.pack()
        Form = tk.Frame(self, width=800, height=400)
        Form.pack()

        # Labels
        lbTitle = tk.Label(Top, text="Worknesh: Dashboard - Modulo de Asistencia", font=('arial black', 18))
        lbTitle.pack()
        lbBuscar = tk.Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
        lbBuscar.grid(row=0, column=0, sticky="e")
        lbCodigo = tk.Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
        lbCodigo.grid(row=2, column=0, sticky="e")
        lbNombre = tk.Label(Form, text = "Nombre:", font=('arial', 14), bd=15)
        lbNombre.grid(row=2, sticky="e",column=1)
        lbApellido = tk.Label(Form, text = "Apellido:", font=('arial', 14), bd=15)
        lbApellido.grid(row=2, sticky="e",column=2)
        lbFactual = tk.Label(Form, text = "Factual:", font=('arial', 14), bd=15)
        lbFactual.grid(row=5, sticky="e",column=0)
        lbChekin = tk.Label(Form, text = "Chekin:", font=('arial', 14), bd=15)
        lbChekin.grid(row=5, column=1, sticky="e")
        lbIndetalle = tk.Label(Form, text = "Indetalle:", font=('arial', 14), bd=15)
        lbIndetalle.grid(row=5, sticky="e",column=1)
        lbCheckout = tk.Label(Form, text = "Checkout:", font=('arial', 14), bd=15)
        lbCheckout.grid(row=8, sticky="e",column=2)
        lbOutdetalle = tk.Label(Form, text = "Outdetalle:", font=('arial', 14), bd=15)
        lbOutdetalle.grid(row=8, sticky="e",column=0)

        # Entrys - Cajas de Texto
        tbBuscar = tk.Entry(Form, font=(14))
        tbBuscar.grid(row=1, column=0)
        tbCodigo = tk.Entry(Form, font=(14))
        tbCodigo.grid(row=3, column=0)
        tbNombre = tk.Entry(Form, font=(14))
        tbNombre.grid(row=3, column=1)
        tbApellido = tk.Entry(Form, font=(14))
        tbApellido.grid(row=3, column=2)
        tbFactual = tk.Entry(Form, font=(14))
        tbFactual.grid(row=6, column=0)
        tbChekin = tk.Entry(Form, font=(14))
        tbChekin.grid(row=6, column=1)
        tbIndetalle = tk.Entry(Form, font=(14))
        tbIndetalle.grid(row=6, column=2)
        tbCheckout = tk.Entry(Form, font=(14))
        tbCheckout.grid(row=9, column=0)
        tbOutdetalle = tk.Entry(Form, font=(14))
        tbOutdetalle.grid(row=9, column=1)


        vLunes = tk.IntVar()
        chLunes = tk.Checkbutton(Form, text="Lunes", variable=vLunes).grid(row=12, column=0)
        vMartes = tk.IntVar()
        chMartes = tk.Checkbutton(Form, text="Martes", variable=vMartes).grid(row=12, column=1)
        vMiercoles = tk.IntVar()
        chMiercoles = tk.Checkbutton(Form, text="Miercoles", variable=vMiercoles).grid(row=12, column=2)
        vJueves = tk.IntVar()
        chJueves = tk.Checkbutton(Form, text="Jueves", variable=vJueves).grid(row=13, column=0)
        vViernes = tk.IntVar()
        chViernes = tk.Checkbutton(Form, text="Viernes", variable=vViernes).grid(row=13, column=1)


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


        btnInsert = tk.Button(self, text="Add Libraian", command=lambda: dbquery.addVaciones(tbTipo.get(), tbPeriodo.get(), tbAsistencia.get(), tbVacaciones.get(),tbDetalle.get()))
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