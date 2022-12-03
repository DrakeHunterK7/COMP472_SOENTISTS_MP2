import AStar
import Board as bd
import Node
from AStar import AStar
from GBFS import GBFS
from UCS import UCS
import time
import sys
import collections



directory = "SampleInputOutput/Sample/"
output_directory = "Output/"

file = open(directory + "sample-input.txt", 'r')

boards = []

# Identifying the lines in the output
for line in file.readlines():
    if line[0] != '#' and line.strip() != "":
        board = bd.Board(line)
        boards.append(board)

start_time = time.time()

for index, board in enumerate(boards):
    # solution_file = open(output_directory + "ucs" + "-sol-" + str(index + 1), 'w')
    # search_file = open(output_directory + "ucs" + "-search-" + str(index + 1), 'w')
    #
    # ucs_solver = UCS(board)
    # ucs_solver.search_solution()
    #
    # if ucs_solver.solutionFound:
    #     solution_file.write("--------------------------------------------------------------------------------\n\n")
    #     solution_file.write("Initial Configuration: \n\n")
    #     solution_file.write(board.returnBoardInfo())
    #     solution_file.write(board.printCarFuel() + "\n")
    #
    #     solution_file.write("Runtime: " + str(ucs_solver.runtime) + " seconds\n")
    #     solution_file.write("Search Path Length: " + str(len(ucs_solver.searchPath)) + " states\n")
    #     solution_file.write("Solution Path Length: " + str(len(ucs_solver.solutionPath) - 1) + " moves\n")
    #     solution_file.write("Solution Path: " + ucs_solver.get_solution_moves() + "\n\n")
    #     solution_file.write(ucs_solver.get_board_line() + "\n\n")
    #
    #     solution_file.write("Final Configuration: \n\n")
    #
    #     solution_file.write(ucs_solver.solutionPath[0].board.returnBoardInfo())
    #     solution_file.close()
    # else:
    #     solution_file.write("No solution found!")
    #
    # search_file.write(ucs_solver.get_search_path())
    # search_file.close()

    for h in range(4):
        # solution_file = open(output_directory+"a-h" + str(h+1) + "-sol-" + str(index+1), 'w')
        # search_file = open(output_directory + "a-h" + str(h+1) + "-search-" + str(index+1), 'w')
        #
        # astar_solver = AStar(board)
        # astar_solver.search_solution(h + 1)
        #
        # if astar_solver.solutionFound:
        #     solution_file.write("--------------------------------------------------------------------------------\n\n")
        #     solution_file.write("Initial Configuration: \n\n")
        #     solution_file.write(board.returnBoardInfo())
        #     solution_file.write(board.printCarFuel() + "\n")
        #
        #     solution_file.write("Runtime: " + str(astar_solver.runtime) + " seconds\n")
        #     solution_file.write("Search Path Length: " + str(len(astar_solver.searchPath)) + " states\n")
        #     solution_file.write("Solution Path Length: " + str(len(astar_solver.solutionPath) - 1) + " moves\n")
        #     solution_file.write("Solution Path: " + astar_solver.get_solution_moves() + "\n\n")
        #     solution_file.write(astar_solver.get_board_line() + "\n\n")
        #
        #     solution_file.write("Final Configuration: \n\n")
        #
        #     solution_file.write(astar_solver.solutionPath[0].board.returnBoardInfo())
        #     solution_file.close()
        # else:
        #     solution_file.write("No solution found!")
        #
        # search_file.write(astar_solver.get_search_path())
        # search_file.close()

        solution_file = open(output_directory + "gbfs-h" + str(h + 1) + "-sol-" + str(index + 1), 'w')
        search_file = open(output_directory + "gbfs-h" + str(h + 1) + "-search-" + str(index + 1), 'w')

        gbfs_solver = GBFS(board)
        gbfs_solver.search_solution(h+1)

        if gbfs_solver.solutionFound:
            solution_file.write("--------------------------------------------------------------------------------\n\n")
            solution_file.write("Initial Configuration: \n\n")
            solution_file.write(board.returnBoardInfo())
            solution_file.write(board.printCarFuel() + "\n")

            solution_file.write("Runtime: " + str(gbfs_solver.runtime) + " seconds\n")
            solution_file.write("Search Path Length: " + str(len(gbfs_solver.searchPath)) + " states\n")
            solution_file.write("Solution Path Length: " + str(len(gbfs_solver.solutionPath) - 1) + " moves\n")
            solution_file.write("Solution Path: " + gbfs_solver.get_solution_moves() + "\n\n")
            solution_file.write(gbfs_solver.get_board_line() + "\n\n")

            solution_file.write("Final Configuration: \n\n")

            solution_file.write(gbfs_solver.solutionPath[0].board.returnBoardInfo())
            solution_file.close()
        else:
            solution_file.write("No solution found!")

        search_file.write(gbfs_solver.get_search_path())
        search_file.close()


print("Total Program run time: ", time.time() - start_time)
