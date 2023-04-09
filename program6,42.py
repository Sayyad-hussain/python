#write a progran that display the sum of the following series :
#1+3+5+7+......100

series = 100
sum_no = 0
for i in range(1, series+1, 2):
    sum_no = sum_no + i
    
print(sum_no)