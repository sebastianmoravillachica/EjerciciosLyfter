from datetime import datetime
#1.Cree una función que imprima “Hola, [nombre]” dos veces:
#Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
#Ejemplo:
#Salida:
#"Hola, Jeanca"
#"Hola, Jeanca"


def repeat_twice(func):

    def wrapper(name):

        print(func(name))
        print(func(name))

    return wrapper


@repeat_twice
def greet(name):
    return f"Hola, {name}"


greet("Sebastian")



#2.Cree un decorador @requires_login que:
#Verifique si la variable global user_logged_in es True
#Si no lo es, debe lanzar una excepción "Usuario no autenticado"
#Si lo es, la función decorada se ejecuta normalmente
#Ejemplo:

#Entrada:
#user_logged_in = False

#@requires_login
#def view_profile():
#print("Mostrando perfil del usuario")


def requires_login(func):
    
    def wrapper():
        
        if not user_logged_in:
            
            raise ValueError ("Usuario no autenticado")
        
        return func()
    
    return wrapper

user_logged_in = False

@requires_login
def view_profile():
    
    print("Mostrando perfil del usuario")
    
    

view_profile()


#3.Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
#A esta función se le debe combinar dos decoradores:
#@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
#@validate_numbers: revisa que todos los argumentos sean numéricos
#Ejemplo:
#multiply(3, 4)
"func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
"Resultado 12"

        

def validate_numbers(func):
    
    def wrapper(*args):
        
        for arg in args:
            
            if not isinstance(arg,(int,float)):
                
                print(f"{arg} no es un numero")

        result=func(*args)
            
        return result
        
    return wrapper
    
def log_call(func):

    def wrapper(*args):

        result = func(*args)

        current_date = datetime.now()

        print(f"func:{func.__name__} - args: {args} - [{current_date}] - {result}")
        

        return result

    return wrapper


@log_call
@validate_numbers
def multiply (a,b):
    
    return f"Resultado: {a*b}"



print(multiply(2,4))

