#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ramchennale
#
# Created:     24/07/2018
# Copyright:   (c) ramchennale 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#a,b=0,1
a=0
b=1
for i in range(0,10):
    print(a)
    #a,b = b,a+b  OR
    c=a+b
    a=b
    b=c



# In a, b = b, a + b, the expressions on the right hand side are evaluated before being assigned to the left hand side. So it is equivalent to:
#c = a + b
#a = b
#b = c
#In the second example, the value of a has already been changed by the time b = a + b is run. Hence, the result is different.


