import math
from inputs import *
from Load_BP import *
from partFormulas import *

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

def get_stage_isp(part_list, grav) :
    
    engine_library = csv_interpreter('PartLibrary3.csv')
    stage_thrust = []
    stage_isp = []
    stage_consump = []

    for stage in part_list :
        
        for part in stage :
            
            for item in engine_library :

                if part['Name'] == item['ID'] :
                    stage_thrust.append(int(item['Thrust']) * grav)
                    stage_consump.append(float(item['Consumption']))
        
        if sum(stage_consump) == 0 :
            consump = 1

        else :
            consump = sum(stage_consump)

        stage_isp.append(int(sum(stage_thrust) / (consump * 9.8)))
        stage_thrust = []
        stage_consump = []
    
    return stage_isp

def stage_dv(wet_list, dry_list, isp_list, grav, num_of_stages) :
    
    dv_stage = []

    for stage in range(num_of_stages) :
        extra_mass = 0

        for i in range(stage, num_of_stages) :
            try :
                extra_mass += wet_list[i + 1]
            except :
                extra_mass += 0 
        
        dv_stage.append(deltaV_calc(wet_list[stage] + extra_mass, dry_list[stage] + extra_mass, isp_list[stage], grav))
    
    return dv_stage

if __name__ == '__main__' :

    grav = 9.8

    number_stages = input_check('What is the total number of stages? ', 0)
    rocket_parts = final_list()
    stage_arranged_list = staged_list(rocket_parts, number_stages)

    wet_mass = mass_total(stage_arranged_list, 'wet')
    dry_mass = mass_total(stage_arranged_list, 'dry')
    isp = get_stage_isp(stage_arranged_list, grav)
    dv = stage_dv(wet_mass, dry_mass, isp, grav, number_stages)

    for stage in range(number_stages) :
        print(f'\n\nThe stats for stage {stage + 1} are: \n' + '_' * 26)
        print(f'\n  Wet Mass: {wet_mass[stage]:.2f}\n  Dry Mass: {dry_mass[stage]:.2f}\n  Isp: {isp[stage]}\n  Delta-V: {dv[stage]:.2f}\n' + '_' * 26 + '\n\n')