import Board as bd
from queue import PriorityQueue
from Node import Node
import pickle
import time

class AStar:
    def __init__(self, board):
        self.board = board
        self.open_list = PriorityQueue()
        self.closed_list = []
        self.runtime = 0
        self.solutionPath = []
        self.solutionMoves = []
        self.searchPath = []
        self.solutionFound = False


    def search_solution(self, heuristic: int):

        nodes_created = 0

        start_time = time.time()

        start_node = Node(self.board, parent=None, cost=[0, 0, 0], move=None)
        self.open_list.put([start_node.cost, start_node])

        while not self.open_list.empty() and not self.solutionFound:

            self.closed_list.append(self.open_list.queue[0][1])
            nodes_created = len(self.closed_list)

            newBoard = self.open_list.queue[0][1].board

            if not newBoard.isWinningState():
                for move in newBoard.getAllMoves():
                    moveBoard = pickle.loads(pickle.dumps(newBoard, -1))
                    moveBoard.moveCar(move)

                    is_node_visited = False

                    for node in self.closed_list:
                        if node.board.board == moveBoard.board:
                            is_node_visited = True

                    for node in self.open_list.queue:
                        if node[1].board.board == moveBoard.board:
                            is_node_visited = True

                    if not is_node_visited:
                        newNode = Node(moveBoard, self.open_list.queue[0][1], self.cost_function(moveBoard, self.open_list.queue[0][0], heuristic), move)
                        self.open_list.put([newNode.cost, newNode])
            else:
                self.solutionFound = True
                self.trace_path_to_root(self.open_list.queue[0][1])
                end_time = time.time()
                self.runtime = end_time-start_time
                self.searchPath = self.closed_list

            self.open_list.get()

            if not self.open_list.empty():
                print("", end="\r")
                print("Finding Solution, nodes opened so far:", nodes_created, end="")

        if self.solutionFound:
            print("\n")
            self.print_solution()
        else:
            print("\n")
            print("No solutions were found!")

    def cost_function(self, board: bd, cost, heuristic_index):
        h = 0
        if heuristic_index == 1:
            h = board.identify_blocking_cars()
        elif heuristic_index == 2:
            h = board.identify_blocking_positions()
        elif heuristic_index == 3:
            h = board.identify_blocking_cars() * 4
        elif heuristic_index == 4:
            h = board.board_dimension - board.get_ambulance_column()

        g = cost + 1
        f = g + h
        cost_list = [f, g, h]
        return cost_list

    def trace_path_to_root(self, start_node):
        current_node = start_node

        while current_node is not None:
            self.solutionPath.append(current_node)
            current_node = current_node.parent

    def print_solution(self):
        cost = -1
        for node in reversed(self.solutionPath):
            node.board.printBoardInfo()
            cost = cost + 1
            print("\n")
        print("Total Cost: ", cost)

    def get_solution_moves(self):
        line = ""
        for node in reversed(self.solutionPath):
            if node.move is not None:
                line += node.move[0]
                line += " " + str(node.move[1])
                line += " " + node.move[2]
                line += "; "

        return line

    def get_search_path(self):
        line = ""
        for node in self.searchPath:
            line += str(node.cost)
            line += " " + str(node.g)
            line += " " + str(node.h)
            line += " "*(10-len(str(node.cost) + " " + str(node.g) + " " + str(node.h)))

            for row in node.board.board:
                for cell in row:
                    line += str(cell)
            line+="\n"

        return line

    def get_board_line(self):
        line = ""
        for node in reversed(self.solutionPath):
            if node.move is not None:
                line += node.move[0]
                line += " " + str(node.move[1])
                line += " " + node.move[2]
                line += " "*(16-len(node.move[2]))

                line += str(node.board.last_final_fuel) + " "

                for row in node.board.board:
                    for cell in row:
                        line+=str(cell)

            line+="\n"

        return line