#Implementation of stack as a List
stack=[]
choice='y'
while choice=='y':
    print("1:Push")
    print("2:Pop")
    print("3: Display Element of the stack")
    c=int(input("Enter your choice:"))
    if c==1:
        a=int(input("Enter the Element which you want to Push: "))
        stack.append(a)
    elif c==2:
        if stack==[]:
            print("Stack empty...underflow case...cannot delete an element")
        else:
            print("Deleted item is: ",stack.pop())
    elif c==3:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        print("Wrong input...")
    choice=input("Do you want to continue? (y/n): ")
    