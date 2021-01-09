import os
from termcolor import colored




# colours list must be 
# [are there colours(True/False),
# all one colour (True/False),
# "Colour 1","Colour 2","Colour 3 ect..."]


#Options list must be
# ["op1()","op2() ect..."]






def menu(menuName,menuitems,options,clear,colours):
    
    if colours[0] == False: #No colours just white
        if clear == True:
            os.system('cls')

        print(menuName.center(34,"-"))
        for i in menuitems:
            print("|{:^32}|".format(i))
        print("".center(34,"-"))
        inp = input("Selection [{0}-{1}]: ".format(1,len(options)))
        if inp.isdigit() == True:
            inp = int(inp)
        for i in range(0,len(options)):
            if inp == i+1:
                eval(options[i])
    
    elif colours[0] == True: #There are colours
        if colours[1] == True: #all same colour
            
            if clear == True:
                os.system('cls')

            print(colored(menuName.center(34,"-"),colours[2]))
            for i in menuitems:
                print(colored(("|{:^32}|".format(i)),colours[2]))
            print(colored("".center(34,"-"),colours[2]))
            inp = input("Selection [{0}-{1}]: ".format(1,len(options)))
            if inp.isdigit() == True:
                inp = int(inp)
            for i in range(0,len(options)):
                if inp == i+1:
                    eval(options[i])      
      
      
        elif colours[1] == False: #all different for each menu option
            if clear == True:
                os.system('cls')

            print(colored(menuName.center(34,"-"),colours[2]))
            for i in menuitems:
                print(colored(("{0}{1:^32}{0}".format(colored("|",colours[2]),i)),colours[menuitems.index(i)+3] ))
            print(colored("".center(34,"-"),colours[2]))
            
        
            inp = input("Selection [{0}-{1}]: ".format(1,len(options)))
            if inp.isdigit() == True:
                inp = int(inp)
            for i in range(0,len(options)):
                if inp == i+1:
                    eval(options[i])               

