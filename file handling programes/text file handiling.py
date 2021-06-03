'''
DATE      17-05-21
'''

myfile=open('A Posion Apple.txt','r')      #<file handle>=my file
str1=' '
size=0
tsize=0                                    # total size of file
vcount=ccount=0                            # vcount store vowel and ccount store consonants
while str1 :
    str1=myfile.readline()
    tsize+=len(str1)
    size+=len(str1.strip())
print("Size of file after removing all EOL character and blank line:",size)
print("The Size of the file:",tsize)
myfile.close()

ch=" "
myfile=open('A Posion Apple.txt','r')      #<file handle>=my file)
while ch :
    ch=myfile.read(1)
    if ch in 'aAeEiIoOuU':
        vcount+=1
    else:
        ccount+=1
print("Vowels in the file:",vcount)
print("Consonants in the file:",ccount)