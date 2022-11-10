import Car as car


class Board:
    def __init__(self, string):
        # First pass - create an empty 6x6 board with just 0s on it
        board_dimension = 6
        self.board = [[0 for x in range(board_dimension)] for y in range(board_dimension)]
        self.cars = []
        count = 0

        # Replace all the 0s in this empty 6x6 board with the respective letters from the input file
        for i in range(6):
            for j in range(6):
                self.board[i][j] = string[count]
                count = count+1

        # Identify all the cars on the board and group them into a list
        for alphabet in boardLetters:
            a_count = []

            i_index = 0
            for i in self.board:
                j_index = 0
                for j in i:
                    if j is alphabet:
                        a_count.append([i_index, j_index])
                    j_index = j_index+1
                i_index = i_index + 1

            if len(a_count) > 0:
                temp = a_count[:]
                self.cars.append(car.Car(alphabet, 100, cells=temp))
                temp = []

    def printBoardInfo(self):
        for i in self.board:
            for j in i:
                print(j, end='  ')
            print()

        for c in self.cars:
            c.printCarInfo()


boardLetters =   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']