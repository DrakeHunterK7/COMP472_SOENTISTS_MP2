import Car as car

class Board:
    def __init__(self, string):
        # First pass - create an empty 6x6 board with just 0s on it
        self.board_dimension = 6
        self.board = [[0 for x in range(self.board_dimension)] for y in range(self.board_dimension)]
        self.cars = []
        count = 0

        # Replace all the 0s in this empty 6x6 board with the respective letters from the input file
        for i in range(6):
            for j in range(6):
                self.board[i][j] = string[count]
                count = count+1

        # Identify all the cars on the board and group them into a list

        for alphabet in boardLetters:
            loop_count = 0
            a_count = []
            current_car_fuel = 100
            i_index = 0
            for i in self.board:

                j_index = 0
                for j in i:
                    if j is alphabet:
                        a_count.append([i_index, j_index])
                    j_index = j_index+1
                i_index = i_index + 1

            new_car = None
            if len(a_count) > 0:
                temp = a_count[:]
                new_car = car.Car(alphabet, current_car_fuel, cells=temp)
                self.cars.append(new_car)
                temp = []

            for i in string:
                loop_count = loop_count + 1
                if loop_count > 36:
                    if i is alphabet:
                        new_car.setFuel(string[loop_count])

    def printBoardInfo(self):
        for i in self.board:
            for j in i:
                print(j, end='  ')
            print()

    def isWinningState(self):
        if self.board[2][5] == "A":
            return True
        else:
            return False

    def isCarOnExit(self, car):
        if car.orientation == "vertical": return
        if car.name == "A": return

        on_exit = False
        if car.cell_list[len(car.cell_list)-1][0] == 2 and car.cell_list[len(car.cell_list)-1][1] == 5:
            on_exit = True

        if on_exit:
            for cell in car.cell_list:
                self.board[cell[0]][cell[1]] = "."
            self.cars.remove(car)


    def identify_blocking_cars(self):
        ambulance = self.cars[0]
        ambulance_last_cell = ambulance.cell_list[len(ambulance.cell_list)-1]

        characters_list = []

        for x in range(ambulance_last_cell[1], self.board_dimension-1):
            if self.board[ambulance_last_cell[0]][x] != ".":
                characters_list.append(self.board[ambulance_last_cell[0]][x])

        characters_list = list(dict.fromkeys(characters_list))

        return len(characters_list)


    def getAllMoves(self):
        all_moves = []
        for c in self.cars:
            car_moves = self.checkCarMoves(c)
            if len(car_moves) > 0:
                for move in car_moves:
                    all_moves.append(move)

        return all_moves

    def checkCarMoves(self, car_to_move):

        movesList = []

        car_top_left = car_to_move.cell_list[0]
        car_bottom_right = car_to_move.cell_list[len(car_to_move.cell_list) - 1]

        currentFuel = 0
        if isinstance(car_to_move.fuel, str):
            if int(car_to_move.fuel) <= 0:
                return []
            else:
                currentFuel = int(car_to_move.fuel)
        else:
            if car_to_move.fuel <= 0:
                return []
            else:
                currentFuel = car_to_move.fuel

        if car_to_move.orientation == "horizontal":
            cells_to_move = 1
            while (car_bottom_right[1]+cells_to_move) < self.board_dimension and \
                    self.board[car_bottom_right[0]][car_bottom_right[1]+cells_to_move] == "." and \
                    cells_to_move <= currentFuel:
                movesList.append([car_to_move.name, cells_to_move, "right"])
                cells_to_move = cells_to_move + 1

            cells_to_move = 1
            while self.board[car_top_left[0]][car_top_left[1]-cells_to_move] == '.' and \
                    (car_top_left[1]-cells_to_move) >= 0 and \
                    cells_to_move <= currentFuel:
                movesList.append([car_to_move.name,  cells_to_move, "left"])
                cells_to_move = cells_to_move + 1

        else:
            cells_to_move = 1
            while (car_bottom_right[0] + cells_to_move) < self.board_dimension and \
                    self.board[car_bottom_right[0] + cells_to_move][car_bottom_right[1]] == "." and \
                    cells_to_move <= currentFuel:
                movesList.append([car_to_move.name, cells_to_move, "down"])
                cells_to_move = cells_to_move + 1

            cells_to_move = 1
            while (car_top_left[0] - cells_to_move) >= 0 and \
                    self.board[car_top_left[0] - cells_to_move][car_top_left[1]] == "." and \
                    cells_to_move <= currentFuel:
                movesList.append([car_to_move.name, cells_to_move, "up"])
                cells_to_move = cells_to_move + 1

        return movesList

    def moveCar(self, move):
        car_to_move = None

        for car in self.cars:
            if car.name is move[0]:
                car_to_move = car
                break

        distance = move[1]
        direction = move[2]

        if direction == "up" or direction == "down":
            for cell in car_to_move.cell_list:
                self.board[cell[0]][cell[1]] = "."

            for cell in car_to_move.cell_list:
                if direction == "up":
                    cell[0] = cell[0] - distance
                else:
                    cell[0] = cell[0] + distance

            for cell in car_to_move.cell_list:
                self.board[cell[0]][cell[1]] = car_to_move.name
        else:
            if direction == "left" or direction == "right":
                for cell in car_to_move.cell_list:
                    self.board[cell[0]][cell[1]] = "."

                for cell in car_to_move.cell_list:
                    if direction == "left":
                        cell[1] = cell[1] - distance
                    else:
                        cell[1] = cell[1] + distance

                for cell in car_to_move.cell_list:
                    self.board[cell[0]][cell[1]] = car_to_move.name

        self.isCarOnExit(car_to_move)



boardLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']