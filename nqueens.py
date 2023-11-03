def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
            
    # Check this row on right side
    for i in range(col,N):
        if board[row][i]==1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on right side
    for i, j in zip(range(row, N),
                    range(col, N)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    # Check Upper diagonal on right side
    for i, j in zip(range(row, -1, -1), 
                    range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True
 
 
def solveNQUtilapproach1(board, col):
 
    if col >= N:
        return True
    
    if col==first_queen_col:
        return solveNQUtilapproach1(board, col + 1)
    
    for i in range(N):
            
        if i!=first_queen_row and isSafe(board, i, col):
            board[i][col] = 1
 
            if solveNQUtilapproach1(board, col + 1) == True:
                return True

            board[i][col] = 0
 
    return False
 


def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
    print("----------------------------------------------------------------")

def solveNQUtilapproach2(board, col):
    if (col >= N):
        return True
    
    if col==first_queen_col:
        return solveNQUtilapproach2(board, col + 1)
        
    for i in range(N):
        
        if (i!=first_queen_row and (ld[i - col + N - 1] != 1 and
            rd[i + col] != 1) and cl[i] != 1):

            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if (solveNQUtilapproach2(board, col + 1)):
                return True
    
            board[i][col] = 0 
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

    return False
    
def solveNQ(N):
    board1=[[0 for x in range(N)] for x in range(N)]
    
         # Place the first queen at (0, 0)
    board1[first_queen_row][first_queen_col] = 1 #and then pass solveNQUtilapproach1(board1, first_queen_col+1)
    board2=board1.copy()
    
    solveNQUtilapproach1(board1, 0)
    print("Approach 1:")
    printSolution(board1)
    
    ld[first_queen_row-first_queen_col+N-1]=rd[first_queen_row+first_queen_col]=cl[first_queen_row]=1
    solveNQUtilapproach2(board2,0)
    print("Approach 2:")
    printSolution(board2)
   
if __name__=="__main__":
    # N=8
    # first_queen_col = 4
    # first_queen_row = 6
    N = int(input("Enter N:"))
    first_queen_col = int(input("Enter the col for the 1st queen to be placed:"))
    first_queen_row = int(input("Enter the row for the 1st queen to be placed:"))
    
    ld=[0]*N*2
    rd=[0]*N*2
    cl=[0]*N*2
    
    solveNQ(N)
