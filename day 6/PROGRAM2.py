#number of rows
n = 5
#loop for each row
for i in range(1, n + 1):

    #initialize empty string for the current row
    pattern = ""

    #loop for each chracater in the row
    for j in range(i):

        #altering 1 and 0
         pattern += str((j+1) % 2)
    print(pattern)
    
   
