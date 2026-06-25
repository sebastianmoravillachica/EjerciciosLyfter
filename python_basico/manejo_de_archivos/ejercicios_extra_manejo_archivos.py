#Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y
# escriba todo el contenido en un solo renglón en un nuevo archivo

def read_and_join_lines(path):
    output_path = 'nuevo_saludo.txt'
    content = ""

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            content += line.strip() + " "

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content.strip())


read_and_join_lines('saludo.txt')


#2.Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
def count_words_in_file(path):
    word_count = 0

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            word_count += len(words)

    print(f"Este archivo contiene {word_count} palabras")


count_words_in_file('contar_palabras.txt')

#3.Cree un programa que:
#Lea un archivo línea por línea
#Convierta cada línea a mayúsculas
#Escriba el contenido en un nuevo archivo

def read_file_by_lines(path):
    output_path='nuevo_mayusculas.txt'
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            write_new_file(output_path, line)


def write_new_file(path, line):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(line.strip().upper() + '\n')


read_file_by_lines('mayusculas.txt')



#4.Cree un programa que:
#Pida al usuario una línea de texto
#Agregue esa línea al final de un archivo existente
#Si el archivo no existe, lo crea automáticamente

def write_new_file(path):
    user_input=input("Digite lo que quiera: ")
    
    with open(path,'a',encoding='utf-8') as file:
        file.write(user_input)   


write_new_file('notas.txt')