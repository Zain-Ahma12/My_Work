n=int(input('Enter the number of lines:'))
for i in range(n+1):
    print(" "*(n-i)," *"*i,sep='')
