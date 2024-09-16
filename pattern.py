'''for i in range(1,6):
    for j in range (1,i+1):
        print("*",end="")
    print()'''

'''for i in range(5,0,-1):
    for j in range (1,i+1):
        print("*",end="")
    print()'''

'''for i in range(4,0,-1):
    for j in range (1,i+1):
        print("+",end="")
    print()'''
#PATTERN 
'''row=int(input("row:"))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()'''
#NORMAL (1-5) PATTERN 
'''row=int(input("row:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''

# Step 1: Input the number of rows from the user
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Print a new line after each row


# TRIANGLE
'''row=int(input("row:"))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("* " ,end="")
    print()'''
    
#TRIANGLE INVERSE
'''row=int(input("row:"))
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("* " ,end="")
    print()'''

 #DIAMOND
'''row=int(input("row:"))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("* " ,end="")
    print()
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("* " ,end="")
    print()'''
