#write a python program that finds the sum of the square of the integers 
#from 1 to n .where n is a positive value entered by the user 
#(i.e. 1^2+2^2+3^2.....)

n = int(input("please enter a number: "))
sum = 0
for i in range(1,n+1):
    j = i*i
    sum = sum +  j

print("Sum: ",sum)

