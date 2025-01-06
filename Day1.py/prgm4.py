a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

side = (a + b + c) / 2

area = (side * (side - a) * (side - b) * (side - c)) ** 0.5

print("The area of the triangle is:", area)