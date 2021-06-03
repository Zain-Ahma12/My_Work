import random
def random_1(num1,num2):
    if num1>>num2:
        a=random.random()
        b=(num2-num1)*a+num1
        return(b)
    else:
        retun(f'Wrong input because {num1} !> {num2}')    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
r=random_1(num1, num2)
print(f'Random number between {num1} and {num2} is {r}')
