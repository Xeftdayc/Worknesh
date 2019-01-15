from tkinter.messagebox import showinfo

import sqlite3

# Variable Global de Conexion a la Base de Datos
def Database():
    global iConn, iCur
    iConn = sqlite3.connect("dbworknesh.db")
    iCur = iConn.cursor()

# Conexion de Login
def login(self):
    # Establish Connection
    with sqlite3.connect('dbworknesh.db') as db:
        c = db.cursor()

    # Find user If there is any take proper action
    find_user = ('SELECT * FROM tUser WHERE user = ? and pswd = ?')
    c.execute(find_user, [(self.USERNAME.get()), (self.PASSWORD.get())])
    result = c.fetchall()
    if result:
        self.logf.pack_forget()
        self.head['text'] = self.USERNAME.get() + '\n Conectado'
        self.head['pady'] = 150
    else:
        print('ups!', 'Nombre de usuario no encontrado.')

# Definicion de insert
def insert(area, detalle):
    #from backend import calculation
    Database()
    iCur.execute('INSERT INTO tArea VALUES (NULL, ?, ?);', (area, detalle))
    print("Entry Added To Database")
    iConn.commit()
    iConn.close()
    showinfo( title = "Nuevos Datos", message = "El nuevo dato fue ingresado correctamente")
    #view()

def addDatos(dni, nombre, apellido, sexo, direccion, f_nacimiento, email, nromovil):
    Database()
    iCur.execute('INSERT INTO tDatos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?);',(dni, nombre, apellido, sexo, direccion, f_nacimiento, email, nromovil))
    print("Entry Added")
    iConn.commit()
    iConn.close()
    showinfo( title = "Modulo para Insertar Registro", message = "El nuevo dato fue ingresado correctamente")
    #view()

def addVacaciones(tipo, periodo, c_asistencia, c_vacaciones, detalle):
    Database()
    iCur.execute('INSERT INTO tVacaciones VALUES (NULL, ?, ?, ?, ?, ?);',(tipo, periodo, c_asistencia, c_vacaciones, detalle))
    print("Entry Added")
    iConn.commit()
    iConn.close()
    showinfo( title = "Modulo para Insertar Vacaciones", message = "El nuevo dato fue ingresado correctamente")
    #view()

def addAsistencia(f_actual, checkin, i_detalle, checkout, o_detalle):
    Database()
    iCur.execute('INSERT INTO tAsistencia VALUES (NULL, ?, ?, ?, ?, ?);',(f_actual, checkin, i_detalle, checkout, o_detalle))
    print("Entry Added")
    iConn.commit()
    iConn.close()
    showinfo( title = "Modelo para Insertar Asistencia", message = "El nuevo dato de Asistencia fue agregado")

def addPapeletas(tipo, fecha, h_salida, h_retorno, motivo, lugar, autoriza):
    Database()
    iCur.execute('INSERT INTO tPapeletas VALUES (NULL, ?, ?, ?, ?, ?, ?, ?);',(tipo, fecha, h_salida, h_retorno, motivo, lugar, autoriza))
    print("Entry Added")
    iConn.commit()
    iConn.close()
    showinfo( title = "Modelo para Insertar Papeletas", message = "Los datos se ingresaron correctamente")

def addPermisos(tipo, fecha_in, fecha_out, c_dias, motivo, autoriza):
    Database()
    iCur.execute('INSERT INTO tPermisos VALUES (NULL, ?, ?, ?, ?, ?, ?);',(tipo, fecha_in, fecha_out, c_dias, motivo, autoriza))
    print("Entry Added")
    iConn.commit()
    iConn.close()
    showinfo( title = "Modelo para Insertar Permisos", message = "Los datos se ingresaron correctamente")

# Define Search in DB
def search(area="", detalle=""):
    Database()
    iCur.execute("SELECT * FROM tArea where area=? OR detalle=?",(area,detalle))
    row=iCur.fetchall()
    iConn.close()
    return row

def queryAsistencia(f_actual, checkin, i_detalle, checkout, o_detalle):
    Database()
    iCur.execute("SELECT * FROM tAsistencia WHERE f_actual=?, checkin=?, i_detalle=?, checkout=?, o_detalle=?",(f_actual, checkin, i_detalle, checkout, o_detalle))
    row=iCur.fetchall()
    iConn.close()
    return row

def queryDatos(id, dni, nombre):
    Database()
    iCur.execute("SELECT * FROM tDatos")
    varDatos = iCur.fetchall()
    for Datos in varDatos:
        print("ID:", id[0], "DNI:", dni[1], "Nombre:", nombre[2])

    iConn.commit()
    iConn.close()

# Define Update in DB
def update(id,area,detalle):
    #from dbquery import calculation
    Database()
    iCur.execute("UPDATE tArea SET area=?, detalle=?",(area,detalle))
    iConn.commit()
    iConn.close()

def upAsistencia():
    #from dbquery import calculation
    Database()
    iCur.execute("UPDATE tAsistencia SET f_actual=?, checkin=?, i_detalle=?, checkout=?, o_detalle=?", (f_actual, checkin, i_detalle, checkout, o_detalle))
    iConn.commit()
    iConn.close()

# Define Delete in DB
def delete(id):
    Database()
    iCur.execute("DELETE FROM tArea where id=?",(id))
    iConn.commit()
    iConn.close()

def delAsistencia(id):
    Database()
    iCur.execute("DELETE FROM tAsistencia where id=?", (id))
    iConn.commit()
    iConn.close()

# Define Parametro Calculation
def calculation(no_days,room_type):
    if room_type==("normal" or "NORMAL"):
        total=int(no_days)*1500
        return total
    elif room_type==("KING" or "king"):
        total=int(no_days)*1800
        return total
    elif room_type==("DELUX" or "delux"):
        total=int(no_days)*2000
        return total

Database()