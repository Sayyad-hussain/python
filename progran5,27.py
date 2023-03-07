#write a program that inputs a number from a user and print its factorial 

n = int(input("please enter a number for factorial "))
f=1
i=1
while i<=n:
    f=f*i
    i=i+1

print("factorial: ",f)

