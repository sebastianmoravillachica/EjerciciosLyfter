import os
import shutil

def export_students():

    source = "data/students.csv"
    destination = "data/students_export.csv"

    if not os.path.exists(source):
        print("\nNo hay estudiantes para exportar.")
        return

    shutil.copy(source, destination)

    print("\nLos datos fueron exportados correctamente.")