#write a program that input three nunber and print the largest one.

a = int(input("please enter first number: "))
b = int(input("please enter second number: "))
c = int(input("please enter third number: "))

max=0

if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
elif c>a and c>b:
    max=c

print(max," is the largest integer.")