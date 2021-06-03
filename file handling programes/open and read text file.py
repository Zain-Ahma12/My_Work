'''
date            15-05-21
programme to print total number of lines in a file
'''

f=open("A Posion Apple.txt",'r')
#  READING FILE
for data in f:                               
    print(data,end="")

f.seek(0)
contant=f.readlines()
s=len(contant)
for i in contant:
    if i=="\n":
        s-=1
print("\nTotal Number of lines in file: ",s)
f.close()
