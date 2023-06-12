import json
import csv

def blueprint_importer(file_name, key) :
   
    file = open(file_name)
    data = json.load(file)
    file.close()
    part_list = []

    for obj in data['parts'] :

        try :
            part_list.append(obj[key])  # fetches all the items for a type in the dictionary indexed as 'parts'
        
        except :
           part_list.append('null')

    return part_list

def csv_interpreter(file_name) :

    file = open(file_name)
    data = csv.DictReader(file)
    part_library = []

    for row in data :
        part_library.append(row) #  Creates a nested dictionary where the list is each part and each dictionary is the ID and mass from the csv file
    
    file.close()
    return part_library

def list_of_parts(): 

    part_names = blueprint_importer('Blueprint.txt','n') # creates a list of all the part ID's in the json file

    return part_names

def unified_library() :
    library = csv_interpreter('PartLibrary.csv') + csv_interpreter('PartLibrary2.csv') + csv_interpreter('PartLibrary3.csv')
    return library
