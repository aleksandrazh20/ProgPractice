class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Garage:
    def __init__(self, car, garage_num):
        self.car = car
        self.garage_num = garage_num

    def get_car_info(self):
        print(f"The car in the {self.garage_num} garage is a {self.car.color} {self.car.model}")


car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")

garage1 = Garage(car1, 'first')
garage1.get_car_info()
car1.change_color("green")
garage1.get_car_info()

garage2 = Garage(car2, 'second')
garage2.get_car_info()
car2.change_color("pink")
garage2.get_car_info()