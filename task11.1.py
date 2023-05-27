class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Worker(Table):
    def __init__(self, l, w, h, start, finish):
        super().__init__(l, w, h)
        self.start = start
        self.finish = finish

    def late(self):
        if self.start > 8:
            print("You are late")
        else:
            print("You are not late")

    def work_hrs(self):
        if self.finish - self.start < 8:
            print("You didn't work enough")
        else:
            print("Good job!")




t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Worker(1, 3, 0.7, 9, 15)
t_2.outing()
t_2.late()
t_2.work_hrs()