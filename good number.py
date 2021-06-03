'''
Programe tell a number is great or not 
GREAT NUMBER (n):   Number whose sum of digits (l)
                    Product of digit (m) satisfy
                           'm+l=n'
'''

def great(n):
    a=0
    b=1
    for i in str(n):
        a+=int(i)
        b=b*int(i)
    if a+b==n:
        return("GREAT NUMBER")
    else:
        return("NOT A GREAT NUMBER")

n=int(input("Enter a number: "))
for i in range(1,n+1):
    z=great(i)
    print(i,':',z)