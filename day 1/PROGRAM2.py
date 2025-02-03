#Take the input from the user
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

# Use a ternary operator to find the largest 
Number=num1 if num1>num2 else num2

#Print the result
print("The Largest Number is: ",Number)
