# Ejercicios de Algoritmos de Ordenamiento

# 1.Crea un bubble_sort por tu cuenta sin revisar el código de la lección.


def first_bubble_sort(list_to_sort):
    
    for out_index in range(0, len(list_to_sort)-1):
        
        has_made_changes=False
        
        for index in range(0, len(list_to_sort)-1-out_index):
            
            current_element=list_to_sort[index]
            
            next_element=list_to_sort[index+1]
            
            print(f"Iteracion {out_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}")
            
            if current_element > next_element:
                
                print("El elemento actual es mayor al sigiente, intercambiandolos...")
                
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                
                has_made_changes=True
            
            
        if not has_made_changes:
            return


my_test_list = [18, -11, 68, 6, 32, 53, -2]
first_bubble_sort(my_test_list)

print(my_test_list)


# 2.Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).



def second_bubble_sort(list_to_sort):

    for out_index in range(0, len(list_to_sort) - 1):

        has_made_changes = False

        for index in range(len(list_to_sort) - 1, out_index, -1):

            current_element = list_to_sort[index]
            next_element = list_to_sort[index - 1]

            print(
                f"Iteracion {out_index}, {index}. "
                f"Elemento actual: {current_element}, "
                f"Elemento anterior: {next_element}"
            )

            if current_element < next_element:

                print("El elemento actual es menor al anterior, intercambiandolos...")

                list_to_sort[index] = next_element
                list_to_sort[index - 1] = current_element

                has_made_changes = True

        if not has_made_changes:
            return


my_seond_test_list = [5, 3, 4, 1, 2]

print("Lista antes:")
print(my_seond_test_list)

second_bubble_sort(my_seond_test_list)

print("Lista después:")
print(my_seond_test_list)
