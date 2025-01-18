# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Input from the user
number = float(input("Enter a number: "))

# Check the number and display the result
result = check_number(number)
print(f"The number {number} is {result}.")
