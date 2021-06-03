'''
Function that takes two numbers and return the number that has minimum one's digit number
e.g.
Input               Output
n1=532              532
n2=2346
'''

def one_digit(num1,num2):
    a1=num1%10
    a2=num2%10
    if a1>a2:
        return(num2)
    elif a2>a1:
        return(num1)
    else:
        return("Error both numbers are same...")    
n1=int(input("Enter First number: "))
n2=int(input("Enter Second number: "))            
z=one_digit(n1, n2)
print(z)