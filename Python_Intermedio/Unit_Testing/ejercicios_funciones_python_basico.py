#3.Cree una función que retorne la suma de todos los números de una lista.
#La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41



def sum_list(numbers):
    sum_total=0
    for number in numbers:
        sum_total= number+sum_total
    
    return sum_total
    
    



#4.Cree una función que le dé la vuelta a un string y lo retorne.
#Esto ya lo hicimos en iterables.
#“Hola mundo” → “odnum aloH”


def reverse_text(text):
    result=""
    for word in range(len(text)-1,-1,-1):
        result+=text[word]
    return result
        
    


#5.Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def check_text(text):
    lowercase=0
    uppercase=0
    for letter in text:
        
        if letter.isupper():
            uppercase+=1
        elif letter.islower():
            lowercase+=1
        else:
            continue
    print(f"El texto es ({text}) y tiene una cantidad de minusculas de {lowercase} y de mayusculas {uppercase}")
        



#6.Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”



def create_list(text):
    list_1= text.split("-")
    return sort_list(list_1)

def sort_list(list_2):
    
    list_2.sort()
    return create_new_string(list_2)

def create_new_string(second_string) :
    new_string=""
    for word in range(len(second_string)):
        new_string+=second_string[word]
        if word != len(second_string)-1:
            new_string += "-"
    return new_string 




#7.Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def find_prime_numbers(numbers):
    list_primes = []

    for number in numbers:
        if is_prime(number):
            add_number_new_list(list_primes, number)

    return list_primes

def is_prime(number):
    i = 5

    if number <= 1:
        return False

    elif number == 2 or number == 3:
        return True

    elif number % 2 == 0 or number % 3 == 0:
        return False

    while i * i <= number:

        if number % i == 0:
            return False

        elif number % (i + 2) == 0:
            return False

        i += 6

    return True

def add_number_new_list(list_primes, number):
    
    list_primes.append(number)


