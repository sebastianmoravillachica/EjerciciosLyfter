#1.Cree una clase de BankAccount que:
#Tenga un atributo de balance.
#Tenga un método para ingresar dinero.
#Tengo un método para retirar dinero.
#Cree otra clase que herede de esta llamada SavingsAccount que:
#Tenga un atributo de min_balance que se pueda asignar al crearla.
#Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. 
#Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def _deposit_money(self, amount):

        if amount < 0:
            return "La cantidad a depositar no puede ser un número negativo"

        self.balance += amount
        return f"Depósito realizado con éxito. Balance actual: {self.balance}"

    def _withdraw_money(self, amount):

        if amount < 0:
            return "La cantidad a retirar no puede ser un número negativo"

        if amount > self.balance:
            return "Fondos insuficientes"

        self.balance -= amount
        return f"Dinero retirado con éxito. Balance actual: {self.balance}"


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def _withdraw_money(self, amount):

        if self.balance - amount < self.min_balance:
            return (
                f"No se puede retirar esa cantidad. "
                f"El balance mínimo es de {self.min_balance}."
            )

        return super()._withdraw_money(amount)


account = SavingsAccount(10000, 5000)

print(account._withdraw_money(2000))
print(account._withdraw_money(4000))
print(account._deposit_money(1000))

#2.Cree una clase abstracta de Shape que:
#Tenga los métodos abstractos de calculate_perimeter y calculate_area.
#Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
#Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    
    @abstractmethod
    
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    
    def __init__(self,radius):
        
        self.radius=radius
    
    def calculate_perimeter(self):
            
        return 2*math.pi*self.radius
    
    def calculate_area(self):
                    
        return math.pi*self.radius**2
    
class Square(Shape):
    
    def __init__(self,length):
        
        self.length=length
        
    def calculate_perimeter(self):
            
        return 4 * self.length
    def calculate_area(self):
            
        return self.length**2
class Rectangle(Shape):
    
    def __init__(self,width,height):
        
        self.width=width
        self.height=height
    
    def calculate_perimeter(self):
        
        return 2*(self.width+self.height)
    
    def calculate_area(self):
        
        return self.width*self.height

    
#3.Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#Ejemplos

#1. Combinar comportamientos

class Fly:
    def fly(self):
        print("Estoy volando.")

class Swim:
    def swim(self):
        print("Estoy nadando.")

class Duck(Fly, Swim):
    pass

duck = Duck()

duck.fly()
duck.swim()

#2. Reutilizar código

class Printer:
    def print_document(self):
        print("Imprimiendo documento")

class Scanner:
    def scan_document(self):
        print("Escaneando documento")

class MultifunctionPrinter(Printer, Scanner):
    pass

device = MultifunctionPrinter()

device.print_document()
device.scan_document()

#3. Agregar funcionalidades mediante mixins

class LoggerMixin:
    def log(self, message):
        print(f"LOG: {message}")

class User(LoggerMixin):
    def create(self):
        self.log("Usuario creado")

user = User()
user.create()

#4. Compartir atributos y métodos

class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def work(self):
        print("Trabajando")

class Developer(Person, Employee):
    pass

dev = Developer("Sebastián")

print(dev.name)
dev.work()

