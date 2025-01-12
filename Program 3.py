#Accepting Inputs from users

principal = float(input("Enter the principal amount (Rs.): "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (in years): "))

# Calculate Simple Interest

simple_interest = (principal * rate * time) / 100

print("The Simple Interest is:",simple_interest)
