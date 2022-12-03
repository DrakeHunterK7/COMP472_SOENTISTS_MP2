import Board as bd

class Node:
    def __init__(self, board: bd, parent, cost, move):
        self.board = board
        self.parent = parent
        self.cost = cost[0]
        self.g = cost[1]
        self.h = cost[2]
        self.move = move

    def __lt__(self, other):
        return self.cost < other.cost

    def printBoard(self):
        self.board.printBoardInfo()

    def printNode(self):
        return str(self.cost) + " " + str(self.g) + " " + str(self.h) + "\n" + self.board.returnBoardInfo()