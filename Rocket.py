import math
from inputs import *

def staged_list(part_list, number_stages) :

    stage_list_init = []
    stage_list_final = []

    for i in range(number_stages) :

        for part in part_list :

            if int(part['Stage']) == i+1 :
                stage_list_init.append(part)
        
        stage_list_final.append(stage_list_init)
        stage_list_init = []
    
    return stage_list_final

def mass_total(part_list, wet_dry):
    masses = []
    total_mass = []

    for stage in part_list :

        for part in stage :
            if part['Name'] == 'Fuel Tank' :

                if wet_dry == 'dry' :
                    masses.append(float(part['Mass']) * 0.1)
                
                else : 
                    masses.append(float(part['Mass']))
                
            else :
                masses.append(float(part['Mass']))

        stage_mass = sum(masses)
        masses = []
        total_mass.append(stage_mass)

    return total_mass

if __name__ == '__main__' :

    number_stages = input_check('What is the total number of stages? ', 0)
    rocket_parts = final_list()
    stage_arranged_list = staged_list(rocket_parts, number_stages)

    wet_mass = mass_total(stage_arranged_list, 'wet')
    dry_mass = mass_total(stage_arranged_list, 'dry')
    print(dry_mass)
    print(wet_mass)