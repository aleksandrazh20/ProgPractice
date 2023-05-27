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

class Dev(Employee):
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


class Smm(Employee):
    def __init__(self, name, salary, exp, soc_med):
        super().__init__(name, "SMM", salary, exp)
        self.soc_med = soc_med

    def info(self):
        print("SMM")
        super().info()
        print("Social media:", self.soc_med)


employees = [
    Project_Manager("Maria", 40000, 3),
    Dev("Anton", 80000, 5, "senior", "java"),
    Accountant("Natali", 60000, 6, "CRM"),
    Smm("Alina", 50000, 2, "Instagram")
]

for employee in employees:
    employee.info()
    print()