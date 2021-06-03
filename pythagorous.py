'''
3*3 + 4*4 = 25

'''
def binary_search(arr,x):
    beg=0
    end=len(arr)-1
    while beg<=end:
        mid=(beg+end)//2
        if x>arr[mid]:
            beg=mid+1
        elif x<arr[mid]:
            end=mid-1
        else:
            return mid
    return -1

arr=eval(input('Enter the list of numbers:\n')
x=int(input("Enter the number you want to find:"))
result=binary_search(arr,x)
if result==-1:
    print('Element is not in list')
else:
    print(f"Element is at index {result}")
