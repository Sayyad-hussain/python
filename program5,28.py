#write a program that display sum of the series using while loop

# 1+1/2+1/4+1/6+1/8+.........+1/100

i = 2
series = 1

while i<=100:
    series = series + 1/i
    i=i+2

print("Sum", series)

