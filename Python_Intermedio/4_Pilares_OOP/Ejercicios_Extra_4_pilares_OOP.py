from abc import ABC, abstractmethod

#1.Cree una clase Employee con los siguientes requisitos:
#Atributos privados: _name, _salary
#Use @property y @<atributo>.setter para:
#Mostrar el nombre y el salario
#Validar que el salario nunca sea negativo
#Cree un método promote que aumente el salario un porcentaje definido

class Employee:
    
    def __init__(self, name, salary):
        
        self._name=name
        self._salary=salary
        
    @property
    def name(self):
        
        return self._name
    
    
    @property
    def salary(self):
            
        return self._salary
    
    @name.setter
    def name(self,new_name):
        if new_name =="":
            raise ValueError("El nombre no puede estar vacío.")
        
        self._name = new_name
        
    @salary.setter
    def salary(self, new_salary):
        
        if new_salary < 0:
            
            raise ValueError("El salario no puede ser un numero negativo.")
        
        self._salary = new_salary
        
    
    def promote(self,percentage_increase):
        
        self.salary = self.salary * (1 + percentage_increase)
    
    
employee = Employee("Ana", 1000)
employee.promote(0.1)  # +10%


print(employee.salary)  # 1100


#2.Cree una clase abstracta User con los siguientes métodos abstractos:
#get_role()
#has_permission(permission)
#Luego cree dos clases que hereden de ella:
#AdminUser
#RegularUser
#Cada una debe implementar los métodos
#Por ejemplo:
#AdminUser siempre tiene permisos
#RegularUser solo tiene permisos limitados ("read", por ejemplo)


class User(ABC):
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def get_role(self):
        
        pass
    
    @abstractmethod
    def has_permission(self,permission):
        pass
    
class AdminUser(User):

        
    def get_role(self):
        
        return f"{self.name} es un administrador"
    
    def has_permission(self, permission):
        
        return True
        

class RegularUser(User):

    def get_role(self):
        
        return f"{self.name} es un usuario regular"

    def has_permission(self, permission):
        
        return permission.lower() == "read"
    
    
    
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False


#3.Cree una clase base Vehicle con los atributos:
#_brand
#_year
#Agregue un método get_info() que devuelva una descripción del vehículo.
#Luego cree dos clases hijas:
#Car
#Motorcycle
#Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() para incluir esta información adicional.

class Vehicle:
    def __init__(self,brand,year):
        
        self._brand=brand
        self._year=year
        
    def  get_info(self):
        
        return (f"{self._brand} ({self._year})")
    
class Car(Vehicle):
    
    def __init__(self, brand, year,car_type):
        super().__init__(brand, year)
        self.car_type=car_type
        
    def  get_info(self):
            
            return (f"{super().get_info()} - Tipo: {self.car_type}")
    
class Motorcycle(Vehicle):
    
    def __init__(self, brand, year,engine_cc ):
            super().__init__(brand, year)
            self.engine_cc =engine_cc 
            
    def  get_info(self):
                
        return (f"{super().get_info()} - Motor: {self.engine_cc } cc")

vehicle1 = Car("Toyota", 2020, "Todoterreno")
vehicle2 = Motorcycle("Yamaha", 2022, 650)
    


print(vehicle1.get_info())
print(vehicle2.get_info())



        