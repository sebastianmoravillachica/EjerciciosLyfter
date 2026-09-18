
def bubble_sort(list_to_sort):
    
    
    for out_index in range(0,len(list_to_sort)-1):
        
        had_made_changes=False
        
        for index in range(0,len(list_to_sort)-1-out_index):
            
            current_element=list_to_sort[index]
            next_element=list_to_sort[index+1]
            
            if current_element > next_element:
                
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                
                had_made_changes=True
                
        
        if not had_made_changes:
            
            return



