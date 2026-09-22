#1. 
def add(number1, number2):
    return number1 + number2


def calculate_average(number1, number2, number3):
    return (number1 + number2 + number3) / 3


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


print(divide(10, 2))


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

