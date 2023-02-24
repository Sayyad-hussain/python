#write a python program that inputs time in seconds and converts it into
#hh-mm-ss formats.

seconds = int(input("please enter time in seconds: "))

hours = int(seconds/3600)
seconds = int(seconds % 3600)
minutes = int(seconds/60)
seconds = int(seconds % 60)



print("HH-MM-SS: ",hours,":",minutes,":",seconds)
