#write a python program that inputs a three-digit number from the user and dispaly
#it in reverse order.
#for example if the user enter 123. it display 321...

number = int(input("please enter three digit number(e.g 123): "))

a = int(number / 100)
number =int(number % 100)
b = int(number / 10)
number = int(number % 10)

print("Number in reverse order: ",number,b,a)


