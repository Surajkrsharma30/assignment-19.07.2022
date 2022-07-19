#--------------------------------ASSIGNMENT-01-----------------------
#write a programme that accepts a word from the user and reverse it.
#sample test case
#input:Edyoda
#output:adoydE
#----------------------------------------------------------------------------
                  #coding answer#


s=(input("enter the string which have to reversed:"))
output = ' '
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
print("string reversed")


