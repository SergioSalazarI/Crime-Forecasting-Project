Create database CrimeDataSet 

-- Crear tabla con un crimen
Create table homicidios(
	Fecha DATE NOT NULL,
	Departamento VARCHAR (255) NOT NULL,
	Municipio VARCHAR (255) NOT NULL,
	Dia VARCHAR (255) NOT NULL,
	Hora TIME NOT NULL,
	Barrio VARCHAR (255) NOT NULL,
	Mes VARCHAR (255) NOT NULL,
	Zona VARCHAR (255) NOT NULL,
	Clase VARCHAR (255) NOT NULL,
	ArmaEmpleada VARCHAR (255) NOT NULL,
	MovilVictima VARCHAR (255) NOT NULL,
	MovilAgresor VARCHAR (255) NOT NULL,
	Edad int,
	EstadoCivil VARCHAR (255) NOT NULL,
	PaisNacimiento VARCHAR (255) NOT NULL,
	ClaseEmpleado VARCHAR (255) NOT NULL,
	Profesion VARCHAR (255),
	Escolaridad VARCHAR (255),
	CodigoDANE VARCHAR (255) NOT NULL,
	Genero VARCHAR (255) NOT NULL,
	Descripcion VARCHAR (255) NOT NULL,
	Cantidad int
)