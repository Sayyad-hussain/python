#write a program thats input two numbers and finds whether both are 
#equal or differ
n1 = int(input("please enter first number: "))
n2 = int(input("please enter second number: "))

if n1==n2:
    print("Both number are equal.")
elif n1<n2:
    print("Both number are differ.")
elif n1>n2:
    print("Both number are differ")
else:
    print("invalid entry...")

    