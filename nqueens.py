def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 
 
def solveNQUtilapproach1(board, col):
 
    if col >= N:
        return True
 
    for i in range(N):
 
        if isSafe(board, i, col):
            board[i][col] = 1
 
            if solveNQUtilapproach1(board, col + 1) == True:
                return True
            
            board[i][col] = 0
 
    return False
 


def printSolution(board):
	for i in range(N):
		for j in range(N):
		    #print(board[i][j], end=" ")
		    if board[i][j]==1:
		        print("Q",end=" ")
		    else:
		        print(".",end=" ")
		print()



def solveNQUtilapproach2(board, col):
	if (col >= N):
		return True

	for i in range(N):

		if ((ld[i - col + N - 1] != 1 and
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
	board2=board1
	
	if (solveNQUtilapproach1(board1, 0) == False): # TC:O(N!*N) SC:O(N)
		printf("Solution does not exist")
		return False
	print("Using approach 1: ")
	printSolution(board1)
    	
	if (solveNQUtilapproach2(board2, 0) == False): # TC:O(N!) SC:O(N)
		printf("Solution does not exist")
		return False
		
	print("\nUsing approach 2: ")
	printSolution(board2)	
	
	return True


if __name__ == '__main__':
    N=int(input("Enter n: "))
    ld = [0] * N * 2

    rd = [0] * N * 2
    
    cl = [0] * N * 2
    solveNQ(N)

   
