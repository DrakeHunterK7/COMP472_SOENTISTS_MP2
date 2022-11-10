import Board as bd

directory = "SampleInputOutput/Sample/"

file = open(directory + "sample-input.txt", 'r')

boards = []

# Identifying the lines in the output
for line in file.readlines():
    if line[0] != '#' and line.strip() != "":
        board = bd.Board(line)
        boards.append(board)

# Printing all the boards one by one
for board in boards:
    board.printBoardInfo()
    print()



