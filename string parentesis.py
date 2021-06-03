n=str(input("Enter the string of parenthetic:"))
s=0
x=['[]','{}','()','<>']

for i in range(int(len(n)/2)) :
    if n[i]+n[len(n)-i-1] in x:
        s+=1
    else:
        continue

if s==int(len(n)/2):
    print(1)
else:
    print(0)