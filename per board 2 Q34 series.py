n=int(input("Enter the number of terms:"))
s=a=0
for i in range(1,n+1):
    if i%5==4 or i%5==0:
       a+=1 
    else:
        continue
for j in range(1,(n+a+1)):
    if j%5==4 or j%5==0:
        continue
    else:
        s+=j
        print(j,end=',')
print()
print("Sum of the series =",s)
print(i,j,sep='  ')
