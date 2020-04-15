from unittest.test.test_result import __init__


class Calc:
    num = 100

    def __init__(self, a, b):
        self.fn = a
        self.sn = b
        print("I am called automatically when opject is created")

    def getData(self):
        print("I am now executing method in class")

    def Summ(self):
        return self.fn + self.sn + Calc.num




obj = Calc(2,3)
obj.getData()

print(obj.num)
print(obj.Summ())

obj1 = Calc(4,5)
obj1.getData()

print(obj1.Summ())