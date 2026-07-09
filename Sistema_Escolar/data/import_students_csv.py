import os
import shutil

def import_students():

    source = "data/students_export.csv"
    destination = "data/students.csv"

    if not os.path.exists(source):
        print("\nNo existe un archivo previamente exportado.")
        return

    shutil.copy(source, destination)

    print("\nLos datos fueron importados correctamente.")