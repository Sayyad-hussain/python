#write a program that reads two numbers and prints the sum and product of the numbers 
#.if the first number is positive

a= int(input("please enter first number: "))
b = int(input("please enter second number: "))
if a>0:
 sum = a+b
 print("Sum: ",sum)
 product = a*b
 print("product: ", product)
else:
 print("first number is not positive")
