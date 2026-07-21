import csv
from models.student import Student




def load_student_on_file(path):
    with open(path,'r', encoding='utf-8') as file:
        
        students=csv.DictReader(file,delimiter='|')
        
        for student_data in students:

            student = Student(
                student_data["Full_name"],
                student_data["Section"],
                int(student_data["Spanish_grade"]),
                int(student_data["English_grade"]),
                int(student_data["Social_studies_grade"]),
                int(student_data["Science_grade"])
            )   
            print("\nInformación del estudiante")
            print("-----------------------------------------------")
            print(f"Nombre del estudiante: {student.full_name}")
            print(f"Sección: {student.section}")
            print(f"Español: {student.spanish_grade}")
            print(f"Inglés: {student.english_grade}")
            print(f"Estudios Sociales: {student.social_studies_grade}")
            print(f"Ciencias: {student.science_grade}")
            print("-----------------------------------------------")