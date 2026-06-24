# Ejercicio 1

#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:
#120 → 108
#40 → 39.2


product_price= float(input("Digite el precio del producto: "))


if product_price < 100:
    discount= product_price * 0.02
    final_price=product_price-discount
    
else:
    discount=product_price*0.1
    final_price=product_price-discount

print(f"El precio final del es de {final_price}")

# Ejercicio 2
#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
# Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
#Ejemplos:
#1040 → Mayor
#140 → 460
#600 → Igual
#599 → 1

user_seconds=int(input("Digite la cantidad de segundos: "))

if user_seconds >600:
    print("Mayor")
elif user_seconds <600:
    missing_seconds= 600-user_seconds
    print(f"Te faltan {missing_seconds} segundos para igual a 600")
else:
    print("Igual")


# Ejercicio 3

#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
#5 → 15 (1 + 2 + 3 + 4 + 5)
#3 → 6 (1 + 2 + 3)
#12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

user_number= int(input("Digite el numero que desee: "))

total_sum=0

for number in range (1, user_number+1): #Basicamente este es el contador si necesidad de declararlo como variable anteriormente, se inicaliza en uno 1 y se le suma uno a la variable para llegue el monto exacto si no daria uno menos 
    total_sum+=number

print(total_sum)

#PARTE 2

#Ejercicio 1
#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.

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


#Ejercicio 2

#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
#Ejemplos:
#23, 30, 768 → Correcto (hay un 30)
#10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

first_number= int(input("Digite el primer numero: "))
second_number=int(input("Digite el segundo numero: "))
third_number=int(input("Digite el tercer numero: "))

if first_number == 30 or second_number == 30 or third_number ==30:   # Nota tambien se puede hacer poniendo (first_number+second_number+third_number) dentro de la primer condicion, pero inicialmente lo hice asi
    print("Correcto, hay un 30")
else:
    total_sum=first_number + second_number + third_number
    
    if total_sum == 30:
        print("Correcto, la suma dio 30")
    
    else:
        print ("No hay ningun 30")

#Ejercicio 3

#Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores
#Ejemplo:
#Entrada:
#"Ingrese temperatura en Celsius:"25
#Salida:
#Fahrenheit: 77.0
#Kelvin:298.15


print("----- Converitdor de temperaturas -----")

temperature_celsius=float(input("Digite la temperatura que desea convertir a Kelvin y Fahrenheit: "))
temperature_kelvin= temperature_celsius+273.15
temperature_fahrenheit=(temperature_celsius * 9/5) + 32
print(f"La temperatura en Celsius es de {temperature_celsius}°C y convertida a Fahrenheit es de {temperature_fahrenheit}°F")

print(f"La temperatura en Celsius es de {temperature_celsius}°C y convertida a Kelvin es de {temperature_kelvin}K")



#Ejercicio 4

#Tabla de multiplicar personalizada
#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12
#Ejemplo:
#Entrada:
#"Ingrese un número:"7
#Salida:
#7 x 1 = 7
#7 x 2 = 14
#...
#7 x 12 = 84

print("---- Table de multiplicar ----")

user_number=int(input("Digite un numero del 1 al 10 para realizar la multiplicacion hasta el numero 12: "))

for number in range(1,13):
    multiplication=user_number*number
    
    print(f"{user_number} X {number} = {multiplication}")
