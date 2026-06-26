import csv
import os #sistema operativo

def register_student(path):
    while True:
        try:
            students_count=int(input("\nDigite la cantidad de estudiantes que desea ingresar: \n"))
            with open (path, 'a', encoding='utf-8', newline='') as file:
                
                field_names=['Full name','Section','Spanish grade','English grade','Social studies grade', 'Science grade']
                
                writer=csv.DictWriter(file,fieldnames=field_names,delimiter='|')
                
                if os.path.getsize(path) == 0: #nos ayuda a verificar si el documento esta vacio o si ya contiene algo
                    writer.writeheader()
                
                for student in range(students_count):
                    print(f"\nEstudiante #{student + 1}")
                    
                    #NAME
                    while True:
                        try:
                            
                            full_name=input("\nDigite el nombre completo del estudiante:").strip().lower()
                            
                            if full_name =="" :
                                raise ValueError ("\nEspacio obligatorio, por favor digite el nombre completo del estudiante\n")
                            
                            if full_name.isdigit():
                                raise ValueError ("\nEl nombre del estudiante no puede ser un numero \n")
                            
                            for name in full_name:
                                if name.isdigit():
                                    raise ValueError ("\nEl nombre del estudiante no puede llevar numeros\n")
                            break
                        
                        except ValueError as error:
                            print(error)
                            
                    #SECTION
                    while True:
                        try:
                            section=input("\nDigite la seccion del estudiante, por ejemplo (11B):").strip().lower()
                            
                            if section =="" :
                                    raise ValueError ("\nEspacio obligatorio, por favor digite la seccion del estudiante!\n")
                            if section.isdigit():
                                    raise ValueError ("\nLa seccion del estudiante no puede ser un numero \n")
                            break
                        except ValueError as error:
                            print(error)
                            
                    #SPANICH GRADE
                    while True:
                        spanish_grade=input("\nDigite la nota de Español del estudiante:").strip()
                        if spanish_grade =="" :
                            print("\nLa nota no puede estar vacía.\n")
                        else:
                            try:
                                spanish_grade=float(spanish_grade)
                                break
                            except ValueError:
                                print("\nPor favor digite una nota válida.\n")
                                
                    #ENGLISH GRADE            
                    while True:
                        english_grade=input("\nDigite la nota de Ingles del estudiante:").strip()
                        if english_grade =="" :
                            print("\nLa nota no puede estar vacía.\n")
                        else:
                            try:
                                english_grade=float(english_grade)
                                break
                            except ValueError:
                                print("\nPor favor digite una nota válida.\n")
                                
                    #SOCIAL STUDIES GRADE 
                    while True:
                        social_studies_grade=input("\nDigite la nota de Estudios Sociales del estudiante:").strip()
                        if social_studies_grade =="" :
                            print("\nLa nota no puede estar vacía.\n")
                        else:
                            try:
                                social_studies_grade=float(social_studies_grade)
                                break
                            except ValueError:
                                print("\nPor favor digite una nota válida.")
                                
                    #SCIENCE GRADE 
                    while True:
                        science_grade=input("\nDigite la nota de Ciencias del estudiante:").strip()
                        if science_grade =="" :
                            print("\nLa nota no puede estar vacía.")
                        else:
                            try:
                                science_grade=float(science_grade)
                                break
                            except ValueError:
                                print("\nPor favor digite una nota válida.\n")    

                    writer.writerow({
                        'Full name':full_name,
                        'Section':section,
                        'Spanish grade':spanish_grade,
                        'English grade': english_grade,
                        'Social studies grade':social_studies_grade,
                        'Science grade':science_grade
                    })
                
            
            print("Archivo creado con éxito.")
            break
                    

        except ValueError:
            print("Porfavor digit solo numeros")
