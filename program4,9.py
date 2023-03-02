#write a program that inputs marks and print grade based on the obtained marks according to give Scheme:
#Marks           #Grade
#>=80 <=100        A
#>=70 <=79        B
#>=60 <=69       C
#>=50 <=59       D

marks = int(input("please enter your marks: "))

if marks >=80 and marks <=100 :
    print("A Grade")
elif marks >=70 and marks <=79 :
    print("B Grade")
elif marks >=60 and marks <=69 :
    print("C Grade")
elif marks >=50 and marks <=59 :
    print("D Grade")
elif marks >= 0 and marks <=49:
    print("F Grade")
else:
    print("...Invalid Input...")