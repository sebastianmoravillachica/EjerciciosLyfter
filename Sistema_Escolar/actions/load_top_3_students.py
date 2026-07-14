import csv

from actions.average import calculate_average


def read_student_csv(path):

    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student in students:
            student_list.append(student)

    average_list = calculate_average(student_list)

    average_list.sort(key=get_average, reverse=True)

    show_top_3(average_list)


def get_average(student):

    return student["grade_average"]


def show_top_3(average_list):

    print("\n------ TOP 3 ESTUDIANTES ------\n")

    top = 3

    if len(average_list) < 3:
        top = len(average_list)

    for position in range(top):

        print(f"{position + 1}. Nombre: {average_list[position]['student_name']}")
        print(f"   Promedio: {average_list[position]['grade_average']:.2f}\n")