class Bag:
    def __init__(self, color, material):
        self.color = color
        self.material = material


class Backpack:
    def __init__(self, color, material):
        self._color = color
        self._material = material

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value


class Purse:
    def __init__(self, color, material):
        self.__color = color
        self.__material = material

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value


bag1 = Bag("black", "leather")
print(bag1.material)
bag1.material = "fake leather"
print(bag1.material)

backpack1 = Backpack("brown", "fabric")
print(backpack1.get_color())
backpack1.set_color("black")
print(backpack1.get_color())

purse1 = Purse("white", "plastic")
print(purse1.get_color())
purse1.set_color("pink")
print(purse1.get_color())
print(purse1.__color)  # AttributeError: 'Purse' object has no attribute '__color'.