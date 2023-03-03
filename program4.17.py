#write a python program that reads the coefficient a ,b ,c of the quadratic 
#equation ax^2 + bx + c = 0 and print the real solution of x using the 
#formula:
 
#Quadratic equation formula <--------

#Note that if b^2 - 4ac = 0 then there is only one real solution. if it is 
#greater then there are two real solution and if it less then zero then 
#print the message "No real solution"

import math

a = int(input("please enter (a) in quadratic equation: "))
b = int(input("please enter (b) in quadratic equation: "))
c = int(input("please enter (c) in quadratic equation: "))

value = int(b*b - 4*a*c)

if value > 0:
    x1 = (-b + math.sqrt(value)) / (2 * a)
    x2 = (-b - math.sqrt(value)) / (2 * a)
    print("Two real solution....")
    print("X1: ",x1)
    print("X2: ",x2)
elif value == 0 :
    x1 = (-b + math.sqrt(value) /(2 * a))
    print("one real solution....")
    print("X: ",x1)
else:
    print("No real solution")

    
    

