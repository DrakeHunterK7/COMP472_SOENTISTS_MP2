import Board as bd

class Node:
    def __init__(self, board: bd, parent, cost):
        self.board = board
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


    def printBoard(self):
        self.board.printBoardInfo()