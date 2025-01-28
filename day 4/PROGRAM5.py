# Define the lambda function
# nested conditional (ternary operatrs)
check_number = lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero'

# test the lambda function with two different numbers
#output: negative
print(check_number(-10))

#output: zero
print(check_number(0))

#output: positive
print(check_number(10))
