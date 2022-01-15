import utils
def mainFunc():
    print('''
    1. mathematical operation 
    2. area of triangle, square, rectangle
    3. surface area of cone and cube
    4. volume of cube, cone, sphere
    ''')

    user_input = input("> ")
    return user_input
    
def subFunc(user_input):
    diction = {
        '1': '''
        Choose Further Operations

        1. addition
        2. subtraction
        3. divison
        4. multiplication
        ''',
        '2': '''
        Choose Further Operations

        1. Area of Triangle
        2. Area of Square
        3. Area of Cube
        ''',
        '3':'''
        Choose Further Operations

        1. Surface Area of Cube 
        2. Surface Area of Cone
        ''',
        '4':'''
        Choose Further Operations

        1. Volume of Sphere 
        2. Volume of Cone
        3. Volume of Cube
        ''',
    }
    print(diction.get(user_input))
    subUserChoice = input('>')
    var = user_input,subUserChoice
    print(f'VAR: {var}')
    return var

def callRespFunc(tupleVal):
    print(f'First CALLRESPFUNC{type(tupleVal)}')
    if ('1','1') == tupleVal:
        return utils.mathAddi()
    elif ('1','2') == tupleVal:
        return utils.mathSubt()
    elif ('1','3') == tupleVal:
        return utils.mathDivi()
    elif ('1','4') == tupleVal:
        return utils.mathMulti()
    else: 
        start()   

def start():
    userInput = mainFunc()
    subUserInputFunc = subFunc(userInput)
    print(type(subUserInputFunc))
    val = callRespFunc(subUserInputFunc)
    print(type(val))
    return val


dmv = start()
print(f'Post Start(): {dmv}')
