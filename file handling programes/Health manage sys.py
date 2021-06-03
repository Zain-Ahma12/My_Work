'''

'''
def getdate():
    import datetime as d
    return d.datetime.now()

t=getdate()

def log(file1,file2):
    if m in "Ee":
        f=open(file1,"a")
        a=input("Enter the name of Exercise\n")
        f.write(str(t)+" "+a)
        f.close()
    else:
        f=open(file2,"a")
        a=input("Enter the name of Food\n")
        f.write(str(t)+" "+a)
        f.close()

def retrive(file1,file2):
    if m in "Ee":
        try:
            f=open("file1")
            for i in f:
                print(i)
        except EOFError:
            print("First write you shudle...")
        f.close()
    else:
        try:
            f=open("file2")
            for i in f:
                print(i)
        except EOFError:
            print("First write you shudle...")                
        f.close()


print("Welcome to our 'Health Management App'")
print("Do you want to LOG your routine or RETRIVE your previous routine.")
dec=input("Press L to log \nPress R to retrive \n")
print("Clients enroll: \n1) Rhona \n2) Harry \n3) Hammad")
ch=int(input("Press '1' for Rohan \nPress '2' for Harry \nPress '3' for Hammad\n"))
m=input("Press 'E' for Exercise \nPress 'F' for Food\n")

if dec=='L':
    if ch==1:
        log(Rhoan_exercise.txt,Rhoan_food.txt)
    elif ch==2:
        log(Harry_exercise.txt,Harry_food.txt)
    elif ch==3:
        log(Hammed_exercise.txt,Hammad_food.txt)
    else:
        print("Wrong input......")
else:
    if ch==1:
        retrive(Rhoan_exercise.txt,Rhoan_food.txt)
    if ch==2:
        retrive(Harry_exercise.txt,Harry_food.txt)
    if ch==3:
        retrive(Hammed_exercise.txt,Hammad_food.txt)    
    else:
        print("Wrong input......")