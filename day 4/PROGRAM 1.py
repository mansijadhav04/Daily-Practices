# define the div() function
def div(a,b):

# check for division by zero
    if b != 0:
        result = a / b
        print(f"the division of {a} by {b} is : {result}")
    else:
        print("error: division by zero is not allowed")

# call the function with two numbers
div(10,27)
div(14,16)
        
    
