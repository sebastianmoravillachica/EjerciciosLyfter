from menu.user_menu import menu
print("---- Bienvenido al Sistema de Control de Estudiantes ----")

def main():
    while True:
        try:
            print("\nDigite su opcion:\n")
            user_option=input("Desea continuar SI/NO: ").lower()
            if user_option.isdigit():
                
                raise ValueError ("\nDigite SI o NO para la opcion anterior, no se permiten numeros.\n")
        
            if user_option =="si":
                menu()
            elif user_option == "no":
                print("Te esperamos pronto")
                print("Adios!!")
                break
            else:
                print(f"\nLa opcion que digitaste ( {user_option} ) no se encuentra dentro del menu, intentemos de nuevo.")
        except ValueError as error:
            print(error)
            
            
if __name__ == "__main__":
    main()