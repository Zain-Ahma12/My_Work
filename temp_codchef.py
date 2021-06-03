l='abcdefghijklmnop'
for t in range(int(input())):
    n=int(input())
    a=input()
    g=[0,1,2,3]
    s=0
    for i in range(1,len(a)+1):
        if i%4==1:
            s+=int(a[i-1])*2**(3)
        elif i%4==2:
            s+=int(a[i-1])*2**(2)
        elif i%4==3:
            s+=int(a[i-1])*2**(1)
        elif i%4==0:
            s+=int(a[i-1])
            print(s)
            print(l[s])
            s=0
