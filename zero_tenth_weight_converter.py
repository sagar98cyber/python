weight = int(input('Enter your Weight: '))
p_or_k = str(input('Entered in (L)bs or (K)ilos: '))
dis_weight = 0
#this is what I did
#if p_or_k == 'k' or p_or_k == 'K':

#optimizing the code:
if p_or_k.upper() == 'K':
    dis_weight = weight/0.45
    print(f'The entered weight is in Kilos: {weight} \n The corresponding Lbs for that is: {dis_weight}')
#similarly I did this to improve the code below
#elif p_or_k == 'l' or p_or_k == 'L':
#we do this:
elif p_or_k.upper() == 'L':
    dis_weight = weight*0.45
    print(f'The entered weight is in Lbs: {weight} \n The corresponding Kilos for that is: {dis_weight}')
else:
    print("Enter a valid Input dude!")

