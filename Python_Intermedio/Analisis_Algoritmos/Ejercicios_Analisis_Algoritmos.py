#1.Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(list_to_sort):  #O(1)


    for outer_index in range(0, len(list_to_sort) - 1): #O(N)


        has_made_changes = False #O(1)


        for index in range(0, len(list_to_sort) - 1 - outer_index):#O(N^2)
            
            
            current_element = list_to_sort[index] #O(1)
            next_element = list_to_sort[index + 1] #O(1)

            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}') #O(1)

            
            if current_element > next_element: #O(1) 
                print('El elemento actual es mayor al siguiente. Intercambiandolos...') #O(1)
                list_to_sort[index] = next_element #O(1)
                list_to_sort[index + 1] = current_element #O(1)
                has_made_changes = True #O(1)

        
        if not has_made_changes: #O(1)
            return #O(1)


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8] #O(1)
bubble_sort(my_test_list) #O(1)

print(my_test_list) #O(1)


#2.Analice los siguientes algoritmos usando la Big O Notation:


#print_numbers_times_2

def print_numbers_times_2(numbers_list): #O(1) 
	for number in numbers_list: #O(N)
		print(number * 2) #O(1) 

#check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b):#O(1) 
	for element_a in list_a: #O(N)
		for element_b in list_b: #O(N^2)
			if element_a == element_b: #O(1) 
				return True #O(1) 
				
	return False #O(1)

#print_10_or_less_elements

def print_10_or_less_elements(list_to_print): #O(1) 
	list_len = len(list_to_print) #O(1) 
	for index in range(min(list_len, 10)): #O(1) 
		print(list_to_print[index]) #O(1) 


#generate_list_trios

def generate_list_trios(list_a, list_b, list_c): #O(1) 
	result_list = [] #O(1) 
	for element_a in list_a:  #O(N)
		for element_b in list_b: #O(N^2)
			for element_c in list_c: #O(N^3)
				result_list.append(f'{element_a} {element_b} {element_c}') #O(1)
				
	return result_list #O(1)