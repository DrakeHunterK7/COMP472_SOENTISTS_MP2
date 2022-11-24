import Board as bd
from AStar import AStar
import pickle

directory = "SampleInputOutput/Sample/"

file = open(directory + "sample-input.txt", 'r')

boards = []

# Identifying the lines in the output
for line in file.readlines():
    if line[0] != '#' and line.strip() != "":
        board = bd.Board(line)
        boards.append(board)


astar_solver = AStar(boards[1])
astar_solver.search_solution(1)

# board = boards[0]
# board.printBoardInfo()
# print("\n")
# board.moveCar(["M", 2, "down"])
# board.printBoardInfo()
# print("Has Won? ", board.isWinningState())
# print("\n")
#
# board.moveCar(["A", 1, "right"])
# board.printBoardInfo()
# print("Has Won? ", board.isWinningState())
# print("\n")
