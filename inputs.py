def input_check_num(message) :
    while True :
        
        try :

            user_input = float(input(message))

            if user_input > 0 :
                return user_input
            
            else :
                print('Please enter a positive number.')
        
        except :  
            print('please enter a number.')

def tank_input() :
    blah = 1
