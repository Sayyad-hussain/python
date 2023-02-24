#write a python program that inputs the distance traveled and the speed of 
#vehile.it calculates the time required to reach the destination and 
#display it

distance = int(input("please enter distance: "))

speed = int(input("please enter speed: "))

time = distance  / speed

print("Time required to reach destination: ", time)