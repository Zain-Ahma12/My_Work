#program to print sum of the number in given string
#input is string "jsjadhjkh8679898"
#output is 55



a=str(input('Enter the string:'))
c=d=0
b='0123456789'
for i in range(len(a)):
    if a[i] in b:
        c+=int(a[i])
        d+=1
    else:
        continue
print('Total numbers in the string :',d)
print('Their sum :',c)


