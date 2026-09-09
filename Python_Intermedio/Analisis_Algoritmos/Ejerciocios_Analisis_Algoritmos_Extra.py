#Ejercios Extra

#1.Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

#Versión 1:
    
def manual_add(number): #O(1)
    result = 0 #O(1)
    for i in range(1, number + 1): #O(N)
        result += i #O(1)
    return result #O(1)

#Versión 2:
    
def add_formula(number): #O(1)
    
    return number * (number+1) // 2 # O(log N)
    

# Preguntas:
# ¿Cuál es la complejidad de cada versión?

# Version 1: O(1),O(1),O(n),O(1) y O(1)
# Version 2: O(1),O(log N)

# ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?

#Yo usuraria la version dos ya que acorta el camino ya que su nivel de complejidad es mas bajo que el de la version 1, 
# tambien la utilizaria ya que el codigo se ve mucho mas elegante y limpio como en la segunda version


# 2.Considere los siguientes dos algoritmos:

def linear_search(my_list, target): # O(1)
    for item in my_list: #O(N)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)

def binary_search(my_list, target): # O(1)
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: #O(N)
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else: # O(1)
            high = mid - 1 # O(1)
    return False # O(1)



# Preguntas:

# ¿Cuál es la complejidad de cada algoritmo?

#1. O(1),O(N),O(1),O(1),O(1)
#2. O(1),O(1),O(1),O(N),O(1),O(1),O(1),O(1),O(1),O(1),O(1),O(1)

# ¿En qué condiciones conviene usar cada uno?

# Cuando la lista esta ordena el mejor seria el 2 y cuando la lista esta en desorden seria el numero 1

# ¿Qué pasa si la lista no está ordenada?

# Con el segundo codigo no se podria buscar tan facil el numero ya que, el segundo codigo corta para poder asi buscar segundo si es menor o mayor, y con el primero si por que le busca por todo los indices

# 3.Analice la siguiente función:

def print_all_pairs(my_dict): # O(1)
    for key1 in my_dict: #O(N)
        for key2 in my_dict: #O(N^2)
            print(f"{key1}-{key2}") # O(1)
            
# Preguntas:
# ¿Cuál es la complejidad temporal?

# O(1), O(N), O(N^2), O(1)

# ¿Cuanto dura si hay 1 millón de claves?

# 1,000,000,000,000
