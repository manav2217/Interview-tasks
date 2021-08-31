'''simple triangle'''

# row = int(input("Enter the Rows"))
# for num in range(0,row+1):  # loop for print sequence wise number like 1 2 3...
#     for j in range(num): # print number as number of row like 1st row have 1  , 2nd have 22 , 3rd have 333 ...
#         print(num , end="")
#     print() 
    
'''inverted tiangle'''

row = int(input("Enter the Rows"))
num = 0
for i in range(row , 0 , -1):   # reverce index for the inverted
    num +=  1  #increment num for print numbers
    for j in range(1,i+1): #print numbers as the row 
        print(num , end="")
    print('\r')
    
'''for star'''

for i in range(row+1):
    print(i*"*")