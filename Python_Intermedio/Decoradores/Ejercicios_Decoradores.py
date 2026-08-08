from datetime import date

#1.Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def show_parameters(func):

    def wrapper(*args):

        print(f"Parámetros: {args}")

        result = func(*args)

        print(f"Retorno: {result}")

        return result

    return wrapper


@show_parameters
def sum_numbers(a, b):
    return a + b


print(sum_numbers(10, 20))




#2.Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def number_checking(func):
    
    def wrapper(*args):
        
        
        for  arg in args:
            
            
            if not isinstance(arg, int):
                
                raise ValueError(f"El dato ({arg}) no es un número")
            
        return func(*args)
            
    return wrapper
    
@number_checking
def get_numbers(*args):
    
    return f"Numero validados"

print(get_numbers(1,2,3,4,5,6,7,8,9,10))




#3.Cree una clase de User que:
#Tenga un atributo de date_of_birth.
#Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.



class User:
    
    date_of_birth : date
    
    def __init__(self,name,date_of_birth):
        self.name=name
        self.date_of_birth=date_of_birth
        
    def validate_age(func):
        
            def wrapper(user):
                age=user.age
                if age < 18 :
                    
                    raise ValueError ("Menor de edad")
                    
                func(user)
                
            return wrapper
        
    @property
    def age(self):
        
        today = date.today()
        age=(today.year- self.date_of_birth.year- ((today.month, today.day)< (self.date_of_birth.month, self.date_of_birth.day)))
        return age
    
    @validate_age
    def check_user_age(self):
        
        print("Edad verificada") 
        
        
my_user=User("Sebastian",date(2003,9,8))

my_user.check_user_age()
#print(f"{my_user.name} tu edad seria {my_user.age}")
        


