'''
date            14-05-2021
programme to print list as shown:
  input                         output
[1,2,3,4,5]                   [2,3,4,5,1]
'''


l=eval(input("Enter a list:\n "))
if l==[]:
    print("Enter some elements in list...")
else:
    m=[]
    for i in range(1,len(l)):
        m.append(l[i])
    m.append(l[0])
    print(m)
