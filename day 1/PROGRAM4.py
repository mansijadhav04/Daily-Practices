#Take the sides of the tringle
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

#Calculate the semi-perimeter
side = (a + b + c) / 2

#Calculate the area of the tringle
area = (side * (side - a) * (side - b) * (side - c)) ** 0.5

#Print the result
print("The area of the triangle is:", area)
