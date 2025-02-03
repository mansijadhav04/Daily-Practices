#number of rows
n=5
for i in range(1, n + 1):
    #creating spaces
    spaces = " " * (n - i)
    #creating stars
    stars = "*" * i
    print(spaces + stars)
    
