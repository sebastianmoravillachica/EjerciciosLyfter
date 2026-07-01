import csv

def load_student_on_file(path):
    with open(path,'r', encoding='utf-8') as file:
        
        students=csv.DictReader(file,delimiter='|')
        
        for student in students:
            
            print("\nInformacion del estudiante")
            print("\n-----------------------------------------------")
            print(f"Nombre del estudiante: {student['Full_name']}")
            print(f"Seccion: {student['Section']}") 
            print(f"Español: {student['Spanish_grade']}") 
            print(f"Ingles: {student['English_grade']}") 
            print(f"Estudios Sociales: {student['Social_studies_grade']}") 
            print(f"Ciencias: {student['Science_grade']}") 
            print("-----------------------------------------------")