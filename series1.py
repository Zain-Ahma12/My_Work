'''
function which takes first and last values of the series and then generates
four terms that are equidistant
e.g.
    input                              output
first  term:1                          1,3,5,7
second term:7
'''

def ser_fun(First_term,Last_term):
    d=(Last_term-First_term)/3
    return(First_term,First_term+d,First_term+2*d,Last_term)
n1=int(input("Enter First term: "))
n2=int(input("Enter Last term: "))
a,b,c,d=ser_fun(n1,n2)
print(a,b,c,d,sep=' , ')