'''
Function that takes a number n and then return a randomly generated number having exactly
n digit
e.g.
input: 2
output:
randomly generated number between 10-99
'''

import random as r
def rand_digit(N):
    a=r.random()
    b=(10**N-1-10**(N-1))*a+10**(N-1)
    return(b)
n=int(input("Enter a Number: "))
z=rand_digit(n)
print(z)