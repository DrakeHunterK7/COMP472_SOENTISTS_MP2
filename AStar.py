import Board as bd
from queue import PriorityQueue
from Node import Node
import pickle

class AStar:
    def __init__(self, board):
        self.board = board

        self.open_list = PriorityQueue()
        self.closed_list = []

        self.solutionPath = []


    def search_solution(self, heuristic: int):

        nodes_created = 0
        solutionFound = False

        start_node = Node(self.board, parent = None, cost = 0)
        self.open_list.put([start_node.cost, start_node])

        while not self.open_list.empty() and not solutionFound:

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
                        newNode = Node(moveBoard, self.open_list.queue[0][1], self.cost_function(newBoard, self.open_list.queue[0][0], heuristic))
                        self.open_list.put([newNode.cost, newNode])
            else:
                solutionFound = True
                self.trace_path_to_root(self.open_list.queue[0][1])

            self.open_list.get()

            if not self.open_list.empty():
                print("", end="\r")
                print("Finding Solution, nodes opened so far:", nodes_created, end="")

        if solutionFound:
            print("\n")
            self.print_solution()
        else:
            print("\n")
            print("No solutions were found!")



    def cost_function(self, board: bd, cost, heuristic_index):
        h = 0
        if heuristic_index == 1:
            h = board.identify_blocking_cars()

        g = cost + 1
        f = g + h
        return f

    def trace_path_to_root(self, start_node):
        current_node = start_node

        while current_node is not None:
            self.solutionPath.append(current_node)
            current_node = current_node.parent

    def print_solution(self):
        cost = -1
        for node in self.solutionPath:
            node.board.printBoardInfo()
            cost = cost + 1
            print("\n")
        print("Total Cost: ", cost)