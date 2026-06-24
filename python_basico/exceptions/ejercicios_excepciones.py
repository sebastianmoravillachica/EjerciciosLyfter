#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

print("---- Bienvenido a tu Calculadora ----")

def main(current_number):
    
    print("---- Menu ----")
            
    print("1- Suma\n2- Resta\n3- Multiplicacion\n4- Division\n5- Borrar resultado\n")
    print(f"valor actual {current_number}\n")
    
    try:
        user_option=int(input("Digite el numero de la opcion que desea ejecutar:"))
        while (True):
            if user_option == 1:
                return sum_numbers(current_number)
            elif user_option == 2:
                return subtract_numbers(current_number)
            elif user_option == 3:
                return multiply_numbers(current_number)
                
            elif user_option == 4:
                return divide_numbers(current_number)
            elif user_option == 5:
                delete_content(current_number)
                
            else:
                print("Opcion fuera del rango, dijete un numero del 1 al 5") 
                
    except ValueError as error:
        print("\nEl dato que ingresaste no es una opcion del menu, porfavor digite un numero del 1 al 5")
        print(f"{error}\n")
        main(current_number)
        
        
def sum_numbers(current_number):
    
    try:
        user_number=int(input(f"Digite el numero que desea sumar entre el numero {current_number}:  "))
        sum_result=user_number+current_number
        print(f"\nResultado: {sum_result}\n")
        current_number=sum_result
        return main(current_number)
    except ValueError as error:
        print("Porfavor digite un numero, para poder realizar la suma\n")
        print(error)
        sum_numbers(current_number)


def subtract_numbers(current_number):
    
    try:
        user_number=int(input(f"Digite el numero que desea restar entre el numero {current_number}:"))
        subtract_result=current_number-user_number
        print(f"\nResultado: {subtract_result}\n")
        current_number=subtract_result
        return main(current_number)
    except ValueError as error:
        print("Porfavor digite un numero, para poder realizar la resta\n")
        print(error)
        subtract_numbers(current_number)


def multiply_numbers(current_number):
    
    try:
        user_number=int(input(f"Digite el numero que desea multiplicar entre el numero {current_number}:  "))
        multiplication_result=user_number*current_number
        print(f"\nResultado: {multiplication_result}\n" )
        return main(multiplication_result)
    except ValueError as error:
        print("Porfavor digite un numero, para poder realizar la multiplicacion\n")
        print(error)
        multiply_numbers(current_number)


def divide_numbers(current_number):
    
    try:
        user_number=int(input(f"Digite el numero que desea dividir entre el numero {current_number}:  "))
        division_result=current_number/user_number
        print(f"\nResultado: {division_result}\n")
        return main(division_result)
    except ValueError as error:
        print("Porfavor digite un numero, para poder realizar la division\n")
        print(error)
        divide_numbers(current_number)
    except ZeroDivisionError as error:
        print("Porfavor digite un numero distinto del cero\n")
        print(error)
        divide_numbers(current_number)
        
        
def delete_content(current_number):
    current_number=0
    return main(current_number)


if __name__ == '__main__':
	main(0)
