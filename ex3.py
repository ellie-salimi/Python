five_by_five_grid = [
['X','0','X','X','X'],
['X','X','0','0','0'],
['X','0','X','0','X'],
['0','X','X','X','X'],
['X','0','0','X','X'],
]

#comment
counter = 0
for items in five_by_five_grid [counter]:
    a = 0
    b = 0
    if five_by_five_grid [counter] == 'X':
        a=a+1
    else:
        b=b+1
    if a
        
    counter = counter +1
    
#original for loop to print grid
for items in five_by_five_grid:
    print(items)

#input request from user
change = input("What row and column do we change?" )
#takes the user's string index 1 (row) and turns it into an interger
change_r = int(change[1])
#takes the user's string index 3 (column) and turns it into an integer
change_c = int(change[3])
#determines if it's 0 based on row index and column index
#then if so, make that row index and column index into X
if five_by_five_grid[(change_r - 1)][(change_c-1)] == '0':
    five_by_five_grid[(change_r - 1)][(change_c-1)] = ('X')
#if it's not 0, turn it into 0 at that row and column index
else:
    five_by_five_grid[(change_r - 1)][(change_c-1)] = ('0')

#print the new grid again
for items in five_by_five_grid:
    print(items)

