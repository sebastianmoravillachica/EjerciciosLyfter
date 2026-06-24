#Cree un diccionario que guarde la siguiente información sobre un hotel:
#nombre
#numero_de_estrellas
#habitaciones
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
#numero
#piso
#precio_por_noche

hotels={
    "name":"barcelo",
    "stars_numbers":7,
    "room":[{"room_number":2,
                "floor":3,
                "price":85},
                {"room_number":3,
                "floor":5,
                "price":90}
            ]
}


for key, value in hotels.items():

    if type(value) == list:
            
        for room in value:
            print(key)
            for data, info in room.items():
                
                print(data, ":", info)

    else:
        print(key, ":", value)

#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#Ejemplos:
#list_a = [’first_name’, ‘last_name’, ‘role’]
#list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
#→ {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}
    

list_a = ["first_name","last_name","role"]
list_b = ["Sebastian","Mora","Software"]
dictionary={}

for list1 in range(len(list_a)):
    dictionary[list_a[list1]]=list_b[list1]

print(dictionary)


#Cree un programa que use una lista para eliminar keys de un diccionario.
#Ejemplos:
#list_of_keys = [’access_level’, ‘age’]
#employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
#→ {’name’: ‘John’, 'email’: ‘john@ecorp.com’}


list_of_keys = ['access_level', 'age']

employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
}

for key in list_of_keys:
    del employee[key]

print(employee)