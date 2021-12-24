temp = 3

if temp > 30:
    print("Hot Day")
elif temp<30:
    print("Cold Day")
elif temp == 30:
    print("Normal Day")
elif temp != 30:
    print("Just another Day")
else:
    print("Default Case")



name = "Sagar Tushar Shah"
if len(name)<7:
    print("Name must be Greater than 7 Characters")
elif len(name)>20:
    print("Name too big")
else:
    print(f'Got it {name}')