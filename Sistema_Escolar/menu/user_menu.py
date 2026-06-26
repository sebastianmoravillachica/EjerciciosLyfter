from actions.register_student import register_student
from data.load_all_students import load_student_on_file
from data.load_top_3_students import load_students

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
                load_students()

                
        except ValueError:
            print(f"\nPorfavor digite un numero del 1 al 7.")
            menu()
    
        
        
