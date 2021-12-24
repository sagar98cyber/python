weight = int(input('Enter your Weight: '))
p_or_k = str(input('Entered in (L)bs or (K)ilos: '))
dis_weight = 0
if p_or_k == 'k' or p_or_k == 'K':
    dis_weight = weight*2
    print(f'The entered weight is in Kilos: {weight} \n The corresponding Lbs for that is: {dis_weight}')
elif p_or_k == 'l' or p_or_k == 'L':
    dis_weight = weight/2
    print(f'The entered weight is in Lbs: {weight} \n The corresponding Kilos for that is: {dis_weight}')
else:
    print("Enter a valid Input dude!")

