import json

def get_new_pokemon(path, pokemons):

    while True:
        try:
            amount_of_pokemons = int(input("\nDigite la cantidad de pokemons que desea agregar: "))

            if amount_of_pokemons <= 0:
                raise ValueError( "La cantidad de pokemons debe ser mayor que cero.")
            break
        except ValueError as error:
            print(f"Data no valida: {error}")

    for pokemon in range(1, amount_of_pokemons + 1):

        print(f"\nPokemon numero {pokemon}")

        # NOMBRE
        while True:
            try:
                pokemon_name = input("Digite el nombre de su pokemon: ")

                if pokemon_name.isdigit():
                    raise ValueError(f"El nombre del pokemon no puede ser un numero: {pokemon_name}")
                break
            except ValueError as error:
                print(f"Data no valida: {error}")

        # TIPO
        while True:
            try:
                pokemon_type = input("Digite el tipo de pokemon: ")

                if pokemon_type.isdigit():
                    raise ValueError(f"El tipo de pokemon no puede ser un numero: {pokemon_type}")
                break
            except ValueError as error:
                print(f"Data no valida: {error}")
                
        # NIVEL
        while True:
            try:
                pokemon_level = int(input("Digite el nivel de su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        # PESO
        while True:
            try:
                pokemon_weight_kg = float(
                    input("Digite el peso de su pokemon en kilos: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero decimal.")

        # SHINY
        while True:
            try:
                pokemon_shiny = input("Su pokemon brilla digite SI/NO: ").lower()
                if pokemon_shiny not in ["si", "no"]:
                    raise ValueError(
                        f"Respuesta incorrecta, por favor responda SI o NO: {pokemon_shiny}")
                    
                if pokemon_shiny == 'si':
                    pokemon_shiny=True
                else:
                    pokemon_shiny=False
                break
            except ValueError as error:
                print(f"Data no valida: {error}")

        # OBJETO
        while True:
            try:
                pokemon_held_item = input("Digite el objeto que porta su pokemon, en caso de no portar dejar el espacio en blanco: ").lower()
                if pokemon_held_item.isdigit():
                    raise ValueError(f"El objeto no puede ser un numero: {pokemon_held_item}")
                if pokemon_held_item == "":
                    pokemon_held_item = None
                break
            except ValueError as error:
                print(f"Data no valida: {error}")

        # HABILIDADES
        while True:
            try:
                amount_of_pokemon_skills = int(input("Digite la cantidad de habilidades de su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        list_of_pokemon_skills = []

        for count in range(1, amount_of_pokemon_skills + 1):

            while True:
                try:
                    skills = input(f"Digite la habilidad numero {count} de su pokemon: ")
                    if skills.isdigit():
                        raise ValueError(f"La habilidad numero {count} no puede ser un numero: {skills}")
                    list_of_pokemon_skills.append(skills)
                    break
                except ValueError as error:
                    print(f"Data no valida: {error}")

        # STATS

        while True:
            try:
                pokemon_hp_level = int(input("Digite la cantidad de vida que posee su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        while True:
            try:
                pokemon_attack_level = int(input("Digite el nivel de ataque de su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        while True:
            try:
                pokemon_defense_level = int(input("Digite el nivel de defensa de su pokemon: "))
                break

            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        while True:
            try:
                pokemon_special_attack_level = int(input("Digite el nivel de ataque especial de su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        while True:
            try:
                pokemon_special_defense_level = int(input("Digite el nivel de defensa especial de su pokemon: "))
                break

            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        while True:
            try:
                pokemon_speed = int(input("Digite el nivel de velocidad de su pokemon: "))
                break
            except ValueError:
                print("Data no valida: Debe ingresar un numero entero.")

        pokemon_stats = {
            "hp": pokemon_hp_level,
            "attack": pokemon_attack_level,
            "defense": pokemon_defense_level,
            "sp_attack": pokemon_special_attack_level,
            "sp_defense": pokemon_special_defense_level,
            "speed": pokemon_speed,
        }

        new_pokemon = {
            "name": pokemon_name,
            "type": pokemon_type,
            "level": pokemon_level,
            "weight_kg": pokemon_weight_kg,
            "is_shiny": pokemon_shiny,
            "held_item": pokemon_held_item,
            "skills": list_of_pokemon_skills,
            "stats": pokemon_stats,
        }

        save_pokemon_as_a_JSON(path, pokemons, new_pokemon)
        


def save_pokemon_as_a_JSON(path,pokemons,new_pokemon):
    
    with open(path,'w',encoding="utf-8") as file:
        pokemons.append(new_pokemon)
        json.dump(pokemons, file, indent=2,ensure_ascii=False)
        
    print("\nPokemon guardado con exito!")

def read_JSON_pokemons(path):
    with open(path, "r", encoding="utf-8") as file:
        pokemons = json.load(file)
        for pokemon in pokemons:
            print("\n--- Pokémon ---")
            for label, content  in pokemon.items():
                print(f"{label}:{content}")
    
    get_new_pokemon(path,pokemons)     


read_JSON_pokemons('pokemones.json')
