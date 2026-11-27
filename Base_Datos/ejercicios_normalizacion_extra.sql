--1. Normalización de Empleados y Proyectos


--Instrucciones:
--Explique paso a paso cómo llevar esta tabla a 3FN
--Muestre todas las tablas intermedias (1FN, 2FN, 3FN)
--Justifique cada cambio



1. Primera Forma Normal (1FN)
La tabla cumple 1FN porque cada campo contiene un único valor y no existen grupos repetidos.

Se establece una clave compuesta:

(employee_id, project_id)

Justificación: un empleado puede trabajar en varios proyectos y un proyecto puede tener varios empleados.
2. Segunda Forma Normal (2FN)
Se separan los datos en tres tablas:
- employees: datos del empleado.
- projects: datos del proyecto.
- employees_per_projects: relación entre empleados y proyectos.
Justificación: se eliminan las dependencias parciales. Los datos del empleado dependen de employee_id y los del proyecto dependen de project_id.
3. Tercera Forma Normal (3FN)
Se crea una tabla independiente llamada departments.
- departments: nombre y teléfono del departamento.
- employees: incluye department_id como clave foránea.
Justificación: el teléfono depende del departamento, no directamente del empleado. Así se elimina la dependencia transitiva.



CREATE TABLE deparments (

id INTEGER PRIMARY KEY AUTO_INCREMENT,
department_name VARCHAR(100) NOT NULL,
department_phone_number VARCHAR(20) NOT NULL
);


CREATE TABLE projects(
id VARCHAR(10) PRIMARY KEY NOT NULL,
project_name VARCHAR(150) NOT NULL,
project_budget DECIMAL(12,2) NOT NULL
);

CREATE TABLE employees ( 

id INTEGER PRIMARY KEY NOT NULL,
employee_name VARCHAR(25) NOT NULL,
department_id INTEGER REFERENCES deparment (id)
);

CREATE TABLE employees_per_project(
id INTEGER PRIMARY KEY AUTOINCREMENT,
employee_id  INTEGER REFERENCES employees (id),
project_id VARCHAR(10) REFERENCES projects(id)

);



--2. Normalización de Registro de Clases

--Instrucciones:
--Normalice hasta 3FN mostrando el paso por cada forma normal



1. Primera Forma Normal (1FN)
La tabla original cumple 1FN porque cada campo contiene un solo valor.

La clave primaria es compuesta:

(student_id, course_code)

Cada fila representa la inscripción de un estudiante en un curso.

2. Segunda Forma Normal (2FN)
Se separan los datos que dependen parcialmente de la clave compuesta:
- students: datos del estudiante.
- courses: datos del curso e instructor.
- courses_per_student: relación entre estudiante y curso.

3. Tercera Forma Normal (3FN)
Se separan los datos del instructor de los cursos, porque el nombre y el correo dependen del instructor, no directamente del curso.



CREATE TABLE students(
id INTEGER PRIMARY KEY NOT NULL, 
student_name VARCHAR(25) NOT NULL,
);


CREATE TABLE instrustors(

id INTEGER PRIMARY KEY NOT NULL, 
instrustor_name VARCHAR(25) NOT NULL,
email VARCHAR(254) NOT NULL UNIQUE 

);

CREATE TABLE courses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
course_code VARCHAR(20) NOT NULL UNIQUE,
course_name VARCHAR(100) NOT NULL,
instrustor_id INTEGER REFERENCES instrustors (id)
);

CREATE TABLE courses_per_student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER REFERENCES students (id),
course_id INTEGER REFERENCES courses (id)

);


-- 3. Normalización de Hospital y Citas Médicas
--Indicaciones:
--Descomponga en tablas separadas hasta 3FN

1FN: La tabla cumple con la primera forma normal porque cada columna contiene un único valor y cada cita tiene un identificador único. 
No existen grupos de valores repetidos dentro de una misma celda.

2FN: Se separan los datos de pacientes, doctores y citas en tablas independientes. Esto evita repetir la información del paciente y del doctor cada vez que se registra una cita.

3FN: Se crea una tabla independiente llamada specialties para almacenar las especialidades médicas. Así se evita repetir el nombre de la especialidad en cada doctor y 
se elimina la dependencia transitiva, ya que la especialidad depende del doctor y su nombre depende de specialty_id.

CREATE TABLE patients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_name VARCHAR(25) NOT NULL,
patient_phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE specialties(

id INTEGER PRIMARY KEY AUTOINCREMENT,
specialty_name VARCHAR(100) NOT NULL UNIQUE 
);


CREATE TABLE doctors(

id INTEGER PRIMARY KEY AUTOINCREMENT,
doctor_name VARCHAR(25) NOT NULL,
specialty_id INTEGER REFERENCES specialties(id)
);

CREATE TABLE appointments(

id VARCHAR(10) PRIMARY KEY NOT NULL,
appointment_date DATE NOT NULL,
appointment TIME NOT NULL,
doctor_id INTEGER REFERENCES doctors(id),
patient_id INTEGER REFERENCES patients(id)
);





