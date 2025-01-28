import random

# generate 5 random numbers
numbers = [random.randint(1,50) for _ in range(8)]

# display the random numbers
print(f"random numbers: {numbers}")

# find the maximum and minimum
maximum = max(numbers)
minimum = min(numbers)

# display the result
print(f"the maximum number is {maximum}")
print(f"the minimum number is {minimum}")
