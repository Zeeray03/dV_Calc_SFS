import math

def input_check(message) :

    while True :
        
        try :

            user_input = float(input(message))

            if user_input > 0 :
                
                return user_input
            
            else :
                
                print('Please enter a positive number.')
        
        except : 
            
            print('please enter a number.')

if __name__ == '__main__' :

    input_check('Enter fucker ')