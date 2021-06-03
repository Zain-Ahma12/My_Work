"""
Function to convert Doller to Rupee
"""
def D_R(Dollar):
    return(73.25*Dollar)
n=float(input("Enter the Amount in DOLLAR:"))   
r=D_R(n) 
print(f'Amount in RUPEE is {r}')


