class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def info(self):
        pass


class Oval(Figure):
    def __init__(self, r1, r2):
        super().__init__()
        self.rad1 = r1
        self.rad2 = r2

    def info(self):
        print("This is an oval with radius 1 =", self.rad1, "and radius 2 =", self.rad2, "and color", self.color)


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def info(self):
        print("This is a square with side =", self.side, "and color", self.color)


oval = Oval(28, 14)
square = Square(15)
oval.info()
square.info()

oval.change_color("pink")
square.change_color("green")

oval.info()
square.info()