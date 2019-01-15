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

def addVaciones(tipo, periodo, c_asistencia, c_vacaciones, detalle, id_asistencia):
    Database()
    iCur.execute('INSERT INTO tVacaciones VALUES (NULL, ?, ?, ?, ?, ?, 1);',(tipo, periodo, c_asistencia, c_vacaciones, detalle, id_asistencia))
    print("Entry")
    iConn.commit()
    iConn.close()
    showinfo( title = "Nuevos Datos", message = "El nuevo dato fue ingresado correctamente")
    #view()

# Define Search
def search(area="", detalle=""):
    Database()
    iCur.execute("SELECT * FROM tArea where area=? OR detalle=?",(area,detalle))
    row=iCur.fetchall()
    iConn.close()
    return row

# Define Delete in DB
def delete(id):
    Database()
    iCur.execute("DELETE FROM tArea where id=?",(id))
    iConn.commit()
    iConn.close()

# Define Update in DB
def update(id,area,detalle):
    from dbquery import calculation
    Database()
    iCur.execute("UPDATE tArea SET area=?, detalle=?",(area,detalle))
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