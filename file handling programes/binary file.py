import pickle as p
f=open("Binary_test1.dat","wb")                #file handle
n=int(input("Enter the total number records you want to store: "))
d={}
for i in range(n):                            #range function
    d["Name"]=input("Enter student name: ")
    d["Class"]=int(input("Enter student class: "))
    d["Roll number"]=int(input("Enter roll number of student: "))
    d["Marks of student"]=int(input("Enter marks of student: "))
    p.dump(d,f)                               #  write in binary file  dump(data,file handle)
f.close()

f=open("Binary_test1.dat","rb") 
e={}
try: 
    while True:
        e=p.load(f)
        print(e)
except EOFError:
    f.close()
