l1=eval(input("Enter first listL: "))
l2=eval(input("Enter second listL: "))
l3=[]
if len(l1)==len(l2):
    for i in range(len(l2)):
        a=l1[i]+l2[i]
        l3.append(a)
    print(l3)
else:
    print("Enter lists of equal length")
