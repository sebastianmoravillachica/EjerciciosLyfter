
# PARTE NUMERO 1 DE LOS EJERCICIOS 

# Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

sum_strings= "1" + "2" #/ CONCATENA CON EXITO LOS DOS STRINGS
print(sum_strings)

#sum_strings_int= 1 + "2"  / DA ERROR YA QUE NO SE PUEDE SUMAR UN INT CON UN STRING
#print(sum_strings_int) 


#sum_strings_int2= "1" + 2 / DA ERROR YA QUE NO SE PUEDE CONCATENAR UN STRING CON UN INT
#print(sum_strings_int2)

sum_list= [1,2,3] + [4,5,6] # CONCATENA O UNE LAS DOS LISTAS
print(sum_list)

#sum_list_string= [1,2,3] + "Hola"  / DA ERROR YA QUE NO SE PUEDE CONCATENAR UNA LISTA CON UNA STRING SOLO SE PUEDE DE LISTAS A LISTAS 
#print (sum_list_string)

sum_flot_int= 25.5 + 4 #SUMA CON EXITO EL FLOAT Y EL INT 
print(sum_flot_int)

sum_bools= True + True # ESTO SE PUEDE SUMAR CON EXITO SIN EMBARGO PUEDE DAR NOS DISTINTAS SOLUCIONES YA QUE TRUE = 1 y FALSE = 0 por ser 
print (sum_bools)

#sum_tupla_list= (1,2,3) + [1,2,3] #NO SE PUEDE HACER UNA UNION ENTRE TUPLAS Y LISTAS SOLO ENTRE TUPLAS A TUPLAS
#print (sum_tupla_list)

sum_tupla_list= (1,2,3) + (1,2,3) # NOS UNE LA TUPLAS CON EXITO
print (sum_tupla_list)

#sum_tupla_dic= (1,2,3) + {"numero":2} #NO SE PUEDE HACER UNA UNION ENTRE TUPLAS Y DICIONARIOS SOLO ENTRE TUPLAS
#print (sum_tupla_dic)

#sum_dic={"numero1":2} + {"numero1":2} # NO SE PUEDE HACER SUMAS ENTRE DICCIONARIOS 
#print (sum_dic)


# PARTE NUMERO 2 DE LOS EJERCICIOS 

#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.



print("---- Identificar la etapa de la vida ----")

user_name = input("Digite su nombre: ")
last_name = input("Digite su apellido: ")
age = int(input("Digite su edad: "))

if age <= 2:
    stage = "bebé"
elif age <= 8:  # Simplificado, ya cubre de 3 a 8
    stage = "niño/a"
elif age < 12:  # Desde 9 hasta 11
    stage = "preadolescente"
elif age < 18:  # Desde 12 hasta 17
    stage = "adolescente"
elif age < 25:  # Desde 18 hasta 24
    stage = "adulto joven"
elif age < 60:  # Desde 25 hasta 59
    stage = "adulto"
else:
    stage = "adulto mayor"

print(f"{user_name} {last_name}, eres un {stage}")


# PARTE NUMERO 3 DE LOS EJERCICIOS 
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random
print ("--- Adivina el numero secreto ---")
secret_number= random.randint(1,10)
while True:
    user_number= int(input("Digite un numero del 1 al 10 para adivir el numero secreto: "))
    
    if user_number == secret_number:
        print("Excelente lograste encontrar el numero secreto")
        break
    else:
        print(f"Numero incorrecto intentalo de nuevo, tu numero {user_number}")
    
print (f"El numero secreto era {secret_number}")

# PARTE NUMERO 4 DE LOS EJERCICIOS 
#Cree un programa que le pida tres números al usuario y muestre el mayor.


print("\n--- Acomodador de números ---")

first_number = int(input("Digite el primer número: "))
second_number = int(input("Digite el segundo número: "))
third_number = int(input("Digite el tercer número: "))

# Si los tres son iguales
if first_number == second_number == third_number:
    print("Los números son iguales")

# Si hay empate entre dos o simplemente uno mayor
else:
    higher_number = first_number

    if second_number > higher_number:
        higher_number = second_number

    if third_number > higher_number:
        higher_number = third_number

    print(f"El número mayor es {higher_number}")
    



#PARTE NUMERO 5 DE LOS EJERCICIOS
#Dada n cantidad de notas de un estudiante, calcular:
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.


total_grades= int(input("Digite la cantidad de notas que desea verificar: "))

counter=0

number_passing_grades=0
number_failing_grades=0

average_all_grades=0
average_passing_grades=0
average_failing_grades=0

while counter < total_grades:
    current_grade= int(input("Digite la nota que desea verificar: "))
    counter+=1
    
    average_all_grades += current_grade
    
    if current_grade < 70:
        print(f"Nota reprobada {current_grade}")
        number_failing_grades+=1
        average_failing_grades += current_grade
        
    else:
        print(f"Nota aprobada {current_grade}")
        number_passing_grades+=1
        average_passing_grades += current_grade


# Promedio general
average_all_grades = average_all_grades // total_grades


# Promedio reprobadas
if number_failing_grades > 0:
    average_failing_grades = average_failing_grades // number_failing_grades
else:
    average_failing_grades = 0


# Promedio aprobadas
if number_passing_grades > 0:
    average_passing_grades = average_passing_grades // number_passing_grades
else:
    average_passing_grades = 0


print(f"El estudiante obtuvo una cantidad de notas aprobadas de {number_passing_grades}")
print(f"El estudiante tuvo un promedio de notas aprobadas de {average_passing_grades}")

print(f"El estudiante obtuvo una cantidad de notas reprobadas de {number_failing_grades}")
print(f"El estudiante tuvo un promedio de notas reprobadas de {average_failing_grades}")

print(f"El estudiante tuvo como promedio final {average_all_grades}")

