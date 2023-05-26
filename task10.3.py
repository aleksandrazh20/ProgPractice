class Box:
    def __init__(self, numb):
        self.numb = numb
        self.figures = []

    def put(self, figure):
        self.figures.append(figure)

    def box_info(self):
        print(f"{self.numb} box has this items:")
        for figure in self.figures:
            figure.desc()

class Figure:
    name = None

    def __init__(self, color):
        self.color = color

    def desc(self):
        print(self.color, self.name)


class Rhombus(Figure):
    name = "rhombus"

    def __init__(self, color, side):
        self.side = side
        super().__init__(color)


class Triangle(Figure):
    name = "triangle"

    def __init__(self, color, a,b,c):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        super().__init__(color)


class Circle(Figure):
    name = "circle"

    def __init__(self, color, radius):
        self.radius = radius
        super().__init__(color)


box1 = Box("first")
box2 = Box("second")

f1 = Rhombus("green", 20)
f2 = Circle("blue", 15)
f3 = Triangle("pink", 10,15,20)
f4 = Circle('yellow', 10)
box1.put(f1)
box1.put(f2)
box1.box_info()

box2.put(f3)
box2.put(f4)
box2.box_info()

