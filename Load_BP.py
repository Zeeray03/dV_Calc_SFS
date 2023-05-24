import json

def blueprint_interpreter(data,obj_type) :
    part_list = []

    for obj in data['parts'] :
        part_list.append(obj[f'{obj_type}'])  

    return part_list

def load_func(): 

    file =  open('Blueprint.txt')
    data = json.load(file)
    file.close()

    part = blueprint_interpreter(data,'n')
    part_scale = blueprint_interpreter(data,'o')

    part_info = [part, part_scale]

    return part_info