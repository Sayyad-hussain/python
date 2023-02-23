#write a python that reads four integers and print their sum, product 
#and average



a = int(input("please enter first integer: "))
b = int(input("please enter second integer: "))
c = int(input("please enter third integer: "))
d = int(input("please enter fourth integer: "))
sum = int(a+b+c+d)

product = int(a*b*c*d)
average = float(sum/4)
print("Sum: ", sum)
print("Product: ", product)
print("Average: ", average)

