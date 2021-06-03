n=int(input("Enter the number of lines:"))
if n%2==0:
    for i in range(n//2):
        print("*"*(n//2-i)," "*2*i,"*"*(n//2-i),sep="")
    for i in range(n//2+1,n+1):
        print("*"*(i-n//2)," "*2*(n-i),"*"*(i-n//2),sep="")
else:
    print("an even number required....")