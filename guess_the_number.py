guess_number=50
Chance=10
print("Welcome to 'Guess the Number' game...")
while Chance>0:
    print(f"*********************************Change Left : {Chance}")
    a=int(input("Enter your number : "))
    if a-guess_number>10:
        print("Your guess is 'TOO HIGH'")
    elif a-guess_number<0:
        print("Your guess is 'TOO LOW'")
    elif a==guess_number:
        print("Your guess is 'CORRECT'*****YOU WIN*****")
        break
    Chance-=1





