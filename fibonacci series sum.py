'''
programme for fibonacci series
1,1,2,3,5,8,13,...,n terms
'''
n=int(input('Enter the number of terms:'))
a=s=0
b=1
print('FIBONACCI SERIES :')
print(b,end=' , ')
for i in range(1,n):
    c=a+b
    a,b=b,c
    s+=c
    print(c,end=' , ')
print()    
print(f'The sum of first {n} terms of  Fibonacci series = {s+1}')    
