#write a python program that inputs salary and grade.it adds 50% 
#bonus if the the grade is greater than 15.it adds bonus if the
#grade is 15 or less and then display the total salary 

salary = int(input("please enter your salary: "))
grade = int(input("please enter your grade: "))

if grade > 15:
    bonus = salary * 50/100
else: 
    bonus = salary * 25/100

salary = salary + bonus

print("Your Net salary: ",salary)
