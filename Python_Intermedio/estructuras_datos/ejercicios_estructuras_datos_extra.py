# 1. Cree una estructura que represente una cola básica (Queue) con objetos enlazados
# Restricción:
# no usar list, dict, tuple, collections
# Métodos requeridos:
# enqueue(data): agrega un nodo al final
# Ejemplo:
# Entrada:
#     q.enqueue("A")
# q.enqueue("B")
# q.enqueue("C")
# Salida:
# A -> B -> C

# dequeue(): elimina y retorna el nodo del inicio
# Ejemplo:
# Entrada:
# q.dequeue()
# Salida:
# "A"
# print_all(): imprime todos los elementos de la cola en orden
# Ejemplo:
# Entrada:
#     q.print_all()
# Salida:
#     B -> C


class Node:
    
    data:str
    next="Node"
    
    def __init__(self, data, next=None):
        
        self.data=data
        self.next=next
class Queue:
    
    def __init__(self):
        self.head=None
    
    def enqueue(self, data): #ingresar datos 
        
        new_node=Node(data)
        
        if self.head is None:
            
            self.head=new_node
            return
        
        else:
            
            current_node=self.head
            
            while current_node.next is not None:
                
                current_node=current_node.next
                
            current_node.next=new_node
    
    def dequeue(self): #eliminar datos
        
        if self.head is None:
                    
            print("La fila esta vacia")
            return
        
        removed_head=self.head.data
        
        self.head= self.head.next
        
        return removed_head
    
    def print_all(self):
        
        current_node=self.head
        
        while current_node is not None:
            
            print(current_node.data)
            
            current_node=current_node.next

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()

print("Dequeue:", q.dequeue())

q.print_all()

# 2.Cree una clase LinkedList con los métodos:
# insert_front(data): Inserta al inicio
# Ejemplo:
# Entrada:
#     ll.insert_front(10)
#     ll.insert_front(20)

# Salida:
#     20 -> 10

# insert_back(data): Inserta al final
# Ejemplo:
# Entrada:
#     ll.insert_back(30)

# Salida:
#     20 -> 10 -> 30

# delete(data): Elimina el primer nodo con el valor dado
# Ejemplo:
# Entrada:
#     ll.delete(10)

# Salida:
#     20 -> 30
    

# print_all(): Imprime todos los valores
# Ejemplo:
# Salida:
#     ll.print_all() #20 -> 30


class Node:

    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    head: Node

    def __init__(self):
        self.head = None

    def print_all(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def insert_back(self, adding_number):

        new_node = Node(adding_number)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, number):

        current_node = self.head
        previous_node = None

        while current_node is not None:

            if current_node.data == number:

                # Si estamos eliminando el HEAD
                if previous_node is None:
                    self.head = current_node.next
                    return

                # Si estamos eliminando cualquier otro nodo
                previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

        print(f"El número {number} no existe en la lista")

    def insert_front(self, adding_number):

        new_node = Node(adding_number)
        new_node.next = self.head
        self.head = new_node


ll = LinkedList()

print("Insertando al frente:")
ll.insert_front(10)
ll.insert_front(20)
ll.insert_front(30)
ll.print_all()

print("\nInsertando al final:")
ll.insert_back(40)
ll.print_all()

print("\nEliminando 20:")
ll.delete(20)
ll.print_all()

print("\nEliminando el primero:")
ll.delete(30)
ll.print_all()

print("\nEliminando el último:")
ll.delete(40)
ll.print_all()

print("\nIntentando eliminar un número que no existe:")
ll.delete(100)


# 3. Lista doblemente enlazada
# Requisitos:
# Cada nodo debe tener referencia al siguiente y al anterior
# Métodos:
# append(data): Agrega al final
# Ejemplo:
# Entrada:
#     dll.append("A")
#     dll.append("B")
#     dll.append("C")

# Salida (print_forward):
#     A -> B -> C
# Salida(print_backward):
#     C -> B -> A -> X


# delete(data): Elimina el primer nodo con ese valor
# Ejemplo:
# Entrada:
#     dll.delete("B")

# Salida(print_forward):
#     X -> A -> C
# Salida(print_backward):
#     C -> A -> X
    

# print_forward() y print_backward(): Imprime en ambas direcciones
# Ejemplo:
# Salida:
#     print_forward()  #→ X -> A -> C
#     print_backward() #← C -> A -> X

class Node:

    data: int
    next: "Node"
    previous: "Node"

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, data):

        current_node = self.head

        while current_node is not None:

            if current_node.data == data:

                # Si estamos eliminando el HEAD
                if current_node is self.head:
                    self.head = current_node.next

                    if self.head is not None:
                        self.head.previous = None
                    else:
                        self.tail = None

                    return

                # Si estamos eliminando el TAIL
                if current_node is self.tail:
                    self.tail = current_node.previous
                    self.tail.next = None
                    return

                # Si estamos eliminando un nodo del medio
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                return

            current_node = current_node.next

        print(f"El número {data} no existe en la lista")

    def print_forward(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_backward(self):

        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous