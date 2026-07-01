import csv

def get_list_of_students(path):

    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student in students:
            student_list.append(student)

    delete_student_by_name_and_section(student_list, path)


def delete_student_by_name_and_section(student_list, path):

    student_name = input("Digite el nombre completo del estudiante tal y como fue ingresado al sistema: ").strip().lower()

    student_section = input("Digite la sección del estudiante tal y como fue ingresado al sistema: ").strip().upper()

    student_found = False

    for student in student_list:

        if student_name == student['Full_name'].lower() and student_section == student['Section'].upper():

            student_list.remove(student)
            student_found = True
            break

    if student_found:
        save_student_list(path, student_list)
        print("\nEstudiante eliminado correctamente.")
    else:
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
        writer.writerows(student_list)