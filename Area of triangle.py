import math as m                                  # date            14-05-2021
def AOT(side,height):
    a=(side*height)/2
    return(a)

def AOET(side):
    a=(m.sqrt(3)/4)*(side**2)
    return(a)

side=float(input("Enter the side length of Triangle:"))
height=float(input("Enter the height of Triangle:"))
x=AOT(side,height)
y=AOET(side)
print(f"Area of the Triangle = {x} sq units")
print(f'Area of Equilateral triangle of side {side} = {y} sq units')