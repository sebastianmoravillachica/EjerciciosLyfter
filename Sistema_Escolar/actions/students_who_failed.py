import csv

def read_students(path):
    
    student_list = []

    with open(path, 'r', encoding='utf-8') as file:

        students = csv.DictReader(file, delimiter='|')

        for student in students:
            student_list.append(student)
            
    show_student_who_failed(student_list)

def show_student_who_failed(student_list):
    
    for student in student_list:
        
        failed_subjects = []
        
        if float(student['Spanish_grade']) <= 60:
            failed_subjects.append(f"Español: {student['Spanish_grade']}")
        if float(student['English_grade']) <= 60:
            failed_subjects.append(f"Inglés: {student['English_grade']}")
        if float(student['Social_studies_grade']) <= 60:
            failed_subjects.append(f"Estudios Sociales: {student['Social_studies_grade']}")
        if float(student['Science_grade'])  <= 60:
            failed_subjects.append(f"Ciencias: {student['Science_grade']}")
            
        
        if failed_subjects:
            print(f"\n----- Esudiantes reprobados -----")
            
            print(f"\nNombre: {student['Full_name']}")
            print(f"Sección: {student['Section']}")
            print("Materias reprobadas:")
            
            for subject in failed_subjects:
                print(f"{subject}")
            print("----------------------------------------------\n")