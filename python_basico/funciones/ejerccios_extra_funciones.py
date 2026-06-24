
#1.Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

def count_char_occurrences(text,character):
    counter=0
    
    for letter in text:
        if letter.lower()==character.lower():
            counter+=1 
    return f"Se a encontrado {counter} veces el {character}"

use_text=count_char_occurrences(input("Digite el texto que desee: "), input("Digite el caracter que sea contar: "))

print(use_text)

#2. Cree una función que reciba una lista de palabras y un número n, 
# y retorne una nueva lista con solo las palabras que tengan más de n letras

def count_vowels (list_words,number):
    new_list=[]
    for word in list_words:
        if len(word) > number:
            new_list.append(word)
    return new_list
            


first_list=["Hola","Adios","Buenas","Carro","Moto"]
result=count_vowels(first_list, int(input("Digite la cantidad mínima de letras: ")))

print(result)

#3.Cree una función que reciba un string y retorne cuántas vocales contiene

def filter_amount_vowels(text):
    vowels_counter=0
    for letter in text:
        if letter.lower() in 'aeiou':
            vowels_counter+=1
    return vowels_counter
            

result=filter_amount_vowels(input ("Digite la cantidad mínima de letras: "))

print(f"El texto una cantidad de vocales de {result}")