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


class QueueNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = QueueNode(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            print("La cola está vacía")
            return

        removed_head = self.head.data
        self.head = self.head.next

        return removed_head

    def print_all(self):
        current_node = self.head
        result = ""

        while current_node is not None:
            result += str(current_node.data)

            if current_node.next is not None:
                result += " -> "

            current_node = current_node.next

        print(result)


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


class LinkedListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = LinkedListNode(data)

        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = LinkedListNode(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = None

        while current_node is not None:

            if current_node.data == data:

                if previous_node is None:
                    self.head = current_node.next
                    return

                previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

        print(f"El valor {data} no existe en la lista")

    def print_all(self):
        current_node = self.head
        result = ""

        while current_node is not None:
            result += str(current_node.data)

            if current_node.next is not None:
                result += " -> "

            current_node = current_node.next

        print(result)


ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.insert_back(30)

ll.print_all()

ll.delete(20)

ll.print_all()


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

class DoublyNode:

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def append(self, data):
        new_node = DoublyNode(data)

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

                if current_node is self.head:
                    self.head = current_node.next

                    if self.head is not None:
                        self.head.previous = None
                    else:
                        self.tail = None

                    return

                if current_node is self.tail:
                    self.tail = current_node.previous
                    self.tail.next = None
                    return

                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                return

            current_node = current_node.next

        print(f"El valor {data} no existe en la lista")

    def print_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.previous is not None:
                print(" -> ", end="")

            current_node = current_node.previous

        print()


dll = DoublyLinkedList()

dll.append("B")
dll.append("C")
dll.prepend("A")

dll.print_forward()
dll.print_backward()

dll.delete("B")

dll.print_forward()
dll.print_backward()
