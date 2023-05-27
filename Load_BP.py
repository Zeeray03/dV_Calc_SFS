import json
import csv

def blueprint_interpreter(data,obj_type) :
    part_list = []

    for obj in data['parts'] :
        part_list.append(obj[f'{obj_type}'])  # fetches all the items for a type in the dictionary indexed as 'parts'

    return part_list

def csv_interpreter(file_name) :

    file = open(file_name)
    data = csv.DictReader(file)
    part_library = []

    for row in data :
        part_library.append(row) #  Creates a nested dictionary where the list is each part and each dictionary is the ID and mass from the csv file
    
    file.close()
    return part_library

def load_func_parts(): 

    file =  open('Blueprint.txt')
    data = json.load(file)
    file.close()

    part_names = blueprint_interpreter(data,'n') # creates a list of all the part ID's in the json file

    return part_names

def load_func_tanks(): 
    file =  open('Blueprint.txt')
    data = json.load(file)
    file.close()

    parts = data['parts'] # creates an array of all the dictionaries
    dimension_list = []

    for part in parts :

        if part['n'] == 'Fuel Tank' : # gets dimensions for each part 

            part_dimen = part['N']

            part_dimen_xa = part_dimen['width_a']
            part_dimen_xb = part_dimen['width_b']
            part_dimen_y = part_dimen['height']
        
        for dimension in range(part['n'].count('Fuel Tank')) :
            dimension_list.append([part_dimen_xa, part_dimen_xb, part_dimen_y]) #creates a 2d list with each list being a fuel tanks dimensions
    
    return dimension_list