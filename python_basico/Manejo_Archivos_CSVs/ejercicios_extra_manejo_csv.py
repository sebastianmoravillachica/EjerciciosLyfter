# 1. Cree un programa que abra un archivo .csv con la información de videojuegos
# (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea.

import csv


def read_games_line_by_line(file_path):

    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file, delimiter=',')
        next(reader)  # Saltar encabezados

        for game in reader:

            print(f"Nombre: {game[0]}")
            print(f"Género: {game[1]}")
            print(f"Desarrollador: {game[2]}")
            print(f"Clasificación ESRB: {game[3]}\n")


read_games_line_by_line('video_games.csv')


#2.Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo CSV de videojuegos
#Pida al usuario una clasificación ESRB (por ejemplo: "T")
#Muestre todos los videojuegos que tengan esa clasificación

def filter_games_by_esrb_classification(file_path):

    user_classification_type = input(
        "Digite el tipo de clasificación ESRB que desea filtrar: "
    ).strip().lower()

    found = False

    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file, delimiter=',')
        next(reader)  # Saltar encabezados

        for game in reader:

            if game[3].lower() == user_classification_type:

                found = True

                print(f"Nombre: {game[0]}")
                print(f"Género: {game[1]}")
                print(f"Desarrollador: {game[2]}")
                print(f"Clasificación ESRB: {game[3]}\n")

    if not found:
        print("Clasificación ESRB no encontrada")


filter_games_by_esrb_classification('video_games.csv')

#3.Cree un programa que abra un archivo .csv con la información de videojuegos
# ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Cuente cuántos videojuegos hay de cada género
#Muestre el resultado de forma ordenada
#Ejemplo:
#Salida:
#Géneros encontrados:
#Acción: 5
#Aventura: 3
#Deportes: 4
#...

def count_games_by_genre(file_path):

    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        reader = csv.DictReader(file)

        genre_counts = {}

        for game in reader:

            genre = game["genre"]

            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

        print("Géneros encontrados:")

        for genre_name, count in sorted(genre_counts.items()):
            print(f"{genre_name}: {count}")

count_games_by_genre('video_games.csv')

#4.Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
#Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
#Ejemplo:
#Salida:
#Videojuegos desarrollados por Ubisoft:
#- Assassin's Creed II (Clasificación: M, Género: Aventura)
#- Rayman Legends (Clasificación: E, Género: Plataforma)

def filter_games_by_developer(file_path):

    developer_name = input(
        "Digite el desarrollador de videojuegos que desea filtrar: "
    ).strip().lower()

    found = False

    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        reader = csv.DictReader(file)

        print(f"\nVideojuegos desarrollados por {developer_name.title()}:")

        for game in reader:

            if developer_name in game["developer"].lower():

                found = True

                print(
                    f"- {game['name']} "
                    f"(Clasificación: {game['esrb_rating']}, "
                    f"Género: {game['genre']})"
                )

        if not found:
            print("Desarrollador no encontrado")

filter_games_by_developer('video_games.csv')