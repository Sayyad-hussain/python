#write a python program that reads a numebr and print its square if the
# number is greater than 10 otherwise prints its cube.

number = int(input("please enter a number: "))

if number > 10 :
    print("Number is greater then 10 so square of this number: ",number*number)
else:
    print("Cube of the number: ",number*number*number)
