n = int(input(""))
t = int(input(""))
yard = [[0 for col in range(n)] for row in range(n)]
#yard = [[0]*n]*n
trees = []
largest_m = 0

for i in range(t):
    location_in = input("").split(' ')
    loc_x = int(location_in[0]) - 1
    loc_y = int(location_in[1]) - 1 
    trees.append([loc_x, loc_y])
    yard[loc_x][loc_y] = 1

def exterior(start_row, start_col, size):
    global yard
    qualified = True 
    for i in range(size):
        if start_col + size - 1 > n-1 or start_row + size - 1 > n-1:
            qualified = False
            break 
        if yard[start_row + i][start_col + size - 1] == 1:
            qualified = False 
            break
        if yard[start_row + size - 1][start_col + i] == 1:
            qualified = False 
            break
    if qualified:
        return exterior(start_row, start_col, size + 1)
    else:
        return size - 1

for row in range(n):
    for col in range(n):
        if yard[row][col] == 1:
            continue
        else:
            largest_cur = exterior(row, col, 2)
            if largest_m < largest_cur:
                largest_m = largest_cur


print(largest_m)