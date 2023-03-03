#Sameer works in a firm as a programmer and is getting a monthly pay.
#write a program to take his basic pay as input and through the keyboard 
#and calculate his net pay.His net pay is to be calcualted as given below 

#net pay = basic pay + house rent

#sameer gets his house rent based on his basic pay according to the scheme 
#given below
    #Basic pay                              $House rent   
#basic pay < 30000                          #30% of basic pay
#basic pay >=  30000 and <= 50000           #35% of basic pay
#basic pay > 50000                          #40% of basic pay

pay = int(input("please enter sameer salary: "))

if pay < 30000:
    rent = 30/100 * pay
    netpay = pay + rent
    print("Net pay =",netpay)
elif pay >= 30000 and pay <= 50000:
    rent = 35/100 * pay
    netpay = pay + rent
    print("Net pay =",netpay)
elif pay > 50000:
    rent = 40/100 * pay
    netpay = pay + rent
    print("Net pay =",netpay)
else :
    print("Invalid entry.")