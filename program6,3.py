#write a python program that input a number from the user and display 
#a table of that number using for loop

number = int(input("please enter a number for table: "))

for i in range(1,10):
    print(number, " x ", i , " = ", number * i)

