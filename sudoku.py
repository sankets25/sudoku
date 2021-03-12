'''Steps:
1. find the empty element coordinate
2. fill some element and move ahead
3. if there is some conflict, backtrack
4. repeat steps'''

#sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]  
]

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




# Function to print the sudoku to get the look and feel
def print_board(board):
    #separate lines by each 3 rows
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - ")
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

print(find_empty(board))