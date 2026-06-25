
#Cree un programa que:
#Pida al usuario su nombre
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

#Luego pida su edad
#Si no es un número válido, capture el ValueError y muestre un mensaje

#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def get_user_name():
    while (True):
        try:
            user_name=input("Digite su nombre: ")
            if user_name.isdigit():
                raise ValueError("El nombre no puede ser un número")
            return get_user_age(user_name)
        except ValueError as error:
            print(error)
    
def get_user_age(user_name):
    while(True):
        try:
            user_age=int(input("Digite su edad: "))
            return show_result(user_name,user_age)
        except ValueError:
            print("Número no valido")
            
def show_result(name,age):
    
    print( f"Hola {name}, su edad es {age}")
    
get_user_name()



#Cree una función convertir_a_entero(lista) que:
#Reciba una lista de strings
#Intente convertir cada elemento a entero usando int()
#Use try-except para atrapar los errores ValueError
#Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
#Ejemplo:
#Entrada:
#my_list =['4', 'hola','10','5.2']
#Salida:
#"Resultado:"
# "4" "convertido a" 4
#"No se pudo convertir el elemento: hola"
#"10" "convertido a" 10
#"No se pudo convertir el elemento: 5.2"


def convert_to_integer(string_list):
    
    for data in string_list:
        
        try:
            convert_value=int(data)
            print(f"\n{data} convertido a {convert_value}\n")
            
        except ValueError as error:
            print((f"\nNo se pudo convertir el elemento: {data}\n"))

    
    
            


my_list =['4', 'hola','10','5.2']
result=convert_to_integer(my_list)



#3.cree una función sumar_valores(lista) que:
#Reciba una lista de elementos (strings, enteros, flotantes mezclados)
#Intente convertir cada elemento a tipo float
#Si puede, sume el valor y muestre: "<valor> sumado correctamente"
#Si no puede, muestre: "Elemento inválido: <valor>"
#Al final, imprima la suma total
#Ejemplo:
#Entrada:
#my_list = ['10', 'manzana', '5.5', '3', 'n/a']
#Salida:
#10.0 "sumado correctamente"
#"Elemento inválido: manzana"
#5.5 "sumado correctamente"
#3.0 "sumado correctamente"
#"Elemento inválido: n/a"
#"Total de la suma:" 18.5


def sum_values(string_list):
    sum_result=0.0
    for data in string_list:
        
        try:
            convert_value=float(data)
            print(f"\n{convert_value} sumado correctamente\n")
            sum_result+=convert_value
            
        except ValueError as error:
            print((f"\nElemento inválido: {data}\n"))
    return f"\nTotal de la suma: {sum_result}"
    


my_list =['10', 'manzana', '5.5', '3', 'n/a']
result=sum_values(my_list)

print(result)
