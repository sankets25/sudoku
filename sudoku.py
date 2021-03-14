'''Steps:
1. find the empty element coordinate
2. fill some element and move ahead
3. if there is some conflict, backtrack
4. repeat steps'''

#sudoku board list
board = [
    [4,0,0,0,0,0,0,6,9],
    [0,0,3,2,0,0,0,8,1],
    [0,0,0,6,0,0,4,0,0],
    [1,5,7,0,0,0,6,9,0],
    [0,0,0,0,7,0,8,0,2],
    [2,0,4,0,1,6,0,0,0],
    [5,0,0,0,0,3,7,2,8],
    [6,0,2,8,9,4,0,3,0],
    [8,3,1,5,2,0,0,4,0] 
]

#solver function with backtrack algorithm.
def solve(board):
    #empty spaces in board.
    #if found is None then board is completely filled
    found = find_empty(board)
    if not found:
        return True
    else:
        row, col = found

    #check each values from 1-9 for valid number
    for i in range(1,10):
        #if the value is valid then add it into the board
        if valid(board, i, (row,col)):
            board[row][col] = i

            #if board solved then return True otherwise make the vlaue to 0
            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False


#check if board is valid 
def valid(board, num, pos):
    # checking the row by traversing from start to the end
    for i in range(len(board[0])):
        #check if the row has the number which we are inserting and ignore the position column where we are inserting value
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # checking the column by traversing from start to the end
    for i in range(len(board)):
        #check if the column has the number which we are inserting and ignore the position column where we are inserting value
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #checking each box if the given number is valid or not
    # considering the values for x and y coordinate
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #loop through the box as box_x gives values from 0 -2 we are 
    # multiplying coordinate values with 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            #check if value exists then return false
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True
    

# Function to print the sudoku to get the look and feel
def print_board(board):
    #separate lines by each 3 rows
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        #separate line for column division
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")
            #print values when board column is 8
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#find out the empty values in the board to perform actions
def find_empty(board):
    #traverse through the board to find the empty fields
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Return position of element where we have empty value
            if board[i][j] == 0:
                return i,j
    return None

# print(find_empty(board))
print("*************** Input board ************************")
print_board(board)
solve(board)
print("*************** Output board ***********************")
print_board(board)


