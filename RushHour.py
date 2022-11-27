import Board as bd
from AStar import AStar
import pickle

directory = "SampleInputOutput/Sample/"
output_directory = "Output/"

file = open(directory + "sample-input.txt", 'r')

boards = []

# Identifying the lines in the output
for line in file.readlines():
    if line[0] != '#' and line.strip() != "":
        board = bd.Board(line)
        boards.append(board)


for index, board in enumerate(boards):
   for h in range(1):

    solution_file = open(output_directory+"a-h" + str(h+1) + "-sol-" + str(index+1), 'w')
    search_file = open(output_directory + "a-h" + str(h+1) + "-search-" + str(index+1), 'w')

    astar_solver = AStar(board)
    astar_solver.search_solution(h + 1)

    if astar_solver.solutionFound:

        solution_file.write("--------------------------------------------------------------------------------\n\n")
        solution_file.write("Initial Configuration: \n\n")
        solution_file.write(board.returnBoardInfo())
        solution_file.write(board.printCarFuel() + "\n")

        solution_file.write("Runtime: " + str(astar_solver.runtime) + " seconds\n")
        solution_file.write("Search Path Length: " + str(len(astar_solver.searchPath)) + " states\n")
        solution_file.write("Solution Path Length: " + str(len(astar_solver.solutionPath) - 1) + " moves\n")
        solution_file.write("Solution Path: " + astar_solver.get_solution_moves() + "\n\n")
        solution_file.write(astar_solver.get_board_line() + "\n\n")

        solution_file.write("Final Configuration: \n\n")

        solution_file.write(astar_solver.solutionPath[0].board.returnBoardInfo())
    else:
        solution_file.write("No solution found!")

    search_file.write(astar_solver.get_search_path())
    search_file.close()


    solution_file.close()