import csv
from models.student import Student
def read_students(path):
    
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
            
    show_student_who_failed(student_list)

def show_student_who_failed(student_list):
    
    for student in student_list:
        
        failed_subjects = []
        
        if int(student.spanish_grade) < 60:
            failed_subjects.append(f"Español: {student.spanish_grade}")
        if int(student.english_grade) < 60:
            failed_subjects.append(f"Inglés: {student.english_grade}")
        if int(student.social_studies_grade) < 60:
            failed_subjects.append(f"Estudios Sociales: {student.social_studies_grade}")
        if int(student.science_grade)  < 60:
            failed_subjects.append(f"Ciencias: {student.science_grade}")
            
        
        if failed_subjects:
            print(f"\n----- Estudiantes reprobados -----")
            
            print(f"\nNombre: {student.full_name}")
            print(f"Sección: {student.section}")
            print("Materias reprobadas:")
            
            for subject in failed_subjects:
                print(f"{subject}")
            print("----------------------------------------------\n")