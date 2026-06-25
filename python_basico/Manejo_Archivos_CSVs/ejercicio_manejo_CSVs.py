#1.Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
import csv
def save_games_to_csv(file_path):

    game_count = int(input("Digite la cantidad de videojuegos que desea ingresar: "))

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        field_names = ["name", "genre", "developer", "esrb_rating"]

        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        for game_number in range(game_count):

            print(f"\nVideojuego #{game_number + 1}")

            name = input("Nombre: ")
            genre = input("Género: ")
            developer = input("Desarrollador: ")
            esrb_rating = input("Clasificación ESRB: ")

            writer.writerow({
                "name": name,
                "genre": genre,
                "developer": developer,
                "esrb_rating": esrb_rating
            })

    print("Archivo creado con éxito.")


save_games_to_csv('video_games.csv')

#2.Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del 
# ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.


import csv

def save_games_to_tsv(file_path):

    game_count = int(input("Digite la cantidad de videojuegos que desea ingresar: "))

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        field_names = ["name", "genre", "developer", "esrb_rating"]

        writer = csv.DictWriter(
            file,
            fieldnames=field_names,
            delimiter='\t'
        )

        writer.writeheader()

        for game_number in range(game_count):

            print(f"\nVideojuego #{game_number + 1}")

            name = input("Nombre: ")
            genre = input("Género: ")
            developer = input("Desarrollador: ")
            esrb_rating = input("Clasificación ESRB: ")

            writer.writerow({
                "name": name,
                "genre": genre,
                "developer": developer,
                "esrb_rating": esrb_rating
            })

    print("Archivo creado con éxito.")


save_games_to_tsv('video_games_with_tabulation.csv')