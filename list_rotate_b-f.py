'''
date            14-05-2021
programme to print list as shown:
  input                         output
[1,2,3,4,5]                   [5,1,2,3,4]
'''


l=eval(input("Enter a list:\n "))
if l==[]:
    print("Enter some elements in list...")
else:
    m=[l[len(l)-1]]
    for i in range(len(l)-1):
        m.append(l[i])
    print(m)

