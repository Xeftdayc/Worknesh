CREATE TABLE tDatos(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    dni INTEGER NOT NULL,
	nombre TEXT NOT NULL,
	apellido TEXT,
    sexo TEXT,
    direccion TEXT,
    f_nacimiento TEXT,
    email TEXT,
    nromovil INTEGER
);

CREATE TABLE tArea(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	area TEXT,
	detalle TEXT
);

CREATE TABLE tCargo(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cargo TEXT,
    detalle TEXT
);

CREATE TABLE tPersonal(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo TEXT,
    estado TEXT,
    turno TEXT,
    salario NUMERIC(6,2),
    contrato TEXT,
    id_area INTEGER NOT NULL,
    id_cargo INTEGER NOT NULL,
    FOREIGN KEY(id_area) REFERENCES tArea(id),
    FOREIGN KEY(id_cargo) REFERENCES tCargo(id)
);

CREATE TABLE tContrato(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    detalle TEXT,
    periodo TEXT,
    f_inicio TEXT,
    f_salida TEXT,
    pariente INTEGER,
    id_personal INTEGER NOT NULL,
    FOREIGN KEY(id_personal) REFERENCES tPersonal(id)
);

CREATE TABLE tPariente(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    relacion TEXT,
    nombre TEXT,
    apellidos TEXT,
    edad INTEGER,
    f_nacimiento TEXT,
    id_contrato INTEGER,
    FOREIGN KEY(id_contrato) REFERENCES tContrato(id)
);

CREATE TABLE tAsistencia(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    f_actual TEXT,
    checkin TEXT,
    i_detalle TEXT,
    checkout TEXT,
    o_detalle TEXT,
    id_personal INTEGER,
    FOREIGN KEY(id_personal) REFERENCES tPersonal(id)
);

CREATE TABLE tVacaciones(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    periodo TEXT,
    c_asistencia INTEGER,
    c_vacaciones INTEGER,
    detalle TEXT,
    id_asistencia INTEGER,
    FOREIGN KEY(id_asistencia) REFERENCES tAsistencia(id)
);

CREATE TABLE tUser(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    pswd TEXT NOT NULL
);