#--------------------------------ASSIGNMENT-01-----------------------
#WRITE A PYTHON PROGRAM TO GET THE FIBONACCI SERIES NETWEEN 0-50
#0,1,1,2,3,5,8,13,21
#Q. every next number is found by adding up the two number before it.
# expected output= 1,1,2,3,5,8,13,21,34.
#----------------------------------------------------------------------------
                  #coding answer#

a=0   #initialize a=0
b=1   #b=1
s=0   # it will print s storing value
while (s<50):
    print(s,end=" ")
    s = a+b
    b = a  #swapping
    a = s  



