#write a program that inputs a number from a user and display the factorial 
#of that number using for loop .

n = int(input("please enter a number: "))
fac=1
for i in range(1,n+1):
    fac = fac * i
    i=i+1

print("Factorial of a number :",fac)

