import csv

from models.student import  Student
def get_list_of_students(path):

    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student_data in students:

            student = Student(
                student_data["Full_name"],
                student_data["Section"],
                int(student_data["Spanish_grade"]),
                int(student_data["English_grade"]),
                int(student_data["Social_studies_grade"]),
                int(student_data["Science_grade"])
            )

            student_list.append(student)

    delete_student_by_name_and_section(student_list, path)


def delete_student_by_name_and_section(student_list, path):

    student_name = input("Digite el nombre completo del estudiante tal y como fue ingresado al sistema: ").strip().lower()

    student_section = input("Digite la sección del estudiante tal y como fue ingresado al sistema: ").strip().upper()

    student_found = False
    student_deleted = False
    for student in student_list:

        if student_name == student.full_name.lower() and student_section == student.section.upper():

            print("\n------ ESTUDIANTE ENCONTRADO ------")
            print(f"Nombre: {student.full_name}")
            print(f"Sección: {student.section}")
            print("-----------------------------------")

            confirm_delete = input("\n¿Desea eliminar este estudiante? (SI/NO): ").strip().upper()

            if confirm_delete == "SI":
                student_list.remove(student)
                save_student_list(path, student_list)
                student_deleted = True
                print("\nEstudiante eliminado correctamente.")

            elif confirm_delete == "NO":
                print("\nOperación cancelada. El estudiante no fue eliminado.")

            else:
                print("\nOpción inválida. Operación cancelada.")

            break

    if not student_found:
        print("\nNo se encontró un estudiante con ese nombre y sección.")

    


def save_student_list(path, student_list):

    field_names = [
        'Full_name',
        'Section',
        'Spanish_grade',
        'English_grade',
        'Social_studies_grade',
        'Science_grade'
    ]

    with open(path, 'w', encoding='utf-8', newline='') as file:

        writer = csv.DictWriter(
            file,
            fieldnames=field_names,
            delimiter='|'
        )

        writer.writeheader()
        
        for student in student_list:
            writer.writerow(student.to_dict())