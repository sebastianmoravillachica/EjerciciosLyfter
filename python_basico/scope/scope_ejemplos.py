"SCOPE LOCAL"
def declare_variable():
    variable_inside_function_scope = 8
    print(f'Inside function: {variable_inside_function_scope}') # ETSA VARIABLE ES LOCAL DENTRO DE LA FUNCION


declare_variable()
print(f'Out of function: {variable_inside_function_scope}')# PERO ESTA VARIABLE DESDE AFUERA NO EXISTE

"SCOPE GOBAL"
variable_outside_function_scope = 7 #ESTO ES UNA VARIABLE LOCAL LO QUE SIGNIFICA QUE SI PODEMOS ACCEDER A ELLA DENTRO DE UN DEF

def print_variable():
    print(f'Inside function: {variable_outside_function_scope}')# POR EJEMPLO AQUI, ESTA DECLARADA EN LA LINEA 10 PERO DE IGUAL FORMA LA PODEMOS USAR DENTRO DEL DEF


print_variable()
print(f'Outside function: {variable_outside_function_scope}') # Y TAMBIEN LA PODEMOS USAR FUERA DEL DEF

#======================================================================================#

"VARIABLE GLOBAL"

numbers_list = [53, 60, 32, 62, 400, 10]


def remove_tenths():
    index = 0
    while (index < len(numbers_list)):
        if numbers_list[index] % 10 == 0:
            numbers_list.pop(index)
        else:
            index += 1


def multiply_numbers_by_2():
    for index, number in enumerate(numbers_list):
        numbers_list[index] = number * 2


def main():
    remove_tenths()
    multiply_numbers_by_2()
    print(numbers_list)


if __name__ == "__main__":
    main()
    
"VARIABLE LOCAL"
    
def remove_tenths(numbers_list):
    index = 0
    while (index < len(numbers_list)):
        if numbers_list[index] % 10 == 0:
            numbers_list.pop(index)
        else:
            index += 1


def multiply_numbers_by_2(numbers_list):
    for index, number in enumerate(numbers_list):
        numbers_list[index] = number * 2


def main():
    numbers_list = [53, 60, 32, 62, 400, 10]
    remove_tenths(numbers_list)
    multiply_numbers_by_2(numbers_list)
    print(numbers_list)


if __name__ == "__main__":
    main()
    