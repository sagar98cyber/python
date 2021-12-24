command=""
started = False
help = '''
        TYPE THE FOLLOWING COMMANDS TO DRIVE THE CAR!!
        "START" to Start the Engine
        "STOP" to Stop the Engine
        "QUIT" to Quit the Simulation    
        '''
print(help)
while command.lower() != 'quit':
    command=str(input("> "))
    if command.lower() == 'quit':
        print('Thank you!! Please come back soon!!')
        break

    elif command.lower() == 'start':
        if started:
            print('Car has already started!!!')
        else:
            started = True
            print("Car has just started!!!")
    
    elif command.lower() == 'help':
        print(help)
    
    elif command.lower() == 'stop':
        if started:
            print('Car has stopped!!!')
            started = False
        else:
            print('Start the car first!!!')
    
    else:
        print('Sorry I do not understand you at all! Please enter the input again\n')