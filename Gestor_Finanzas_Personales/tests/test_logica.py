import pytest

from logica import FinanceManager



# Test CATEGORY
def test_add_category():
    
    #AAA
    #Arrange
    manager= FinanceManager()
    
    #Act
    manager.add_category("Comida")
    
    #Assert
    
    assert len(manager.categories_list)==1
    assert manager.categories_list[0].name=="Comida"


def test_add_empty_category():
    
    #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act + Assert
    
    with pytest.raises(ValueError):
        
        manager.add_category("")
        

def test_add_duplicate_category():
    
    #AAA
    # Arrange
    manager= FinanceManager()

    # Act
    
    manager.add_category("Comida")
    
    
    #Act + Assert
    with pytest.raises(ValueError):
        
        manager.add_category("Comida")
        
        
#Test EXPENSE
        
def test_add_expense():
    
    #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act
    manager.add_category("Transporte")
    manager.add_expense("Gasolina",200,"Transporte")
    
    
    #Assert
    assert len(manager.movements_list)==1

def test_add_expense_with_wrong_amount_value():
    
    #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act
    manager.add_category("Transporte")
    
    #Act + Assert
    
    with pytest.raises(ValueError):
        
        manager.add_expense("Gasolina","10000","Transporte")
        
    
def test_add_expense_with_zero_amount():
    
        #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act
    manager.add_category("Transporte")
    
    #Act + Assert
    
    with pytest.raises(ValueError):
        
        manager.add_expense("Gasolina",0,"Transporte")
        
        
def test_add_expense_with_negative_amount():
        
        #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act
    manager.add_category("Transporte")
    
    #Act + Assert
    
    with pytest.raises(ValueError):
        
        manager.add_expense("Gasolina",-500,"Transporte")
        

# Test INCOME

def test_add_income():
    #AAA
    
    #Arrange
    
    manager=FinanceManager()
    
    #Act
    manager.add_category("Salario")
    manager.add_income("Pago del mes",500000,"Salario")
    movement = manager.movements_list[0]
    
    
    #Assert
    
    assert movement.title == "Pago del mes"
    assert movement.amount == 500000
    assert movement.category == "Salario"
    assert movement.type_movement == "Ingreso"
    
# Test SAVINGS

def test_add_saving():
    
    #AAA
    
    # Arrange
    manager = FinanceManager()

    # Act
    manager.add_category("Ahorro")
    manager.add_saving("Ahorro del mes", 40000, "Ahorro")

    # Assert
    assert len(manager.movements_list) == 1

    movement = manager.movements_list[0]

    assert movement.title == "Ahorro del mes"
    assert movement.amount == 40000
    assert movement.category == "Ahorro"
    assert movement.type_movement == "Ahorro"
    
    
# Test calculate_summary()


def test_calculate_summary():
    manager = FinanceManager()

    manager.add_category("Salario")
    manager.add_category("Comida")
    manager.add_category("Ahorro")

    manager.add_income("Salario", 500000, "Salario")
    manager.add_expense("Comida", 100000, "Comida")
    manager.add_saving("Ahorro mensual", 50000, "Ahorro")

    result = manager.calculate_summary()

    assert result["income"] == 500000
    assert result["expense"] == 100000
    assert result["saving"] == 50000
    assert result["balance"] == 350000
    
    
def test_calculate_summary_without_movements():
    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.calculate_summary()

    # Assert
    assert result["income"] == 0
    assert result["expense"] == 0
    assert result["saving"] == 0
    assert result["balance"] == 0