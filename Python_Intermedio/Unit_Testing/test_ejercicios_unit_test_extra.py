from funciones_ejercicios_extra import add, calculate_average, multiply, divide,read_lines
import pytest
from unittest.mock import mock_open, patch

#1.Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
# Un caso con números positivos
# Un caso con números negativos
# Un caso con ceros



class TestNumbers:

    def test_add_with_negative_numbers(self):

        # Arrange
        number1 = -10
        number2 = -5

        # Act
        result = add(number1, number2)

        # Assert
        assert result == -15


    def test_calculate_average_with_positive_numbers(self):

        # Arrange
        number1 = 80
        number2 = 90
        number3 = 60

        # Act
        result = calculate_average(number1, number2, number3)

        # Assert
        assert result == 76.66666666666667


    def test_multiply_by_zero(self):

        # Arrange
        number1 = 10
        number2 = 0

        # Act
        result = multiply(number1, number2)

        # Assert
        assert result == 0



# 2.Cree un test que:
# Valide que dividir(10, 2) retorna 5.0
# Verifique que dividir por cero lanza un ValueError
# Valide que dividir con un string como parámetro también lanza TypeError

def test_divide_with_posivite_numbers():
    
    #AAA
    
    # Arrange
        number1 = 10
        number2 = 2

    # Act
        result = divide(number1, number2)

    # Assert
        assert result == 5.0

def test_divide_valueError_when_try_with_0():
    
    #AAA
    
    # Arrange
        number1 = 10
        number2 = 0

    # Act + Assert

        with pytest.raises(ValueError):
            
            divide(number1,number2)
    

def test_divide_typeError_when_try_with_a_string():
    
    #AAA
    
    # Arrange
        number1 = 10
        string_1 = "string"

    # Act + Assert

        with pytest.raises(TypeError):
            
            divide(number1,string_1)



#3.Cree un test que:
# Use unittest.mock para simular el contenido de un archivo
# Verifique que retorna las líneas esperadas sin crear archivos reales
# Compruebe que lanza FileNotFoundError si el archivo no existe

def test_read_lines():

    #AAA

    # Arrange
    file_content = "Línea 1\nLínea 2\nLínea 3\n"
    expected = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]

    # Act
    with patch("builtins.open", mock_open(read_data=file_content)):
        result = read_lines("archivo.txt")

    # Assert
    assert result == expected


def test_read_lines_file_not_found():

    #AAA

    # Arrange
    file_path = "archivo_inexistente.txt"

    # Act + Assert
    with pytest.raises(FileNotFoundError):
        read_lines(file_path)