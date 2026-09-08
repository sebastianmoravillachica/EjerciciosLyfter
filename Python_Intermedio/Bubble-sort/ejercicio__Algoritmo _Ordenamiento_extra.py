#Ejercicios Extra de Algoritmos de Ordenamiento

# 1.Implemente un bubble_sort que funcione para los ejercicios de estructura de datos: https://learning.lyfter.team/dashboard/duad/roadmap/python-intermedio/activity/ejercicios-de-estructuras-de-datos
# La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso

# 2.Conteo de pasos (bubble_sort_steps)
# Modifique su implementación de bubble_sort para que:
# Cuente cuántas iteraciones (pasadas) realiza el algoritmo
# Cuente cuántos intercambios se hicieron en total

# 3.Validación de entrada antes de ordenar
# Cree una función que reciba una lista y valide:
# Que todos los elementos sean números
# Que no esté vacía
# Luego aplique bubble_sort si pasa las validaciones
# Si hay error, debe lanzar un mensaje apropiado

class StackNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Pila vacia")
            return

        pop_top = self.top.data
        self.top = self.top.next

        return pop_top

    def print_stack_information(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    def bubble_sort_steps(self):

        if self.top is None:
            print("Error: La estructura esta vacia")
            return

        iterations = 0
        swaps = 0
        out_index = self.top

        while out_index is not None:

            current_node = self.top
            has_made_changes = False

            while current_node.next is not None:

                next_node = current_node.next

                if current_node.data > next_node.data:

                    temp = current_node.data
                    current_node.data = next_node.data
                    next_node.data = temp

                    swaps += 1
                    has_made_changes = True

                current_node = current_node.next

            iterations += 1

            if not has_made_changes:
                break

            out_index = out_index.next

        print("Lista ordenada:", end=" ")
        self.print_stack_information()

        print("Iteraciones:", iterations)
        print("Intercambios:", swaps)

    def validated_bubble_sort(self):

        if self.top is None:
            print("Error: La estructura esta vacia")
            return

        current_node = self.top

        while current_node is not None:

            if not isinstance(current_node.data, (int, float)):
                print("Error: La estructura contiene elementos no numericos")
                return

            current_node = current_node.next

        self.bubble_sort_steps()


stack = Stack()

stack.push(5)
stack.push(2)
stack.push(8)
stack.push(1)
stack.push(4)

print("STACK")
print("Antes:")
stack.print_stack_information()

stack.validated_bubble_sort()


class DequeNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = DequeNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def push_right(self, data):
        new_node = DequeNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("Cola vacia")
            return

        removed_left = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_left

    def pop_right(self):
        if self.head is None:
            print("Cola vacia")
            return

        removed_right = self.tail.data

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return removed_right

        current_node = self.head

        while current_node.next is not self.tail:
            current_node = current_node.next

        self.tail = current_node
        self.tail.next = None

        return removed_right

    def print_deque_information(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    def bubble_sort_steps(self):

        if self.head is None:
            print("Error: La estructura esta vacia")
            return

        iterations = 0
        swaps = 0
        out_index = self.head

        while out_index is not None:

            current_node = self.head
            has_made_changes = False

            while current_node.next is not None:

                next_node = current_node.next

                if current_node.data > next_node.data:

                    temp = current_node.data
                    current_node.data = next_node.data
                    next_node.data = temp

                    swaps += 1
                    has_made_changes = True

                current_node = current_node.next

            iterations += 1

            if not has_made_changes:
                break

            out_index = out_index.next

        print("Lista ordenada:", end=" ")
        self.print_deque_information()

        print("Iteraciones:", iterations)
        print("Intercambios:", swaps)

    def validated_bubble_sort(self):

        if self.head is None:
            print("Error: La estructura esta vacia")
            return

        current_node = self.head

        while current_node is not None:

            if not isinstance(current_node.data, (int, float)):
                print("Error: La estructura contiene elementos no numericos")
                return

            current_node = current_node.next

        self.bubble_sort_steps()


deque = Deque()

deque.push_right(5)
deque.push_right(2)
deque.push_right(8)
deque.push_right(1)
deque.push_right(4)

print()
print("DEQUE")
print("Antes:")
deque.print_deque_information()

deque.validated_bubble_sort()


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self, node):

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):

        if node is None:
            return

        self.inorder(node.left)

        print(node.data, end=" ")

        self.inorder(node.right)

    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        print(node.data, end=" ")

    def bubble_sort_steps(self):

        if self.root is None:
            print("Error: La estructura esta vacia")
            return

        iterations = 0
        swaps = 0
        changed = True

        while changed:

            changed = False
            previous_node = None

            def traverse(node):

                nonlocal previous_node
                nonlocal changed
                nonlocal swaps

                if node is None:
                    return

                traverse(node.left)

                if previous_node is not None:

                    if previous_node.data > node.data:

                        temp = previous_node.data
                        previous_node.data = node.data
                        node.data = temp

                        swaps += 1
                        changed = True

                previous_node = node

                traverse(node.right)

            traverse(self.root)

            iterations += 1

        print("Lista ordenada:", end=" ")
        self.inorder(self.root)
        print()

        print("Iteraciones:", iterations)
        print("Intercambios:", swaps)

    def validated_bubble_sort(self):

        if self.root is None:
            print("Error: La estructura esta vacia")
            return

        valid = True

        def validate(node):

            nonlocal valid

            if node is None:
                return

            if not isinstance(node.data, (int, float)):
                valid = False
                return

            validate(node.left)
            validate(node.right)

        validate(self.root)

        if not valid:
            print("Error: La estructura contiene elementos no numericos")
            return

        self.bubble_sort_steps()


node_g = TreeNode(7)
node_f = TreeNode(6)

node_d = TreeNode(4, node_f)
node_e = TreeNode(5, None, node_g)

node_b = TreeNode(2, node_d, node_e)

node_c = TreeNode(3)

node_a = TreeNode(8, node_b, node_c)

tree = BinaryTree()

tree.root = node_a

print()
print("BINARY TREE")

print("Inorder antes:")
tree.inorder(tree.root)
print()

tree.validated_bubble_sort()