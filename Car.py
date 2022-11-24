class Car:
    def __init__(self, name, fuel, cells=None):
        self.name = name
        self.fuel = fuel
        self.cell_list = []

        if cells is None:
            cells = []
        else:
            for i in cells:
                self.cell_list.append(i)

        if self.cell_list[0][0] == self.cell_list[1][0]:
            self.orientation = "horizontal"
        else:
            self.orientation = "vertical"

    def printCarInfo(self):
        print("Name: " + self.name, ", Fuel: ", self.fuel, ", Cells: ", self.cell_list, ", Orientation: ", self.orientation)

    def setFuel(self, fuel):
        self.fuel = fuel