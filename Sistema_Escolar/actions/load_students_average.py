import csv

from actions.average import calculate_average


def load_all_students(path):

    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student in students:
            student_list.append(student)

    average_list = calculate_average(student_list)

    show_average(average_list)


def show_average(average_list):

    print("\nInformación del estudiante")

    for student in average_list:

        print("\n-----------------------------------------------")
        print(f"Nombre del estudiante: {student['student_name']}")
        print(f"Promedio final del estudiante: {student['grade_average']:.2f}")
        print("-----------------------------------------------")