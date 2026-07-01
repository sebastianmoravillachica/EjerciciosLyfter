import csv

def load_all_students(path):import csv

def load_all_students(path):

    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student in students:
            student_list.append(student)

    calculate_average(student_list)



def calculate_average(student_list):

    average_list = []

    for student in student_list:

        student_name = student['Full_name']

        grade_average = (
            float(student['Spanish_grade']) +
            float(student['English_grade']) +
            float(student['Social_studies_grade']) +
            float(student['Science_grade']) 
        ) / 4

        average_list.append({
            "student_name": student_name,
            "grade_average": grade_average
        })
        
    show_average(average_list)
    
def show_average(average_list):
    print("\nInformacion del estudiante")
    for student in average_list:
    
        print("\n-----------------------------------------------")
        print(f"Nombre del estudiando: {student['student_name']}")
        print(f"Promedio final del estudiando: {student['grade_average']}")
        print("-----------------------------------------------")