
#Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_file_by_lines(path):

    new_path = 'new_order_songs.txt'

    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines.sort()

    for line in lines:
        append_to_new_file(new_path, line)


def append_to_new_file(new_path, line):
    with open(new_path, 'a', encoding='utf-8') as file:
        file.write(line)
    


read_file_by_lines('songs.txt')