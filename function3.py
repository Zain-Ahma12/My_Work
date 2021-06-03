'''
date                15-05-2021
function that take a list and swap adjacent value
'''



def Swap_Adjacent(L):
    for i in range(0,len(L)-1,2):
        L[i],L[i+1]=L[i+1],L[i]
    return(L)
a=eval(input("Enter a list of numbers:\n "))
z=Swap_Adjacent(a)
print(z)
