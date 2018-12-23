from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import sqlite3

#---Conexion Base de Datos---
iConn = sqlite3.connect("workneshdb.sqlite")
iCur = iConn.cursos()

#---Creacion de tablas---
try:
    iCur.execute ('''
        create table tDatos (
        id integer primary key autoincrement,
        dni int(8) not null,
        nombre varchar(50),
        apellidos varchar(100),
        nromovil int(9),
        email varchar(100),
        direccion varchar(100),
        ''')

#---Salir base de datos


#------Primera Capa

print("Primera prueba para el test v1")

#------Segunda Capa

print("Segunda prueba para el test v2")

#------Tercera Capa

print("Tercera prueba para el test v3")