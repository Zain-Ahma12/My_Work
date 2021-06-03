n=int(input("Enter the number of lines:"))
if n%2==0:
    for i in range(n):
        if i<n//2:
            print(" "*(n//2),"*"*(n//2))
        else:
            print("*"*(n//2)," "*(n//2))
else:
    print("even number required....")