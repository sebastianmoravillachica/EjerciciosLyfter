import csv

from actions.average import calculate_average
from models.student import Student

def load_all_students(path):

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

    average_list = calculate_average(student_list)

    show_average(average_list)


def show_average(average_list):

    print("\nInformación del estudiante")

    for student in average_list:

        print("\n-----------------------------------------------")
        print(f"Nombre del estudiante: {student['student_name']}")
        print(f"Promedio final del estudiante: {student['grade_average']:.2f}")
        print("-----------------------------------------------")