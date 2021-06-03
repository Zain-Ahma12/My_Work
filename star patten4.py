n=int(input("Enter the number of lines:"))
for i in range(n+1):
    print(" "*(n-i)," *"*i,sep='')
for j in range(n):
    print(" "*(j)," *"*(n-j),sep='')