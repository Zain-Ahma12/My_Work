'''
date            10-05-2021
Programme that calculate the difference between a number and the number made after its digits interchange 
'''

import math as m
import statistics as st
a=int(input("Enter a number"))
l=[]
for i in range(10,a+1):
    b=str(i)
    c=b[::-1]
    d=m.fabs(int(c)-i)
    l.append(d)

    print(f'The difference of {int(c)} and {i} = {(d)}')
print(f'The max difference = {max(l)}')
print("The mean of the differences = ",st.mean(l))
print("The mode of the differences = ",st.mode(l))
print("The median of the differences = ",st.median(l))