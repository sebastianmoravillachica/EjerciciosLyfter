import json
import csv

from logica import FinanceManager,Category,Movement


def save_categories(manager,path):
    
    categories_data=[]

    for category in manager.categories_list:
        
        
        add_new_category={
            'name':category.name,
            'color':category.color
        }
        
        categories_data.append(add_new_category)
        
    with open (path,"w",encoding="utf-8") as file:
        
        json.dump(categories_data,file,indent=4)
        
        
def load_categories(manager,path):
    
    try:
        with open(path,"r",encoding="utf-8") as file:
            
            
            categories_data= json.load(file)
            
            for category in categories_data:
                
                new_category=Category(
                    category['name'],
                    category.get('color',"#FFFFFF")
                )
                
                manager.categories_list.append(new_category)
                
    except FileNotFoundError:
        pass


def save_movements(manager, path):
    
    movements_data=[]
    
    for movement in manager.movements_list:
        
        add_new_movement={
            'title': movement.title,
            'amount': movement.amount,
            'category': movement.category,
            'type_movement': movement.type_movement,
            'date': movement.date
        }

        movements_data.append(add_new_movement)
        
    with open (path,"w",encoding="utf-8") as file:
        
        json.dump(movements_data,file,indent=4)


        
def load_movements(manager,path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            
            
            movements_data= json.load(file)
            
            for movement in movements_data:
                
                new_movement=Movement(
                    movement['title'],
                    movement["amount"],
                    movement['category'],
                    movement['type_movement'],
                    movement.get(
                        'date',
                        None
                    )
                )

                manager.movements_list.append(new_movement)
            
    except FileNotFoundError:
        pass


def export_movements_csv(manager,path):
    
    summary=manager.calculate_summary()
    
    with open(path,"w",newline="",encoding="utf-8") as file:
        
        writer=csv.writer(file)
        
        writer.writerow([
            "Fecha",
            "Título",
            "Monto",
            "Categoría",
            "Tipo"
        ])
        
        for movement in manager.movements_list:
            
            amount=movement.amount
            
            if movement.type_movement=="Gasto":
                
                amount=-amount
            
            writer.writerow([
                movement.date,
                movement.title,
                amount,
                movement.category,
                movement.type_movement
            ])
        
        
        writer.writerow([])
        
        writer.writerow([
            "Totales:"
        ])
        
        writer.writerow([
            "Ingresos:",
            summary["income"]
        ])
        
        writer.writerow([
            "Gastos:",
            summary["expense"]
        ])
        
        writer.writerow([
            "Balance Neto:",
            summary["balance"]
        ])