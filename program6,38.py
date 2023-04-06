#write a python program that inputs a number for table and lenght of the 
#table and display the table using for loop.

table = int(input("please enter a number for table: "))
lenght = int(input("please enter the length of the table: "))

for i in range(1,lenght+1):
    print(table," x ",i," = ",table*i)
