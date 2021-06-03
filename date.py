n=int(input("Enter the date as 'MMDDYYYY': "))
d={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
a=str(n//1000000)
for i in list(d.keys()):
    if i==a:
        print(d[i],(n//10000)%100,n%10000)
    else:
        continue
