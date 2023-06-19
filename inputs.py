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
    part_dimensions = blueprint_importer('Blueprint.txt', 'N')
    
    for index, elem in enumerate(parts_name_list) :
        if elem == name :
            part_index_list.append(index)
    
    total_part = parts_name_list.count(name)
    count = 0
    
    for part in parts_name_list :
        if part == name :
            if name == 'Fuel Tank' :
                part_dimen = part_dimensions[int(part_index_list[count])]
                width = 'width_original'
                height = 'height'
                part_stage_stuff.append({'Stage' : input_check(f'What stage is Fuel Tank {int(part_dimen[width]*2)}x{int(part_dimen[height]*2)} {total_part}? ', 0), 'Index' : part_index_list[count], 'Name' : part})

            else :
                part_stage_stuff.append({'Stage' : input_check(f'What stage is {part} {total_part}? ', 0), 'Index' : part_index_list[count], 'Name' : part})

            total_part -= 1
            count += 1
    
    return part_stage_stuff

def unified_part_list(stuff) :

    parts_data_list = blueprint_importer('Blueprint.txt', 'N')
    unified_list = []

    for part in range(len(stuff)) :

        try :
            item = stuff[part]
            item.update({'Dimensions' : parts_data_list[item['Index']]})
            unified_list.append(item)
        except :
            'null'
    return unified_list

def mass_getter(unified, library) :

    list_mass = []

    for index in unified :
        for part in library :
            if part['ID'] == index['Name'] :

                if int(part['Type']) == 2 :
                   mass = part['Mass']

                elif int(part['Type']) == 1 :
                    dimensions = index['Dimensions']
                    mass = area_formula(dimensions['width_a'], dimensions['width_b'], dimensions['height'], part['Coeffcient'])

                elif int(part['Type']) == 0 :
                    dimensions = index['Dimensions']
                    try :
                        mass = width_formula(dimensions['width'], part['Coeffcient'])
                    except :
                        mass = width_formula(dimensions['size'], part['Coeffcient'])

                elif int(part['Type']) == 3 :

                    dimensions = index['Dimensions']
                    mass = aread_formula2(dimensions['width'], dimensions['height'], part['Coeffcient'])

            else :
                continue

        item = unified[unified.index(index)]
        item['Mass'] = mass
        item.pop('Dimensions')
    
    return unified       

def final_list() :

    part_names = [*set(list_of_parts())]
    libraries = unified_library()
    list_final = []

    for part in part_names :
        list_final = mass_getter(unified_part_list(part_stage_indexing(part)), libraries) + list_final

    return list_final
