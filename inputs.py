import math
from Load_BP import *
from partFormulas import *

def input_check(message, type_val) :
    while True :
        
        try :
            if type_val == 1 :
                user_input = float(input(message))

            else :
                user_input = int(input(message))

            if user_input > 0 :
                return user_input
            
            else :
                print('Please enter a positive number.')
        
        except :  
            print('please enter a number.')

def tank_input() : # assigns stage index to the tank dimensions
    
    tank_dimensions = load_func_tanks()

    for tank in range(len(tank_dimensions)) :

        tank_dimensions[tank].append(
            input_check(f'Please enter the stage of tank {tank+1} {int(tank_dimensions[tank][0])}x{int(tank_dimensions[tank][2])}: ', 0)
            )
    
    return tank_dimensions

def part_input() :
    
    part_list = load_func_parts()
    part_library = csv_interpreter('PartLibrary.csv')

    for part_type in range(len(part_library)) :
        part_ID = part_library[part_type]
        print(part_ID)
        part_counts = part_list.count(part_ID['ID'])
        print(part_counts)

part_input()

