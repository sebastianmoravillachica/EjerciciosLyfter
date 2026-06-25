#EJERCICIO #1
#1.Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

amount_of_numbers=int(input("Digite la cantidad de numeros que desea ingresar: "))
counter=0
numbers_list=[]
if amount_of_numbers <= 0:
    print("Gracias por participar")
else:
    for number in range(amount_of_numbers):
        user_numbers=int(input(f"Digite {amount_of_numbers} numeros, numero {number +1}:  "))
        numbers_list.append(user_numbers)

    specific_number=int(input("Digite el numero que desea buscar: "))

    for search in numbers_list:
        if search == specific_number:
            counter+=1
    print(f"El numero {specific_number} aparece {counter} veces")

#2.Cree un programa que verifique si todos los elementos de una lista son positivos
numbers_list=[3,0,7,-1,5]
all_positive=True
for number in numbers_list:
    if number <=0:
        all_positive=False

if all_positive:
    print("Todos los números son positivos")
else:
    print("Hay un número negativo o un cero")   

#3.Cree un programa que muestre el valor más pequeño de una lista sin usar min().
#Use una variable para comparar uno a uno

numbers_list=[3,0,7,1,5]
minor=numbers_list[0]

for number in numbers_list:
    if number < minor:
        minor=number
    
print(f"El numero menor es {minor}")


#4.Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

numbers_list=[3,0,7,1,5]
average= sum(numbers_list)/len(numbers_list)

new_list=[]
for number in numbers_list:
    if number > average:
        new_list.append(number)
print(f"Lista actual {numbers_list}")
print(f"El promedio de los numeros de la lista es de {average}")
print(f"La nueva lista es {new_list}")

#5.Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
long_words=[]
for word in range(5):
    user_word=input(f"Digite 5 palabras, palabra {word +1}: ")
    if len(user_word) > 4:
        long_words.append(user_word)
print(long_words)



