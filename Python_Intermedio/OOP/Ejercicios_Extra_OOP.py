#1.Cree una clase Rectangle que:
#Tenga atributos width y height
#Tenga un método get_area() que retorne el área
#Tenga un método get_perimeter() que retorne el perímetro
#Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle():
    
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
        if width <0 or height <0:
            raise ValueError ("Existe un valor negativo, los valores deben ser positivos")
    
    
    def get_area(self):
        
            rectangle_area=self.width*self.height
            return rectangle_area
            
            
    def get_perimeter(self):
        rectangle_perimeter=2*(self.width+self.height)
        return rectangle_perimeter


try:
    width=float(input("Ingrese el ancho: ").strip())
    height=float(input("Ingrese la altura: ").strip())
    
    rectangle_1=Rectangle()

    print(rectangle_1.get_area(width,height))

    print(rectangle_1.get_perimeter(width,height))
except ValueError as error:
    print(error)

#2.Cree una clase base Animal y dos clases hijas Dog y Cat:
#Animal debe tener nombre y método speak() que retorne "Hace un sonido"
#Dog debe sobrescribir speak() para decir "Guau"
#Cat debe sobrescribir speak() para decir "Miau"


class Animal():
    
    def __init__(self,name):
        
        self.name=name

class Dog(Animal):
        
    def speak(self):
        return f"{self.name} dice: Guau"

class Cat(Animal):
        
    def speak(self):
        return f"{self.name} dice: Miau"

dog=Dog("Kira")
print(dog.speak())

cat=Cat("Minino")
print(cat.speak())


#3.Cree una clase Product con:
#Nombre, precio y cantidad
#Cree una clase Inventory que:
#Guarde productos en una lista
#Tenga métodos para:
##Mostrar todos los productos
#Calcular el valor total del inventario


class Product:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Inventory:

    def __init__(self):
        self.product_list = []

    def save_product(self, product):
        self.product_list.append(product)
        

    def show_inventory(self):
        for product in self.product_list:
            print(
                f"Nombre: {product.name}, "
                f"Precio: ₡{product.price}, "
                f"Cantidad: {product.amount}"
            )

    def get_total_value(self):
        total_value = 0

        for product in self.product_list:
            total_value += product.price * product.amount

        return total_value



inventory = Inventory()


product_1 = Product("Arroz", 2500, 9)
product_2 = Product("Leche", 1800, 5)
product_3 = Product("Azúcar", 1500, 3)


inventory.save_product(product_1)
inventory.save_product(product_2)
inventory.save_product(product_3)


inventory.show_inventory()


print(f"\nValor total del inventario: ₡{inventory.get_total_value()}")
