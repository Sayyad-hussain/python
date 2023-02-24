#write a python program that inputs two numbers ,swaps values and then 
#display them.

x = input("please enter first number: ")

y = input("please enter second number: ")

print("You input the number as ",x,"and ",y)

temp = x

x = y

y = temp

print("********After swaping******")
print("The numbers are  ",x,"and ",y)
