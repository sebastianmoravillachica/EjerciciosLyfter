#Ejercicio #1
#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#Ejemplos:
#first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
#second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’] ->
#Hay casos
#en los
##iteracion por
#indice es
#muy util

print("---- Unir listas -----")

first_list = ["El","es"]
second_list = ["sushi","delicioso"] 

if len(first_list) != len(second_list):
    print("El tamaño de la lista es diferente")
else:
    for word in range(len(first_list)):
        print(first_list[word],second_list[word])

        
# Ejercicios #2 
#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#Pista: investigue de que otras maneras se puede usar el range.
#Ejemplos:
#my_string = ‘Pizza con piña’ →
#a
#ñ
#i
#p

#n
#o
#c

#a
#z
#z
#i
#p

print("---- Invertir texto ----")
#my_string="ZORO RORONOA" [::-1]
#print(my_string)
my_string="ZORO RORONOA"

for index in range(len(my_string)-1,-1,-1):
    
    print(my_string[index])

#Ejercicio #3

#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#Ejemplos:
#my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]


my_list = [3, 3, 6, 1, 9]

for i in range(len(my_list)):
    if i == 0:
        first_index = my_list[i]
        my_list[i] = my_list[-1]
        my_list[-1] = first_index
        break  # Detiene el ciclo después del intercambio

print(my_list)


#Ejercicio #4

#Cree un programa que elimine todos los números impares de una lista.
#Ejemplos:
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(len(my_list) - 1, -1, -1): #range(inicio, fin, paso) #Regla sencilla:#Si el inicio es mayor que el final:#Usa -1#Si el inicio es menor que el final:#Usa +1
    if my_list[index] % 2 != 0:   # Si es impar
        my_list.pop(index)

print(my_list)
    
        
#Ejercicio 5
#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#Ejemplos:
#86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

numbers = []  # Lista vacía para guardar los números

for i in range(10):
    number = int(input(f"Digite el número {i + 1}: "))
    numbers.append(number)  # Agrega cada número a la lista

highest_number = numbers[0]  # Tomamos el primer número como referencia

for number in numbers:
    if number > highest_number:
        highest_number = number  # Actualizamos si encontramos uno mayor

print(f"Los números ingresados fueron: {numbers}")
print(f"El número más alto fue: {highest_number}")
    
    