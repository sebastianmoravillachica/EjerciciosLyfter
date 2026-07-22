#1.Cree una clase de Circle con:
#Un atributo de radius (radio).
#Un método de get_area que retorne su área.

class CircleAreaCalculator:
    
    
    def get_area(self,radius):
        
        pi=3.14159
        self.radius=radius
        circle_area=pi*pow(self.radius,2)
        return circle_area
    
        
    
circle=CircleAreaCalculator()

print(circle.get_area(8))


#Cree una clase de Bus con:
#Un atributo de max_passengers.
#Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#Un método para bajar pasajeros uno por uno (en cualquier orden).


class Person:

    def __init__(self, name):
        self.name = name


class Bus:

    def __init__(self):
        self.max_passengers = 8
        self.passengers = []

    def add_passenger(self, person):

        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} subió al bus.")
        else:
            print("El bus está lleno.")

    def let_passenger_off(self):

        if len(self.passengers) > 0:
            person = self.passengers.pop()
            print(f"{person.name} se bajó del bus.")
        else:
            print("No hay pasajeros en el bus.")


my_bus = Bus()

person1 = Person("Sebastián")
person2 = Person("Ana")
person3 = Person("Carlos")

my_bus.add_passenger(person1)
my_bus.add_passenger(person2)
my_bus.add_passenger(person3)

my_bus.let_passenger_off()
my_bus.let_passenger_off()
my_bus.let_passenger_off()





# EJERCICIO 3 ESTA EN LA CARPETA SISTEMA_ESCOLAR_2



#4.ree las siguientes clases:
#Head
#Torso
#Arm
#Hand
#Leg
#Feet
#Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
#Por ejemplo (este código esta incompleto, pero describe la idea):


"""
class Torso:
	def __init__(self, head, right_arm, ...):
		self.head = head
		self.right_arm = right_arm
		...
		
class Hand:
	def __init__(self):
		pass

class Arm:
	def __init__(self, hand):
		self.hand = hand


right_hand = Hand()
right_arm = Arm(right_hand)
torso = Torso(head, right_arm, ...)
"""


class Torso:
    
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        
        self.head=head
        self.right_arm=right_arm
        self.left_arm=left_arm
        self.right_leg=right_leg
        self.left_leg=left_leg

class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass


class Arm:
    def __init__(self,hand):
        self.hand=hand
        
class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self,foot):
        
        self.foot=foot


class Human:
    def __init__(self,torso):
        self.torso=torso
        
head=Head()

right_hand=Hand()
left_hand=Hand()
right_arm=Arm(right_hand)
left_arm=Arm(left_hand)

right_feet=Feet()
left_feet=Feet()
right_leg=Leg(right_feet)
left_leg=Leg(left_feet)

torso=Torso(head,right_arm,left_arm,right_leg,left_leg)

human_1=Human(torso)

