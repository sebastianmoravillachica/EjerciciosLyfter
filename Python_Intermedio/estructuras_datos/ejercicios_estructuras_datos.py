# 1. Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:
    
    data:str
    next="Node"
    
    def __init__(self,data,next=None):
        
        self.data=data
        self.next=next

class Stack:
    
    def __init__(self):
        
        self.top=None
    
    def push(self, data):
        
        new_node = Node(data)
    
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        
        if self.top is None:
            
            print("Pila vacia")
            
            return
        
        pop_top=self.top.data
        
        self.top=self.top.next 
        
        return pop_top
    
    def print_stack_information(self):
        
        current_node= self.top
        
        while current_node is not None:
            
            print(current_node.data)
            
            current_node=current_node.next

stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

stack.print_stack_information()

print("Sacando:", stack.pop())

stack.print_stack_information()


# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:
    
    data: str
    next:"Node"
    
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
class Deque:
    
    def __init__(self):
        
        self.head=None
        self.tail=None
    
    def push_left(self,data):
        
        new_node=Node(data)
        
        if self.head is None:
            
            self.head=new_node
            self.tail=new_node
            return
        
        new_node.next=self.head 
        self.head=new_node
        
    def push_right(self,data):
        
        new_node=Node(data)
        
        if self.head is None:
                    
            self.head=new_node
            self.tail=new_node
            return
        
        self.tail.next=new_node
        
        self.tail=new_node
    
    def pop_left(self):
        
        if self.head is None:
        
            print("Cola Vacia")
            return
        
        removed_left=self.head.data
        
        self.head=self.head.next
        
        if self.head is None:
            self.tail = None
            
        
        return removed_left
    
    def pop_right(self):
        
        
        if self.head is None:
                
            print("Cola Vacia")
            
            return
                
        removed_right=self.tail.data
        
        if self.head is self.tail:
            
            self.head=None
            self.tail=None
            
            return removed_right
        
        current_node=self.head
        
        while current_node.next is not self.tail:
            
            current_node=current_node.next
            
        self.tail=current_node
        
        self.tail.next=None
        
        return removed_right

    
    def print_dequeu_information(self):
        
        current_node= self.head
        
        while current_node is not None:
            
            print(current_node.data)
            
            current_node=current_node.next


# 3. Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    
    data: str
    left:"Node"
    right:"Node"
    
    def __init__(self,data,left=None,right=None):
        
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    
    def __init__(self):
        
        self.root=None
        
    
    def preorder(self, node):

            if node is None:
                return

            print(node.data)            #YO

            # Recursividad 
            
            self.preorder(node.left) # Left

            self.preorder(node.right) # Right
            
            # Result A-B-D-F-E-G-C
        
    def inorder(self, node):
        
        if node is None:
            return
        
        # Recursividad 
                
        self.inorder(node.left) # Left
        
        print(node.data)        #YO
        
        self.inorder(node.right) # Right
        
        # Result F-D-B-E-G-A-C
        
    def postorder (self, node):
        
        
        if node is None:
            
            return
        
        self.postorder(node.left) # Left
        
        self.postorder(node.right) # Right
        
        print(node.data)        #YO
        
        # Result F-D-G-E-B-C-A
            
node_g=Node("G")           
node_f=Node("F")       
node_d = Node("D",node_f)
node_e = Node("E",None,node_g)
node_b = Node("B", node_d, node_e)
node_c = Node("C")
node_a=Node("A",node_b,node_c)

#AQUI LE INDICAMOS QUIEN ES LA NODO PRINCIPAL DEL ARBOL
tree=BinaryTree()
tree.root=node_a

tree.preorder(node_a)