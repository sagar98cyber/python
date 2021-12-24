guess_limit = 3
secret_number = 9
guess_count = 0

while guess_count<guess_limit:
    guess_num = int(input("Guess the number: "))
    if guess_num == secret_number:
        print('You won!')
        break
    guess_count += 1

else:
    print("Sorry you failed!!")   