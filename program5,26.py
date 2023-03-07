#write a python program that inputs an integer from the user and print 
#its  table upto 20

n = int(input("please enter a number for table: "))
i = 1
while i <= 20:
    print(n," * ",i," = ", i* n)
    i=i+1

