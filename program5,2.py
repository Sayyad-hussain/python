#write a python program that repeatedely inputs a number from the user and 
#print its square.The loop terminates if the user enters 0 and the program 
#prints "GoodBye"
import math
n = int(input("please enter a number: "))

while n != 0:
    print("Square of the number: ", n*n)
    n = int(input("please enter a number: "))

print("GoodBYE")