class Employee:
    def __init__(self, name, position, salary, exp):
        self.name = name
        self.position = position
        self.salary = salary
        self.exp = exp

    def info(self):
        print("Name:", self.name)
        print("Position:", self.position)
        print("Salary:", self.salary)
        print('Experience:', self.exp)


class Project_Manager(Employee):
    def __init__(self, name, salary, exp):
        super().__init__(name, "Project Manager", salary, exp)

    def info(self):
        print("Project Manager")
        super().info()

class dev(Employee):
    def __init__(self, name, salary, exp, it_exp, language):
        super().__init__(name, "Developer", salary, exp)
        self.it_exp = it_exp
        self.language = language

    def info(self):
        print("Developer")
        super().info()
        print("IT experience:", self.it_exp)
        print("Programming language:", self.language)

class Accountant(Employee):
    def __init__(self, name, salary, exp, prog):
        super().__init__(name, "Accountant", salary, exp)
        self.prog = prog


    def info(self):
        print("Accountant")
        super().info()
        print("Program used:", self.prog)


class dev2(Employee):
    def __init__(self, name, salary, exp, it_exp, language):
        super().__init__(name, "developer", salary, exp)
        self.it_exp = it_exp
        self.language = language

    def print_info(self):
        print("developer")
        super().info()
        print("Programming language:", self.language)


employees = [
    Project_Manager("Maria", 40000, 3),
    dev("Anton", 80000, 5, "senior", "java"),
    Accountant("Natali", 60000, 6, "CRM"),
    dev2("Sergey", 50000, 1, "Junior", "python")
]

for employee in employees:
    employee.info()
    print()