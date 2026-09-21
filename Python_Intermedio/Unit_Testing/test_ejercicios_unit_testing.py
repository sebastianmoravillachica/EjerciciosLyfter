from bubble_sort import bubble_sort
from ejercicios_funciones_python_basico import sum_list,reverse_text,check_text,create_list,find_prime_numbers
import pytest
import random

# 1.Cree los siguientes unit tests para el algoritmo bubble_sort:
# Funciona con una lista pequeña.
# Funciona con una lista grande (de más de 100 elementos.)
# Funciona con una lista vacía.
# No funciona con parámetros que no sean una lista.
def test_bubble_sort_small_list():
    
    #AAA
    
    #Arrange
    list_to_sort=random.sample(range(1, 100), 10)
    expected_list = list_to_sort.copy()
    expected_list.sort()
    #Act
    
    bubble_sort(list_to_sort)
    
    assert list_to_sort == expected_list

    
    
    
def test_bubble_sort_big_list():
    
    #AAA
    
    #Arrange
    list_to_sort=random.sample(range(1, 1000), 101)
    expected_list = list_to_sort.copy()
    expected_list.sort()
    #Act
    
    bubble_sort(list_to_sort)
    
    assert list_to_sort == expected_list
    
    
    
    
    
    
def test_bubble_sort_empty_list():
    
    #AAA
    
    #Arrange
    list_to_sort=[]
    #Act
    
    bubble_sort(list_to_sort)
    
    assert len(list_to_sort) == 0
    

def test_bubble_sort_if_not_list():
    
    #AAA
    
    #Arrange
    list_to_sort=(9,0,0,0,1)
    #Act + Assert
    
    with pytest.raises(TypeError):
        bubble_sort(list_to_sort)

# 2.Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2). Enlace:

#SUM_LIST

def test_sum_all_numbers_of_a_list():
    
    #AAA
    
    #Arrange
    list_to_sum=[1,1,1,1,1,1,1,1,1,1]
    #Act
    
    result=sum_list(list_to_sum)
    
    assert result ==10
    
    

def test_sum_all_numbers_of_a_list_with_negative_numbers():
    
    #AAA
    
    #Arrange
    list_to_sum=[1,1,1,-1,1,-22,1,1,1,1]
    #Act
    
    result=sum_list(list_to_sum)
    
    assert result == -15
    
def test_sum_all_number_of_a_list_with_big_numbers():
    
        #AAA
    
    #Arrange
    list_to_sum=[1000,2000,500,6000]
    
        #Act
    
    result=sum_list(list_to_sum)
    
    assert result == 9500

#REVERSE_TEXT

def test_reverse_small_text():
    #AAA
    
    #Arrange
    small_text="hola"
    
    #Act
    
    result=reverse_text(small_text)
    
    assert result == "aloh"
    
def test_reverse_text_with_spaces():
    
    text_with_spaces="Hola mundo"
    
    #Act
        
    result=reverse_text(text_with_spaces)
        
    assert result == "odnum aloH"
    

def test_reverse_text_with_number_and_special_characters():
    
    #AAA
    
    #Arrange
    text_with_number_and_characters = "Python123!"
    
    #Act
    
    result=reverse_text(text_with_number_and_characters)
    
    assert result == "!321nohtyP"

#check_text

def test_check_lowercase_and_uppercase_in_a_text(capsys):
    
    #AAA
    
    #Arrange
    small_text="Hola"
    
    #Act
    
# Capturing what we printed
    check_text(small_text)
    
    capture=capsys.readouterr()
    
    
    assert capture.out == f"El texto es ({small_text}) y tiene una cantidad de minusculas de 3 y de mayusculas 1\n"
    
    
def test_check_without_lowercase_in_a_text(capsys):
    
    #AAA
    
    #Arrange
    text_without_lowercase="PYTHON"
    
    #Act
    
# Capturing what we printed
    check_text(text_without_lowercase)
    
    capture=capsys.readouterr()
    
    
    assert capture.out == f"El texto es ({text_without_lowercase}) y tiene una cantidad de minusculas de 0 y de mayusculas 6\n"
    

def test_check_with_special_characters_in_a_text(capsys):
    
    #AAA
    
    #Arrange
    text_with_special_character="Python123!"
    
    #Act
    
# Capturing what we printed
    check_text(text_with_special_character)
    
    capture=capsys.readouterr()
    
    
    assert capture.out == f"El texto es ({text_with_special_character}) y tiene una cantidad de minusculas de 5 y de mayusculas 1\n"

#create_list

def test_sort_small_text():
    
    #AAA
    
    #Arrange
    first_text="zebra-casa-arbol"
    
    #Act
    
    result=create_list(first_text)
    
    
    assert result=="arbol-casa-zebra"

def test_sort_big_text():
    
    #AAA
    
    #Arrange
    first_text="monitor-python-computadora-variable-funcion"
    
    #Act
    
    result=create_list(first_text)
    
    
    assert result=="computadora-funcion-monitor-python-variable"

def test_check_text_already_sorted():
    
    #AAA
    
    #Arrange
    third_text="arbol-casa-zebra"
    
    #Act
    
    result=create_list(third_text)
    
    
    assert result=="arbol-casa-zebra"



#find_prime_numbers

def test_find_prime_numbers_case_1():
    
    #AAA
    
    #Arrange
    numbers = [1, 2, 3, 4, 5]
    
    #Act
    
    result=find_prime_numbers(numbers)
    
    
    assert result== [2,3,5]
    

def test_find_prime_numbers_case_2():
    
    #AAA
    
    #Arrange
    numbers = [37, 49, 53, 60, 71, 84, 91, 97]
    
    #Act
    
    result=find_prime_numbers(numbers)
    
    
    assert result== [37,53,71,97]
    
    
def test_find_prime_numbers_case_3():
    
    #AAA
    
    #Arrange
    numbers = [4, 6, 8, 9, 10, 12]
    
    #Act
    
    result=find_prime_numbers(numbers)
    
    
    assert result== []