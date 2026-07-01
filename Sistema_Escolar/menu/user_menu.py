from actions.register_student import register_student
from actions.load_all_students import load_student_on_file
from actions.load_top_3_students import read_student_csv
from actions.load_students_average import load_all_students
from data.export_students_csv import export_students
from data.import_students_csv import import_students
from actions.delete_student import get_list_of_students


def menu():
    while True:
        data_path='data\students.csv' 
        print("\n---- Menu ----\n")
        print("1- Para registrar estudiante.")
        print("2- Ver estudiantes.")
        print("3- Ver Top 3 de estudiantes (promedio global).")
        print("4- Ver el promedio de todos los estudiantes.")
        print("5- Exportar datos, estilo CSV")
        print("6- Importar datos a CSV")
        print("7- Eliminar estudiante")
        print("8- Salir")
        try:
            user_menu_option=int(input("\nDigite la opcion del menu que desea realizar: "))
            if user_menu_option == 1:
                register_student(data_path)
            elif user_menu_option == 2:
                load_student_on_file(data_path)
            elif user_menu_option ==3:
                read_student_csv(data_path)
            elif user_menu_option ==4:
<<<<<<< HEAD
                load_all_students()
=======
                load_all_students(data_path)
>>>>>>> creacion-sistema-escolar
            elif user_menu_option==5:
                export_students()
            elif user_menu_option==6:
                import_students()
            elif user_menu_option ==7:
                get_list_of_students(data_path)
            elif user_menu_option ==8:
                return
            else:
                print(f"\nNumero {user_menu_option}  fuera del rango digite un numero del 1 al 7")

        except ValueError:
            print(f"\nPorfavor digite un numero del 1 al 7.")
            