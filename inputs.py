import math
from Load_BP import *
from partFormulas import *

def input_check(message, type_val) :
    while True :
        
        try :
            if type_val == 1 :
                user_input = float(input(message))
                
                if user_input >= 0 :
                    return user_input
                
                else :
                    print('Enter a number equal too or greater than zero')

            elif type_val == 0 :
                user_input = int(input(message))

                if user_input > 0 :
                    return user_input
                
                else :
                    print('Enter a number greater than zero')
                
            if type_val < 0 :
                user_input = input(message)
                return user_input
            
        except :  
            print('please enter a number.')

def part_stage_indexing(name) :

    part_index_list = []
    part_stage_stuff = []
    parts_name_list = blueprint_importer('Blueprint.txt', 'n')

    for index, elem in enumerate(parts_name_list) :
        if elem == name :
            part_index_list.append(index)
    
    total_part = parts_name_list.count(name)
    count = 0

    for part in parts_name_list :
        if part == name :

            part_stage_stuff.append({'Stage' : input_check(f'What stage is {part} {total_part}? ', 0), 'Part' : name, 'Index' : part_index_list[count]})

            total_part -= 1
            count += 1
    
    return part_stage_stuff

def unified_part_list(staged_index) :
    l = 1

print(part_stage_indexing('Separator'))