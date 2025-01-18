# Function to find the largest among three numbers
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = find_largest(num1, num2, num3)

# Output the result
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")
