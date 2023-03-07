#write a program that display alphabets form A to Z using for loop.
j = chr

print("The Alphabets from A to Z are: ");

for i in range(ord('A'), ord('Z') + 1 ):
    print(chr(i), end=" ");
print("\nThe Alphabets from a to z are: ");
for i in range(ord('a'), ord('z') + 1 ):
    print(chr(i), end=" ");
		
