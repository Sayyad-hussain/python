#write a program that reads two numbers and prints the sum and product of the numbers 
#.if the first number is positive

x = int(input("please enter first number: "))
y = int(input("please enter second number: "))

if x>0:
 sum = x+y
 print("Sum: ",sum)
 product = x*y
 print("product: ", product)
else:
 print("first number is not positive")
