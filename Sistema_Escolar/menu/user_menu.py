from actions.register_student import register_student
from actions.load_all_students import load_student_on_file
from actions.load_top_3_students import load_students_top
from actions.load_students_average import load_average_by_student
from data.export_students_csv import export_students
from data.import_students_csv import import_students


def menu():
    while True:
        
        print("\n---- Menu ----\n")
        print("1- Para registrar estudiante.")
        print("2- Ver estudiantes.")
        print("3- Ver Top 3 de estudiantes (promedio global).")
        print("4- Ver el promedio de todos los estudiantes.")
        print("5- Exportar datos, estilo CSV")
        print("6- Importar datos a CSV")
        print("7- Para salir")
        try:
            user_menu_option=int(input("\nDigite la opcion del menu que desea realizar: "))
            if user_menu_option == 1:
                register_student()
            elif user_menu_option == 2:
                load_student_on_file()
            elif user_menu_option ==3:
                load_students_top()
            elif user_menu_option ==4:
                load_average_by_student() 
            elif user_menu_option==5:
                export_students()
            elif user_menu_option==6:
                import_students()
            elif user_menu_option ==7:
                return
            else:
                print(f"\nNumero {user_menu_option}  fuera del rango digite un numero del 1 al 7")

        except ValueError:
            print(f"\nPorfavor digite un numero del 1 al 7.")
            