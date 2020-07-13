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

def print_board(bo):
	for i in range(9):
		for j in range(9):
			print(bo[i][j],end = " ")
		print()

def findEmpty(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return (i,j) #x=rows y= cols; i,j = x,y
	return None

def possible(number,x,y,board):
	#To check in columns
	for i in range(9):
		if(number == board[i][y] and i!= x):
			return False
	#to check in rows	
	for i in range(9):
		if(number == board[x][i] and i!= y):
			return False
	
	#to check in squares
	square_y = x//3
	square_x = y//3
	for i in range(square_y*3,square_y*3+3):
		for j in range(square_x*3,square_x*3+3):
			if(number == board[i][j] and (i,j)!=(y,x)):
				return False
	return True

def solve(bo):
	find = findEmpty(bo)
	if not find:
		return True
	else:
		x,y = find 
	for i in range(1,10):
		if possible(i,x,y,bo):
			bo[x][y] = i
			if solve(bo):
				return True
			bo[x][y] = 0
	return False

if __name__ == '__main__':
	solve(board)
	print_board(board)