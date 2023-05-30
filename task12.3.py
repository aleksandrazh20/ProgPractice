class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def info(self):
        print("Hello, my name is", self.name, "I am", self.age)
        self.__languages()

    def __languages(self):
        print(f"I speak Russian, English & Chinese")


person1 = Person("Maria", 25)
person1.info()