#write a pythin progra that produce this pattern 
#1
#1 2
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 

a = 5

for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# for i in range(0, 5):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()
        
    