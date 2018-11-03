
class Employee:
    emcount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emcount += 1
        self.fuck = 10

    def displaycount(self):
        print("Total employess:" % (Employee.emcount))
    def employee(self):
        print("name: %s, salary: %s" % (self.name, self.salary))


if __name__ == "__main__":
    epl = Employee("nguyen xuan chai", "500$")
    epl2 = Employee("Hoang Thi My Lin", "700$")
    print(epl2.fuck)
