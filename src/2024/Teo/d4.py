# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() # puts the file into an array
    fileObj.close()
    return words


def printBoard(board):
    for row in board:
        print(row)

def find_XMAS(board):
    found = []
    # rows: forward and backwards
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j+3 >= len(board[0]):
                continue
            if board[i][j] == "X" and board[i][j+1] == "M" and board[i][j+2] == "A" and board[i][j+3] == "S":
                found.append((i, j))
            if board[i][j] == "S" and board[i][j+1] == "A" and board[i][j+2] == "M" and board[i][j+3] == "X":
                found.append((i, j))
    

    # columns: forward and backwards
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+3 >= len(board):
                continue
            if board[i][j] == "X" and board[i+1][j] == "M" and board[i+2][j] == "A" and board[i+3][j] == "S":
                found.append((i, j))
            if board[i][j] == "S" and board[i+1][j] == "A" and board[i+2][j] == "M" and board[i+3][j] == "X":
                found.append((i, j))

    
    # diagonals: forward and backwards
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+3 >= len(board) or j+3 >= len(board[0]):
                continue
            # NW to SE
            if board[i][j] == "X" and board[i+1][j+1] == "M" and board[i+2][j+2] == "A" and board[i+3][j+3] == "S":
                found.append((i, j))
            if board[i][j] == "S" and board[i+1][j+1] == "A" and board[i+2][j+2] == "M" and board[i+3][j+3] == "X":
                found.append((i, j))

    # other diagonal: forward and backwards
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+3 >= len(board) or j-3 < 0:
                continue
            # NE to SW
            if board[i][j] == "X" and board[i+1][j-1] == "M" and board[i+2][j-2] == "A" and board[i+3][j-3] == "S":
                found.append((i, j))
            if board[i][j] == "S" and board[i+1][j-1] == "A" and board[i+2][j-2] == "M" and board[i+3][j-3] == "X":
                found.append((i, j))

    return len(found)

def find_X_MAS(board):
    # find the pattern
    # M.S
    # .A.
    # M.S

    found = []

    # M's on top
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if i + 2 >= len(board) or j + 2 >= len(board[0]):
                continue

            # print("---", "(", i, ",", j, ")", "---")
            # print(board[i][j], ".", board[i+2][j])
            # print(".", board[i+1][j+1], ".")
            # print(board[i][j+2], ".", board[i+2][j+2])

            # M.S
            # .A.
            # M.S
            if board[i][j] == "M" and board[i][j+2] == "S" and board[i+1][j+1] == "A" and board[i+2][j] == "M" and board[i+2][j+2] == "S":
                found.append((i, j))

            # S.M
            # .A.
            # S.M
            if board[i][j] == "S" and board[i][j+2] == "M" and board[i+1][j+1] == "A" and board[i+2][j] == "S" and board[i+2][j+2] == "M":
                found.append((i, j))

            # M.M
            # .A.
            # S.S
            if board[i][j] == "M" and board[i][j+2] == "M" and board[i+1][j+1] == "A" and board[i+2][j] == "S" and board[i+2][j+2] == "S":
                found.append((i, j))

            # S.S
            # .A.
            # M.M
            if board[i][j] == "S" and board[i][j+2] == "S" and board[i+1][j+1] == "A" and board[i+2][j] == "M" and board[i+2][j+2] == "M":
                found.append((i, j))

    return len(found)




def pt1(arr):
    board = []
    for line in arr:
        l = []
        for char in line:
            l.append(char)

        board.append(l)

    # printBoard(board)
    return find_XMAS(board)


def pt2(arr):
    board = []
    for line in arr:
        l = []
        for char in line:
            l.append(char)

        board.append(l)

    # printBoard(board)
    return find_X_MAS(board)

arr = readFile("AoC_Inputs/AoC_2024_d4_input.txt")
print("Part 1", pt1(arr))
# 2297
print("Part 2", pt2(arr))
# 1745
