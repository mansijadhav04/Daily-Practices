#number of rows
n = 5
#loop for each row
for i in range(n):
    spaces = " " * i
    pattern = ""

    #decreasing numberfor each chracater in each row
    for j in range(n - i):

        #altering 1 and 0
         pattern += str((j+i) % 2)
         
    print(spaces + pattern)
    
   
