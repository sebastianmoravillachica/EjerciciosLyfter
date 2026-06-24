#1.Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)
import json

def load_first_list_of_pokemon(path):
    with open(path,'r', encoding='utf-8') as file:
        
        list_pokemons=json.load(file)
        filter_pokemon_atribute(list_pokemons)

        
def filter_pokemon_atribute(list_pokemons):

        for pokemon in list_pokemons:
            
            print(f"Nombre:{pokemon['name']}, Tipo:{pokemon['type']}, Nivel:{pokemon['level']}\n")
            
                

load_first_list_of_pokemon('pokemones.json')



#2.Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
#Lea el archivo JSON de Pokémon
#Pida al usuario un tipo de Pokémon
#Muestre todos los Pokémon que sean de ese tipo
#Ejemplo:
#Entrada:
#"Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): "
#"Fuego"
#Salida:
#"Los pokemos que existen de ese tipo son: "
#Charmander
#Growlithe
#Victini

def load_second_list_of_pokemons(path):
    
    
    with open(path,'r', encoding='utf-8') as file:
        
        list_pokemons=json.load(file)
        filter_pokemon_by_type(list_pokemons)

        
def filter_pokemon_by_type(list_pokemons):
    
    pokemon_user_type=input("Digite el tipo de pokemon que desea filtrar, escriba el tipo en ingles: ").lower()
    found=False
    print(f"Los pokemos que existen de ese tipo son:")
    
    for pokemon in list_pokemons:  
        if pokemon_user_type == pokemon['type'].lower():
            print(pokemon['name'])
            found=True
    if not found:
        print("No se encontraron pokemones de ese tipo.")


load_second_list_of_pokemons('pokemones.json')


#3.Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
#Ejemplo:
#Salida:
#Nombre: Pikachu
#Ataque: 55
#Defensa: 40
#Velocidad: 90
#Nombre: Bulbasaur
#Ataque: 49
#Defensa: 49
#Velocidad: 45

def load_third_list_of_pokemons(path):
    with open(path,'r', encoding='utf-8') as file:
        
        list_pokemons=json.load(file)
    filter_pokemon_by_name_and_stats(list_pokemons)

        
def filter_pokemon_by_name_and_stats(list_pokemons):

    for pokemon in list_pokemons:
        print(f"Nombre: {pokemon['name']}")
        print(f"Vida:{pokemon['stats']['hp']}")
        print(f"Ataque:{pokemon['stats']['attack']}")
        print(f"Defensa:{pokemon['stats']['defense']}")
        print(f"Ataque especial:{pokemon['stats']['sp_attack']}")
        print(f"Defensa especial:{pokemon['stats']['sp_defense']}")
        print(f"Velocidad:{pokemon['stats']['speed']}\n")
                
                

load_third_list_of_pokemons('pokemones.json')

#4.Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
#Calcule y muestre el promedio de nivel para cada tipo:
#Ejemplo:
#Salida:
#Tipo: Agua → Promedio de nivel: 42.6
#Tipo: Fuego → Promedio de nivel: 37.2
#Tipo: Planta → Promedio de nivel: 30.4

def load_fourth_list_of_pokemons(path):
    with open(path, 'r', encoding='utf-8') as file:

        list_pokemons = json.load(file)
        group_type_of_pokemons(list_pokemons)


def group_type_of_pokemons(list_pokemons):

        pokemon_types = {} 

        for pokemon in list_pokemons:

            pokemon_type = pokemon["type"]
            pokemon_level = pokemon["level"]

            if pokemon_type not in pokemon_types:

                pokemon_types[pokemon_type] = {
                    "total_level": pokemon_level,
                    "count": 1
                }

            else:

                pokemon_types[pokemon_type]["total_level"] += pokemon_level
                pokemon_types[pokemon_type]["count"] += 1

        for pokemon_type, data in pokemon_types.items():

            average_level = data["total_level"] / data["count"]
            print(f"Tipo: {pokemon_type} → Promedio de nivel: {average_level:.1f}")
            
            
load_fourth_list_of_pokemons("pokemones.json")
